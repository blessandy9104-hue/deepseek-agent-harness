# Maya Website Integration Blueprint — Universal Embed Runtime

- **Status:** blueprint v1.0. Web surfaces referenced are EXISTING
  (`maya_runtime/ui/web.py`, `maya_runtime/deploy/web.py`, `rendering`,
  `_loader` normal+headless). Embed endpoints (`/embed`, `/assistant`) and
  `maya.js` are **PROPOSED** appendices over those surfaces.
- **Design posture:** Maya runs as a standalone runtime; a website only loads a
  universal embed. Website builders never see a backend, never register
  platform code, never get memory, account access, or external-API reach.
- **Address in architecture:** MAYA_FULL_DEPLOYMENT_BLUEPRINT §C7 (demo/web
  context), §C8 (enterprise posture), §C9 (tenancy), §C10 (governance).

---

## 1. Universal Embed Runtime

### 1.1 Topology
```
 site origin (static, any host)                     Maya origin
 ┌──────────────────────────────┐   postMessage     ┌─────────────────────────────┐
 │  Mode C page ────────────┐   │   MSG.v1, exact   │ /embed (iframe content)      │
 │  Mode B maya.js ──┐      │   │◄─────────────────►│ /assistant (full page)        │
 │  Mode A <iframe> ─┘      │   │   origin-checked  │ maya.js (widget bootstrap)    │
 │  (no backend, static OK) │   │                   │ persona loader bridge         │
 └──────────────────────────────┘                   │ identity profile bridge       │
                                                     │ web render surface            │
                                                     │ tenant slots + kill switch    │
                                                     │ announcement layer            │
                                                     └─────────────────────────────┘
```

### 1.2 iframe endpoint `/embed`
- Serves the sandboxed runtime UI for Modes A and B. Bootstrap parameters are
  **configuration pointers only** — never secrets: `?origin=…&mode=A|B&persona=
  <allowlisted id>&profile=<tenant profile id>&sid=<session token>`.
- `sandbox="allow-scripts allow-same-origin"` — no allow-top-navigation, no
  allow-popups, no allow-forms. Storage remains denied by application policy
  (memory-only), independent of the flag (below).

### 1.3 widget script `maya.js`
- Lazy-loads the Mode B floating assistant: injects a sandboxed iframe, runs
  the mount handshake, toggles the drawer, forwards user text in the MSG.v1
  envelope, and drops every message that is not from the configured Maya origin.
- `defer`, no dependencies, no network call except the embed load itself.

### 1.4 Sandbox rules (deny-by-default)
Runtime-level deny list (pinned in `embed_config.json`, all eight enforced):
`outbound_http`, `local_storage`, `indexed_db`, `cookie_write`,
`clipboard_write`, `window_top_navigation`, `external_apis`, `account_access`.

Plus transport-level controls: server `Content-Security-Policy
frame-ancestors <allowlisted origins>`; exact-origin check on every inbound
message; unknown origin ⇒ **ignore, no state change**.

### 1.5 Persona loader bridge
- Loads the persona selected by the (allowlisted) `persona` parameter through
  the persona layer (C1). Pinned fail-closed: unknown persona id ⇒ reject mount
  and return `maya:error {code:"persona_unknown"}`; the persona **cannot** be
  changed by the site at runtime — switching goes through the switching
  protocol, site-side requests to change persona are ignored.

### 1.6 Identity profile bridge
- `profile` selects a validated identity profile
  (`maya_identity/profiles/identity_profile.schema.json`) for the tenant slot
  only. No cross-tenant profile reuse; CORED and protected fields never leave
  the runtime; identity surfaces on the site are display-only (`canonical_name`,
  `tagline`, persona-chosen register).

### 1.7 Render surface for web
- `RenderFrame` (bounded; existing rendering determinism) adapts to DOM/canvas
  in the iframe; parity native==headless already verified at READY time and
  asserted per suite. No GPU dependency; CPU-light cadence ≤ 30/s.

### 1.8 Communication channel (postMessage-safe)
- One envelope format, `MSG.v1` (`postmessage_envelope.schema.json`):
  `{version, direction, type, session_id, payload≤16KB}`.
- Event types are a fixed set of six:
  `maya:mount` (site→Maya), `maya:message` (site→Maya),
  `maya:ready` (Maya→site), `maya:reply` (Maya→site),
  `maya:error` (Maya→site), `maya:status` (Maya→site).
- Rules: `targetOrigin` always pinned to the Maya origin; sender verified by
  `event.origin` exact-match against `allowed_origins`; payloads carry **no
  control surface** (no commands other than the six types); no secrets ever in
  an envelope; direction/type pairing validated (battery-verified).

## 2. Website Integration Modes

### Mode A — iframe embed (universal)
```html
<iframe
  src="https://maya.example/embed?origin=https://site.com&mode=A&persona=receptionist&profile=public_pro"
  width="400" height="560" style="border:0;border-radius:12px"
  sandbox="allow-scripts allow-same-origin"
  referrerpolicy="no-referrer"></iframe>
```

