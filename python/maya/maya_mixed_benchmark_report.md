# Maya Mixed Individual-and-Circumstance Benchmark

This benchmark compares the prior opportunity mapper with the bounded event-stream mapper. Outcomes are held out during mapping. Individual scenarios are synthetic and contain no private-person data.

Scenarios: 6 (3 circumstance, 3 synthetic individual)
Baseline average coverage: 0%
Hardened average coverage: 93%
Hardened failure rate on expected-pattern coverage: 7%

| Scenario | Kind | Coverage | Misses |
|---|---|---:|---|
| apollo13 | circumstance | 100% | None |
| chilean_miners | circumstance | 100% | None |
| netflix_streaming_pivot | circumstance | 100% | None |
| individual_career_choice | individual_synthetic | 100% | None |
| individual_learning_plateau | individual_synthetic | 60% | resource-preservation, uncertainty |
| individual_competing_priorities | individual_synthetic | 100% | None |

## Interpretation

Coverage measures detection of predefined structural patterns in these fixtures. It is not future-prediction accuracy and cannot be generalized from six cases.

## Safety

No memory, profile, permission, or external-action state changed during the benchmark.
