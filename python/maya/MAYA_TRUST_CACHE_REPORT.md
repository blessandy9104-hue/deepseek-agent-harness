# Maya trust-runtime caching — phase report

**Date:** 2026-09-18
**Phase:** Narrowly-scoped trust-runtime metadata caching (registry parse/read reuse) + validation A–F
**Verdict:** **READY** (all mandated validation passed; no trust semantics changed; one bounded-memory hardening applied)

---

## 1. Scope and constraints honored

Removed the repeated JSONL parse/read cost that `maya_trust` paid on every lookup, **without**
caching any authorization fact. The cache stores only non-authoritative registry metadata
and is revalidated against a deterministic fingerprint on every access.

| Req | Constraint | How it is honored |
|---|---|---|
| 1 | Cache only safe, non-authoritative metadata | Stores the parsed rows exactly as on disk (capability metadata, registry structure, immutable descriptions) plus a malformed-validity flag. Never a verdict, owner/pending approval, revoke/grant outcome, context/scope decision, or execution result. |
| 2 | Do not cache authorization facts | `maya_trust.authorize` is byte-for-byte unchanged; it re-evaluates status, owner, context, scope, permission, approval and newest-record/revocation on **every** request against the rows returned by the cache. |
| 3 | Deterministic invalidation | Six layered rules: explicit `store_record` mutation, file identity+size+mtime_ns, content sha256, malformed/validity transition, process/runtime reset, and TTL. See §3. |
| 4 | Fail closed | Cache-machinery failure falls back to the uncached `read_rows` (the exact pre-cache behavior); a malformed row stays `{"malformed": True}` and can never be read as valid; absent file → empty list. |
| 5 | Bounded size and lifetime | LRU bound (`max_entries=32`) **and** a total-row budget (`max_total_rows=2000`); TTL `5s` absolute (no refresh-on-hit). |
| 6 | No sensitive data, no new disk writes | The cache is in-memory only and touches no disk of its own; no cache files are created; the real trust artifacts are never written by tests. |

---

## 2. Changed files

| File | Change |
|---|---|
| `maya_trust_cache.py` | **New.** `read_rows(path)` (uncached parse; missing → `[]`; bad line → `{"malformed": True, "line": …}`), `_stat`, `_hash_bytes`, immutable `_Entry`, and `TrustMetadataCache` (`configure`/`invalidate`/`clear`/`reset`/`stats`/`rows`/`malformed`, `DEFAULT_TTL_SECONDS=5.0`, `DEFAULT_MAX_ENTRIES=32`, `DEFAULT_MAX_TOTAL_ROWS=2000`). `_UNSET` sentinel so `configure(clock=None)` restores the monotonic clock. |
| `maya_trust.py` | `import maya_trust_cache as _trust_cache`; module-level `_REGISTRY_CACHE`; `load_registry` reads through the cache and returns **independent top-level row copies**; `store_record` invalidates **before and after** the append; new public `cache_stats()`, `cache_invalidate()`, `cache_reset()`, `cache_configure(**kwargs)`. No change to any decision logic. |
| `test_trust_cache.py` | **New.** 36 `=OK` contract + security/ethics + cross-layer suite. |
| `verification/manifest.py` | Registered `test_trust_cache.py` (`expected_ok: 36`) in `SUITES` + `SUITE_CONTRACTS`. |

No capability, identity, math, orchestration, `maya_chat`, instrumentation or Qt-bridge logic was
modified. (`maya_instrumentation.py` is unchanged this phase; its bridge-phase fix remains.)

---

## 3. Cache design

**Validity fingerprint.** Each entry carries dev/inode, size and `mtime_ns` (fast path, checked on
every access), the sha256 of the exact bytes, the generation token it was admitted under, and its
parse time. With `verify_content=True` (used by the trust tests) the hash is recomputed on every
access, so a same-size/same-mtime content rewrite is still detected.

**Invalidation.**
1. **Explicit mutation** — `store_record` (used by `refresh`, `grant`, `revoke`) bumps a process
   generation token before and after the append, so the next reader always re-parses.
2. **File identity + metadata** — any append/rewrite/removal is seen immediately.
3. **Content hash** — keyed to exact bytes; strict mode hashes every access.
4. **Malformed transition** — a malformed parse is stored as malformed and can never read as valid.
5. **Process/runtime reset** — `reset()`/`clear()`; a fresh process starts empty.
6. **TTL** — every entry expires; TTL bounds *metadata* staleness only and is never what makes an
   authorization fresh (that is always recomputed).

**Concurrency.** Entries are immutable once built and swapped atomically under an `RLock`; readers
never observe a partial entry. The returned list is a fresh list of row copies, so a caller cannot
mutate cached state.

**Bounds.** At most `max_entries` paths (LRU). Additionally, total cached rows are capped at
`max_total_rows`; the just-read entry is retained even if a single registry exceeds the budget, so
the resident set is bounded by `max(max_total_rows, rows-in-largest-registry)`.

---

## 4. Validation A–F

