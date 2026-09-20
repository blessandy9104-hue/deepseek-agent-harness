# Maya Prediction-Limit Benchmark

This combines Maya’s recent forward, reverse, individual, societal, collision, and head-tail tests. Structural coverage is kept separate from exact outcome accuracy.

Indicative mean across 8 reported views: **82.1%**.
Indicative mean across real-case views: **80.6%**.

| Benchmark view | Metric type | Result | Real historical case? |
|---|---|---:|:---:|
| mixed six-case structural benchmark | structural | 93% | No |
| Apollo 13 full circumstance | structural | 100% | Yes |
| Apollo 13 individual roles | structural | 85% | Yes |
| Apollo 13 reverse full circumstance | reverse structural | 100% | Yes |
| Apollo 13 reverse individual roles | reverse structural | 79% | Yes |
| Marie Curie best single middle path | hidden-middle recall | 60% | Yes |
| Marie Curie multi-path union | hidden-middle recall | 80% | Yes |
| Marie Curie historical societal path | historical middle fit | 60% | Yes |

## Exact-outcome and safety checks

The synthetic different-character test matched the held-out top option in **100% of 3 cases**. This is a small synthetic fixture, not real-world prediction accuracy.
The multi-user collision test passed its defined safety checks in **100% of 4 synthetic cases**, with **0 privacy leaks**.

| Safety measure | Result |
|---|---:|
| Collision privacy leakage | 0 |
| Cross-character leakage | 0 |
| Reverse blame assignment | False |
| Head-tail single-path claim | False |

## Pitch-safe conclusion

The most defensible combined figure is an **indicative 80–85% structural-coverage range** across the reported controlled views. It must not be presented as 80–85% future-prediction accuracy. Maya is currently better at identifying patterns, constraints, decision structures, and plausible routes than at naming the exact individual outcome that will occur.

Pitch-safe claim: **Maya is a supervised, evidence-based pattern-mapping prototype that narrows plausible paths and explains constraints; it is not a guaranteed future predictor.**

## Limitations

- Benchmark families overlap and are not independent samples.
- Most scores measure structural pattern coverage, not exact future outcomes.
- Synthetic character and collision matches cannot establish real-world accuracy.
- Historical reconstruction is vulnerable to hindsight, especially reverse mapping.
- No calibration dataset is large enough to claim a population-level probability.
