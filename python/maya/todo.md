
## Historical pattern-mapping holdout simulation
- [ ] Select a well-documented historical story and define the information cutoff.
- [ ] Gather primary or authoritative sources for the pre-cutoff timeline and known outcome.
- [ ] Build a blinded simulation fixture containing only pre-cutoff information.
- [ ] Run Maya's pattern mapper without exposing the outcome.
- [ ] Compare mapped predictions, alternatives, uncertainty, and omissions with the actual history.
- [ ] Recommend and implement only safe, user-reviewable mapping improvements.
- [ ] Re-run regression and safety tests; document limitations.
- [ ] Report the result and whether Maya is close or still far from the target.

## Multi-scenario historical holdout benchmark
- [ ] Define the scenario suite and common evaluation schema.
- [ ] Source authoritative timelines and record each source URL.
- [ ] Build blinded pre-outcome fixtures with held-out outcomes.
- [ ] Run the baseline mapper across all scenarios and collect misses.
- [ ] Group failures by ontology, temporal, causal, uncertainty, and response gaps.
- [ ] Implement bounded improvements without changing safeguards or personal-memory behavior.
- [ ] Rerun the identical benchmark and compare coverage, failure rate, and regressions.
- [ ] Save the benchmark dataset, results, and a final limitations report.

## Mixed individual-and-circumstance benchmark expansion
- [ ] Add individual-level cases with explicit consent-safe, non-diagnostic evaluation boundaries.
- [ ] Add circumstance-level cases covering failures, rescues, pivots, and resource crises.
- [ ] Keep personal scenarios synthetic or user-approved; do not use private third-party data.
- [ ] Score observed-pattern detection, causal sequencing, uncertainty calibration, alternative paths, and safe next-step framing.
- [ ] Track false positives, missed patterns, unsupported certainty, and safeguard regressions separately.

## Individual-within-circumstance and multi-user collision benchmark
- [ ] Define public, shared, private, and consented data boundaries.
- [ ] Add synthetic scenarios where users have colliding goals, resources, or interests.
- [ ] Test whether Maya separates private memories from shared circumstance facts.
- [ ] Test competing-benefit decisions without silently prioritizing one user.
- [ ] Require explicit consent before cross-user coordination or information sharing.
- [ ] Detect conflicts, disclose tradeoffs, and return human-reviewable alternatives.
- [ ] Measure privacy leakage, unfair priority, unsupported inference, and safe abstention.

## Same-scenario, different-character benchmark
- [ ] Define one shared circumstance and multiple contrasting synthetic characters.
- [ ] Keep outcomes hidden and run each character independently.
- [ ] Measure whether maps differ when goals, constraints, and preferences differ.
- [ ] Compare mapped options with each character’s held-out outcome.
- [ ] Test cross-character privacy leakage and accidental profile mixing.
- [ ] Harden character-conditioned mapping if differentiation or isolation fails.

## Real multi-person historical conditional-prediction test
- [ ] Select a documented event with identifiable individuals and a shared circumstance.
- [ ] Define a cutoff and hide all aftermath information from Maya.
- [ ] Generate individual and full-circumstance if-then maps.
- [ ] Compare mapped paths with documented subsequent events.
- [ ] Score conditional closeness, misses, false positives, hindsight contamination, and privacy safety.
- [ ] Harden the framing so “then you should” remains a human-reviewable option, not an automatic instruction.

## Reverse historical reconstruction benchmark
- [ ] Define reverse abduction versus prediction and mark hindsight-sensitive fields.
- [ ] Build an ending-to-root Apollo 13 timeline from authoritative sources.
- [ ] Reconstruct full-circumstance and individual causal chains separately.
- [ ] Compare inferred causes, missed causes, and candidate mistakes with the documented record.
- [ ] Track false causal links and unsupported blame separately from useful structural matches.
- [ ] Add bidirectional mapping safeguards and rerun regression tests.

## Historical figure head-and-tail simulation
- [ ] Select a well-documented historical figure with a clear early-life head and end-goal or outcome tail.
- [ ] Source authoritative biography materials and define the hidden middle interval.
- [ ] Give Maya only the head, constraints, and tail; keep the documented middle withheld.
- [ ] Generate multiple plausible middle paths rather than one deterministic story.
- [ ] Compare path elements with the documented biography and record misses and false links.
- [ ] Harden against hindsight, biography completion bias, and unsupported psychological claims.

