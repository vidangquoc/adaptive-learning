# Adaptive Learning State Specification v0.1

## 1. Purpose

This specification defines how Adaptive Learning keeps track of what the learner knows, what needs review, what needs remediation, and what can be skipped.

The system is **adaptive**: the learner is not required to complete every lesson, word, or hour. Learning time is allocated according to demonstrated mastery and the current learning frontier.

Core principle:

> Test first → locate the frontier → teach only what is needed → verify transfer → review only what is at risk.

A learning-time budget is a **ceiling / available learning budget**, not a completion quota.

## 2. Separation of concerns

The repository uses four related but distinct layers:

```text
RAW / EVIDENCE
      ↓
CURATED / NORMALIZED
      ↓
OFFICIAL KNOWLEDGE / CURRICULUM
      ↓
LEARNING STATE
      ↓
REVIEW QUEUE / NEXT BEST ACTIVITY
```

- **Knowledge** answers: What should potentially be learned?
- **Competency/module definitions** answer: What capability does the learner need to demonstrate?
- **Learning state** answers: How well does the learner currently know it?
- **Review queue** answers: What should be done next, and why?

Learning state must never alter source evidence or canonical knowledge.

## 3. Units of tracking

The system tracks mastery at three levels.

### 3.1 Item

A single lexical or knowledge item.

### 3.2 Competency

A transferable ability involving one or more items.

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

## 4. Knowledge dimensions

At minimum, distinguish:

| Dimension | Meaning |
|---|---|
| `recognition` | Can identify/understand the item when encountered |
| `recall` | Can retrieve the answer without strong prompting |
| `usage` | Can use/select the item correctly in context |
| `collocation` | Knows required patterns, prepositions, and fixed combinations |
| `discrimination` | Can distinguish it from near-synonyms/confusable forms |
| `transfer` | Can apply it in the target task context |
| `retention` | Remains correct after a delay |

Not every module requires every dimension. The module definition specifies which dimensions matter.

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
The learner demonstrates stable performance across the dimensions required by the competency, including relevant transfer where applicable.

### `MAINTENANCE`
Previously mastered knowledge remains stable through delayed checks.

### `EXTENDED`
Core mastery is secure and the learner has moved into higher-discrimination or advanced transfer work.

## 6. Mastery gates

Default thresholds are heuristics and may be tuned after collecting real learner data.

| Result | Interpretation | Default action |
|---:|---|---|
| ≥95% | Very strong | Skip routine teaching; test transfer/extension |
| 90–94% | Mastery candidate | Verify weak dimensions and delayed retention |
| 80–89% | Secure but incomplete | Continue targeted practice |
| 65–79% | Developing | Teach/practice weak dimensions |
| <65% | Weak | Remediate before advancing |

These thresholds must not be applied only to an aggregate score.

## 7. Diagnostic-first rule

Every substantial module should begin with a diagnostic unless reliable recent evidence already exists.

Diagnostic outcomes should identify mastered, partially mastered, weak, unseen, strong/weak dimensions, and whether extension is appropriate.

If the diagnostic is consistently ≥90–95% and no critical dimension is weak, the module should normally be skipped or compressed.

## 8. Assessment interactions

Assessment interactions may produce evidence used to update the learner's current review data. These interactions are not stored in `review-data.yaml` as attempts or history.

## 9. Review-data model

The learner's persisted review state is a latest-state snapshot. Each learner has exactly one file:

```text
data/learners/<learner-id>/review-data.yaml
```

Each review record contains exactly:

```yaml
- atom_id:
  total_review_times:
  effective_review_times:
  last_review_date:
  next_review_date:
```

| Field | Meaning |
|---|---|
| `atom_id` | Identifies the Knowledge Atom being reviewed. |
| `total_review_times` | Total number of times the learner has reviewed the Atom, regardless of whether the learner answered correctly or incorrectly. |
| `effective_review_times` | Number of times the learner answered the question correctly when the question was presented to test the Atom. |
| `last_review_date` | Date and time of the learner's most recent review. |
| `next_review_date` | Calendar date on which the Atom is scheduled for its next review. |

`review-data.yaml` references the Official Knowledge Store by `atom_id` and does not copy Atom content. `last_review_date` is a datetime; `next_review_date` is a date only.

Only the latest values are persisted. Attempts and review history are outside the scope of this file.

## 10. Review scheduling

Review is triggered by evidence, not by a fixed textbook calendar.

Suggested initial intervals after successful delayed recall:

```text
1 day → 3 days → 7 days → 14 days → 30 days → 60+ days
```

These are starting heuristics and should be adjusted using observed retention data.

## 11. Review queue

The review queue is a derived view, not the source of truth. Each entry should explain why an activity is recommended and what activity should be performed.

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
priority
created_at
```

## 12. Priority calculation

Learning priority is not the same as difficulty. A task priority may consider:

```text
current weakness
× forgetting risk
× competency dependency
× learning-target relevance
× opportunity cost
```

Exact numeric weighting remains open until real performance data exists.

## 13. Next-best-activity logic

```text
Is required competency already mastered?
 ├─ YES → Is there a weak transfer dimension?
 │          ├─ YES → target transfer
 │          └─ NO  → extension or skip
 │
 └─ NO → Is weakness localized?
           ├─ YES → targeted practice
           └─ NO  → remediation / core teaching
```

If performance is high, increase difficulty rather than repetition. If weakness is narrow, do not reteach the entire module.

## 14. Adaptive branching

### Fast learner branch

Diagnostic ≥90–95%, no critical dimension weak, and strong delayed retention:

```text
skip core → advanced discrimination → difficult transfer → optional advanced extension
```

### Normal branch

```text
targeted core → usage → transfer → mastery gate
```

### Remediation branch

```text
reduce scope → reteach weak concept → controlled practice → delayed check
```

## 15. Transfer coverage

A competency should map to one or more target task types. A learner should not receive `MASTERED` solely because they know a vocabulary meaning if the competency's required transfer dimension is weak.

## 16. Maintenance

A mastered item/competency should enter maintenance when immediate performance, delayed recall, and required transfer are strong.

A maintenance failure should reopen only the failed dimension whenever possible rather than resetting the entire competency.

## 17. Learning frontier

```text
GREEN   = already solid → skip / maintain
BLUE    = partially solid → targeted practice
YELLOW  = within reach → active learning
RED     = low value or currently out of reach → defer or omit
```

The frontier is dynamic and can move after new evidence.

## 18. Learning-time integration

A learning-time framework is a budget, not a syllabus-completion requirement. Actual allocation is generated from learning state.

The system optimizes for competency and learning value, not seat time.

## 19. Data integrity rules

1. Never fabricate a learning result.
2. Never infer mastery from exposure alone.
3. Never mark an item mastered because it appeared in a lesson.
4. Keep assessment evidence separate from derived state.
5. Do not store attempts or review history in `review-data.yaml`.
6. Allow mastery to regress when new evidence warrants it.
7. Do not use difficulty as a proxy for mastery.
8. Do not use vocabulary breadth as a proxy for readiness for a particular target.
9. Keep source/provenance for assessment material.
10. Treat thresholds and scheduling intervals as tunable heuristics until validated by project data.

## 20. Minimum implementation for v0.1

The first learner-review implementation can use:

```text
1. one review-data.yaml per learner
2. Official Knowledge Atoms referenced by atom_id
3. the deterministic review scheduling ruleset
```

A separate historical event/attempt store is outside the scope of this file.
