# Maya Monetization & Client Acquisition Blueprint — Phase 10 Revenue Engine

- **Status:** implementation blueprint v1.0 · Phase 10 of the founder journey:
  the solo founder (ThinkPad) runs a **repeatable, scalable revenue engine** for
  Maya deployments. Backed by a validated revenue registry
  (`maya_identity/revenue/revenue_plan.json`, 39/39 checks).
- **Preconditions met:** Phase 8 platform launched; Phase 9 operator mode active
  (all non-legal operational tasks automated).
- **Pricing discipline (carried through):** all pricing in the registry is
  **abstract tier-index** (`one_time_index`, recurring multipliers, ratios) —
  the commercial catalog's currency is `abstract_index`. Real prices live in a
  **founder-defined private ledger outside the repository**; the conversion
  step is explicit and founder-owned. No currency literals appear anywhere.

---

## 1. Monetization Architecture

### 1.1 Unified tier-index pricing model
Every offer is described by a small set of abstract indices:
- **one_time_index** — the relative one-time build/deploy value (e.g., 1.0
  essentials, 1.6 growth, 2.5 premium per the catalog).
- **recurring_monthly_multiplier** — the recurring component as a multiplier of
  the one-time index (0.0 → 0.15 → 0.4).
All offers share this one model → one number set per offer, comparable,
consistent, machine-validatable.

### 1.2 Persona pricing (5 personas)
Each of the five personas (receptionist, tutor, concierge, sales_agent,
market_analyst) is priced from the same tier-index structure in the commercial
catalog, with its own ceiling carried alongside. Positioning is problem-value,
tiering is behavior-based (essentials / growth / premium).

### 1.3 Bundle pricing (website + AI staff)
Bundles pair an accessibility-minded website with a mounted persona
("Website + AI Receptionist", "Website + AI Tutor", "Website + AI Sales Agent").
A bundle's index sums its one-time components (site + persona config) and its
recurring components (hosting + support/content updates), per the catalog's
`one_time` / `recurring` item kinds.

### 1.4 Platform pricing (cloud, embed rent, marketplace fees)
- **Cloud tenant:** abstract tenant fee index (hosted isolation, per-tenant
  namespaces, quotas) — abstract indices only.
- **Embed rent:** small per-deployment index (frictionless on-ramp).
- **Marketplace fee:** the 0.30 platform share of the 70/30 creator split.
All fees sit strictly below the marketplace platform share, keeping the embed
path the cheap on-ramp.

### 1.5 Conversion of tier indices → real pricing (founder-defined)
```
base_price(real)    = founder maps one_time_index 1.0  -> real one-time price
recurring(real)     = founder maps recurring multiplier -> real monthly price
```
The registry deliberately carries **only ratios**; the founder maintains a
private conversion ledger (private file, never committed). This keeps pricing
schemas currency-free while giving an explicit, auditable conversion step.

## 2. Offer System (14 offers)

| Group | Offers | Count |
|---|---|---|
| Core | Starter, Standard, Premium | 3 |
| Persona | Receptionist, Tutor, Concierge, Sales Agent, Market Analyst | 5 |
| Bundle | Website + AI Receptionist, + AI Tutor, + AI Sales Agent | 3 |
| Special | Kiosk offer · Cloud tenant offer · Marketplace creator offer | 3 |
| **Total** | | **14** |

- **3 core offers:** Starter (single persona, essentials), Standard (one persona
  growth/bundle), Premium (multi-surface / bundle premium).
- **5 persona-specific offers:** one per persona, tier-index priced.
- **3 bundle offers:** website + AI staff per persona.
- **Kiosk offer:** single-site physical deployment (offline-safe loop), priced
  as a special deployment.
- **Cloud tenant offer:** hosted tenant (per-tenant NS/quota), priced by tenant
  fee index.
- **Marketplace creator offer:** creator-side entry with 70/30 split and listing
  quota (10).

## 3. Client Acquisition Engine

### 3.1 Outreach system (scripts, channels)
- Per-persona founder-style outreach scripts (problem-and-fix, a concrete
  visitor/user problem → how the persona solves it).
- Promotional channel one (email / local business lists).
- Referral channel with a structured intro flow.
Rationale: targeted, small, credible outreach beats broad advertising for a solo
founder; each script maps to a validated persona + offer.

### 3.2 Founder-style messaging (non-salesy)
`non_salesy: true`. Tone: founder-to-owner, plain, helpful. The message tells a
story of a specific problem a specific persona fixes, not a generic pitch —
which also matches the verified runtime's calm, non-directive register.

### 3.3 Pilot → diversification → scaling workflow
1. **Pilot:** one focused deployment per persona/vertical, prove value + referral.
2. **Diversification:** broaden to adjacent verticals and the persona's other
   uses once a pilot is stable.
3. **Scaling:** add tenants and personas within deployment capacity (see §6).

### 3.4 Referral engine
Built into every deployment handover: a structured "who else should we build
for" ask, plus the referral channel in §3.1. Referrals are the highest-leverage
acquisition for a solo founder.

### 3.5 Positioning: "Websites with AI Staff"
The single, repeatable pitch: Maya sells **websites with AI staff** — a site
that answers, routes, teaches, sells, or advises for its owner. Clear, one-line,
non-exotic, and directly maps to the bundle offers.

## 4. Sales Workflow

`intake → requirements → persona_selection → proposal → deployment → payment`

| Step | Owner | Detail |
|---|---|---|
| intake | operator (auto) | non-legal lead intake, channel + script |
| requirements | operator (auto) | structured questionnaire → profile fields |
| persona_selection | operator assist + founder sign-off | decision table from web allowlist |
| proposal | **founder** | legal/commercial proposal — human |
| deployment | operator (auto prep) + founder go/no-go | operator engine setup + prep; founder approves go-live |
| payment | **founder** | invoices/contracts — human, legal |

