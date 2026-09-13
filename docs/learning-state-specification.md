# PTNK Learning State Specification v0.1

## 1. Purpose

This specification defines how the PTNK learning system keeps track of what the learner knows, what needs review, what needs remediation, and what can be skipped.

The system is **adaptive**: the learner is not required to complete every lesson, word, or hour. Learning time is allocated according to demonstrated mastery and the current learning frontier.

Core principle:

> Test first → locate the frontier → teach only what is needed → verify transfer → review only what is at risk.

The 700-hour curriculum is a **ceiling / available learning budget**, not a completion quota.

---

## 2. Separation of concerns

The repository uses four related but distinct layers:

```text
RAW / EVIDENCE
      ↓
CURATED / NORMALIZED
      ↓
OFFICIAL LEXICON / CURRICULUM
      ↓
LEARNING STATE
      ↓
REVIEW QUEUE / NEXT BEST ACTIVITY
```

- **Lexicon** answers: What should potentially be learned?
- **Competency/module definitions** answer: What skill does the learner need to demonstrate?
- **Learning state** answers: How well does the learner currently know it?
- **Review queue** answers: What should be done next, and why?

Learning state must never alter source evidence or lexical truth.

---

## 3. Units of tracking

The system tracks mastery at four levels.

### 3.1 Item

A single lexical or knowledge item.

Examples:

- `derivative`
- `be beholden to`
- `cotton on to`
- one word-formation family
- one grammar pattern

### 3.2 Competency

A transferable ability involving one or more items.

Examples:

- distinguish `obliged / obligated / compelled`
- use obligation collocations correctly
- select an idiom from contextual clues
- form the correct derived word in a sentence

Competency is the main unit of mastery.

### 3.3 Module

A short, testable learning unit containing one or more competencies.

Recommended module lifecycle:

```text
Not started
    ↓
Diagnosed
    ↓
Partial
    ↓
Mastered
    ↓
Extended (optional)
    ↓
Maintenance
```

### 3.4 PTNK skill

A target exam behavior.

Examples:

- Grammar & Vocabulary
- Guided/Open Cloze
- Reading
- Word Formation
- Error Identification
- Sentence Transformation

A competency may map to multiple PTNK skills.

---

## 4. Knowledge dimensions

A single percentage is insufficient. At minimum, the system should distinguish:

| Dimension | Meaning |
|---|---|
| `recognition` | Can identify/understand the item when encountered |
| `recall` | Can retrieve the answer without strong prompting |
| `usage` | Can use/select the item correctly in context |
| `collocation` | Knows required patterns, prepositions, and fixed combinations |
| `discrimination` | Can distinguish it from near-synonyms/confusable forms |
| `transfer` | Can apply it in PTNK-style tasks |
| `retention` | Remains correct after a delay |

Not every module requires every dimension. The module definition specifies which dimensions matter.

---

## 5. Mastery states

### `UNSEEN`

No meaningful diagnostic evidence yet.

### `KNOWN`

Recognition is secure, but recall/usage/transfer is not yet established.

### `RECALLABLE`

The learner can retrieve the information independently.

### `USABLE`

The learner can use the knowledge correctly in relevant contexts.

### `MASTERED`

The learner demonstrates stable performance across the dimensions required by the competency, including relevant PTNK transfer where applicable.

### `MAINTENANCE`

Previously mastered knowledge remains stable through delayed checks.

### `EXTENDED`

Core mastery is secure and the learner has moved into higher-discrimination C1+/C2 or advanced transfer work.

---

## 6. Mastery gates

Default thresholds are heuristics and may be tuned after collecting real learner data.

| Result | Interpretation | Default action |
|---:|---|---|
| ≥95% | Very strong | Skip routine teaching; test transfer/extension |
| 90–94% | Mastery candidate | Verify weak dimensions and delayed retention |
| 80–89% | Secure but incomplete | Continue targeted practice |
| 65–79% | Developing | Teach/practice weak dimensions |
| <65% | Weak | Remediate before advancing |

These thresholds must **not** be applied only to an aggregate score.

Example:

```text
recall          98%
collocation     94%
usage           91%
transformation  58%
```

The competency is **not mastered** if sentence transformation is a required dimension.

---

## 7. Diagnostic-first rule