| | Validation | Result |
|---|---|---|
| **A** | New contract suite registered; exact label contract | `test_trust_cache.py` → **36 `=OK`**, `status=pass`, exit 0 on `C:\Program Files\Python313\python.exe`, Python 3.14 and the project venv. Manifest 79 suites / 79 contracts aligned. |
| **B** | Security / ethics checks (cached metadata never becomes cached permission) | 8 dedicated checks pass: metadata-not-permission, revocation-immediate, approval-not-inferred, cross-scope-not-reused, malformed-ambiguous-untrusted, unavailable-not-silently-trusted, four-honest-outcomes-distinct, diagnostics-no-secrets. |
| **C** | Black-box validation (public surface only, no cache imports) | `trust_cache_blackbox_probe.py` → **16/16 cases**, both interpreters: repeated lookups, read-only router, authorize-before-revoke, identical-request-after-revoke refused, grant visible, approval blocked then retry allowed, owner/context changes, registry removal/restoration, malformed replacement/refusal/recovery, 240 concurrent requests (0 errors), fresh-process restart, real artifacts absent. |
| **D** | Performance validation (cached vs uncached) | `trust_cache_perf_probe.py` → see §5. Registry parse/read **19.2×** faster, lookup **15.3×**, `:trust` show turn **10.4×**, core tick trust projection **3.1–3.4×**, authorize **6.0×** (its action-log write is the remaining constant). 199 hits / 1 miss over 200 lookups, 0 errors, invalidation 0.0055 ms and forces re-parse. |
| **E** | Cross-layer consistency | Suite checks confirm trust runtime, action log, intelligence-core (`build_core_view`/`runtime_core_view`) and `:trust` diagnostics never show allowed/approved/completed when the runtime refuses; a pending/revoked capability forces fail-closed. |
| **F** | Full regression + repository state | `python -m verification.sweep` → **79 suites, 2270 ok-labels, clean=True**; controlled launch clean; stabilization report clean (0 anomalies in all 6 categories). `verification.independent.run()` → 2 interpreters + PowerShell + cmd + static-analysis + git, `consensus=True`, `required_ok=True`, `cross_agreement=True`, 0 disagreements. Real trust artifacts (`trusted_capabilities.jsonl`, `maya_trust_actions.jsonl`) **absent**; no cache files created; `py_compile` clean; `HEAD 1890617e`. |

---

## 5. Performance evidence (`trust_cache_perf_probe.py`)

Controlled A/B on the **same** 300-record temp registry and the **same** target record
(worst case: the first-written row, so an uncached `lookup` scans the whole file). Per-operation
wall latency, best of both measurement orders; cache ENABLED (shipped default) vs DISABLED
(pre-cache behavior).

| Operation | Uncached ms | Cached ms | Speedup |
|---|---|---|---|
| `load_registry` | 6.03 | **0.31** | **19.2×** |
| `lookup` | 6.15 | **0.40** | **15.3×** |
| `authorize` | 13.73 | **2.27** | **6.0×** |
| `:trust show` turn | 7.13 | **0.69** | **10.4×** |
| `build_core_view` (tick projection) | 8.29 | **2.44** | **3.4×** |
| `runtime_core_view` (live tick read) | 8.59 | **2.77** | **3.1×** |

Cache accounting over 200 cached lookups: **199 hits, 1 miss, 0 errors**; explicit invalidation
**0.0055 ms** and the next read is a miss (mutation visible immediately). `authorize` remains
I/O-bound on its mandatory action-log append, which is unchanged and intentional.

**Bounded footprint.** Reading 64 distinct 300-row registries through the cache left **6 resident
entries** (bounded by the 2000-row budget under the 32-path LRU; 58 evictions) and RSS grew to
37.4 MB. Before the row budget was added the same stress held 32 entries and RSS grew to 76.6 MB —
the hardening cut the stress footprint by roughly half while keeping the path LRU. The full A/B
run's RSS (18.1 → 37.4 MB after GC) is dominated by one-time lazy imports and the 200×300-parse
workload, not by retained cache state.

Artifacts: `trust_cache_perf_probe.py`, `trust_perf.json` (out-of-tree, `%TEMP%\opencode`).

---

## 6. Privacy and security notes

- No secret/token/credential/digest is stored, emitted or logged by the cache; `cache_stats()`
  exposes only counters and policy (`enabled`, `entries`, `rows`, `hits`, `misses`,
  `invalidations`, `evictions`, `errors`, `generation`, TTL/bounds).
- The suite's `trustcache_diagnostics_no_secrets_ok` confirms `:trust` diagnostics and stats carry
  no digests or credentials.
- A cached row can never be read as a decision; the security checks in B explicitly mutate a
  returned row and re-run `authorize` to prove the next decision is recomputed and a different
  user/context/action cannot reuse a prior verdict.

---

## 7. Issue found and fixed

The path-only LRU bound did not bound memory under a stress registry: 32 cached paths × 300 rows
retained tens of MB. Added a `max_total_rows` budget (`DEFAULT_MAX_TOTAL_ROWS=2000`) with LRU
eviction that always keeps the just-read entry; a new suite check
`trustcache_bounded_rows_ok` covers it. Under the 64×300-row stress this reduced retained entries
from 32 to 6 and RSS growth from ~48 MB to ~9 MB, with no behavioral change and all 36 checks
still passing.

---

## 8. Verdict

**READY.** Registry metadata caching is additive, deterministic, bounded and fail-closed; every
authorization decision is still recomputed from current state; all existing trust/compat suites,
the new 36-check suite, the full 79-suite sweep, the 16-case black-box probe, the A/B performance
probe and independent cross-source verification pass cleanly.
