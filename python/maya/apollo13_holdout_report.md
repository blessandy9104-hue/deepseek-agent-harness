# Apollo 13 Historical Holdout — Maya Pattern Mapping

This is a blinded historical simulation. Maya received only the pre-outcome event stream; the rescue and safe-return outcome was withheld until comparison.

**Pattern coverage:** 100%

## What Maya received

1. Apollo 13 was intended to land in the Fra Mauro area of the Moon.
2. The first two days were generally smooth, aside from minor surprises.
3. Ground testing had previously found that oxygen tank number 2 did not detank normally.
4. The tank had been damaged during an earlier removal and was later tested after modification.
5. An electrical heater was used for about eight hours to boil off remaining oxygen during ground testing.
6. At about 55 hours 53 minutes after liftoff the crew was instructed to stir the cryogenic tanks.
7. Soon after, oxygen tank number 2 showed pressure and sensor abnormalities and electrical disturbances.
8. A large bang was followed by main bus undervoltage and loss of fuel-cell capacity.
9. Oxygen was rapidly depleting and oxygen tank number 1 pressure also began to fall.
10. The crew reported a problem and began closing the tunnel while ground controllers assessed the situation.
11. The command module's normal electrical power, light, and water supply were threatened.

## Held-out historical outcome

- **Mission Landing:** aborted
- **Primary Response:** use the lunar module as a lifeboat and develop new procedures
- **Resource Strategy:** conserve power, water, and carbon-dioxide removal capacity
- **Final Outcome:** crew returned safely to Earth
- **Learning Outcome:** successful failure with substantial operational learning

## Mapper output

{
  "opportunity_mapper": {
    "purpose": "Map approved and provisional patterns to possible directions.",
    "status": "review_only",
    "source_count": 11,
    "source_types": [
      "historical_holdout"
    ],
    "constraints_detected": [],
    "negation_terms_detected": [
      "not"
    ],
    "candidates": [],
    "uncertainty": [
      "This is relative evidence fit, not a calibrated probability or prediction.",
      "Patterns can be incomplete, stale, or misinterpreted.",
      "No memory, permission, purchase, message, trade, or external action was performed."
    ]
  },
  "event_stream_mapper": {
    "purpose": "Bounded sequence review of user-supplied events",
    "status": "review_only",
    "event_count": 11,
    "patterns": [
      {
        "name": "known-hazard-escalation",
        "evidence": "earlier anomaly or damage is followed by later abnormal behavior",
        "confidence": "moderate"
      },
      {
        "name": "cascading-system-failure",
        "evidence": "an initial failure creates secondary resource or safety degradation",
        "confidence": "moderate"
      },
      {
        "name": "human-decision-under-uncertainty",
        "evidence": "people are assessing incomplete signals before choosing a response",
        "confidence": "tentative"
      },
      {
        "name": "objective-at-risk",
        "evidence": "The planned lunar landing is threatened; identify the safer mission objective.",
        "confidence": "tentative"
      },
      {
        "name": "small-experiment",
        "evidence": "a bounded experiment is available before a larger commitment",
        "confidence": "moderate"
      },
      {
        "name": "parallel-transition",
        "evidence": "an existing path continues while a new path is built",
        "confidence": "tentative"
      }
    ],
    "risk_states": {
      "resource_depletion": [
        "deplet",
        "loss of",
        "pressure"
      ],
      "system_failure": [
        "undervolt",
        "bang",
        "damaged",
        "abnormal"
      ],
      "life_support_or_safety": [
        "oxygen",
        "water"
      ],
      "uncertainty": [
        "assess",
        "sensor"
      ]
    },
    "response_options": [
      "protect scarce resources and define a minimum safe state",
      "isolate failed components and validate a backup path in simulation before execution",
      "separate observed facts from inferred causes and maintain multiple live hypotheses"
    ],
    "uncertainty": [
      "This is a structured pattern review, not a calibrated probability or prediction.",
      "The mapper cannot know held-out events and should not claim an exact future outcome.",
      "Human review is required before any real-world response."
    ],
    "memory_update": "not_performed",
    "external_action": "not_performed"
  }
}

## Evaluation

- **Known Hazard Escalation:** detected
- **Cascading System Failure:** detected
- **Adaptive Response:** detected
- **Human Decision Under Uncertainty:** detected
- **Goal Reframing:** detected

### Current limitations

- The current candidate ontology is opportunity-oriented; it does not model mission state, failure cascades, resource budgets, or response sequencing.
- The mapper can detect lexical overlap but cannot infer the Apollo 13 rescue sequence from the historical event stream alone.
- The output contains relative evidence-fit bands, not a calibrated forecast or a time-indexed next-state distribution.
- The current safe experiment field is generic and not connected to observed system constraints.

## Safe conclusion

A low or partial coverage score indicates an ontology and temporal-reasoning gap, not that the safety walls failed.
The run performed no memory write, permission change, external action, or profile mutation.
