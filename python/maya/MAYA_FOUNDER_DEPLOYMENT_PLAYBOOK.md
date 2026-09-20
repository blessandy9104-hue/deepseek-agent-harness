# Maya Founder Deployment Playbook — First 10 Clients

- **For:** solo founder, one ThinkPad, no GPU dependency, AI-assisted builds.
- **State of the system:** Maya is verified and stable (sweep 18/18, READY
  protocol v2.0) and deployable through the universal embed on any website.
- **Guarantee of practicality:** every form, script, and checklist below is a
  validated artifact (`maya_identity/founder/founder_templates.json`,
  35/35 checks). Use them as-is or adapt the wording; the safety boundaries do
  not change.
- **Goal of this playbook:** acquire and deploy to your first 10 clients in
  ~16 weeks while staying inside the verified runtime and business-safety
  boundaries.

---

## 1. Founder Setup

### 1.1 Minimal stack
- **Hardware:** one ThinkPad (CPU-light is a verified constraint — no GPU, no
  cloud compute needed).
- **AI tools for building:** AI site generators for static pages (works with
  the embed), AI copy drafting (then paste content into personas you configure
  manually), and this repo’s verification tooling for every deploy.
- **Maya runtime:** local Maya runtime + `maya_identity` registries + embed
  runtime (Modes A/B/C) + sweep/readiness gate.
- **Services (zero backend):** static hosting for client sites; the embed
  loads from the Maya origin (`/embed`, `maya.js`); nothing else needed.

### 1.2 Recommended folder structure
```
maya-project/
├── maya_runtime/            # core runtime (never redistribute)
├── maya_identity/           # profiles, personas, registries (config source)
├── verification/            # sweep + readiness (run before every launch)
├── clients/
│   └── <slug>/
│       ├── intake/          # onboarding template answers (no end-user PII)
│       ├── site/            # AI-built static site
│       ├── config/          # embed_config.json, origin pin, mode, persona
│       ├── verify/          # sweep output + READY record
│       └── handover/        # admin summary, contracts, support notes
└── playbook/                # this file + founder templates
```
Rule: one folder per client; no end-user personal data anywhere (embed is
memory-only; intake holds business context only).

### 1.3 Client onboarding template
Use the 10 validated fields (OB01–OB10): business name/sector, existing site,
primary goal, who visits, top questions, source material, preferred embed
style, live domain, tier, and — mandatory for market_analyst — consent to the
interpretation-only disclaimer. Run the 6-item intake checklist (exact origin,
client-approved material, persona from allowlist, abstract-tier quote,
disclaimer in proposal, financial consent before any market_analyst work).

### 1.4 Persona selection guide (from the validated decision rows)
| If the client … | Persona | Why |
|---|---|---|
| …needs first contact for hours/directions/services | receptionist | Low-risk, never leaves a visitor hanging |
| …explains lessons step by step for learners | tutor | Adaptive teaching, calm register |
| …is hospitality/events/memberships/communities | concierge | Warm guidance, no overpromising |
| …has offers on a landing page to explain + hand off | sales_agent | Information-over-persuasion |
| …runs chart/market-structure content | market_analyst | Interpretation-only, financial-safety ruleset |

Modes follow the catalog: receptionist A, tutor B, concierge B, sales_agent C,
market_analyst B.

## 2. Client Acquisition Strategy — Positioning “Websites with AI Staff”

One message, repeated plainly: **you build simple websites with an AI
staff member that answers visitors’ routine questions, honestly and without
hype.** Outbound is founder-style: short, specific, no guarantees, one clear
next step.

### 2.1 Phase 1 — two pilot clients (validate the full loop)
- **Pilot A — small business, receptionist:** demonstrate the universal iframe
  on their existing site; goal is a working `mount→ready→reply` in days.
- **Pilot B — content/trading-education site, market_analyst:** prove the
  compliance-heavy path end to end (financial consent, disclaimer, MPM
  interpretation trace, re-verification readiness).

### 2.2 Phase 2 — four diversification clients
- **tutor** (school/academy or course creator), **concierge** (hospitality or
  member community), **sales_agent** (a product landing page), and one more
  **creator-community concierge** (creator-assistant use case). These four
  exercise every embed mode and corpus type: lessons, offerings, offers.