### Mode B — script widget (floating assistant)
```html
<script src="https://maya.example/maya.js" defer></script>
<script>MayaEmbed.mount({origin:"https://site.com", persona:"concierge"});</script>
```
`maya.js` (reference implementation):
```javascript
(function () {
  "use strict";
  var MAYA_ORIGIN = "https://maya.example";
  var V = "MSG.v1";
  function frame(persona) {
    var f = document.createElement("iframe");
    f.src = MAYA_ORIGIN + "/embed?origin=" + encodeURIComponent(location.origin) +
            "&mode=B&persona=" + persona;
    f.setAttribute("sandbox", "allow-scripts allow-same-origin");
    f.setAttribute("referrerpolicy", "no-referrer");
    f.style.cssText = "position:fixed;right:16px;bottom:16px;width:380px;height:600px;" +
                      "border:0;border-radius:14px;box-shadow:0 8px 28px rgba(0,0,0,.25)";
    return f;
  }
  function send(target, type, sid, payload) {
    target.postMessage({version: V, direction: "to_maya", type: type,
                        session_id: sid, payload: payload || {}}, MAYA_ORIGIN);
  }
  window.MayaEmbed = {
    mount: function (cfg) {
      var el = frame(cfg.persona);
      document.body.appendChild(el);
      var sid = "webrt_" + Date.now().toString(36);
      window.addEventListener("message", function (ev) {
        if (ev.origin !== MAYA_ORIGIN) return;          // exact-origin drop
        var m = ev.data;
        if (!m || m.version !== V) return;              // envelope check
        if (m.type === "maya:ready") el.style.opacity = "1";
        if (m.type === "maya:reply") console.log("[Maya]", m.payload.text);
      });
      send(el.contentWindow, "maya:mount", sid, {mode: "B", persona: cfg.persona});
    }
  };
})();
```

### Mode C — full-page assistant
```html
<a href="https://maya.example/assistant?origin=https://site.com&persona=tutor">Ask Maya</a>
```
Serves `/assistant` — the full-page surface, same envelope rules, no widget DOM.

### Mode D — kiosk mode (optional future)
Kiosk UI/deploy surfaces already exist (`ui/kiosk.py`, `deploy/kiosk.py`).
Paused for the web blueprint save active until the sandbox/isolation runtime
modules land; kiosk stays single-site, verified-runtime-required per the
deployment matrix in the full blueprint.

## 3. Persona Deployment for Websites

Site-facing set is allowlisted in `embed_config.json`. Ceilings are the
verified `emotional_ceiling` values (all ≤ `CHANNEL_MAX` `{0.5,0.35,0.012}`).

| Persona | Site purpose | expression | viseme | micro | Register |
|---|---|---|---|---|---|
| receptionist | first contact, directions, FAQs | 0.38 | 0.24 | 0.008 | even/warm |
| tutor | explainer, step-by-step guidance | 0.40 | 0.26 | 0.009 | even/technical |
| concierge | recommendations, event flows | 0.35 | 0.20 | 0.006 | warm/even |
| sales_agent | offer explanation (not persuasion) | 0.42 | 0.28 | 0.010 | even/technical |
| market_analyst | market-pattern interpretation (MPM) | 0.25 | 0.12 | 0.002 | even/technical |

Per-persona safety:
- **All:** failure yields fail-closed `calm/even`; drift/taboo/urgency flatten;
  no brand, PII, or CORED leakage.
- **market_analyst:** confidence cap 0.5, directive blocklist, news-as-
  unverified-context, professional disclaimer + uncertainty reminder, humor off
  (persona + `financial_safety_rules.json`).
- **sales_agent:** information-over-persuasion register; no urgency language;
  no offer stability claims (flagged non-determinism).
- **tutor/concierge:** adaptive-teaching ceiling respected; no personalized
  advice beyond provided context.

Switching between these personas at runtime only via the switching protocol
(G1–G10 guards + S1–S4 reset); sites cannot request personas outside the
allowlist and cannot request a switch.

## 4. Multi-Tenant Safety

- **Tenant = site origin slot.** Each mounted origin occupies one tenant slot
  (`max_active_slots: 8`), identified by its origin; short-lived session token
  (TTL ≤ 900 s) scopes the session.
- **Namespaces** follow the isolation contract: `NS(t,k)` = tenant t resource k;
  all reads/writes checked against the tenant's namespace before any action.
- **Identity boundaries:** profiles per tenant slot only; a tenant never
  resolves another tenant's profile id; identity `key_class`/redact rules apply
  on any site-facing surface.
- **Persona boundaries:** persona allowlist is global config; tenant can mount
  only allowlisted personas; no tenant may inject a persona or override its
  profile.
- **Sandbox enforcement:** the eight deny flags + CSP `frame-ancestors` + exact
  origin checks; enforcement is application-level (memory-only runtime) and
  transport-level (no popups/top-navigation via sandbox flags).
- **Forbidden cross-tenant actions** (aligns with F1–F10 contract): reading
  another slot’s namespace; impersonating another origin; replaying another
  tenant’s session token; quota spoofing; sharing profile bundles across slots;
  mutating `embed_config.json` from any site; consuming the account-access path
  (blocked at the sandbox); opening Maya’s own origin chrome from the embed.
