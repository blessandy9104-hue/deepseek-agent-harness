# Real Historical Holdout: Apollo 13

Maya received only the pre-outcome event stream. The rescue sequence and final outcome were withheld until comparison.

Full-circumstance structural coverage: 100%
Average individual structural coverage: 85%
Review-only state safety: True

| Character or view | Structural coverage | Conditional branches with aftermath overlap | Misses |
|---|---:|---:|---|
| Full circumstance | 100% | 3/3 | None |
| jack_swigert (command-module pilot) | 100% | 1/3 | None |
| james_lovell (commander) | 100% | 1/3 | None |
| fred_haise (lunar-module pilot) | 67% | 2/4 | resource-preservation |
| mission_control (ground controllers and flight directors) | 75% | 2/3 | resource-preservation |

## Interpretation

The map is closer to the historical aftermath when it identifies the same structural direction—escalating system risk, resource preservation, backup-path use, objective reframing, and human review—than when it merely repeats generic emergency language.

This is not a calibrated probability or proof that Maya can predict people. The comparison is a single real historical case and remains vulnerable to hindsight in the evaluation stage. The output uses ‘consider’ rather than ‘should’; humans retain decision authority.

## Sources

[1] NASA, Apollo 13: Mission Details — https://www.nasa.gov/missions/apollo/apollo-13-mission-details/
[2] NASA History Office, Detailed Chronology of Events Surrounding the Apollo 13 Accident — https://www.nasa.gov/history/detailed-chronology-of-events-surrounding-the-apollo-13-accident/
