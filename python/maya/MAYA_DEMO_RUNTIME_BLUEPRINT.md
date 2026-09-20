# Maya Demo Runtime Blueprint — Architecture Specification

- **Status:** Blueprint (v1.0) — complete runtime architecture for the **public demo**
- **Demo principles (non-negotiable):** *predictable, safe, deterministic,
  private, verified.* The demo must run identically everywhere, touch nothing
  it must not, and fail closed to a calm/neutral face — never to a crash, a
  guess, or a leak.
- **Bindings:** EXISTING = built & verified; PROPOSED = module path this
  blueprint defines (to be implemented behind the persona layer).

---

## 1. System Diagram

```
        ┌──────────────────────────── runtime sandbox ─────────────────────────────┐
        │                                                                          │
 [ identity loader ] ─► [ math engine ] ─► [ world model ] ─► [ safety layer ]      │
        │                      |                 |                 |                 │
        │                      v                 v                 v                 │
        │             [ expression engine ] ◄── [ persona selector ] ◄── context    │
        │                      |                                                  │
        │                      v                                                  │
        │             [ rendering loop ] ──► [ UI wrapper ] ──► desktop/web/kiosk   │
        │                      |                                                  │
        │                      v                                                  │
        │             [ runtime sandbox checks / resource governor ]               │
        └──────────────────────────────────────────────────────────────────────────┘
        deployment constraints gate the whole composite (verified runtime, budgets)
```

Data flows strictly downstream on one deterministic track; sandbox runs
synchronously at each stage boundary (deny-by-default).

---

## 2. Component Specifications

### 2.1 Math Engine
**Binding:** `maya_identity/wireframe/rig_math.py` → `math_coordinator.py`
(EXISTING); surface re-exported via `maya_runtime/core.py` (`MATH_AGENT`,
`CHANNEL_MAX`, `TASK_BLEND_WEIGHTS`, precision constants).

Responsibilities: pure canonical math for poses, blends, world patterns,
smoothing (`stable_exp_smooth`, `stable_lerp`, `clamp01`). Adds no RNG, time,
or hardware reads.
**Constraint:** nothing below this layer is device-dependent; frame values are
bit-identical across devices.

### 2.2 World Model
**Binding:** `maya_runtime/world_model.py` → `WORLD_MODEL` (EXISTING) over
`WORLD_STATE_PATTERNS`.

Responsibilities: maintained 4-dim world state, stability features, domain
alignment (`PATTERN_ALIGNMENT`). Drift is guarded; loads flatten expression
(downward-only modulation).
**Constraint:** world state is session-scoped and isolated per tenant/user
(Isolation Manager).

### 2.3 Safety Layer
**Binding:** `maya_runtime/safety_monitor.py` → `SAFETY_MONITOR` (EXISTING);
`current_pc_safety` resources; `safety_anomalies` suite.

Responsibilities: bound enforcement (ceilings, step caps), load-aware
down-shaping, urgency/taboo escalation inputs, isolation drift/leak counters.
**Constraint:** safety is algebra over the same canonical surface; a safety
violation neutralizes the frame, no partial states, audit to metadata.

### 2.4 Expression Engine
**Binding:** Expression Engine spec (L0–L7). L1/L2/L4 PROPOSED orchestration
over existing `interaction` + `math_coordinator` primitives; L7 `rendering.py`
(EXISTING).

Responsibilities: semantic→intensity, tone shaping, micro blend (0.6/0.3/0.1),
gesture mapping, persona gates, frame assembly.
**Constraint:** every lane inside `CHANNEL_MAX`; step caps ≤ persona rule;
transitions monotone.

### 2.5 Persona Selector
**Binding:** `maya_runtime/personality.py` (EXISTING `PERSONAS`,
`channel_targets`, `paced_state`) + persona package (PROPOSED: profiles, tone,
vocabulary, switching, safety) + Isolation Manager gates.

Responsibilities: active persona resolution from the identity profile; tone and
vocabulary selection; guarded switching (verified-runtime + context gates);
fail-closed `calm/even`.
**Constraint:** one persona per session; switch via monotone smooth; no hybrid.

### 2.6 Identity Loader
**Binding:** `maya_runtime/_loader.py` (EXISTING: canonical import or headless
file-based fallback); `identity.json` immutable (CORED), profile loader
(PROPOSED per Identity Profile format).

Responsibilities: load canonical identity + active profile, validate strict
(JSON Schema → registries → disjointness → bands), keep CORED fields internal.
**Constraint:** loader is all-or-nothing; any error → calm/even fallback
profile, no partial identity.

### 2.7 Rendering Loop
**Binding:** `maya_runtime/rendering.py` (EXISTING: `RenderFrame`, registry,
`render_engine`, `get_renderer`, `sample_frame`).

Responsibilities: produce bounded frames at cadence, feed registered renderer,
never mutate, no timestamps in frames.
**Constraint:** cadence-capped (e.g., ≤ 30/s), per-frame budget bounded; frame
signature native == headless (asserted by verification launch).

### 2.8 UI Wrapper
**Binding:** `maya_runtime/ui/` (EXISTING: tk, web, kiosk, robotics renderers).

