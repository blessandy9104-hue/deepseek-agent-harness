# Maya Founder Command System Blueprint — Phase 11 Command Layer

- **Status:** implementation blueprint v1.0 · Phase 11 of the founder journey:
  a **unified, deterministic founder command interface** to control Maya's
  operations, deployments, onboarding, and maintenance. Backed by a validated
  command-system registry (`maya_identity/command/command_system.json`,
  47/47 checks).
- **Preconditions met:** Phase 8 platform launched; Phase 9 operator mode active
  (all non-legal operational tasks automated); Phase 10 monetization defined.
- **Core posture (consistent with Phases 9–10):** the command layer automates
  **operation commands**, legal commands (contracts, payments, proposal,
  pricing, go/no-go) are **founder-only gated**, and every surface access runs
  under the isolation runtime's **deny-by-default**. The engine is
  table-based, deterministic, schema-validated, and audit-trailed — it never
  free-interprets a command.

---

## 1. Command Layer Definition

### 1.1 Purpose
A single founder interface to issue, run, and audit Maya operations across
deployments, onboarding, project setup, operator tasks, platform, ecosystem,
and maintenance — while keeping legal authority gated founder-only and
everything operational routed deterministically through the operator engine and
isolation runtime.

### 1.2 Boundaries (operator-only vs founder-only)
- **Operator-only commands (automated):** `deployment`,
  `onboarding_nonlegal`, `project_setup`, `monitoring_sweeps`,
  `verification_moderation`, `maintenance_checks`. These execute
  deterministically without founder labor.
- **Founder-only commands (human):** `legal_approval`, `contract`, `payment`,
  `proposal`, `go_no_go`, `pricing`. These require founder auth and are never
  delegated.

### 1.3 Authority map (legal vs non-legal)
| Actor | Owns | Cannot |
|---|---|---|
| **Legal (founder)** | contract approval, payment authorization, proposal sign-off, pricing, go/no-go on legal-scope actions | be delegated to the operator; run silently without founder auth and audit |
| **Non-legal (operator)** | deterministic execution of operational commands: deployment, onboarding, project setup, monitoring, verification, moderation, maintenance | approve legal commands; commit payments or pricing; exceed surfaces; act outside its scope |

The command layer makes this split explicit at the grammar level: a command
carries an `auth` slot that determines whether it routes to the operator engine
(non-legal, auto) or the founder gate (legal, sign-off).

## 2. Command Categories (7 groups)

| Category | Commands | Owning surface |
|---|---|---|
| **deployment** | `embed`, `persona_load`, `config_prep` | Embed runtime, persona loader |
| **onboarding** | `client`, `tenant`, `creator` | operator engine (non-legal) + founder sign-off at legal step |
| **project** | `setup`, `structure`, `config_stubs` | operator engine (project prep) |
| **operator** | `monitor`, `sweep`, `verify`, `moderate` | operator engine (monitoring, sweeps, verification, moderation pre-review) |
| **platform** | `marketplace`, `cloud_runtime`, `api` | platform surfaces |
| **ecosystem** | `creator`, `tenant`, `kiosk` | marketplace/cloud/kiosk |
| **maintenance** | `audit`, `regression`, `isolation_checks` | audit hooks + isolation runtime |

Every category is a fixed set of named commands (schema-enumerated); unknown
commands are rejected at the router.

## 3. Command Syntax

### 3.1 Unified command grammar
```
verb  category  target  parameters  auth
 deploy deployment config_prep tenant=<slug> operator
 approve platform marketplace persona=<id> founder-legal
```
Five fixed slots: **verb · category · target · parameters · auth**. All
commands share this grammar; nothing else is accepted.

### 3.2 Deterministic command parsing
`deterministic: true`, `strict: true`. Parsing is a pure table lookup with no
RNG, no wall-clock, no probabilistic or LLM interpretation. The same command
string always routes, validates, and executes identically (parity native ==
headless).

### 3.3 Safe command envelopes
`scoped: true` (every command is tenant/session-scoped), `exact_origin: true`
(origin-checked like the MSG.v1 embed envelope), and
`no_llm_interpretation: true` (the command is parsed structurally, never
semantically reinterpreted — preventing ambiguous natural-language commands from
reaching the executor).

### 3.4 Founder-only command gating
Commands whose `auth` is legal (`approve contract`, `authorize payment`,
`sign proposal`, `set pricing`, `go/no-go`) are gated founder-only: they are
queued for founder auth, never auto-executed, and every such action writes a
distinct audit marker. `legal_required: true`.

### 3.5 Operator-only command automation
Commands whose `auth` is operator run automatically through the operator engine
(`operator_auto: true`): onboarding non-legal steps, setup/prep, monitoring,
verification, moderation pre-review. They are founder-invocable but need no
founder labor.

## 4. Command Engine Architecture

### 4.1 Command router
`table_based: true`, `rejects_unknown: true`. A fixed routing table maps each
enumerated verb+category to its owning surface and executor. Anything not in the
table is denied immediately.

### 4.2 Command validator
`schema_checked: true`, `deterministic: true`. Validates parameters (target,
auth, tenant slug) against per-command schemas before any execution; invalid or
over-scoped commands are rejected.

### 4.3 Command executor
`operator_bound: true`, `isolation_guarded: true`. Executes within the
operator engine's capability and every surface call is guarded by the isolation
runtime's deny-by-default. Executor cannot issue legal commands.

### 4.4 Command audit hooks
`record_all` (every command + outcome logged), `founder_visible` (founder can
review all), `no_cored_log` (identity CORED never written to logs). Legal gates
write a distinct marker so nothing legal is ever auto-applied.

