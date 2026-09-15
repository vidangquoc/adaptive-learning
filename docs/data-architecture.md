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

The structure is a logical target architecture. Individual directories/files may be introduced incrementally as the implementation phase progresses.

## 3. Knowledge layer

`data/knowledge/` contains information that is independent of a particular learner.

### `sources/`

Contains source material used to derive or validate knowledge. For books, the source boundary should preserve book/chapter identity and precise provenance.

### `atoms/`

Contains canonical knowledge atoms.

```text
data/knowledge/atoms/
├── grammar/
└── lexicon/
```

A knowledge atom is a unit that can be independently diagnosed, taught, and assessed.

One lexical sense is one atom by default. Independently useful grammar uses, constructions, rules, or contrasts may be separate atoms when supported by source evidence.

Knowledge atoms must not contain learner mastery or learner-specific review state.

### `relations/`

Contains explicit typed relationships between knowledge atoms and other knowledge entities.

Relationships should not be represented through an obligatory parent/child ancestry tree.

### `assessments/`

Contains definitions of questions/challenges and their relationships to the knowledge or competency dimensions they test.

An assessment definition answers:

> What does this question test?

It does not contain a learner's response history.

One assessment may test multiple atoms, and one atom may be tested by multiple assessments.

## 4. Learner layer

`data/learner/` contains learner-specific state and history.

### `profile.yaml`

Contains stable learner configuration that is necessary for the learning system, without duplicating knowledge definitions.

### `state/`

Contains the current derived interpretation of the learner's accumulated evidence.

```text
data/learner/state/
├── atom-state.yaml
└── competency-state.yaml
```

An atom-state record references a knowledge atom by ID and stores the learner's current evidence-derived state.

Conceptually:

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

The state is an interpretation of attempts; it is not source evidence itself.

### `attempts/`

Contains the historical assessment events produced by the learner's interactions.

Attempts should be append-oriented and preserved rather than overwritten, because they are the evidence from which learner state is derived.

Conceptual record:

```yaml
attempt_id: attempt-00052
session_id: 2026-09-15-001
question_id: q.ch01.0007
atom_ids:
  - gram.c1.00042
response:
  answer: "had gone"
result:
  correctness: correct
  confidence: uncertain
timestamp: 2026-09-15T10:32:00+07:00
```

### `sessions/`

Contains review-session records.

A session is a sequence of adaptive decisions, not merely a static list of questions. A session should preserve its goal, selected activities, attempts, resulting state changes, and next actions.

Conceptually:

```text
Question
   ↓
Learner response
   ↓
Attempt / evidence
   ↓
State update
   ↓
Select next question
   ↺
```

### `review-queue.yaml`

The review queue is a derived view of learner state and attempt history. It is not the source of truth.

Each queue entry should explain why the activity is recommended and what activity should be performed.

## 5. Book-to-data workflow

When a learner supplies a book and requests a chapter, the intended data flow is:

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
2. Learner state must reference knowledge-atom IDs rather than duplicate the knowledge definition.
3. Assessment definitions belong to the knowledge side because they describe what can be assessed.
4. Learner responses and outcomes belong to the learner side.
5. Attempt history is historical evidence and should not be overwritten by the latest state.
6. Review queues are derived and can be regenerated from learner state and history.
7. Source provenance must remain traceable through the knowledge layer.
8. Generated questions are not evidence that a knowledge item is required.
9. Changes to static knowledge must not silently rewrite historical learner attempts.
10. Changes to learner state must not alter source evidence or the canonical meaning of a knowledge atom.

## 7. Multiple learners

The initial implementation may use one learner directory, but the model should remain compatible with multiple learners.

A future multi-learner layout may use:

```text
data/
└── learner/
    ├── <learner-id>/
    │   ├── profile.yaml
    │   ├── state/
    │   ├── attempts/
    │   ├── sessions/
    │   └── review-queue.yaml
    └── ...
```

The knowledge layer remains shared.

## 8. Versioning and validation

Schemas for knowledge atoms, assessment definitions, attempts, learner state, sessions, and review queues should be versioned and validated before data is accepted as canonical.

Invalid or structurally ambiguous data should fail closed rather than being silently promoted.

The data architecture supports Git-based provenance: changes to knowledge and learner data can be reviewed and traced through repository history.