- **Founder-only legal steps:** proposal and payment (contracts, payments,
  liability) — never automated (Phase 9 §1.2).
- **Operator-mode automated steps:** intake, requirements, deployment prep,
  plus monitoring after go-live.
This is exactly the Phase-9 split applied to revenue: the operator accelerates
everything non-legal; the founder owns the two legal steps and go/no-go.

## 5. Revenue Loops

| Loop | Recurring? | Source | Owner |
|---|---|---|---|
| **One-time** | no | site build + persona config (bundle one-time) | founder |
| **Recurring** | yes | hosting + support/content updates (bundle recurring) | founder (operator maintains) |
| **Marketplace** | yes | persona recurring component 70/30 split | 70% creator, 30% platform/founder |
| **Cloud runtime** | yes | hosted tenant fee index | founder (operator operates) |
| **Kiosk** | yes | single-site physical deployment+support | founder |

The **recurring ratio** is the core health metric: subscriptions (bundle
recurring + marketplace + cloud + kiosk) should dominate one-time so the
founder's effort isn't re-spent every sale. Operator mode raises how many
recurring loops one founder can carry.

## 6. Scaling Economics

### 6.1 10 → 50 → 100+ clients
| Tier | Clients | Cost index | Revenue index | Leverage (rev/cost) |
|---|---|---|---|---|
| solo | 10 | 1.0 | 1.0 | 1.00 |
| operator | 50 | 2.4 | 4.2 | 1.75 |
| platform | 100 | 4.5 | 11.0 | 2.44 |

Revenue outpaces cost at each step; **leverage improves monotonically**
(1.00 → 1.75 → 2.44) — the whole point of platformizing + automating.

### 6.2 Solo founder capacity rules
- Max 2 client builds in parallel.
- Support ratio ≤ 30 clients per founder before operator-assist.
- Retainer automation **must be live before 50 clients**.
- Acquisition is limited by **deployment capacity, not demand** — a solo
  founder's honest constraint.

### 6.3 Automation leverage (operator mode)
Phase-9 operator mode absorbs onboarding, setup, deployment prep, monitoring,
and moderation, so the founder's time concentrates on legal approval, closing,
and exceptions. That is what makes 50–100 clients feasible for one founder.

### 6.4 Revenue/cost leverage curve
The computed leverage `[1.00, 1.75, 2.44]` matches the registry's stored curve;
KPIs track `revenue per client` and `revenue per effort` to confirm the curve
holds in practice.

## 7. Phase 10 Roadmap

| Stage | Name | Gates | KPIs |
|---|---|---|---|
| **10.1** | Monetization Core | tier_index_model_verified; conversion_ledger_founded | offer set complete; price consistency rate |
| **10.2** | Offer System | core_persona_bundle_offers_live; kiosk_cloud_creator_offers_defined | offer publish rate; quote-to-proposal time |
| **10.3** | Acquisition Engine | outreach_scripts_ready; referral_flow_live; pilot_workflow_verified | qualified leads/month; pilot→diversification rate |
| **10.4** | Revenue Loops | recurring_loop_live; marketplace_split_verified; cloud_kiosk_loops_live | recurring ratio; loop churn rate |
| **10.5** | Scaling Economics | capacity_rules_respected; automation_leverage_verified; leverage_curve_monotone | revenue/client index; revenue/effort index; capacity utilization |

### Stage detail
- **10.1 Monetization Core (current).** Establish the tier-index model and the
  founder conversion ledger; verify price consistency across personas/bundles
  (39/39 registry checks pass).
- **10.2 Offer System.** Publish all 14 offers; slash quote→proposal time.
- **10.3 Acquisition Engine.** Outreach scripts + referral flow live; pilot→
  diversification workflow proven before scaling.
- **10.4 Revenue Loops.** Stand up the 5 loops; get the recurring ratio up and
  churn down.
- **10.5 Scaling Economics.** Grow 10→50→100 strictly inside capacity rules with
  operator-leverage verified and the leverage curve monotone.

### Cross-stage discipline
Real, verified gates at every stage (matching the whole chain). Acquisition
never outruns deployment capacity (§6.2). Recurring dominance and the leverage
curve are monitored forward so a solo founder sees overcommit coming. Legal
steps (proposal, payment) stay founder-owned in every revenue loop.

## 8. Verification & File Map

- **Revenue battery:** 39/39 checks — schema-valid; unified tier-index model;
  conversion founder-defined and out-of-repo; persona offers match both the
  commercial catalog and the Studio preset set; all 14 offers (3 core / 5
  persona / 3 bundle / kiosk / cloud tenant / marketplace creator); acquisition
  = 3 channels + non-salesy messaging + pilot→diversify→scale + referral +
  "websites with AI staff" positioning; 6-step sales workflow with founder-legal
  (proposal, payment) split from operator-automated steps; exactly 5 revenue
  loops; scaling economics 10/50/100 with monotone cost/revenue and leverage
  improving 1.00→1.75→2.44 matching the stored curve; capacity rules and
  operator-leverage present; roadmap 10.1–10.5 correct with gates and KPIs; no
  secrets, no currency literals.
- **Artifacts:** `maya_identity/revenue/revenue_plan.json` ·
  `revenue_plan.schema.json` · blueprint `MAYA_MONETIZATION_AND_CLIENT_ACQUISITION_BLUEPRINT.md`.
- **Chain:** Phase-5 commercial catalog (persona packages, bundles,
  abstract_index) → Phase-6 platform economics (70/30) → Phase-9 operator mode
  (automation leverage) → Phase-10 revenue engine. Pricing stays abstract and
  conversion founder-owned; automation never touches the legal steps of revenue.