# Maya self-evolution and adaptive-learning audit

## Audit conclusion

Maya does not currently possess an unrestricted self-rewrite loop. The `evolve.py` entry point can create a copied candidate and run a syntax check, but it does not activate, install, or replace the live assistant. Inference from approved evidence creates `pending_review` profile candidates; the approved profile is changed only through the explicit profile approval command. Background research logs previews and explicitly records that no memory update occurred.

The audit did identify one genuine boundary gap: `browser_observe.py` previously read the local Chrome DevTools tab list whenever it was run and consulted a separate network policy, without checking the newer observation policy or Presence Mode state. That path is now hardened.

## Hardening applied

`browser_observe.py` now requires all of the following before it reads browser-tab metadata:

1. `observation_policy.json` must explicitly enable `enabled_sources.browser_tabs`.
2. `maya_activation_state.json` must report both `active: true` and `presence_mode: true`.
3. The policy must remain local-only and raw-content storage must remain disabled.
4. The existing network host filter still applies.

`observation_policy.json` now declares `browser_tabs: false` explicitly. Therefore browser observation is blocked by default, consistent with the current Presence Mode requirement.

## Verified protections

The audit confirmed that profile inference writes candidates with `status: pending_review`; it does not approve them. Approved profile memory requires the separate approval path. `maya_learning.record_signal` only records while learning mode is active and writes provisional interest data, not trusted memory. The background research worker reads the configured interest profile, performs public GET-only research, writes a bounded preview log, and records `memory_update: not_performed`. The activation manager sets Presence Mode to false during learning activation.

The memory audit and deletion feature also require explicit confirmation for deletion. Reflection and onboarding records are marked local or pending rather than approved memory. Opportunity bookmarks are explicit local commands and do not trigger financial or external actions.

## Remaining limitations

The public research engine is broad public-web retrieval rather than a strict source allowlist. It blocks credentials, localhost, private IPs, and non-HTTP schemes, but a future production version should add stronger domain policy, redirect validation, response-size limits, and clearer source trust ranking. The profile CLI is safe when used as intended, but local machine access is inherently trusted; a future packaged application should route all mutations through one audited service instead of leaving multiple direct file mutators.

Free-form Ollama conversation remains latency-limited on the current hardware. That is a reliability limitation, not an adaptive-permission failure; the deterministic local paths remain the safer demonstration surface.

## Test result

The Windows audit compiled the relevant modules and passed adversarial checks:

```text
{"status": "ok", "browser_observation_blocked_by_default": true, "inference_pending_only": true, "evolution_does_not_activate": true}
```

A rollback copy of the app folder was created before hardening.
