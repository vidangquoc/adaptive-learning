# Learner Review Data Specification v0.1

## 1. Purpose

This document defines the learner-specific data used by Adaptive Learning to schedule reviews of Knowledge Atoms.

The review model is intentionally simple:

- A Knowledge Atom is reviewed as one unit.
- A review checks one thing: whether the learner remembers the Atom.
- The system does not maintain separate recognition, recall, usage, collocation, discrimination, transfer, or retention scores for an Atom.
- The learner's review data stores only the latest state needed for future review.

## 2. Review data storage

Each learner has exactly one review-data file:

```text
data/learners/<learner-id>/review-data.yaml
```

The file contains the current review state for the learner's Knowledge Atoms.

It does not contain:

- Knowledge Atom content;
- attempts;
- review history;
- historical states;
- separate mastery dimensions or scores.

Knowledge Atom content remains in the Official Knowledge Store. Review data references an Atom by `atom_id`.

## 3. Review-data model

Each review record contains exactly these fields:

```yaml
- atom_id:
  total_review_times:
  effective_review_times:
  last_review_date:
  next_review_date:
```

### 3.1 `atom_id`

Identifies the Knowledge Atom whose review state is stored.

### 3.2 `total_review_times`

The total number of times the learner has reviewed the Atom, regardless of whether the learner answered correctly or incorrectly.

### 3.3 `effective_review_times`

The number of times the learner answered the question correctly when the question was presented to test the Atom.

Therefore:

```text
0 ≤ effective_review_times ≤ total_review_times
```

### 3.4 `last_review_date`

The date and time at which the learner most recently reviewed the Atom.

This field is a datetime.

### 3.5 `next_review_date`

The calendar date on which the Atom is scheduled to be reviewed next.

This field is a date only; it does not specify a time.

## 4. Review update rules

When an Atom is reviewed:

1. `total_review_times` increases by one.
2. `effective_review_times` increases by one if the learner answers the review question correctly; otherwise it does not increase.
3. `last_review_date` is replaced with the current review datetime.
4. `next_review_date` is replaced with the newly calculated next review date.

Only the latest values are retained.

## 5. Review scheduling

`next_review_date` is determined by the project's review scheduling algorithm.

The scheduling algorithm may use the current review data, including the number of total and effective reviews and the most recent review date.

The exact scheduling algorithm is defined separately from the storage model.

## 6. Data integrity

- Every review record refers to one Knowledge Atom through `atom_id`.
- A Knowledge Atom is tested as one review unit: remembered or not remembered.
- `effective_review_times` must never exceed `total_review_times`.
- `last_review_date` stores only the most recent review datetime.
- `next_review_date` stores only the current scheduled review date.
- Attempts and review history must not be stored in `review-data.yaml`.
- Learner review data must not modify the canonical Knowledge Atom.
