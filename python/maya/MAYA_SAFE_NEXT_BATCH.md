# Maya safe next batch and approval boundaries

## Prioritization result

The previous count of 162 unchecked items represented the checklist before this verification request added five new audit entries. Those five entries are now implemented or verified, so the genuinely pending work returns to the earlier backlog. The backlog is best treated as a dependency queue rather than a single score.

| Priority | Next local batch | Safety and resource profile | Reason to do next |
|---|---|---|---|
| 1 | Expand conflict and source-comparison tests | Safe local; bounded temporary fixtures | Improves truthfulness without granting authority or external access |
| 2 | Add confidence calibration and stale-evidence checks | Safe local; deterministic processing | Makes uncertainty visible before broader research |
| 3 | Complete pending-suggestion review states and audit views | Safe local; human-gated | Turns the current review commands into a trustworthy daily workflow |
| 4 | Run public or synthetic historical holdout benchmarks | Safe local if outcomes remain hidden and data is sourced | Tests mapping quality without changing permissions |
| 5 | Improve prediction-limit and weekly reports | Safe local; output-only | Makes capability and limitation legible to users |
| 6 | Run resource, restart, emergency-stop, and minimum-useful acceptance tests | Safe local; short bounded runs | Protects PC responsiveness and recovery behavior |

Heavy continuous Ollama generation, unrestricted browsing loops, continuous screen or microphone observation, driver installation, and autonomous desktop control are deliberately deferred because they may reduce responsiveness or change the machine’s privacy and control boundary.

## Pending-suggestion approval screen

The Notebook review window is designed as a human gate rather than an automatic action panel. Its top area identifies the screen as `SUGGESTION REVIEW / HUMAN GATE` and states that approval only prepares the next sandbox/regression stage.

The central area contains a suggestion-ID field and an inspection area. The bottom action row contains `Inspect`, `Prepare Approval`, `Prepare Rejection`, and `Close`. The prepare buttons only place the exact command into Maya’s main command line; they do not send it. Andy must still see the command and press `Send`.

The approval state flow is:

`pending_review` → inspect → explicit confirmation → `approved_pending_sandbox_and_regression` → sandbox and regression review → separate activation approval.

The rejection flow is:

`pending_review` → inspect → explicit confirmation → `rejected_by_user`.

Approval and rejection both remain non-activating and preserve audit, rollback, privacy, memory, and external-action boundaries.

## Approvals that are safe to grant now

These approvals do not alter the current PC’s operating effectiveness because they authorize bounded local development and testing only:

| Approval | Scope | Why it is low risk |
|---|---|---|
| Continue deterministic conflict and confidence calibration | Temporary local fixtures and test files | No privileged access, no external action |
| Continue public/synthetic historical mapping benchmarks | Sourced or synthetic evaluation data | Does not use private third-party information |
| Build and test the pending-suggestion review UI | Local Tkinter UI and review metadata | Actions remain staged and manually sent |
| Improve reports, audit views, and rollback documentation | Local output and documentation | Does not change system permissions |
| Run short resource and emergency-stop regression tests | Bounded local test processes | Validates protection rather than expanding authority |
| Prepare disabled-by-default voice-startup routing | No microphone listening or privileged execution | Planning only until separately enabled |

These are development approvals, not blanket authorization for Maya to act autonomously.

## Approvals that should remain separate

Andy should separately approve any activation of continuous presence, microphone listening, unrestricted observation, unrestricted web access, new connectors or accounts, personal-memory changes, cross-user sharing, desktop application control, brightness/power/cooling/process control, package or driver installation, startup services, changes to mission/security/system-preservation walls, or activation of code after sandbox review.