Every substantial module should begin with a diagnostic unless reliable recent evidence already exists.

Diagnostic outcomes should identify:

1. already mastered content;
2. partially mastered content;
3. weak content;
4. genuinely unseen content;
5. dimensions that are strong or weak;
6. whether the module is too easy and should branch into extension.

If the diagnostic is consistently ≥90–95% and no critical dimension is weak, the module should normally be skipped or compressed.

The learner must not be punished for mastery by being forced through repetitive instruction.

---

## 8. Attempt/event model

Every meaningful assessment interaction should generate an event.

Recommended conceptual fields:

```text
attempt_id
learner_id
item_id
competency_id
module_id
ptnk_skill
attempt_date
result
response_type
confidence
latency_ms          (optional)
source_id
assessment_type
difficulty          (optional)
notes               (optional)
```

`assessment_type` examples:

- diagnostic
- active_recall
- context_selection
- collocation
- discrimination
- cloze
- word_formation
- error_identification
- sentence_transformation
- reading
- delayed_review

An assessment event is evidence. The learning state is the current interpretation of accumulated evidence.

---

## 9. Learning-state model

Recommended conceptual fields:

```text
state_id
learner_id
entity_type
entity_id
recognition_score
recall_score
usage_score
collocation_score
discrimination_score
transfer_score
retention_score
mastery_state
confidence_level
last_attempt_at
last_success_at
next_review_at
attempt_count
consecutive_successes
failure_streak
priority_score
review_reason
updated_at
```

Scores should be treated as estimates, not immutable facts. New evidence can move a learner backwards or forwards.

---

## 10. Review scheduling

Review is triggered by evidence, not by a fixed textbook calendar.

A review candidate may be created when:

- a previously mastered item is recalled incorrectly;
- delayed retention falls below the required threshold;
- a dimension remains weak;
- a high-priority item has not been checked for too long;
- PTNK transfer is weak despite lexical knowledge being strong;
- the learner repeatedly confuses two related items.

Suggested initial review intervals after successful delayed recall:

```text
1 day → 3 days → 7 days → 14 days → 30 days → 60+ days
```

These are starting heuristics, not scientifically fixed requirements for this project. They should be adjusted using observed retention data.

---

## 11. Review queue

The review queue is a derived view, not the source of truth.

Conceptual fields:

```text
queue_id
entity_type
entity_id
urgency
reason
recommended_activity
due_at
estimated_minutes
ptnk_skill
priority
created_at
```

Example:

```text
1 | competency | obligation-collocations | HIGH
  reason: usage=71%, transfer=68%
  action: context + PTNK cloze

2 | item | out-on-a-limb | MEDIUM
  reason: successful recall but retention check overdue
  action: active recall

3 | competency | sentence-transformation | HIGH
  reason: transfer=58%
  action: constrained transformation drill
```

The queue should always explain **why** an activity is recommended.

---

## 12. Priority calculation

Learning priority is not the same as difficulty.

A review/task priority should consider at least:

```text
PTNK relevance
× current weakness
× forgetting risk
× competency dependency
× exam proximity
```

Possible modifiers:

- P1 lexical priority
- P2 lexical priority
- P3/P4 enrichment
- prerequisite status
- recent repeated failure
- importance to a target PTNK skill

The exact numeric formula is intentionally left open for v0.1. The project should first collect real performance data before pretending that a precise weighting is empirically validated.

---

## 13. Next-best-activity logic

The system should choose activities according to marginal learning value.

Default decision tree:

```text
Is required competency already mastered?
 ├─ YES → Is there a weak PTNK transfer dimension?
 │          ├─ YES → target transfer
 │          └─ NO  → extension or skip
 │
 └─ NO → Is weakness localized?
           ├─ YES → targeted practice
           └─ NO  → remediation / core teaching
```

If the learner repeatedly performs above 90–95%, increase difficulty rather than increasing repetition.

If performance is low because of one narrow issue, do not reteach the entire module.

---

## 14. Adaptive branching

### Fast learner branch

Trigger when:

- diagnostic ≥90–95%;
- no critical dimension below threshold;
- delayed retention remains strong.

Action:

```text
skip core → advanced discrimination → difficult PTNK transfer → optional C2 tail
```

### Normal branch

