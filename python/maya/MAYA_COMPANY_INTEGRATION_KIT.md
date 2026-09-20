# Maya Company Integration Kit — Enterprise Onboarding Document

- **Version:** 1.0.0
- **Audience:** enterprise integration teams onboarding Maya for branded, safe,
  deterministic assistant experiences.
- **Template:** `maya_identity/profiles/company_template.profile.json` (validated
  against the Identity Profile schema — verified).
- **Core promise:** Maya is **read-only by design** toward your systems. You
  supply whitelisted content, consume schema'd outputs, and get bit-identical
  behavior on every device with zero invented facts, zero outbound network, and
  zero secrets exposure.

---

## 1. Onboarding Flow (overview)

```
 1 Decide persona  ──► 2 Fill profile template ──► 3 Register tenant + npm/bundle
        │                       │                          │
        v                       v                          v
 4 Certify content feeds     5 Install bundle         6 Run verification sweep
        │                       │                          │
        v                       v                          v
 7 Reach READY gate ──► 8 Consume read-only outputs ──► 9 Go-live + audits
```

Every step has a verification gate; nothing runs in production before the READY
gate (§7).

---

## 2. Company Identity Profile Template

File: `maya_identity/profiles/company_template.profile.json` — copy it, then
edit ONLY the allowed fields:

| Field | You edit? | Guidance |
|---|---|---|
| `company_id` | **yes** | Upper-case token, 2–64 chars: `^[A-Z0-9][A-Z0-9_-]*$` (e.g. `ACME`). Becomes the tenant binding key. |
| `persona` | yes | pick from Persona Selection Guide (§3); default `calm`. |
| `theme` | yes | your visual theme slug (`^[a-z][a-z0-9_-]*$`). |
| `tone`, `vocabulary` | yes | from the registries; the guide pre-picks these per persona. |
| `emotional_range` | yes* | must fit `CHANNEL_MAX`; the loader clamps, so keep within bands. |
| `constraints` | yes* | add `x-` extension only; base constraints are mandatory-sensible. |
| `allowed_behaviors` | yes* | select capabilities/domains; **never remove `safety_monitoring` or `world_stability`**. |
| `forbidden_behaviors` | yes | list any directive/feature/domain you must not surface. |
| `brand_personality` | yes | your brand constants; validation is strict (hex color, ≤120 char catchphrase). |
| `runtime_persona_loader` | **no** | pinned: `engine=maya_runtime.persona.loader`, `fail_closed`, `strict`, `deterministic=true`. |
| `isolation_rules` | **no** | pinned: identity/math/safety/world are protected forever. |
| `$schema`, `$id`, `version` | no (bump version only) | schema pin + your bundle id. |

Rules:
- `allowed ∩ forbidden = ∅` (loader invariant; a phrase in both rejects the bundle).
- `override_slot` is the only runtime-mutable brand area and it re-validates on
  every write.
- The template validates as-is (checked against the schema) — editing a
  protected field or breaking an enum rejects the whole bundle (all-or-nothing).

## 3. Persona Selection Guide

Pick by your primary engagement goal:

| Your goal | Recommended persona | base · tone · vocabulary | Why |
|---|---|---|---|
| Front desk, intake, transfer | `receptionist` | warm · even · assistive_base | policy-closed scheduling, verified routing |
| Learning / staff enablement | `tutor` | warm · warm · assistive_base | scaffold-first, evidence-verified progress |
| Sales / conversion support | `sales_agent` | warm · warm · business_clear | catalog-scoped, no invented specs |
| Brand companion / loyalty | `companion` | playful · lively · entertainment_playful | energy-capped, safe-steering |
| Premium services / hospitality | `concierge` | authoritative · even · business_clear | options-first, record-sourced status |
| Self-service / kiosk / floor | `kiosk_assistant` | calm · even · technical_precise | session-bound, no carry-over |

Selection rules:
1. Pick **one** persona per session; hybrid personas are not supported.
2. Tone follows persona: e.g., `soothing` for distress (companion/concierge),
   `technical` in robotics contexts (kiosk).
3. If your requirement is urgent/escalation-heavy, keep urgency detection active
   (do not remove it): urgent → forced `even`/`soothing`, `exclaim=false`.
4. Anti-selection: **do not** pick `companion` for kiosk (ceiling too high) or
   `concierge` for sales (register too flat) — ceilings/shaping must match the
   channel.

## 4. Branding Integration Rules

What you may inject (via `brand_personality` and `override_slot`):

- Brand name, accent color (`#RGB`/`#RRGGBB`), up to 12 visual accent tokens,
  optional catchphrase (≤120 chars, printable ASCII).

Hard rules:
1. Branding is **presentation-only**: it cannot influence ceilings, safety
   thresholds, world model, capabilities, or the stabilization protocol.
2. `branded: false` → catchphrase must be `null`; `true` → catchphrase may be
   surfaced by brand-accented roles only.
3. Brand values are constants at load; `override_slot` writes are validated
   each time and rollback to the last valid value on failure.
4. Cross-tenant: brand assets live under `brand/<company_id>/*` and are never
   readable by other tenants.

## 5. API Integration Points (read-only)

Maya publishes **read-only** surfaces; it never calls you, never accepts
inbound control, and never writes to your systems.

