# Maya Commercialization & Persona Package Blueprint

- **Status:** business blueprint v1.0 for a solo founder with a ThinkPad,
  building websites with AI and deploying Maya via the universal embed.
- **Positioning:** you sell **websites with AI staff** and **Maya personas**
  as services. You build sites with AI tooling, configure personas from
  verified packages, deploy through the embed runtime, and hand over.
- **Grounding:** every product fact below is checked against the validated
  commerce catalog (`maya_identity/commerce/commerce_catalog.json`),
  legal templates (`client_legal_copy.json`) and the runtime registries
  (persona ceilings ≤ CHANNEL_MAX; web allowlist; embed modes A/B/C).
- **Honesty rule:** sell only what the runtime can guarantee today. The
  verification battery certifies what this document claims (85/85 checks).

---

## 1. Persona Packages

Pricing is **currency-agnostic** (abstract index; the catalog pins
`currency: abstract_index`). Tiers are quoted in two components:
- **one_time_index** — setup/build (site + persona config + verification).
- **recurring_monthly_multiplier** — fraction of the one-time index per month
  (hosting + support + content updates). Essentials is one-time only.

To make prices concrete, pick an internal base (e.g., base = B; entry = 1.0×B,
premium = 2.5×B) and quote consistently.

### 1.1 AI Receptionist — `receptionist`
- **Target customers:** small businesses, service professionals, clinics and
  studios, event/venue operators.
- **Value proposition (plain language):** a first-contact assistant on your
  site that answers routine questions, points visitors to the right page, and
  never leaves a lead unanswered.
- **Use cases:** hours and directions; booking/appointment routing; FAQ
  answering; after-hours first contact.
- **Tiers:** 1.0 / 1.6 / 2.5 one-time · 0 / 0.15 / 0.40 monthly.
- **Mode:** A (universal iframe). Ceiling: 0.38/0.24/0.008.

### 1.2 AI Tutor — `tutor`
- **Target customers:** schools and academies, course creators, coaching
  practices, edtech startups.
- **Value proposition:** a patient explainer that walks learners through steps
  at their own pace with calm, technical explanations.
- **Use cases:** step-by-step explanations; practice guidance; course landing
  support; revision Q&A on provided material.
- **Tiers:** 1.0 / 1.7 / 2.6 one-time · 0 / 0.15 / 0.40 monthly.
- **Mode:** B (floating widget). Ceiling: 0.40/0.26/0.009.

### 1.3 AI Concierge — `concierge`
- **Target customers:** hotels and hospitality, event planners, membership
  clubs, creator communities.
- **Value proposition:** a welcoming guide that recommends within provided
  offerings, confirms options, and keeps a warm tone without overpromising.
- **Use cases:** menu and offering guidance; event agendas; local
  recommendations (from provided context); member helpdesk.
- **Tiers:** 1.0 / 1.6 / 2.5 one-time · 0 / 0.18 / 0.45 monthly.
- **Mode:** B. Ceiling: 0.35/0.20/0.006.

### 1.4 AI Sales Agent (Explainer) — `sales_agent`
- **Target customers:** product sellers, service firms, freelancers selling
  services, SaaS landing pages.
- **Value proposition:** a grounded explainer that clarifies offers and
  answers prospect questions from provided material and hands off interested
  visitors cleanly — it presents, it does not pressure.
- **Use cases:** pricing and feature questions; intake from provided lists;
  demo-scheduling routing; objection FAQ from provided material.
- **Tiers:** 1.1 / 1.8 / 2.8 one-time · 0 / 0.20 / 0.50 monthly.
- **Mode:** C (full-page). Ceiling: 0.42/0.28/0.010 (highest of the set, still
  ≤ CHANNEL_MAX). Register: information-over-persuasion, no urgency.

### 1.5 Market Analyst Assistant — `market_analyst` (MPM)
- **Target customers:** trading-focused content sites, finance bloggers,
  chart-reading education sites, community research portals.
- **Value proposition:** an interpretive assistant that reads user-provided
  market data for pattern structure, trends, volatility, and risk zones —
  clearly labeled interpretation, never a trading signal or advice.
- **Use cases:** pattern interpretation of user-provided charts; indicator
  readings in plain language; volatility and risk highlighting; structured
  interpretation objects for content embeds.
