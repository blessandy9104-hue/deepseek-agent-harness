# Maya pattern-mapping upgrade report

## Scope

The pattern mapper was upgraded from a static three-option opportunity response to a deterministic multi-signal engine. It combines approved profile items, the reviewable interest profile, provisional interest signals, saved or revisited opportunity history, and local reflections when available.

The mapper compares those signals against candidate directions such as supervised AI workflows, research and evidence briefs, creative-technical products, decision-support education, and markets research tools. Each candidate reports matched signals, independent source types, detected constraints, caveats, and a small reversible experiment.

## Confidence hardening

The output uses **relative evidence fit** and qualitative confidence bands rather than claiming a calibrated probability. A candidate remains `tentative` when it has fewer than two matched signals or fewer than two independent source types. Negation and exclusion terms are surfaced as caveats. Privacy, local-only, approval, reversible, low-cost, and no-action constraints are carried into the result when detected.

Every result states that it is review-only and that no memory, permission, purchase, message, trade, or external action was performed. The mapper writes no files.

## Test results

The deterministic pattern benchmark passed all 10 behavior cases, including multi-signal matching, education mapping, negation detection, constraint detection, insufficient-evidence uncertainty, and confidence wording:

```text
{"status": "ok", "cases": 10, "passed": 10, "coverage": 1.0}
```

The existing intent benchmark exited successfully. The live integration smoke test also passed:

```text
{"status": "ok", "natural_fast_path": true, "command_route": true, "no_writes": true}
```

These are behavior-coverage results for deterministic fixtures, not evidence of real-world predictive accuracy. Real reliability must be measured with reviewed user sessions and corrected outcomes.

## Controls

Natural opportunity questions now use the upgraded mapper through Maya’s deterministic fast path. Explicit commands include `:map`, `:pattern map`, `map my opportunities`, and `show probable paths`. The mapper does not activate learning, change permissions, promote memory, browse, or take external action.

Rollback copy before this upgrade:

`C:\Users\Andy\OneDrive\Desktop\Maya_App_Copy.before_pattern_mapping_20260818_215831`