### 5.1 Outputs Maya publishes (consume-only, schema'd)
| Surface | Content | Notes |
|---|---|---|
| `outputs/render_frame.json` | per-frame channels, joints, pose, pace | bounded, no timestamps |
| `outputs/market_gate.json` | normalized context: tones, dialect, language route, urgency, shaped phrase | text pipeline insight |
| `outputs/decision.json` | role/domain decision bindings | record-only |
| `info/status.json` | version, persona, readiness state, operational_state | read-only query |

All are **draft-07 schema'd** and deterministic; consumers poll snapshots, no
callbacks, no webhooks.

### 5.2 Inputs you supply (whitelisted, read-only to Maya)
| Feed | Location | Maya may |
|---|---|---|
| Identity profile bundle | `profiles/<company_id>/*.profile.json` | read + validate (never write) |
| Policy / catalog / schedule data | `data/<company_id>/*` | read into session-scoped context |
| Brand assets | `brand/<company_id>/*` | read for presentation only |

Maya treats your files as immutable inputs; it does not modify them.

### 5.3 Explicitly NOT part of the read-only API
- No write-back endpoints, no config mutation, no network callbacks, no
  outbound HTTP, no code execution requests, no secret ingestion.

## 6. Sandbox Constraints

| Dimension | Allow | Deny |
|---|---|---|
| Filesystem | read `profiles/**`, `data/<company_id>/**`, `brand/<company_id>/**`; write `metadata/**` diagnostics only | any other write |
| Network | none | all egress/ingress by default |
| Processes | verification sweep launch only | general subprocess spawning |
| Identity | read canonical (CORED kept internal) | identity edits |
| Registry | snapshot reads | mutation |
| Runtime | headless + native parity | hardware-specific detection |

Fail-closed: any violation neutralizes the frame, logs, and (severe) halts
cleanly — never a partial state. Resource governor caps cadence ≤ 30/s, CPU-light.

## 7. Deployment Checklist

```
[ ] 1. Environment: Python 3.10+; verified runtime bundle installed
[ ] 2. Fill profile template from §2 (company_id, persona, brand)
[ ] 3. Validate: profile passes identity_profile schema (fastjsonschema/ajv)
[ ] 4. Persona selection confirmed against §3 guide
[ ] 5. Branding fields validated (§4) — no safety/ceiling coupling
[ ] 6. Tenant registered: tenant key + namespace + quota + kill switch set
[ ] 7. Content feeds placed in whitelisted dirs (§5.2); secret scan clean
[ ] 8. Sandbox config reviewed against §6 allow/deny
[ ] 9. Run verification sweep (python -m verification.sweep): 18 suites clean
[ ]10. Controlled launch: native == headless signature parity
[ ]11. READY gate reached via stabilization consensus (not self-declared)
[ ]12. Smoke: one session per enabled persona; outputs within ceilings
[ ]13. Multi-tenant isolation spot-check (cross-tenant access denied)
[ ]14. Go-live: monitor self-check anomalies; review weekly audit spans
```

Each unchecked box blocks go-live; there is no "auto-approve" path.

## 8. Multi-Tenant Isolation Rules

1. **Tenant binding:** one `company_id` per session, immutable for that session.
2. **Namespaces:** all data fell under `metadata/logs/brand/data/<company_id>/*`;
   cross-tenant literal keys are auto-denied.
3. **Quotas/burst:** per-tenant budgets enforced at every `can()`; a tenant
   can never exceed its slice, even when global capacity is idle (slot-based).
4. **Kill switch:** per-tenant flag; tripped → that tenant only is denied; other
   tenants unaffected.
5. **No aggregation without consent:** summarizing across tenants requires
   consent markers from every contributing tenant.
6. **Degraded mode:** constrained tenants (kiosk/robotics) require a verified
   runtime; otherwise switch stays blocked.
7. **Identity isolation:** CORED identity fields are never serialized into any
   tenant payload; leakage attempts increment the self-check anomaly counters.

## 9. Acceptance Verification

Contract suite `test_company_integration_kit.py`:

| Label | Asserts |
|---|---|
| `kit_template_valid` | shipped template validates against the identity schema |
| `kit_company_id_pattern` | company_id slug rules enforced |
| `kit_persona_guide_consistent` | every guide recommendation satisfies persona band/vocab tables |
| `kit_branding_nosafety` | branding fields cannot couple to ceilings/safety/math |
| `kit_output_schema` | published outputs adhere to read-only payload schemas |
| `kit_read_only_api` | all integration surfaces are read-only (no writable paths) |
| `kit_sandbox_allow_deny` | §6 whitelist/deny enforced by sandbox checks |
| `kit_tenant_isolation` | cross-tenant read denied; namespaced reads pass |
| `kit_kill_switch` | kill-switch denies only its tenant |
| `kit_deploy_gate` | READY only post sweep + parity + consensus |
| `kit_parity` | native == headless for identical integration inputs |
| `kit_suite` | module import + total label parity |

---

## 10. Version & Sign-off

- Bundle version: bump `version` on any profile change; the loader records the
  active bundle in `info/status.json`.
- Sign-off gate: a bundle is live only after items 1–11 of §7 are green and the
  READY consensus is recorded.