- **Tiers:** 1.2 / 2.0 / 3.0 one-time · 0 / 0.20 / 0.50 monthly (premium
  carries the compliance + re-verification burden).
- **Mode:** B. Ceiling: 0.25/0.12/0.002 (most restrained). Hard constraints:
  confidence cap 0.5, directive blocklist, financial-safety ruleset,
  interpretation-only disclaimer.

## 2. Website + Maya Bundles

| Bundle | Persona | Included (site + persona + embed + config) | One-time | Recurring | Updates / tweaks |
|---|---|---|---|---|---|
| Website + AI Receptionist | receptionist | accessibility-friendly site; Mode A embed; identity profile + persona config; origin allowlist; verification + handover | site build; persona config | hosting; support + content updates | routine content on plan; persona tweaks beyond allowance quoted |
| Website + AI Tutor | tutor | landing/course site; Mode B widget; teaching corpus wiring from provided material; adaptive-profile config; launch checklist | site build; corpus integration | hosting; support + content updates | curriculum on plan; new modules quoted |
| Website + AI Concierge | concierge | brand-focused site; Mode B embed; offerings database; warm-language config with boundary rules; guest-facing launch | site build; offerings config | hosting; offerings + support updates | menu/agenda on plan; seasonal rebrand quoted |
| Website + AI Sales Agent | sales_agent | conversion landing site; Mode C full-page; offer/pricing corpus; intake + handoff flow; compliance framing | site build; offer corpus | hosting; offers, pricing, support updates | pricing/offers on plan; new offer structure quoted |
| Website + Market Analyst Assistant | market_analyst | content site for interpretation; Mode B embed; MPM presets; disclaimer + compliance copy; verification incl. financial-safety ruleset | site build; MPM + persona config | hosting; interpretation-feed + support updates | presets/instruments on plan; safety-ruleset changes require re-verification and are quoted |

**Recurring vs one-time rule:** the embed and persona are deployed once;
value mostly grows through content upkeep, which is the recurring product.
**Handling updates/tweaks:** agreed allowance of persona tweaks per period;
anything past it (new lessons, new offerings, new instruments) is quoted as
corpus-work. Any change to the financial-safety ruleset (market_analyst)
always triggers the verification gate.

## 3. Founder Operating Model

### 3.1 The solo stack
- **Device:** one ThinkPad, CPU-light, no GPU dependency (verified constraint).
- **AI building:** use AI tooling to generate sites (static-host friendly,
  works with the embed), draft copy, and spin up the config objects that the
  runtime validates.
- **Maya deployment:** configure from the verified persona packages, mount via
  the universal embed (Modes A/B/C), pin origins in the config, run the
  verification sweep, launch.

### 3.2 Simple workflow (one client)
```
client → requirements → choose persona → build site (AI) → configure persona
→ embed Maya → readiness verification → handover → recurring support
```
1. **Qualify:** which bundle fits (receptionist for most small owners, tutor
   for education, concierge for hospitality, sales for product pages,
   market_analyst for content sites doing interpretation).
2. **Build:** AI-generate the site, static deploy; no backend for the client.
3. **Configure:** persona profile + identity profile + origin allowlist +
   embed snippet from the config portal.
4. **Verify:** `maya:mount → maya:ready` handshake; sweep clean; READY gate.
5. **Handover:** site + snippet + admin guide; recurring plan active.
6. **Support:** content updates, persona tweaks within allowance, periodic
   re-verification.

### 3.3 Lightweight support model (realistic for one person)
- **Asynchronous by default:** email + a form + a small status page. No
  24/7.
- **Tiered response:** essentials — update within 5 business days; growth —
  3 business days; premium — 1 business day plus a monthly check-in slot.
- **Fix-over-feature:** first response triages; routine content updates
  batched; anything touching rulesets goes through the verification gate
  (readiness before release).
- **Timeboxing:** cap concurrent active projects (see §5) to keep the one-
  person capacity honest.

## 4. Risk & Safety Layer (Business Side)

### 4.1 Required disclaimers
- **All personas (standard disclaimer, pinned):**
  > Maya is an AI assistant that runs on this website. It is not a human
  > employee, and it is not a licensed professional. Responses do not
  > constitute legal, medical, or financial advice, and no outcome is
  > guaranteed. You are responsible for any decision you make based on this
  > assistant.