### 2.3 Phase 3 — four scaling clients (mixed personas)
- Two receptionist/concierge repeats from referrals, one tutor, one sales_agent
  or market_analyst, chosen by local demand. Recurring plans become the norm.

### 2.4 Outreach scripts (non-salesy, founder-style)
Validated drafts in `founder_templates.json` under `outreach`:
- **Pilot A (small business):** “I build simple websites with an AI
  receptionist that answers your visitors’ routine questions any time. No new
  tech on your side — it embeds like a widget. I can set up a free demo on your
  current site. No contracts, just a try.”
- **Pilot B (market analyst):** “…an assistant that gives pattern and
  volatility interpretations on user-provided data — clearly labeled as
  interpretation, never trading advice or a bot.”
- **Diversification (tutor / sales explainer):** one clear value line, “setup
  is a short call and a few documents”, “calm, factual, no pressure language”.
- **Scaling (retainer):** “your assistant's answers depend on your content
  staying fresh. I keep offers, FAQs, and menus updated monthly and tune
  wording within your allowance.”
- **Referral:** one month of hosting credited for a successful intro.

Battery-verified boundaries: no guaranteed-traffic/sales lines, no “will
increase revenue”, no prediction or trading language, every script concise.

## 3. Deployment Workflow (Step-by-Step)

Eight gated stages (template: `deployment_checklist.stages`):

1. **Requirements intake** — send OB01–OB10; confirm exact origin, tier,
   persona. (no gate)
2. **Persona selection** — map goal to decision row; pull persona profile +
   ceiling; for market_analyst confirm disclaimer consent. (no gate)
3. **Website build** — AI-generate the static site from approved material;
   deploy to static host; leave the embed slot ready. (no gate)
4. **Embed runtime integration** — emit the snippet for the chosen mode; pin
   the exact origin; set token TTL (≤900 s) and slot quota; confirm the MSG.v1
   envelope on staging. **Gate: `maya:mount → maya:ready` handshake.**
5. **Persona configuration** — set register from person profile; wire approved
   material as provided context; enable persona safety rules (financial
   blocklist + disclaimer for market_analyst). (no gate)
6. **Verification and readiness** — run the 18-suite sweep; confirm
   external_clean ∧ internal_stable and the mount-to-ready gate. **Gate: READY.**
7. **Client handover** — deliver site access + admin summary + support contact
   + update allowance; close with the loaded disclaimer and signed contract.
   **Gate: handover.**
8. **Support loop** — batch content updates within tier SLA; run periodic
   re-verification; re-quote anything beyond the tweak allowance. **Gate: sweep
   clean is maintained for active sites.**

Per-client time budget (solo): build 2–4 days; config + verify 1 day; handover
half a day; support ≈ 2 h/week/client.

## 4. Pricing & Packaging Execution

### 4.1 How to present tiers
Quote as **one-time index + recurring multiplier** in abstract bands, then
render with your chosen base. One framing that works: *“One-time setup [1.0×]
gets you live; the monthly plan [0.15×] keeps it fresh — hosting, updates, and
wording tweaks within your allowance. Premium [2.5× one-time, 0.40× monthly] adds
a priority lane and a monthly check-in slot.”* Always show all three
alternatives side by side (essentials / growth / premium).

### 4.2 Recurring vs one-time, explained in one sentence
- **One-time = what it takes to go live** (site build, persona configuration,
  verification).
- **Recurring = what keeps it good** (hosting, content updates, support,
  periodic re-verification).
Never sell “lifetime” maintenance; recurring is where the business compounds.

### 4.3 How to upsell personas safely
- Offer the **recurring content retainer** first (keeps answers accurate —
  this is also a safety feature, not just revenue).
- Offer **persona tweaks within allowance**; anything beyond allowance is
  quoted corpus-work.
- Add a second persona only when the site genuinely serves two audiences (e.g.,
  receptionist + tutor on a school site) — via the switching protocol, never by
  self-customizing a profile.
- **market_analyst is not an upsell path:** do not suggest adding it to a
  retail site; only content sites doing market interpretation qualify.

### 4.4 Avoiding financial-advice violations (market_analyst guardrails)
- Relentlessly interpret-only: patterns, trends, volatility, risk zones —
  “picture of the chart”, never “what you should do”.
