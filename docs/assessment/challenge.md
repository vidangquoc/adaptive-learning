# Challenge

A Challenge is a concrete task presented to a learner to assess one Knowledge Atom.

A Challenge is an assessment mechanism. It is not itself knowledge, and it is not limited to a linguistic question.

The detailed internal structure of a Challenge is defined separately in `challenge-extraction/challenge-structure.md`. This document focuses on the conceptual model, boundaries, and lifecycle of Challenges.

## Core principles

### One Challenge assesses one Knowledge Atom

Each Challenge targets exactly one Knowledge Atom.

```text
Knowledge Atom
      │
      │ assessed by
      ▼
  Challenge
```

If a Challenge appears to involve multiple independent knowledge points, the current model still requires exactly one target Knowledge Atom. Contextual analysis must establish which single knowledge target the Challenge assesses. If that cannot be established, the occurrence is unresolved/incomplete rather than a multi-target Challenge.

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

```text
<source-id>_<segment-id>_<exercise>_<item-number>
```

For example:

```text
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

The `answer` contains the expected answer for each input the Challenge requires the learner to provide.

An **input** is one distinct thing that the Challenge requires the learner to provide. Each thing the learner must provide counts as one input. The number of answer values therefore corresponds directly to the number of inputs:

- when the Challenge requires one input, `answer` is a string;
- when the Challenge requires multiple inputs, `answer` is an array of strings, with elements corresponding to the inputs in order.

For example:

- a multiple-choice task requiring one choice has one input and a string answer;
- a fill-in-the-blank task with one blank has one input and a string answer;
- a fill-in-the-blank task with two blanks has two inputs and an answer array containing the two expected values;
- a sentence transformation requiring one complete transformed sentence has one input, even though the sentence contains multiple words;
- a sentence reordering task requiring one complete reordered sentence has one input.

Examples:

```yaml
# One input
answer: got
```

```yaml
# Two inputs
answer:
  - got
  - home
```

The answer represents expected outcomes, not learner responses or evaluation rules. Evaluation of a learner response is a separate assessment/runtime concern.

### Challenge references, rather than copies, its Knowledge Atom

A Challenge references its target Knowledge Atom by ID.

It does not copy the Atom's definition, explanation, pronunciation, or other knowledge content into the Challenge.

For example:

```yaml
target_atom_id: past-simple-go
```

The Knowledge Atom remains the authoritative representation of the knowledge.

## Source

A source-derived Challenge is traceable to a specific source occurrence.

The source occurrence is encoded in the Challenge ID, while explicit machine-readable provenance is preserved in `extra.source`.

For example:

```yaml
extra:
  source:
    source_id: destination-c1-c2
    page_number: 42
    segment_id: unit-1
    exercise_name: "Exercise 3"
    item_number: 2
```

The provenance fields supplement the ID and do not replace it.

Source-independent Challenges are outside the current source-derived extraction identity model and require a separate identity decision before they are persisted as official Challenges.

## Source preservation and fail-closed extraction

Challenge extraction is explicitly fail-closed.

The extractor MUST NOT silently invent, repair, normalize, or infer away missing essential assessment content, including:

- instruction/task wording;
- prompt content;
- explicit options required by the source task;
- learner response elements;
- exercise/item boundaries;
- target Atom;
- expected answer.

Source evidence is authoritative. Canonical Challenge fields may be derived from source evidence, but extraction must preserve the source assessment faithfully and must not silently alter wording or structure in a way that changes the task presented to the learner.

If an essential element cannot be established sufficiently from the available source evidence, the occurrence must be represented as incomplete, unresolved, or skipped rather than emitted as a normal valid Challenge Candidate.

This applies even when the source contains a numbered item, blank, answer line, or other superficial exercise formatting. Such formatting alone does not establish that a complete Challenge can be extracted.

### Reproducibility

Challenge extraction is reproducible under a fixed extraction context.

Given the same source evidence, contextual inputs, and extraction rules/version, the extraction process should produce the same structural result.

An intentional change to extraction rules, contextual interpretation, or another extraction input is a process/model change and must be treated as such rather than being presented as if it were the same extraction result.

The reproducibility requirement does not prevent later human review, correction, or officialization. It governs the extraction result produced from a fixed input and rule set.

## Challenge and learner response

A Challenge produces an opportunity for the learner to demonstrate the targeted knowledge.

Conceptually:

```text
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

```text
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

```text
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

```text
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

It does not define:

- learner attempt storage;
- assessment-result storage;
- adaptive Challenge selection algorithms;
- operational Challenge statistics.

The canonical Challenge structure and Candidate/Official schemas are defined in:

- `challenge-extraction/challenge-structure.md`;
- `schemas/candidate-challenge.schema.json`;
- `schemas/official-challenge.schema.json`.
