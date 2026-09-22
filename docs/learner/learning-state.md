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

## 8. Review data

The current learner-specific review data is a latest-state snapshot. Each learner has exactly one file:

```text
data/learners/<learner-id>/review-data.yaml
```

`review-data.yaml` does not store attempts or review history. Each review record contains exactly:

```yaml
- atom_id:
  total_review_times:
  effective_review_times:
  last_review_date:
  next_review_date:
```

Field semantics:

| Field | Meaning |
|---|---|
| `atom_id` | Identifies the Knowledge Atom being reviewed. |
| `total_review_times` | Total number of times the learner has reviewed the Atom, regardless of whether the learner answered correctly or incorrectly. |
| `effective_review_times` | Number of times the learner answered the question correctly when the question was presented to test the Atom. |
| `last_review_date` | Date and time of the learner's most recent review. |
| `next_review_date` | Calendar date on which the Atom is scheduled for its next review. |

Review data references the Official Knowledge Store by `atom_id` and does not copy Atom content. `last_review_date` is a datetime; `next_review_date` is a date only.

## 9. Review scheduling

Review is triggered by evidence, not by a fixed textbook calendar.

Suggested initial intervals after successful delayed recall:

```text
1 day → 3 days → 7 days → 14 days → 30 days → 60+ days
```

These are starting heuristics and should be adjusted using observed retention data.

Review scheduling updates the current `next_review_date`; prior review events are not stored in `review-data.yaml`.

## 10. Review queue

The review queue is a derived view, not a persisted part of `review-data.yaml`. If a separate queue representation is introduced later, it belongs to the learner/adaptive layer and must reference Knowledge Atoms by `atom_id`.

## 11. Data integrity rules

1. Never fabricate a learning result.
2. Never infer a correct review result from exposure alone.
3. `effective_review_times` increases only when the learner answers the question correctly for the tested Atom.
4. `effective_review_times` must not exceed `total_review_times`.
5. `last_review_date` records the latest review datetime only.
6. `next_review_date` records the current scheduled review date only.
7. Do not store attempts or review history in `review-data.yaml`.
8. Keep static Knowledge Atoms separate from learner-specific review data.
9. Treat scheduling intervals as tunable heuristics until validated by project data.

## 12. Minimum implementation for v0.1

The first learner-review implementation can use:

```text
1. one review-data.yaml per learner
2. Official Knowledge Atoms referenced by atom_id
3. the deterministic review scheduling ruleset
```

A separate historical event/attempt store can be introduced later if the project requires it.