- No “predict”, “target”, “expects to reach”, “you should”, “buy/sell/hold”
  anywhere in copy or replies (validated blocklist plus confidence cap 0.5).
- Never attach to a broker/platform/account; no execute language.
- Always include the market analyst disclaimer and the “interpretation only,
  not a trading bot” line; require OB10 consent before engagement.
- Any change to the financial-safety ruleset forces re-verification before
  relaunch.

## 5. Risk & Safety (Business Side)

- **Contract:** the nine validated clauses apply to every engagement — scope of
  service (answers from provided context, no decision systems); no professional
  advice; no guaranteed outcomes; data handling (memory-only, no account, no
  egress); no automated decisions; liability capped at trailing 12 months;
  updates/maintenance; termination (30 days); IP split (client owns content,
  you own runtime + personas + tooling).
- **Disclaimers:** standard (not a human employee, not a licensed professional,
  no legal/medical/financial advice, no guaranteed outcomes, user
  responsibility) plus the market analyst variant (not financial advice, not a
  trading bot, no prediction, no profit promise, markets uncertain).
- **Landing copy:** headline + 3 value bullets + 3 trust props + CTA + footer
  disclaimer from the validated template; zero banned outcome claims.
- **Multi-tenant hosting boundary:** shared-host multi-tenant isolation is
  *contract-level only until `maya_runtime/isolation/*` and `sandbox.py` are
  implemented* (audit finding). Therefore: sell **one deployment per
  site/domain** now; hosting several clients on shared capacity is a Phase-5
  option gated on that implementation + re-audit. Do not promise cross-tenant
  separation you cannot yet verify.
- **Operational hygiene:** keep folder-per-client (no cross-client material),
  exact-origin allowlists, per-slot quota + TTL, and a READY record before every
  go-live.

## 6. First-10-Clients Roadmap

| Phase | Weeks | Work | Exit criterion |
|---|---|---|---|
| 0 · Setup | 1 | Stack, folders, templates, demo site with own AI Receptionist | Demo live + READY |
| 1 · Pilots | 2–5 | 2 pilots: receptionist + market_analyst | Both live; handover time known |
| 2 · Diversify | 6–10 | tutor, concierge, sales_agent, creator-concierge | ≥ 3 of 4 on recurring plans |
| 3 · Scale | 11–16 | 4 scaling clients (mixed personas) | Reach 10 clients |

**Capacity rule (solo):** ≤ 3 concurrent onboarding builds at any time;
ongoing support load decides whether you take a 4th. Support SLA by tier:
essentials 5 business days, growth 3, premium 1 + monthly check-in slot.

**KPIs**
- Build time per site (target ≤ 5 working days, verify-inclusive).
- Time-to-READY (target ≤ 2 working days from site ready).
- Recurring ratio (target ≥ 0.7 by client 10).
- Support tickets/month per client (target ≤ 2).
- Referral rate (goal: ≥ 3 of clients 6–10 come from referrals).
- Premium share (target ≥ 20%).

**Phase-up gate to Phase 5 (“Scaling Maya”)** — all of:
1. 10 clients live, ≥ 7 on recurring, churn < 1/month.
2. Build time + support load within the ≤ 3-concurrent capacity.
3. Decision: either raise the base (boutique, reserve margins) or pursue
   multi-tenant hosting — the latter **only after `isolation/*` +
   `sandbox.py` are implemented and the full-system audit re-runs with a
   multi-tenant verdict** (currently `issues_detected` on that single gap).
4. Every market_analyst site re-verified against the financial-safety ruleset
   within the last 90 days.

## Annex — File Map
- Blueprint (business): `MAYA_COMMERCIALIZATION_AND_PERSONA_PACKAGES.md`
- This playbook: `MAYA_FOUNDER_DEPLOYMENT_PLAYBOOK.md`
- Templates: `maya_identity/founder/founder_templates.json` + `.schema.json`
- Catalog + legal copy: `maya_identity/commerce/*`
- Web embed config + envelopes: `maya_identity/web/*`
- MPM persona + financial rules: `maya_identity/market/*`
- Verification: `verification/sweep.py` (18 suites) · readiness + stabilization
  (protocol v2.0)