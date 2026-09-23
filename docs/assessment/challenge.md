# Challenge

A Challenge is a concrete task presented to a learner to assess one Knowledge Atom.

A Challenge is an assessment mechanism. It is not itself knowledge, and it is not limited to a linguistic question.

The detailed internal structure of a Challenge is defined separately in `challenge-extraction/challenge-structure.md`. This document focuses on the conceptual model, boundaries, and lifecycle of Challenges.

## Core principles

### One Challenge assesses one Knowledge Atom

Each Challenge targets exactly one Knowledge Atom.

```
Knowledge Atom
      │
      │ assessed by
      ▼
  Challenge
```

If a Challenge appears to require knowledge of multiple independent knowledge points, the knowledge being assessed must be represented by a single Knowledge Atom.

If the Challenge assesses knowledge about a relationship between independent Knowledge Atoms, that relationship is represented by a `relation` Atom. The Challenge then targets that relation Atom.

### Challenge is not Question

A Challenge is a broader concept than a Question.

A Challenge is any concrete exercise or task used to obtain evidence about a Knowledge Atom. Examples include:

- multiple choice;
- fill in the blank;
- sentence completion;
- error correction;
- sentence transformation;
- sentence reordering;
- word formation;
- cloze tasks.

The learner may answer a Challenge, but a Challenge does not have to be phrased as a question.

The current Challenge model supports tasks with a specific expected answer. Speaking and open-ended free-response tasks are outside the current model.

### Challenge is a concrete source occurrence

For source-derived Challenges, a Challenge identifies a specific assessment occurrence in the source material.

Its identity is therefore tied to the source location from which it was extracted. This makes the ID deterministic and traceable: re-extracting the same source occurrence produces the same Challenge ID.

The canonical ID format for a source-derived Challenge is:

```
<source-id>_<segment-id>_<exercise>_<item-number>
```

For example:

```
destination-c1-c2_unit-1_exercise-3_2
```

This means:

- `destination-c1-c2` = source ID;
- `unit-1` = Source Segment ID;
- `exercise-3` = exercise identifier within the segment;
- `2` = item number within the exercise.

Candidate and Official representations of the same source occurrence use the same Challenge ID.

The model intentionally treats Challenge identity as source-occurrence identity rather than as a reusable semantic identity. If two source occurrences happen to represent semantically identical assessment tasks, they still have different source-occurrence IDs. Such rare cases may be reviewed and handled explicitly by a human rather than being resolved by the ID itself.

### Challenge contains a specific expected answer

A supported Challenge contains the information needed to present the task and identify its expected answer.

The specific representation of the task, available alternatives, and expected answer is defined in `challenge-extraction/challenge-structure.md`.

The `answer` is a specific expected answer. It may be represented as structured data when the concrete task requires it.

Examples include:

- a selected option for a multiple-choice task;
- a specific word or form for a fill-in-the-blank task;
- a specific sentence for a sentence transformation;
- a specific arrangement for sentence reordering.

Evaluation of a learner response is a separate assessment/runtime concern. The Challenge provides the expected answer; the assessment process determines the result of comparing a learner response with that answer.

### Challenge references, rather than copies, its Knowledge Atom

A Challenge references its target Knowledge Atom by ID.

It does not copy the Atom's definition, explanation, pronunciation, or other knowledge content into the Challenge.

For example:

```yaml
target_atom_id: past-simple-go
```

The Knowledge Atom remains the authoritative representation of the knowledge.

## Source

A Challenge is currently extracted from a specific source occurrence in learning material.

The source information is therefore part of the Challenge's identity through its ID, while provenance information may also be preserved in `extra`.

For example:

```yaml
extra:
  source:
    source_id: destination-c1-c2
    segment_id: unit-1
    exercise_id: exercise-3
    item_id: 2
```

The source-derived ID is the canonical identity for extracted Challenges. The provenance fields provide explicit source metadata but do not replace the ID.

System-generated or otherwise source-independent Challenges are outside the current source-derived extraction identity model and require a separate identity decision before they are persisted as official Challenges.

## Challenge and learner response

A Challenge produces an opportunity for the learner to demonstrate the targeted knowledge.

Conceptually:

```
Knowledge Atom
      ↓
  Challenge
      ↓
Learner Response
      ↓
Assessment Result
```

The learner's response and performance are not intrinsic properties of the Challenge. They belong to the learner's interaction with the Challenge.

## Difficulty

The Challenge model does not define a `difficulty` concept.

A Challenge may produce different outcomes for different learners, and the adaptive system can use learner performance and other evidence without treating difficulty as an intrinsic Challenge property.

## Challenge lifecycle

Challenge Candidates are reviewed and then either approved or rejected.

```
Challenge Candidate
       ↓
human review
       ├── rejected
       └── approved
                ↓
            officialize
                ↓
       Official Challenge
                ↓
             retired
```

Officialization is a storage transition from Candidate to Official Challenge.

An Official Challenge may be corrected or refined while preserving its identity when the source occurrence and semantic assessment task remain the same. If a change makes it a different assessment occurrence or a different assessment task, a new Challenge identity is required.

## Challenge storage

Challenges are organized by source and Source Segment:

```
data/
└── challenges/
    └── <source-id>/
        └── <segment-id>/
            ├── challenges.md
            └── challenge_candidates.md
```

This is an organizational storage structure. The canonical Challenge identity is defined by the Challenge ID, which for source-derived Challenges encodes the source occurrence.

## Challenge and Adaptive Learning

Challenges provide the concrete assessment mechanism used by the adaptive learning system.

A simplified flow is:

```
Knowledge Atom
      ↓
Select Challenge
      ↓
Learner Response
      ↓
Assessment Result
      ↓
Update Learner State
      ↓
Select next activity
```

Multiple Challenges may target the same Knowledge Atom, allowing the system to assess that Atom through different task presentations and contexts.

Challenge selection is an adaptive-system concern and is not defined by the Challenge model itself.

## Scope

This document defines the conceptual model and boundaries of a Challenge.

It does not yet define:

- the complete Challenge schema;
- the detailed internal Challenge structure;
- reusable Challenge templates or generators;
- learner attempt storage;
- assessment-result storage;
- adaptive Challenge selection algorithms;
- operational Challenge statistics.
