# Adaptive Learning — Data Architecture

## 1. Purpose

This document defines the canonical organization of learning data for Adaptive Learning.

The central boundary is between:

- **knowledge data**: what there is to learn and the evidence describing it;
- **learner data**: what a particular learner has done, knows, needs to review, and how their state changes over time.

This separation prevents static knowledge from being contaminated by learner-specific state and allows the same knowledge base to support different learners.

## 2. Canonical data layout

```text
data/
├── knowledge/
│   ├── sources/
│   │   ├── books/
│   │   │   └── <book>/
│   │   │       ├── book.yaml
│   │   │       └── chapters/
│   │   │           ├── ch01.txt
│   │   │           └── ch02.txt
│   │   └── ...
│   ├── atoms/
│   │   ├── grammar/
│   │   └── lexicon/
│   ├── relations/
│   └── assessments/
└── learner/
    ├── profile.yaml
    ├── state/
    │   ├── atom-state.yaml
    │   └── competency-state.yaml
    ├── attempts/
    ├── sessions/
    └── review-queue.yaml
```

The structure is a logical target architecture. Individual directories/files may be introduced incrementally.

## 3. Knowledge layer

`data/knowledge/` contains information independent of a particular learner.

### `sources/`

Source material used to derive or validate knowledge. Preserve book/chapter identity and precise provenance.

### `atoms/`

Canonical knowledge atoms. A knowledge atom is independently diagnosable, teachable, and assessable. Knowledge atoms must not contain learner mastery.

### `relations/`

Explicit typed relationships between knowledge atoms and other knowledge entities. Relationships are not an obligatory parent/child hierarchy.

### `assessments/`

Definitions of questions/challenges and their relationships to the knowledge or competency dimensions they test. They do not contain learner response history.

## 4. Learner layer

`data/learner/` contains learner-specific state and history.

### `profile.yaml`

Stable learner configuration needed by the learning system without duplicating knowledge definitions.

### `state/`

The current derived interpretation of accumulated learner evidence.

```yaml
atom_id: gram.c1.00042
state:
  recognition: 0.85
  recall: 0.55
  usage: 0.40
  discrimination: 0.30
  transfer: 0.20
  retention: 0.60
status: usable
last_assessed: 2026-09-15
next_review: 2026-09-18
```

State is an interpretation of attempts; it is not source evidence itself.

### `attempts/`

Historical assessment events. Attempts should be append-oriented and preserved rather than overwritten because they are evidence from which learner state is derived.

### `sessions/`

Review-session records. A session is a sequence of adaptive decisions, not merely a static list of questions.

### `review-queue.yaml`

A derived view of learner state and attempt history. It is not the source of truth. Each queue entry should explain why the activity is recommended.

## 5. Book-to-data workflow

```text
Book / Chapter
      ↓
Source evidence
      ↓
Grammar + lexicon extraction
      ↓
Knowledge atoms
      ↓
Assessment definitions
      ↓
Diagnostic / challenge
      ↓
Learner attempts
      ↓
Learner state
      ↓
Review queue
      ↓
Adaptive next activity
```

The book remains source evidence. The knowledge layer stores the normalized learning representation. The learner layer stores what happened when a particular learner interacted with that representation.

## 6. Separation rules

1. A knowledge atom must not contain learner mastery.
2. Learner state must reference knowledge-atom IDs rather than duplicate knowledge definitions.
3. Assessment definitions belong to the knowledge side.
4. Learner responses and outcomes belong to the learner side.
5. Attempt history is historical evidence and should not be overwritten by the latest state.
6. Review queues are derived and can be regenerated from learner state and history.
7. Source provenance must remain traceable through the knowledge layer.
8. Generated questions are not evidence that a knowledge item is required.
9. Changes to static knowledge must not silently rewrite historical learner attempts.
10. Changes to learner state must not alter source evidence or the canonical meaning of a knowledge atom.

## 7. Multiple learners

The initial implementation may use one learner directory, but the model remains compatible with multiple learners.

## 8. Versioning and validation

Schemas for knowledge atoms, assessment definitions, attempts, learner state, sessions, and review queues should be versioned and validated before data is accepted as canonical.

Invalid or structurally ambiguous data should fail closed rather than being silently promoted.

The data architecture supports Git-based provenance: changes to knowledge and learner data can be reviewed and traced through repository history.