## Societal-force head-and-tail integration
- [ ] Add multiple external-force scenarios around the same historical figure and end goal.
- [ ] Model competing actors or institutions with separate interests and privacy boundaries.
- [ ] Generate conditional middle paths for each societal scenario without leaking private character context.
- [ ] Compare how constraints alter path ranking, opportunity access, and likely tradeoffs.
- [ ] Distinguish historical evidence, inferred mechanisms, and uncertainty in every output.
- [ ] Measure path stability, scenario sensitivity, false positives, and hindsight risk.

## Decision-pattern integration
- [ ] Add individual decision tendencies, goals, constraints, and risk tolerance as explicit inputs.
- [ ] Add circumstance, society-at-the-time, rules, resources, and competing actors.
- [ ] Represent decisions as sequences with triggers, alternatives, reversibility, and consequences.
- [ ] Score desired-outcome fit without treating social conditions as destiny.
- [ ] Narrow one recommended direction while retaining alternatives and uncertainty.
- [ ] Test for deterministic conclusions, unfair social assumptions, privacy leakage, and unsupported certainty.

## Neutral world-model layer
- [ ] Define a bounded world snapshot instead of claiming a complete view of everything.
- [ ] Store source, timestamp, confidence, evidence type, and competing perspectives for each claim.
- [ ] Separate observable facts from forecasts, interpretations, and value judgments.
- [ ] Keep world context separate from each user’s private character and approved memory.
- [ ] Personalize only after applying the user’s explicit goals, constraints, values, and consent.
- [ ] Make recommendations conditional, explainable, reversible, and human-reviewed.
- [ ] Test source bias, missing-data effects, stale information, and hidden opinion.

## Historical-head/current-state/conditional-tail world model
- [ ] Define the historical head as sourced baseline conditions and recurring patterns.
- [ ] Define the current state as time-stamped signals, actors, resources, and constraints.
- [ ] Detect whether patterns are strengthening, weakening, repeating, breaking, or changing direction.
- [ ] Produce conditional tails rather than fixed future predictions.
- [ ] Connect each world path to the user’s approved goals and character data.
- [ ] Preserve source provenance, uncertainty, alternative paths, and privacy isolation.

## Prediction-limit benchmark
- [ ] Separate structural coverage from actual held-out outcome accuracy.
- [ ] Combine forward, reverse, individual, societal, collision, and head-tail results.
- [ ] Calculate false positives, misses, single-path versus multi-path recall, and safety failures.
- [ ] Identify which claims are safe for a pitch and which claims must be rejected.
- [ ] Write a pitch-safe capability and limitation report.

## Local integration and PC readiness
- [ ] Identify which tested layers are safe to integrate into the desktop app.
- [ ] Keep heavy research and Ollama optional so deterministic fast paths remain local.
- [ ] Expose review-only conditional mapping and decision-pattern summaries through Maya’s router.
- [ ] Preserve memory, security, mission-integrity, system-preservation, and emergency-stop walls.
- [ ] Run compile, routing, mapping, resource, and safeguard regression tests on this PC.
- [ ] Document what works locally and what still depends on Ollama or external sources.

## Implement validated mapping layers
- [ ] Integrate decision-pattern summaries into the local conversation workflow.
- [ ] Integrate conditional outcome ranking with explicit evidence and alternatives.
- [ ] Integrate societal and competing-interest context without sharing private memory.
- [ ] Keep prediction-limit reporting accessible locally.
- [ ] Preserve human review, consent, no-memory-write, no-external-action, and emergency-stop safeguards.
- [ ] Rerun desktop regression and resource tests after implementation.

## Supervised self-improvement loop
- [ ] Define allowed learning signals: confirmed outcomes, user corrections, dismissed suggestions, and verified evidence.
- [ ] Create an append-only outcome and error ledger with no automatic trusted-memory promotion.
- [ ] Detect recurring misses, false positives, calibration errors, and context-specific failures.
- [ ] Generate improvement proposals as data/rule changes rather than arbitrary code rewrites.
- [ ] Test proposals against frozen regression cases and safety invariants in a sandbox.
- [ ] Require explicit user approval before activation and preserve rollback/version history.
- [ ] Add local reports showing what Maya learned, why, and how confidence changed.

## Concise relevant conversation mode
- [ ] Inspect the local response prompt and continuity context assembly.
- [ ] Add a concise-answer policy that permits one-sentence answers when sufficient.
- [ ] Keep only topic-relevant context and preserve the current conversational thread.
- [ ] Defer optional detail until the user asks for more.
- [ ] Keep safety, approval, and local-command behavior unchanged.
- [ ] Add tests for short answers, follow-ups, irrelevant context exclusion, and continuity.

