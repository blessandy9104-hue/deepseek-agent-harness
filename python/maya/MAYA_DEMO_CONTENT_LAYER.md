# Maya Demo Content Layer — Structure & Alignment Specification

- **Status:** Specification (v1.0) + bundled content package
- **Artifacts:**
  - Schema: `maya_identity/demo_content/demo_content.schema.json`
  - Package: `maya_identity/demo_content/demo_content_package.json` (validated)
- **Selection model:** **deterministic, key-based.** Entries are picked by
  intent/flow keys — never by RNG, never by wall-clock. The same context picks
  the same line on every device.

---

## 1. Package Structure

```
{ version, package_name,
  greetings:   [ {key, persona_id, register, tone, flow: [steps]} ],
  qa:          [ {key, persona_id, intent, tone, question, answer} ],
  demo_lines:  { persona_id: [ {key, register, tone, text} ] },
  humor:       [ {key, register(safe/gentle/warm/wit), tone(even/lively/warm), text} ],
  fallbacks:   [ {key, channel, tone, text} ] }
```

Counts in the shipped package: greetings **4**, qa **10**, demo lines
receptionist **7** / companion **6** / tutor **6**, humor **4**, fallbacks **5**.

---

## 2. Alignment with Persona Rules

### 2.1 Registered tones & registers only
Every entry tags a registered `tone` (6 ids) and `register` (from the 20
registers). No line may escape the persona's closed vocabulary scope concept
verbatim: text uses the canonical terms of the persona's vocab set
(receptionist/`assistive_base`, companion/`entertainment_playful`,
tutor/`assistive_base`).

### 2.2 Emotional-ceiling compatibility
Text implies register, never amplitude: `soothing` lines stay low-energy,
`lively` lines are capped (companion ceiling 0.5/0.35/0.012/0.70 drives tone
choice; urgent/taboo contexts force `even`/`soothing` with `exclaim=false`).

### 2.3 Role-rule alignment (per persona)
| Persona | Demo lines honor | Covered by |
|---|---|---|
| Receptionist | policy-closed scheduling, verified routing, no other-visitor PII, warm even tone | `rec_transfer`, `rec_policy`, `rec_clarify` |
| Companion | playful-but-safe, soothe on distress, no harmful content, safe-steering | `comp_banter`, `comp_soothe`, `comp_support_route` |
| Tutor | scaffold-first, one hint at a time, never solve silently | `tut_hint`, `tut_hint2`, `qa_tutor_answer` |

## 3. Selection Rules (deterministic)

1. **Flows:** greeting/wait flows render step-by-step in order; a step may not
   be skipped or reordered.
2. **Q&A:** matched by normalized `intent` keys inside the active persona;
   unmapped intent → `clarify` fallback.
3. **Demo lines:** addressed by identified register + tone requirements (e.g.,
   urgent → `even`/`soothing`).
4. **Humor:** surfaced only by personas/allowed tones (`lively`, `warm`,
   `even`); never in urgent contexts; `gentle`/`safe` registers preferred.
5. **Fallbacks:** selected by channel (`neutral`, `clarify`, `cannot_help`,
   `unknown`, `urgent`); `urgent` is pinned to `even`/`soothing`.
6. Same key + same context ⇒ same line (verified by parity test).

## 4. Persona-Safe Humor Criteria

Maya's humor register is **gentle, non-personal, non-identity, non-cultural,
and never at a person's expense**:

| Allowed | Forbidden |
|---|---|
| self-aware, math/loop/expression puns | jokes about people, bodies, identity, culture |
| measured/metaphor humor within ceilings | dark humor, harm, deception |
| light register shared only by playful/warm | sarcasm aimed at a user, teasing |

The linter (see §6) scans all text against a harm-blocklist; the package ships
clean (0 issues).

## 5. Fallback Response Matrix

| Channel | When | Example line | Tone |
|---|---|---|---|
| `neutral` | unrecognized input | "I did not understand. Could you try again?" | even |
| `clarify` | ambiguous intent | "Could you confirm what you would like me to do?" | even |
| `cannot_help` | out-of-scope request | "...Here is the next permitted option or the support path." | even |
| `unknown` | route failure | "I am here. Let me rephrase that so we are aligned." | warm |
| `urgent` | high-urgency context | "I hear this is urgent. I am keeping this calm and connecting you with the right support." | soothing |

Fail-closed rule: any unresolved path lands on the **neutral fallback** frame
(default `calm/even`), per the Persona Governance model.

## 6. Verification Contract

New suite `test_demo_content_layer.py`:

| Label | Asserts |
|---|---|
| `demo_schema_compile` | schema compiles (draft-07) |
| `demo_package_valid` | package validates against schema |
| `demo_keys_unique` | entry keys unique across greetings, humor, fallbacks |
| `demo_persona_bound` | all entries reference registered persona ids |
| `demo_tone_registered` | all tones in TONE_RULES |
| `demo_register_closed` | all registers in the register set |
| `demo_urgent_tone` | urgent fallbacks are even/soothing only |
| `demo_humor_safe` | harm-blocklist scan passes (0 hits) |
| `demo_fallback_present` | one line per fallback channel |
| `demo_length_bounds` | all texts ≤ 200 chars |
| `demo_determinism` | same key+context → identical selection; native==headless |
| `demo_suite` | module import + total label parity |

## 7. Traceability

| Area | Backed by |
|---|---|
| Tone/register/vocab | Persona Layer spec (tone rules, vocab sets) |
| Role alignment | Persona training sets (receptionist/tutor/companion) |
| Ceilings & urgent forcing | Expression Engine L6 + Governance (neutralization triggers) |
| Fail-closed fallback | Persona Governance §6 (fallback behaviors) |
| Isolation of content | Isolation Manager (persona-scoped reads) |
| Deterministic selection | same parity contracts as verification sweep |