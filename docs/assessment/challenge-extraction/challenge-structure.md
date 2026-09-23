# Challenge Structure

This document defines the canonical structural model of a Challenge.

It complements [Challenge](../challenge.md), which defines the conceptual model. This document focuses on the information every Challenge needs and on the relationship between those fields.

## 1. Canonical structure

A Challenge is a concrete assessment task that targets exactly one Knowledge Atom and has a specific expected answer.

The current model does not require a Challenge Form taxonomy. The different exercise styles observed in learning material can be represented by the same small set of structural fields.

```text
Challenge
├── id
├── instruction
├── prompt
├── options?
├── target_atom_id
├── answer
└── extra
```

The canonical structure separates:

- source-occurrence identity (id);
- what the learner is asked to do (instruction);
- the concrete material the learner acts on (prompt);
- optional finite choices (options);
- the knowledge being assessed (target_atom_id);
- the expected outcome (answer);
- metadata and provenance (extra).

There is deliberately no form field.

## 2. Why a separate Challenge Form is not required

The exercise forms examined so far can all be expressed using the same core structure:

```text
Challenge
├── instruction
├── prompt
├── options?
└── answer
```

For example:

- a fill-in-the-blank task provides an instruction, a prompt containing the missing material, and an expected answer;
- a sentence transformation task provides an instruction, a source sentence or other prompt, and an expected transformed answer;
- a sentence reordering task provides an instruction, a prompt containing the supplied words or chunks, and an expected ordering;
- a word-formation task provides an instruction, a prompt containing the lexical context and base word, and the expected derived form;
- an error-correction task provides an instruction, a prompt containing the erroneous language, and the expected correction;
- a short-answer task provides an instruction and prompt without finite options, together with a specific expected answer;
- a multiple-choice task additionally provides options, with answer identifying the selected option by its content.

These differences are differences in the content and interpretation of the same fields, rather than evidence that the Challenge ontology needs a persisted form taxonomy.

True/False is likewise not a separate concept. It can be represented as:

```yaml
options:
  - true
  - false
answer: true
```

The presentation labels A/B/C, radio buttons, numbering, or other UI details are not part of the semantic answer.

A Challenge may therefore be classified as a particular exercise style by a UI, extractor, generator, or analysis process when useful, without making that classification part of the canonical Challenge identity or structure.

## 3. id

`id` is the stable identifier of the Challenge source occurrence.

For source-derived Challenges, the canonical ID format is:

```
<source-id>_<segment-id>_<exercise>_<item-number>
```

Example:

```
destination-c1-c2_unit-1_exercise-3_2
```

The components identify:

- `source-id`: the source registered in the source registry;
- `segment-id`: the Source Segment containing the exercise;
- `exercise`: the exercise identifier within the segment;
- `item-number`: the item number within that exercise.

This ID identifies a specific assessment occurrence in the source material. It is intentionally traceable and deterministic.

Candidate and Official representations of the same source occurrence use the same ID.

The following do not independently define Challenge identity:

- extraction order;
- Candidate/Official status;
- learner attempts;
- learner performance;
- adaptive selection state.

Source location is therefore not merely provenance for a source-derived Challenge; it is encoded in the Challenge ID.

If two source occurrences happen to contain semantically identical assessment tasks, they still have different source-occurrence IDs. Rare duplicate or special cases are expected to be handled by human review rather than by automatic ID-level deduplication.

If the source occurrence itself changes in a way that changes the assessment task or its source identity, a new Challenge ID is required.

## 4. instruction

instruction tells the learner what to do.

Examples:

```yaml
instruction: "Choose the correct answer."
```

```yaml
instruction: "Complete the sentence."
```

```yaml
instruction: "Rewrite the sentence using 'used to'."
```

The instruction is part of the concrete Challenge because changing it can change what the learner is being asked to demonstrate.

It should contain only the learner-facing task direction. Source provenance, answer-key information, and learner/runtime state do not belong here.