Responsibilities: attach frames to window/webview/kiosk; user input path back to
semantic/context; pure presentation.
**Constraint:** UI never edits values; adapts only the surface; no UI-specific
math.

### 2.9 Runtime Sandbox (PROPOSED: `maya_runtime/sandbox.py`)
Responsibilities: surface whitelist, resource governor, process/image policy,
violation handler.

```
check(action, surface, tenant_id)  -> allowed | denied (deny-by-default)
budget(action)                     -> frame/steps/bytes/timing budget
violation(kind, detail)            -> neutralize + log(metadata) + demo halt if severe
```

Allowed surface: read profiles + identity.json; write `metadata/**` diagnostic
logs. Denied: network egress, subprocess spawning outside verification,
arbitrary fs writes, identity edits, secret access, registry mutation.
**Constraint:** sandbox is the ONLY authority over surface access; it reports
violations to the self-check engine.

### 2.10 Deployment Constraints
| Constraint | Demo rule |
|---|---|
| Verified runtime | demo boot reaches READY only after external sweep + controlled launch (stabilization protocol) |
| Device parity | native == headless frame signature asserted at boot and per render sample |
| Resource budget | CPU-light; cadence ≤ 30/s; frame path deterministic; no GPU requirement |
| Secrets | none in calls, none in logs, none in profile bundles |
| Network | none outbound in demo mode (except none at all) |
| Filesystem | read: profiles, identity.json; write: `metadata/**` only |
| Concurrency | single session single tenant unless multi-tenant demo explicitly configured |
| Fallback | any sandbox/safety/loader error → calm/even neutral face + log; severe → clean halt |
| Tenants (if enabled) | isolation namespaces + quotas + kill switches active from boot |

---

## 3. Boot Sequence (deterministic)

```
 1  sandbox.init(config)                    deny-by-default surface table
 2  identity_loader.load()                  identity.json + profiles (CORED kept internal)
 3  math_engine.init()                      freeze precision modes, weights
 4  world_model.init()                      session world slice + patterns
 5  safety_layer.init()                     ceilings, step caps, quotas
 6  expression_engine.init()                L1 tonel + L2/L3/L4/L6 gate tables
 7  persona_selector.load(profile)          active persona; fail-closed calm/even
 8  rendering.loop.start()                  cadence + renderer attach
 9  ui_wrapper.attach(kind)                 desktop/web/kiosk
10  readiness: verification sweep + controlled launch -> READY gate
```

Steps 1–9 are deterministic and headless-safe; step 10 is the only external
gate, and the demo will not run before it.

## 4. Rendering Loop

```
 loop tick:
   sample = world_model.sample()          constrained by world slice
   frame  = expression_engine.step(sample, persona, budget)
   render = render_engine(frame, target)  consume-only
   sandbox.check("render", surface)
   if seat lifetimes bounded -> halt cleanly
 cadence <= 30/s; budget check each tick; no timestamps in RenderFrame.
```

Parity: same inputs → identical frame signature on desktop/web/kiosk/robotics
and in headless verification mode.

---

## 5. Failure & Fallback Paths

| Failure | Response | Mode |
|---|---|---|
| loader/schema error | calm/even profile; anomaly logged | continue, neutral |
| tone/gesture unknown | neutral frame | continue |
| sandbox violation (non-critical) | neutralize + log; deny repeat | continue |
| safety violation / urgency forbid | neutralize frame; audit | continue, guarded |
| drift/leak anomaly repeats | readiness self-check flag; drift lock | degraded |
| severe sandbox violation / spoof | clean halt (no partial state) | halt |
| displayless env | headless fallback identical math | demo loops without UI |

---

## 6. Verification Contract

New suite `test_demo_runtime_blueprint.py`:

| Label | Asserts |
|---|---|
| `demo_boot_sequence` | deterministic booot steps resolve without side effects; core freezes hold |
| `demo_identity_load` | all-or-nothing; CORED not exposed; profile strict-validated |
| `demo_sandbox_deny` | network/secret/identity/registry actions denied by default |
| `demo_sandbox_allow` | profiles read + metadata writes allowed |
| `demo_sandbox_violation` | violation neutralizes + logs + counters |
| `demo_render_ceiling` | every sampled frame inside CHANNEL_MAX |
| `demo_render_parity` | native == headless signature on same inputs |
| `demo_fail_closed` | loader/sandbox/expression error yields calm/even neutral |
| `demo_flag_halt` | severe violation yields clean halt, no partial frame emitted |
| `demo_whitelist` | fs/net surface exactly the documented whitelist |
| `demo_ready_gate` | READY only via stabilization consensus |
| `demo_suite` | module import + total label parity |

---

## 7. Dependency Map

- Pros: `_loader` (identity), `core` (math), `world_model`, `safety_monitor`,
  `rendering` + `ui/*` + `deploy/*`, `personality` (ESTABLISHED);
- Proposed: persona package, isolation manager, `demo.py` orchestrator,
  `sandbox.py`, expression-engine orchestration;
- External gate: `verification` sweep + controlled launch (stabilization
  protocol) — demo cannot self-declare ready.