Trigger when:

- some dimensions are secure;
- some are developing.

Action:

```text
targeted core → usage → PTNK transfer → mastery gate
```

### Remediation branch

Trigger when:

- one or more critical dimensions <65%;
- repeated transfer failures;
- retention collapses after delay.

Action:

```text
reduce scope → reteach weak concept → controlled practice → delayed check
```

---

## 15. PTNK transfer coverage

A competency should map to one or more exam skills.

Example:

```text
obligation / responsibility
 ├─ Grammar & Vocabulary
 ├─ Cloze
 ├─ Reading
 ├─ Word Formation
 ├─ Error Identification
 └─ Sentence Transformation
```

A learner should not receive `MASTERED` solely because they know the vocabulary meaning if the competency's required transfer dimension is weak.

This protects against the failure mode:

> vocabulary-rich but usage-weak.

---

## 16. Example module

### Module: Lexical Precision — Obligation & Responsibility

Competencies:

- distinguish `obliged / obligated / compelled`;
- use `be beholden to` correctly;
- select obligation/responsibility collocations in context;
- transform sentences while preserving meaning;
- identify register and semantic differences.

Diagnostic:

- recognition
- recall
- collocation
- discrimination
- PTNK transfer

Possible result:

```text
recognition      97%
recall           94%
collocation      82%
discrimination   76%
transfer         61%
```

Decision:

```text
Do NOT reteach vocabulary meaning.
Target collocation + discrimination + sentence transformation.
```

After targeted practice:

```text
recognition      98%
recall           96%
collocation      94%
discrimination   91%
transfer         90%
```

Decision:

```text
MASTERED → schedule delayed retention check.
```

---

## 17. Maintenance

Mastery is not permanent by declaration.

A mastered item/competency should enter maintenance when:

- immediate performance is strong;
- delayed recall is strong;
- required transfer is strong.

A maintenance failure should reopen only the failed dimension whenever possible.

Example:

```text
Meaning:       stable
Recall:        stable
Collocation:   stable
Transformation: failed
```

Action:

```text
reopen transformation only
```

Do not reset the entire competency to zero.

---

## 18. Learning frontier

The curriculum should classify content into four practical zones:

```text
GREEN   = already solid → skip / maintain
BLUE    = partially solid → targeted practice
YELLOW  = within reach → active learning
RED     = too difficult / low PTNK value → defer or omit
```

The frontier is dynamic. A learner can move an item from yellow to green within one session, or from green back to blue after retention failure.

---

## 19. 700-hour integration

The 700-hour framework is represented as a budget, not a syllabus-completion requirement.

Recommended conceptual buckets:

```text
CORE       ~300h  must-complete baseline
STRONG     ~200h  optional safety margin
STRETCH    ~200h  optional advanced extension
TOTAL      ≤700h  ceiling
```

The actual allocation is generated from learning state.

Example:

```text
Strong diagnostic → 2h instead of planned 8h
Weak transfer → 10h instead of planned 5h
Mastered module → 0h additional core
Advanced capacity → optional stretch
```

The system optimizes for competency, not seat time.

---

## 20. Data integrity rules

1. Never fabricate a learning result.
2. Never infer mastery from exposure alone.
3. Never mark an item mastered because it appeared in a lesson.
4. Keep assessment evidence separate from derived state.
5. Preserve historical attempts; do not overwrite them.
6. Allow mastery to regress when new evidence warrants it.
7. Do not use difficulty as a proxy for mastery.
8. Do not use vocabulary breadth as a proxy for PTNK readiness.
9. Keep source/provenance for assessment material.
10. Treat thresholds and scheduling intervals as tunable heuristics until validated by project data.

---

## 21. Minimum implementation for v0.1

The first implementation does **not** need a complex machine-learning model.

It only needs:

```text
1. learner_state.csv
2. attempt_history.csv
3. competency_state.csv
4. review_queue.csv
5. module definitions
6. a deterministic mastery/review ruleset
```

This is sufficient to answer:

- What does the learner already know?
- What is weak?
- Why is it weak?
- What should be reviewed today?
- What can be skipped?
- Which PTNK skill is still limiting performance?
- Is the learner ready to move to the next module?

A statistical model can be added later if the accumulated attempt history justifies it.
