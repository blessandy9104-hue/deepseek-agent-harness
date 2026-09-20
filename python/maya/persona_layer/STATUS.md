# persona_layer — STATUS: DEPRECATED

**Status:** `deprecated` (decided in MAYA BATCH 8J-A — Identity Layer
Consolidation and Persona Boundary Repair).
**Machine-checkable marker:** `persona_layer.PERSONA_LAYER_STATE == "deprecated"`.

## Why it is deprecated

`persona_layer/` was written as a typed presentation-persona stack (tone
bands, vocabulary sets, emotional ranges, behavioral constraints, rule sets,
and role directives for eight commercial roles). It was committed incomplete:

- `persona_registry.py` and `persona_loader.py` — both imported by the
  original `__init__.py` — were **never materialized anywhere in the
  repository**, so `import persona_layer` failed with `ModuleNotFoundError`.
- No production code, test, or runner ever imported `persona_layer`.
- Its presentation-persona responsibilities overlap the live presentation
  surface that `maya_runtime/personality.py` (channel profiles) and the
  deployment profile deck `maya_identity/profiles/*.json` already provide.

## Replacement

| Concern | Authoritative location |
|---|---|
| Cognitive persona state + fusion | `maya_runtime/intelligence/persona.py` (protocol `maya.persona_fusion.v1`, consumed via `bridge.py` and `bus.py`) |
| Presentation personality (expression/viseme/micro/pace) | `maya_runtime/personality.py` |
| Per-deployment presentation profile deck | `maya_identity/profiles/*.json` (`maya-default.profile.json`, `company_template.profile.json`) |
| Behavioral/safety ceilings | `maya_runtime/core.py` (`CHANNEL_MAX`) + `MAYA_PERSONA_GOVERNANCE_MODEL.md` |

## What was changed (Batch 8J-A)

- `__init__.py` replaced with a deprecation stub that imports cleanly and
  declares `PERSONA_LAYER_STATE = "deprecated"`. The broken imports
  (`persona_registry`, `persona_loader`) are removed.
- The six template modules are retained in place as **historical reference
  only**. They are inert and must not be wired into production.

## History

This package (and its templates) remains in git history. If a future,
non-cleanup decision wants the commercial personas (for example
`persona_layer -> presentation adapter -> personality.py`), it must be
undertaken as a fresh, designed component — not by reviving this boundary.