# Maya Founder Automation Blueprint — Phase 9 Operator Mode

- **Status:** implementation blueprint v1.0 · Phase 9 of the founder journey:
  **the solo founder (ThinkPad) automates every non-legal operational task** on
  the fully-launched Phase-8 platform. Backed by a validated operator registry
  (`maya_identity/operator/operator_plan.json`, 51/51 checks).
- **Preconditions met:** Phase 8 platform launched; Phase 7 isolation runtime
  implemented and verified; post-isolation `platform_ready` gate green.
- **Core safety posture (non-negotiable):** Maya automates **operations, not
  judgment.** Legal authority (contracts, payments, liability, terms), business
  decisions (pricing, negotiation), and financial/medical/legal safety all stay
  **human (founder).** The operator engine is deterministic, ceiling-locked,
  audit-trailed, and escalates every non-legal exception to the founder. It
  **cannot** approve contracts, commit payments, negotiate, or touch safety
  decisions.

---

## 1. Operator Mode Definition

### 1.1 What Maya can automate (operations)
`operations · onboarding_nonlegal · setup_deployment_prep ·
monitoring_sweeps · verification_moderation · api_usage_monitoring`.

Concretely: deterministic execution of onboarding, structured requirements
intake, persona selection assistance, project folder tree + config stubs,
embed/persona/deployment prep, monitoring + regression sweeps, tenant & creator
onboarding (non-legal), marketplace moderation (MR01–MR07), API usage
monitoring, kiosk deployment prep. Everything a solo founder currently does by
hand that does **not** require legal or business judgment.

### 1.2 What Maya cannot automate (legal/business)
`legal_tasks · business_decisions · liability · payments`.
Legal authority is never delegated to the operator; business negotiation and
pricing are founder-only; liability-bearing decisions are founder-only.
Automation stops at these boundaries and hands off.

### 1.3 Founder vs operator authority map
| Actor | Owns | Cannot |
|---|---|---|
| **Founder** | legal authority, contract approval, pricing & negotiation, liability, final marketplace approval | delegate legal authority to the operator; skip audit review |
| **Operator** | deterministic execution of operations: onboarding, intake, setup, deployment prep, monitoring, verification, moderation pre-review | approve legal contracts; commit to payments or pricing; negotiate; touch financial/medical/legal safety decisions; act beyond non-legal operations |

Founder authority is exclusive and non-delegatable over legal scope; operator
authority is bounded to non-legal operations and escalates above its scope.

## 2. Automated Founder Tasks (13)

| # | Task | What operator does | Stays founder-only |
|---|---|---|---|
| 1 | client_onboarding | non-legal steps: identity-of-domain check, config draft | contract/terms approval |
| 2 | requirements_intake | structured questionnaire → profile fields | scope/obligations decisions |
| 3 | persona_selection | decision table (mode map) from web allowlist | final persona choice sign-off |
| 4 | project_setup | folder tree + config stubs, templates | none (operational) |
| 5 | embed_runtime_prep | per-tenant embed config, origin allowlist, TTL/quota draft | go-live approval |
| 6 | persona_config_prep | ceiling-locked persona config under tenant NS | none |
| 7 | deployment_prep | assemble deploy bundle, run validation | deployment go/no-go |
| 8 | monitoring_sweeps | run regression sweeps + isolation suite, report deltas | act on legal-class findings |
| 9 | tenant_onboarding | non-legal onboarding workflow (§6.4) | contract/payment |
| 10 | creator_onboarding | eligibility + guided setup + first submission routing | listing approval (MR07) |
| 11 | marketplace_moderation | auto-verify MR01–MR06, prepare pre-review packet | MR07 founder review |
| 12 | api_usage_monitoring | quota/rate/SLO telemetry, anomaly counters | response to abuse findings |
| 13 | kiosk_deployment_prep | single-site config, offline-safe loop params | physical deploy decision |

Marketplace moderation is split: the operator auto-verifies MR01–MR06 and
prepares the packet, but **MR07 founder review stays human** — auto-verify alone
never lists a persona.

## 3. Operator Engine Architecture

### 3.1 Operator Orchestrator
`operator_orchestrator` binds each operator task to its integration surface,
runs it deterministically, records outcomes to the audit trail, and hands any
non-legal exception to the founder. It never grants legal capability.

### 3.2 Operator Task Registry
Declarative, `scope: operations`. Each task is a declarative operation bound to
its surface and ceiling-locked output; no task performs legal/business action by
construction.

### 3.3 Operator Task Scheduler (deterministic)
`deterministic: true`, `no_parallel_legal: true`. Fixed ordering:
`tenant_onboarding → requirements_intake → persona_selection → project_setup →
embed_runtime_prep → persona_config_prep → deployment_prep →
verification_sweep`. Deterministic (no RNG, no wall-clock branching),
device-identical, and never runs any task whose outcome could be mistaken for a
legal approval in parallel.

### 3.4 Operator Safety Ceilings
Same expression ceilings as the platform: `expression 0.5 · viseme 0.35 ·
micro 0.012 · anatomical 0.8`. Autonomy cap: `nonlegal_operations_only` — the
operator's authority ceiling is explicitly non-legal.

### 3.5 Operator Audit Hooks
Record every operator action (`record_all`); `founder_visible` (founder can
review all); `operator_scoped` (audit spans are tenant/operator-scoped, CORED
never logged). Legal handoffs write a distinct audit marker so nothing legal is
ever auto-applied.