- **market_analyst (extra, pinned):**
  > The Market Analyst Assistant provides market-pattern interpretation only.
  > It is not financial advice, not a trading bot, and does not execute trades
  > or take action with any account. It does not predict future prices and
  > makes no promise of profit. Markets are uncertain, and all decisions remain
  > your responsibility.

### 4.2 Contract phrasing to stay safe
Use the nine validated clauses (scope of service; no professional advice; no
guaranteed outcomes; data handling; no automated decisions; liability;
updates and maintenance; termination; intellectual property). Key frames:
- you sell *answers from provided context*, never decision-making systems;
- no sales/placement/enrollment/return guarantees;
- memory-only runtime, no account access, no outbound egress (correct, and
  saleable as privacy);
- liability capped at trailing twelve months’ fees;
- client owns the site content; you own the runtime, personas, and tooling.

### 4.3 Landing-page copy boundaries
Use the validated landing template: headline, three value bullets, three trust
props, CTA, footer disclaimer. **Do not** write: "buy now/sell now" imperatives
from the assistant, "guaranteed profit", "risk-free income", or any outcome
claim. The catalog battery verifies the templates contain none of these.

### 4.4 What you must NOT promise (boundary list)
- Multi-tenant shared-host isolation is **contract-level, not yet
  runtime-enforced** (PROPOSED isolation/sandbox modules). Sell **one
  deployment per site/domain** until that gap closes; multi-site hosting is a
  Phase-2 revenue line gated on it.
- No professional advice, no human-staff equivalency, no guaranteed outcomes.
- No trading, no account integration, no external market data feeds.
- Kiosk mode (D) is future; do not sell it yet.

## 5. First-10-Clients Plan

### Phase 0 — Preparation (before client 1)
- Fix internal base for pricing; draft your own site with the landing template
  and an AI Receptionist demo embed on it (dogfooding).
- Stand up the config portal workflow: snippet → origin pin → sweep → READY.
- Write your contract from the nine validated clauses; prep re-verification
  process for ruleset changes.

### Phase 1 — Two pilot clients (validate the loop)
- **Pilot A:** one small business → receptionist-or-concierge bundle (lowest
  risk, biggest pool).
- **Pilot B:** one content site → market_analyst bundle (validates the
  compliance-heavy path + disclaimer copy in the real world).
- Goals: prove build→verify→handover under 10 working days each; collect
  support load data; confirm pricing feels right at 1.0× base.

### Phase 2 — Four more clients (diversify)
- Add one tutor (school/academy), one sales_agent (product page), and two
  receptionist/concierge repeats drawn from referrals.
- Add the referral mechanic: each active client credits one month of hosting
  for a successful referral.

### Phase 3 — Up to ten (grow the base)
- Reach 10 paying sites. Objective: ≥ 7 on recurring plans, fewest possible
  at essentials-only.
- Introduce the growth lever: content-update retainers + paid persona-tweak
  batches; open the premium monthly check-in slot pool (cap at 2 premium
  accounts while solo).

### Boundaries and KPIs
- **Capacity rule:** keep ≤ 3 concurrent onboarding projects at a time;
  ongoing support load governs how many you can hold.
- **KPIs:** build time per site; time-to-READY; support tickets/month;
  recurring ratio; churn; referral rate; premium share.
- **Gate for phase-up:** at 10 clients, decide solo-scale (stay boutique,
  raise base) vs. phase-2 multi-tenant hosting after the isolation modules
  are implemented and re-audited.

## 6. Validation & File Map

- **Commerce battery:** 85/85 checks — catalog + copy schemas compile; package
  and bundle personas exactly match the web allowlist; all 15 ceiling values
  match the training/MPM registries and sit within CHANNEL_MAX; tier indices
  ascend (one-time) and recurrencing ascends (premium > growth ≥ essentials);
  embedded modes match the blueprint (A/C/B/B/B); contract clause set complete
  (9/9); every disclaimer contains the required safety anchors; zero banned
  outcome-claims or currency symbols in catalog/copy.
- **Artifacts:** `maya_identity/commerce/commerce_catalog.json` · `commerce_catalog.schema.json`;
  `maya_identity/commerce/client_legal_copy.json` · `client_legal_copy.schema.json`.
- **Runtime truth checked against:** web blueprint (modes, allowlist), persona
  training + MPM registries (ceilings), financial-safety ruleset
  (market_analyst), isolation contract (Phase-2 gate).