### 4.5 Command fallback behaviors
`deny_unknown` (unknown command), `handoff_founder` (non-legal exception →
founder), `fail_closed` (any error → deny, never "maybe allow"),
`rethrow_parse_error` (parse failures are rejected, not silently corrected).

### 4.6 Integration with isolation runtime
`isolation_integration: deny_by_default`. The isolation runtime is the
enforcement core for **every** command surface access — a command cannot read,
write, or switch across a tenant boundary, cannot emit CORED identity, and any
guard error denies the command and audits it. Command determinism inherits the
runtime's native==headless parity.

## 5. Integration Points

| Surface | Command binding |
|---|---|
| **Studio** | guided persona builder; config-prep and publish commands |
| **Marketplace** | moderation pre-review commands (MR01–MR06), list routing; MR07 founder review |
| **Cloud Runtime** | per-tenant NS + quota provisioning commands |
| **API** | read-only telemetry commands (no write surface) |
| **Embed Runtime** | embed/persona-load/config-prep deployment commands |
| **Operator Engine** | routes and executes all non-legal operator commands (Phase 9) |
| **Persona Loader** | persona config loaded only inside tenant NS |
| **Identity Loader** | identity CORED never emitted; fingerprints only |

The command router is the front door; the operator engine is the executor; the
isolation runtime is the guard that every surface call passes through.

## 6. Safety & Boundaries

### 6.1 Legal boundaries (contracts, payments, liabilities)
No command auto-approves a contract, authorizes a payment, or accepts a
liability. All route to the founder legal gate; automation stops at the boundary
and logs a handoff.

### 6.2 Business boundaries (pricing, negotiation)
No command sets or negotiates pricing. `pricing` is a founder-only command.

### 6.3 Operator boundaries (non-legal tasks only)
`operator_boundaries.nonlegal_only: true` — the operator executes exactly the
non-legal commands in §2 and nothing else; any exception is handed to the
founder.

### 6.4 Isolation boundaries (deny-by-default)
`isolation_boundaries: deny_by_default` — every command runs under the
isolation runtime's fail-closed deny-by-default; no cross-tenant access, no
CORED emission, fail-closed on any error. Boundaries are mutually disjoint
(legal/business/operator), so no automation overlaps legal or business scope.

## 7. Phase 11 Roadmap

| Stage | Name | Gates | KPIs |
|---|---|---|---|
| **11.1** | Command Grammar | grammar_verified; parser_deterministic; envelope_safe | command parse accuracy; unknown command deny rate |
| **11.2** | Command Engine | router_ready; validator_schema_checked; executor_isolation_guarded | command execution latency; validator reject rate |
| **11.3** | Operator Integration | operator_engine_bound; operator_command_automation_live; audit_hooks_continuous | deployment command time; monitoring/sweep command rate |
| **11.4** | Platform Integration | all_categories_routable; marketplace_cloud_api_commands_live; isolation_checks_invokable | platform command coverage; cross-surface command success |
| **11.5** | Founder Console | founder_legal_gate_verified; console_audit_dashboard_live; exception_handoff_verified | founder command sign-off rate; command→execution latency; audit coverage |

### Stage detail
- **11.1 Command Grammar (current).** Define and verify the 5-slot grammar;
  parsers deterministic; envelopes safe (scoped, exact origin, no LLM
  interpretation). Unknown commands denied.
- **11.2 Command Engine.** Router + validator + executor live and
  isolation-guarded; all commands validated by schema before execution.
- **11.3 Operator Integration.** Bind the operator engine; operator commands
  (deployment, monitoring, sweeps, verification, moderation) run automatically;
  audit hooks continuous.
- **11.4 Platform Integration.** Route all seven categories across marketplace,
  cloud, API, and embed; isolation checks invokable as commands.
- **11.5 Founder Console.** The founder-facing console with the legal gate,
  full audit dashboard, and verified exception-handoff flow live.

### Cross-stage discipline
Real, verified gates at every stage. Legal gating is in place from 11.1 onward
(never deferred); isolation deny-by-default guards every command from the
engine stage onward; audit coverage is continuous. A command can never
self-escalate in auth — the `auth` slot is fixed by the router and validated
before execution.

## 8. Verification & File Map

- **Command battery:** 47/47 checks — schema-valid; operator-only vs
  founder-only boundaries; legal authority owns contracts/payments and cannot
  delegate; non-legal owns operational commands and cannot approve legal;
  all 7 command categories with their enumerated commands; 5-slot grammar;
  deterministic strict parsing; safe envelope (scoped/exact-origin/no-LLM);
  founder+operator+legal gating; router table-based rejecting unknowns;
  schema-validated deterministic validator; operator-bound isolation-guarded
  executor; full audit hooks (record-all, founder-visible, no-CORED);
  4 fallback behaviors; isolation integration deny-by-default; 8 integration
  points incl. operator engine (isolation enforced at engine level); safety
  boundaries (legal/business/operator/isolation) disjoint; roadmap 11.1–11.5
  correct with isolation gate at 11.2 and legal gate at 11.5; no secrets.
- **Artifacts:** `maya_identity/command/command_system.json` ·
  `command_system.schema.json` · blueprint `MAYA_FOUNDER_COMMAND_SYSTEM_BLUEPRINT.md`.
- **Chain:** Phase-7 isolation runtime (deny-by-default) → Phase-9 operator
  engine (non-legal executor) → Phase-10 monetization → Phase-11 command layer.
  The command layer gives the founder one deterministic interface to the whole
  platform while preserving the honest boundary: legal commands stay human,
  operational commands are automated, and every surface access is isolation-
  guarded.