## 5. prompt

prompt contains the concrete material on which the learner performs the Challenge.

It may be a string or structured data when the task requires more than one component.

Examples:

```yaml
prompt: "Darren ___ home at eight yesterday."
```

```yaml
prompt:
  sentence: "I lived in London when I was a child."
```

```yaml
prompt:
  words:
    - yesterday
    - home
    - went
    - I
```

The prompt may contain blanks, supplied words, a source sentence, a base word, an erroneous sentence, or other concrete task material.

The prompt is not the expected answer.

## 6. options

`options` is optional and is present when the learner must choose from a finite set of explicitly provided alternatives.

For example:

```yaml
instruction: "Choose the correct answer."
prompt: "Darren ___ home at eight yesterday."
options:
  - gets
  - got
  - has got
answer: got
```

The options are semantic values, not presentation labels.

The UI may display them as A/B/C, 1/2/3, radio buttons, or another presentation format. Those presentation details do not belong to the Challenge's semantic structure.

The answer for a multiple-choice Challenge must correspond to an option by its content:

```text
answer ∈ options
```

For True/False:

```yaml
options:
  - true
  - false
answer: true
```

No separate true_false form is required.

If a Challenge does not require finite choices, options is omitted.

## 7. target_atom_id

`target_atom_id` identifies the single Knowledge Atom assessed by the Challenge.

It is mandatory for a valid Challenge.

```text
Challenge
    │
    │ target_atom_id
    ▼
Knowledge Atom
```

The field contains an Atom ID, not a copy of Atom content.

A Challenge must not contain a list of independent target Atom IDs.

If the assessment concerns a relationship between independent Knowledge Atoms, the relationship itself must be represented as a relation Knowledge Atom, and target_atom_id points to that relation Atom.

Structural relationships among components of a grammar construction remain part of the relevant grammar rule and do not become relation targets merely because a Challenge tests them.

## 8. answer

`answer` contains the specific expected outcome for the Challenge.

The answer is intrinsic to the current Challenge model because a supported Challenge must have a specific expected answer.

The answer may be a scalar value or structured data when the Challenge contains multiple response elements.

Examples:

```yaml
# Multiple choice
answer: got
```

```yaml
# Fill in the blank
answer: got
```

```yaml
# Sentence transformation
answer: "I used to live in London when I was a child."
```

```yaml
# Sentence reordering
answer:
  - I
  - went
  - home
  - yesterday
```

```yaml
# Multiple response elements
answer:
  - got
  - home
```

The exact shape of answer is determined by the concrete task content rather than by a separate Challenge Form taxonomy.

For multiple-choice Challenges, the answer must identify one of the provided option values.

The extractor must not invent an answer. If source evidence is insufficient to establish a specific expected answer, the occurrence is incomplete/unresolved and must not be treated as a fully valid Challenge Candidate.

## 9. extra

`extra` contains metadata that is not part of the Challenge's semantic assessment task.

At minimum, it may contain provenance and maintenance information.

For a source-derived Challenge, provenance may be represented as:

```yaml
extra:
  source:
    source_id: destination-c1-c2
    segment_id: unit-1
    exercise_id: exercise-3
    item_id: 2
  notes: ...
```

The source fields duplicate information encoded in the ID for explicit machine-readable provenance. They do not replace the ID.

The exact provenance structure remains to be finalized separately.

extra must not contain learner/runtime state such as:

- learner responses;
- attempts;
- correctness history;
- mastery;
- review state;
- review scheduling;
- aggregate performance statistics;
- adaptive selection state.

## 10. Candidate and Official representation

Candidate and Official Challenges share the same canonical structure and ID.

A Candidate additionally carries review lifecycle information.

Conceptually:

```text
Candidate Challenge
├── canonical Challenge fields
└── review_status
```

where:

```text
review_status ∈ { pending, approved, rejected }
```

Official Challenges do not carry Candidate review status.

Officialization is a storage transition:

```text
Challenge Candidate
      │
      │ approved + officialize
      ▼
Official Challenge
```

The Challenge ID remains unchanged during this transition.

## 11. Structural invariants

A valid Challenge must satisfy these invariants:

1. It has exactly one stable id.
2. For a source-derived Challenge, the id follows the canonical source-occurrence format.
3. It has a concrete instruction.
4. It has a concrete prompt.
5. It has exactly one target_atom_id.
6. target_atom_id identifies a Knowledge Atom.
7. options is optional and, when present, contains the finite semantic choices presented to the learner.
8. A supported valid Challenge has a specific answer.
9. For a multiple-choice Challenge, answer identifies one of the values in options.
10. Source provenance, when present, is metadata that supplements the ID.
11. Learner/runtime data is outside the Challenge structure.
12. Candidate and Official representations use the same Challenge ID.
13. No persisted form field is required by the canonical Challenge structure.
14. Rare duplicate/special source cases are handled through human review rather than by automatic ID-level deduplication.

## 12. Source occurrence and Challenge identity

For source-derived Challenges, the source occurrence is the identity anchor of the Challenge.

The distinction is:

```text
Source occurrence
      ↓
Challenge Candidate
      ↓
Challenge with source-occurrence ID
```

The source occurrence is encoded directly into the Challenge ID through source, segment, exercise, and item identifiers.

Two different source occurrences therefore normally produce two different Challenge IDs, even when their visible tasks are semantically identical.

This deliberately favors deterministic extraction, source traceability, and simple lifecycle management over automatic semantic deduplication.

## 13. Relationship to extraction

Challenge extraction and Knowledge Atom extraction use the same contextual analysis of a Source Segment.

The extractor should determine the target Atom while determining the Challenge itself.

```text
Source Segment
      ↓
Contextual Analysis
      ├── Knowledge Atom Candidates
      └── Challenge Candidates
                 │
                 └── target_atom_id
```

The target Atom may be:

- an existing Knowledge Atom Candidate;
- an existing Official Knowledge Atom;
- a Knowledge Atom identified and created during the same contextual analysis.

A later post-extraction step must not be required to guess which Atom a Challenge assesses.

The same extraction analysis also determines the concrete instruction, prompt, optional options, and answer from the source evidence.

## 14. Source preservation and fail-closed behavior

Challenge structure must preserve source evidence faithfully.

Extraction must not silently invent or repair:

- missing instruction;
- missing prompt;
- missing options when the source requires explicit options;
- missing response elements;
- exercise/item boundaries;
- target Atom;
- expected answer.

If an essential structural element cannot be established from the source, the extraction result must explicitly represent the uncertainty or omission rather than silently producing a normal valid Challenge.

In particular, extraction must not create a Challenge merely because an exercise contains a blank or a numbered item. Contextual analysis must establish that the occurrence is an independent evaluable task and that its required structural information can be established.

## 15. What does not belong in the structure

The following are deliberately outside the canonical Challenge structure:

- learner attempts;
- learner responses;
- assessment results;
- review history;
- learner mastery or ability;
- review scheduling;
- aggregate Challenge statistics;
- adaptive selection priority;
- reusable templates;
- generators;
- presentation-only labels such as A/B/C;
- a Challenge Form taxonomy used only to classify exercise styles.

These belong to assessment runtime, learner state, adaptive-system data, extraction metadata, UI presentation, or implementation mechanisms as appropriate.

## 16. Status of the structure

The canonical Challenge structure is now intentionally small:

```text
Challenge
├── id
├── instruction
├── prompt
├── options?
├── target_atom_id
├── answer
└── extra
```

This structure is the basis for the Candidate and Official Challenge schemas.

The schema should be derived from this structure rather than introducing a separate form taxonomy.

Future work may refine the internal representation of prompt, options, answer, and provenance where real source material demonstrates a genuine structural need. Such refinement should not introduce a Challenge Form field unless there is a clear semantic requirement that cannot be represented by the existing structure.