- **Enforcement status (honest):** contract + data are complete and validated;
  runtime enforcement of tenant isolation remains the documented PROPOSED gap
  (`maya_runtime/isolation/*`) — single-tenant demo posture until then.

## 5. Runtime Governance

### 5.1 Web authority map
| Authority | Owns | Cannot |
|---|---|---|
| Runtime | serving `/embed`,`/assistant`,`maya.js`; config; READY | change tenant quotas or personas |
| Tenant (site slot) | choose mounted persona (allowlist), session duration | alter config, profiles, boundaries |
| User (browser) | in-boundary chat within the mounted persona | switch persona, escalate registers, reveal suppressed surfaces |
| Persona | all wording/register within its profile | cross into another persona’s boundaries |
| Sandbox | deny-list enforcement | bypass origin checks |
| Readiness | consensus gate before any mount serves | self-declare readiness |

### 5.2 Web session state machine (deterministic W1–W7)
`idle → handshake → mounted → active ⇄ paused → suspended → quarantined → teardown`
- Transition guards are pure predicates (origin exact-match, token TTL, quota,
  anomaly counters) — identical inputs ⇒ identical transitions (no RNG/clocks).
- **Fallbacks:** unknown origin ⇒ stays `idle` (dropped); quota hit ⇒ `paused`
  with `maya:error {code:"tenant_quota_exceeded"}`; persona undefined ⇒ mount
  rejected; E1 ⇒ `paused`+neutralized reply; E2 ⇒ fall back to `calm/even`
  generic; E3 ⇒ `suspended → teardown` (E3 clean halt of the scope).

### 5.3 Persona switching protocol (reused)
Any persona change walks the existing 7-state switching machine: guards G1–G10,
reset S1 (tone) → S2 (expression) → S3 (world scenario) → S4, then `SETTLING →
ACTIVE`; any failure returns to the previous persona or to `calm/even`.

## 6. Output for Integrators

### 6.1 AI-built website flow (no backend, static-host friendly)
1. Founder selects mode + persona in the Maya config portal.
2. Portal renders the exact snippet (Mode A iframe or Mode B script) for their
   origin.
3. Builder (AI or human) pastes the snippet — no backend, no SDK beyond the
   snippet, works on static hosting.
4. The embed loads from the Maya origin; the site never proxied Maya resources.
5. Every postMessage is exact-origin checked; mounts from non-allowlisted
   origins stay in `idle` and are ignored (deny-by-default). Origin entries are
   added by the runtime admin, never self-registered by sites.
6. Session is ephemeral: memory-only, no cross-session state, quota + TTL
   enforced at the slot.

### 6.2 Founder deployment checklist
- [ ] Pick integration mode (A universal, B floating, C full-page).
- [ ] Choose one persona from the site allowlist (receptionist/tutor/concierge/
      sales_agent/market_analyst).
- [ ] Confirm origin string is exact (`https://site.com` — no path, no scheme
      variants).
- [ ] Obtain the snippet from the config portal; paste into the site.
- [ ] Load the page; confirm `maya:mount` → `maya:ready` handshake in console.
- [ ] Verify persona register is correct (market_analyst: disclaimer present;
      sales_agent: no urgency language in outputs).
- [ ] Confirm the session token TTL (≤ 900 s) and slot quota are set.
- [ ] Keep `maya.js` `defer`, no inline crossorigin assumptions.
- [ ] Check CSP on the site host: frame/script sources include only the Maya
      origin.
- [ ] Run the verification sweep and confirm READY before public traffic.
- [ ] Monitor `maya:error` events in the integration test harness (quota,
      persona_unknown, origin_denied).
- [ ] Review the isolation gap contract (PROPOSED modules) before any shared-
      host multi-tenant rollout.

## 7. Certification & Verification

37-check web-embed battery passed (all-green): `embed_config` and
`postmessage_envelope` schemas compile; persona allowlist ⊆ legal set and exact
web scope; per-persona ceilings ≤ CHANNEL_MAX; 8 deny flags complete; memory
strict (memory_only/no-persist/no-cross-session); origin shapes valid; six
event types with correct direction mapping; all six sample envelopes conform to
MSG.v1; tenant slot bounds; zero secret literals in configuration and samples.
Runtime parity remains native==headless per sweep; embed mounts additionally
require the global READY gate (external_clean ∧ internal_stable, protocol 2.0).

## 8. File Map

| Artifact | Path |
|---|---|
| Blueprint | `MAYA_WEBSITE_INTEGRATION_BLUEPRINT.md` |
| Embed config schema + config | `maya_identity/web/embed_config.schema.json` · `embed_config.json` |
| Envelope schema + sample messages | `maya_identity/web/postmessage_envelope.schema.json` · `sample_msgs/*.json` |
| PROPOSED runtime | `/embed`, `/assistant`, `maya.js` (over EXISTING `ui/web.py`, `deploy/web.py`) |
| Guarding contracts | isolation contract, financial-safety rules, persona training set, identity profile schema |