## Fix Maya identity and concise research behavior
- [ ] Add an explicit approved Andy identity context.
- [ ] Summarize public research instead of dumping raw source pages into the chat window.
- [ ] Keep ordinary user questions out of the automatic research path unless research is requested.
- [ ] Make Ollama timeout fallback answer the detected topic briefly when possible.
- [ ] Test the desktop router and preserve safeguards.

## Fix Andy topic anchoring
- [ ] Test multiple Andy identity questions through the actual local router.
- [ ] Prevent owner-identity questions from entering public web research.
- [ ] Prevent entity-name search results from merging unrelated topics.
- [ ] Ensure each answer has one topic and no unrelated paragraph spillover.
- [ ] Rerun UI and safeguard regressions.

## Keyboard controls and future voice startup
- [ ] Define shortcuts that do not conflict with emergency stop or common OS shortcuts.
- [ ] Add a launcher script for wake-and-open and focus-or-open behavior.
- [ ] Bind in-app shortcuts for status, focus, help, and safe close.
- [ ] Document Windows-first controls and portable macOS/Linux equivalents.
- [ ] Keep future voice startup confirmation-controlled and separate from privileged actions.
- [ ] Test shortcut scripts and preserve all safety regressions.

## Voice startup preparation and Andy-topic verification
- [ ] Create a voice-startup preparation script with microphone listening disabled by default.
- [ ] Route future wake phrases through the existing fixed launcher only.
- [ ] Require explicit activation and confirmation before privileged actions.
- [ ] Test “Who is Andy?”, “Tell me who Andy is”, and “Who is Andy Warhol?” through Maya’s local router.
- [ ] Verify one-topic answers, concise output, and no unrelated research spillover.

## Smallest useful Maya acceptance test
- [ ] Launch the local desktop app and verify the core is awake.
- [ ] Test greeting, owner identity, concise answer, and one follow-up for continuity.
- [ ] Test one useful pattern or focus command with relevant output only.
- [ ] Verify no unwanted web research, memory write, or external action occurs.
- [ ] Record what the minimum version can do today and what evidence would help it grow.

## Maya company direction
- [ ] Define the public world-information service and its boundaries.
- [ ] Keep public world knowledge separate from private user identity and memory.
- [ ] Map historical patterns, current signals, actor incentives, and possible moves.
- [ ] Add source comparison and misinformation resilience without claiming perfect truth.
- [ ] Translate the engine into practical user-facing services and a first company MVP.

## Credibility and misinformation resilience
- [ ] Define claim-level credibility signals without permanent true/false labels.
- [ ] Track source history, corroboration, corrections, incentives, and manipulation patterns.
- [ ] Learn only from verified corrections and approved evaluation outcomes.
- [ ] Show evidence, disagreement, uncertainty, and reasons for each credibility assessment.
- [ ] Keep credibility analysis separate from private user memory and personalization.
- [ ] Test adaptive adversarial cases so Maya does not become overconfident as tactics change.
- [ ] Plan privacy-preserving cross-device delivery for the public world-information service.

## Tighten Maya’s initial seed from conversation patterns
- [ ] Preserve durable signals: opportunity mapping, building by learning, autonomy, usefulness, and human control.
- [ ] Preserve relevant current constraints: PC-first operation, limited funds/devices, and need for practical next steps.
- [ ] Preserve communication preferences: concise, direct, context-aware, and no unrelated information.
- [ ] Preserve broad interests without treating them as permanent identity or guaranteed priorities.
- [ ] Keep spiritual, philosophical, creative, and entrepreneurial interests available as optional context.
- [ ] Separate temporary frustration, one-off questions, and speculative ideas from durable memory.
- [ ] Allow Andy to correct, delete, or expand the seed at any time.

## Surface Maya’s suggestions safely
- [ ] Inspect whether proposals exist and why the desktop UI does not display them automatically.
- [ ] Define evidence thresholds for surfacing a suggestion without interrupting unnecessarily.
- [ ] Add a review-only pending-suggestions view and a concise notification path.
- [ ] Keep suggestions separate from automatic memory writes, code changes, and external actions.
- [ ] Test no-suggestion, pending-suggestion, approval, rejection, and restart behavior.