### 3.6 Operator Fallback Behaviors
`handoff_to_founder: true` and `no_legal_auto: true`. On any boundary
approached or exception raised, the operator stops deterministically and hands
to the founder — never "maybe approved." Isolation-level fail-closed
deny-by-default governs every operator surface access.

## 4. Integration Points

| Surface | Operator binding |
|---|---|
| **Studio** | guided persona builder; ceiling-locked config prep; publish routed to moderation (never direct) |
| **Marketplace** | MR01–MR06 auto-verify; packet prep; MR07 founder review |
| **Cloud Runtime** | per-tenant NS + quotas provisioned; deterministic scaling monitoring |
| **API** | read-only usage/SLO telemetry; no write surface |
| **Embed Runtime** | per-tenant embed config prep; origin allowlist; routing |
| **Isolation Runtime** | deny-by-default surface guard governs every operator action; fail-closed on exception |
| **Persona Loader** | persona config prepared only inside tenant NS |
| **Identity Loader** | identity CORED never emitted; fingerprints only |

The isolation runtime is the enforcement core for every operator action — the
operator inherits its fail-closed deny-by-default posture.

## 5. Automation Boundaries

### 5.1 Legal boundaries (contracts, payments, liability, terms)
Operator cannot draft, approve, execute, or commit to contracts, payments,
liability, or terms. All route to the founder; automation stops at the boundary
and logs a handoff.

### 5.2 Business boundaries (pricing, negotiation)
Operator cannot set or negotiate pricing, or make business commitments. Pricing
config is founder-only.

### 5.3 Safety boundaries (financial, medical, legal)
Operator cannot act on financial, medical, or legal safety. Market-analyst-
category personas keep their financial-safety ruleset and founder review (MR06);
nothing financial is auto-decided.

### 5.4 Operator-only boundaries (non-legal tasks only)
`nonlegal_only: true`, `founder_escalation: true`. The operator automates
exactly the non-legal operational tasks in §2 and nothing else; any exception or
ambiguous case is escalated to the founder. Boundaries are disjoint (§5.1–5.4),
so legal/business/safety never overlap with the operator's automation scope.

## 6. Operator Roadmap

| Stage | Name | Gates | KPIs |
|---|---|---|---|
| **9.1** | Internal Operator Mode | isolation_runtime_verified; operator_engine_ready; platform_ready_gate | operator task success rate; founder handoff rate |
| **9.2** | Automated Onboarding | task_registry_live; onboarding_templates_verified | client onboard time; requirements intake completion |
| **9.3** | Automated Deployment Prep | project_setup_automated; embed_persona_config_verified | deploy prep time; config validation rate |
| **9.4** | Automated Platform Maintenance | monitoring_automated; regression_sweep_automated | sweep pass rate; anomaly detection latency |
| **9.5** | Automated Ecosystem Operations | marketplace_moderation_automated; tenant_creator_onboarding_automated; api_monitoring_automated | personas verified/week; tenant+creator onboard time; api slo rate |

### Stage detail
- **9.1 Internal Operator Mode.** The operator engine exists, is gated on the
  verified isolation runtime + platform READY, and serves the founder alone.
  KPIs confirm tasks succeed and non-legal exceptions hand to the founder at a
  sane rate. **This is the current working stage.**
- **9.2 Automated Onboarding.** Task registry live; client onboarding and
  structured requirements intake automated off verified templates.
- **9.3 Automated Deployment Prep.** Project folder tree + stubs, embed and
  persona config prep, and deployment bundles automated with config validation.
- **9.4 Automated Platform Maintenance.** Monitoring and regression sweeps
  (existing sweep + isolation 12-step) run automatically; anomaly latency is a
  KPI. MR07 founder review remains human.
- **9.5 Automated Ecosystem Operations.** Marketplace moderation (MR01–MR06),
  tenant + creator onboarding, and API monitoring automated at ecosystem scale.
  Always bounded: legal/business/safety remain founder-only.

### Cross-stage discipline
Each stage gate is **real and verified**, not a checkbox; the isolation runtime
remains verified across all stages; operator authority ceiling
(non-legal-only) is unchanged from 9.1 onward. KPIs are monitored forward so a
solo founder sees the automation succeed (success rate, handoff rate, latency)
before trusting it wider.

## 7. Verification & File Map

- **Operator battery:** 51/51 checks — schema-valid; cannot-automate set =
  legal/business decisions/liability/payments; can-automate = operations incl.
  verification/monitoring; founder owns legal and cannot delegate it; operator
  owns operations and cannot approve contracts/negotiate/touch safety; all 13
  automated tasks present; engine has orchestrator + declarative operations-only
  task registry + deterministic scheduler with no-parallel-legal and ordered
  steps + safety ceilings == CHANNEL_MAX with non-legal autonomy cap + full
  founder-visible audit hooks + handoff/no-legal-auto fallback; all 8
  integration points incl. isolation + identity; legal/business/safety
  boundaries disjoint with operator-only non-legal scope + founder escalation;
  roadmap 9.1–9.5 with correct names, gates (9.1 gated on isolation + READY),
  and KPIs; no secrets, no currency.
- **Artifacts:** `maya_identity/operator/operator_plan.json` ·
  `operator_plan.schema.json` · blueprint `MAYA_FOUNDER_AUTOMATION_BLUEPRINT.md`.
- **Chain:** Phase-5 scaling + marketplace (MR rules) → Phase-6 platform →
  Phase-7 isolation runtime (verified, denied-by-default) → Phase-8 launch →
  Phase-9 operator. The automation is bound by the same honest rule: it
  automates operations and verification, never legal, business, or safety
  judgment.