## Plant the vision as Maya’s directional seed
- [x] Extract durable vision principles from the referenced conversation.
- [x] Keep the product compass separate from Andy’s personal memories and temporary circumstances.
- [x] Enable hypotheses and directional suggestions before verified learning events.
- [x] Label seed-derived suggestions as hypotheses, not learned facts or predictions.
- [x] Preserve multiple paths, correction, deletion, uncertainty, and human approval.
- [x] Test that seed guidance produces relevant suggestions without unrelated topics or automatic actions.

## Mother Maya proactive suggestion and explicit purpose
- [x] Define a small sample scenario with a clear goal, constraints, and changing circumstances.
- [x] Run it through the seed-level suggestion engine without claiming verified learning.
- [x] Make Mother Maya’s vision explicit in the approved role and purpose context.
- [x] Ensure purpose guides relevance but does not override Andy’s current request.
- [x] Verify the suggestion remains review-only, conditional, and human-choice preserving.

## Integrate Humanity-and-Individual Benefit seed
- [x] Add protected principles for human benefit, dignity, coexistence, agency, compassion, access, change, truthfulness, non-harm, and accountability.
- [x] Add the shared decision pipeline and transparent suggestion record schema.
- [x] Preserve current owner control, rollback, audit, privacy, and external-action safeguards.
- [x] Run an individual-benefit and human-benefit convergence sample.
- [x] Test conflict disclosure, alternatives, uncertainty, and no automatic decision behavior.

## Explicit foundational seed approval
- [x] Record Andy's explicit approval of the Humanity-and-Individual Benefit seed as foundational identity guidance.
- [x] Validate that approval does not activate automatic code, memory, external actions, or safety-wall changes.
- [x] Preserve version history, auditability, rollback, privacy, and human review requirements.

## Reconcile, neutral world model, and suggestion review
- [x] Reconcile duplicate checklist entries against completed files and tests, preserving genuinely pending work.
- [x] Add a neutral world-model evidence record with source, retrieval timestamp, publication timestamp when known, confidence, evidence type, and uncertainty.
- [x] Keep public/world evidence separate from private user context and approved memory.
- [x] Add a pending-suggestion review view with inspect, approve, reject, and correction paths.
- [x] Require explicit human approval before any consequential activation; rejection must not write memory or execute actions.
- [x] Test the new world-model and review workflow with regression and safeguard checks.

## World-model and suggestion-review verification
- [x] Run the full world-model and suggestion-review regression suites.
- [x] Test the world-model CLI with a sample claim and confidence value.
- [x] Inspect pending suggestions and run an approval test with explicit confirmation.
- [x] Confirm approval remains non-activating and preserves memory, external-action, audit, and rollback safeguards.

## Approved suggestion sandbox review and PC-safe roadmap
- [x] Run sandbox and regression review for the newly approved suggestion.
- [x] Inspect the current neutral world-model summary listing and active claims.
- [x] Add a labeled conflicting claim and verify conflict handling without auto-resolving truth.
- [x] Assess remaining Mother Maya work that is safe on the current PC.
- [x] Document actions that require Andy's explicit approval.

## Prioritize next safe batch and pre-upgrade approvals
- [x] Categorize the 162 remaining unchecked items by safety, dependency, and PC resource cost.
- [x] Select the next safe local batch and record why higher-risk items are deferred.
- [x] Run a fresh multi-claim conflict calibration suite and record misses or false flags.
- [x] Design the pending-suggestion approval screen layout and interaction states.
- [x] Identify approvals that enable vision-supporting local work without changing PC effectiveness.

## Andy-approved safe local development batch
- [x] Record approval for deterministic conflict detection and confidence calibration with temporary local fixtures.
- [x] Record approval for public or synthetic hidden-outcome historical holdout testing.
- [x] Record approval for local suggestion review UI, audit views, correction paths, and rollback documentation.
- [x] Record approval for short resource-limited PC safety and minimum-useful acceptance tests.
- [x] Record approval for local reports, opportunity bookmarks, prediction-limit summaries, and provenance displays.
- [x] Record approval for disabled-by-default voice-startup routing with microphone listening and privileged execution disabled.

## Strict current-PC stability boundary
- [x] Defer any work that can cause instability, sustained resource pressure, WSL2 stalls, or reduced responsiveness.
- [x] Allow only idle-time, short, deterministic, low-resource local checks with explicit stop conditions.
- [x] Keep continuous sensing, heavy model generation, background loops, system changes, and privileged actions disabled.
- [x] Record the current-PC safe scope and hardware-upgrade prerequisites.
