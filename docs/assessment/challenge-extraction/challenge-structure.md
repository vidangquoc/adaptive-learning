# Challenge Structure

This document defines the canonical structural model of a Challenge.

It complements [Challenge](../challenge.md), which defines the conceptual model. This document focuses on the information every Challenge needs and on the relationship between those fields.

## 1. Canonical structure

A Challenge is a concrete assessment task that targets exactly one Knowledge Atom and has a specific expected answer. The one-Challenge-to-one-Atom invariant is mandatory for both Candidate and Official Challenges.

The current model does not require a Challenge Form taxonomy. The different exercise styles observed in learning material can be represented by the same small set of structural fields.

```text
Challenge
├── id
├── target_atom_id
├── instruction
├── prompt
├── options?
├── answer
└── extra
```

The canonical structure separates:

- source-occurrence identity (id);
- the knowledge being assessed (target_atom_id);
- what the learner is asked to do (instruction);
- the concrete material the learner acts on (prompt);
- optional finite choices (options);
- the expected outcome (answer);
- metadata and source information (extra).

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

```text
<source-id>_<segment-id>_<exercise>_<item-number>
```

Example:

```text
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

Source location is therefore not merely source metadata for a source-derived Challenge; it is encoded in the Challenge ID.

If two source occurrences happen to contain semantically identical assessment tasks, they still have different source-occurrence IDs. Rare duplicate or special cases are expected to be handled by human review rather than by automatic ID-level deduplication.

If the source occurrence itself changes in a way that changes the assessment task or its source identity, a new Challenge ID is required.

## 4. target_atom_id

`target_atom_id` identifies the single Knowledge Atom assessed by the Challenge.

It is mandatory for a valid Challenge and MUST contain exactly one Atom ID.

```text
Challenge
    │
    │ target_atom_id
    ▼
Knowledge Atom
```

The field contains an Atom ID, not a copy of Atom content.

A Challenge must not contain a list of independent target Atom IDs. The following representations are invalid:

```yaml
# Invalid: multiple target IDs
target_atom_id:
  - atom-a
  - atom-b
```

```yaml
# Invalid: plural target field
target_atom_ids:
  - atom-a
  - atom-b
```

There is no multi-target form of Challenge in the canonical model.

If the assessment concerns a relationship between independent Knowledge Atoms, the relationship itself must be represented as a relation Knowledge Atom, and target_atom_id points to that relation Atom.

Structural relationships among components of a grammar construction remain part of the relevant grammar rule and do not become relation targets merely because a Challenge tests them.

## 5. instruction

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

It should contain only the learner-facing task direction. Source information, answer-key information, and learner/runtime state do not belong here.

## 6. prompt

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

## 6.1 Source preservation and fail-closed extraction

Challenge extraction MUST be fail-closed.

The extractor must not silently invent, repair, normalize, or infer away missing essential assessment content. In particular, it must not silently supply or modify:

- instruction/task wording;
- prompt content;
- explicit options required by the source task;
- learner response elements;
- exercise/item boundaries;
- target Atom;
- expected answer.

Source evidence is authoritative. Canonical Challenge fields may be derived from that evidence, but extraction must preserve the source assessment faithfully and must not silently change wording or structure in a way that changes what the learner is asked to do.

A source occurrence may be emitted as a normal valid Challenge Candidate only when the contextual analysis establishes all essential structural information needed by the canonical model.

If an essential element cannot be established sufficiently from the available source evidence, the extraction result MUST be represented as incomplete, unresolved, or skipped rather than silently converted into a normal valid Challenge Candidate.

This rule applies even when the source contains a numbered item, blank, answer line, or other superficial exercise formatting. Such formatting alone is not sufficient evidence that a complete Challenge can be extracted.

### Reproducibility

Challenge extraction is reproducible under a fixed extraction context.

Given the same:

- source evidence;
- contextual inputs;
- extraction rules/version;

the extraction process should produce the same Challenge structural result.

An intentional change to extraction rules, contextual interpretation, or another extraction input is a process/model change. It must be treated as such rather than being presented as if it were the same extraction result.

The reproducibility requirement does not prohibit later human review, correction, or officialization. It governs the extraction result produced from a fixed input and rule set.

## 7. options

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

## 8. answer

`answer` contains the specific expected outcome for the Challenge.

The answer is intrinsic to the current Challenge model because a supported Challenge must have a specific expected answer.

The answer represents the expected value for each input the Challenge requires the learner to provide.

An **input** is one distinct thing that the Challenge requires the learner to provide. Each thing the learner must provide counts as one input.

The cardinality and representation of `answer` follow a simple rule:

```text
1 input
    ↓
answer: string

N inputs (N > 1)
    ↓
answer:
  - string
  - string
  - ...
```

When there is one input, `answer` is a string. When there are multiple inputs, `answer` is an array of strings. The array elements correspond to the inputs in their required order.

The number of answer values MUST equal the number of inputs required by the Challenge.

Examples:

```yaml
# Multiple choice: the learner provides one choice
options:
  - gets
  - got
  - has got
answer: got
```

```yaml
# One blank: the learner provides one word/form
prompt: "Darren ___ home at eight yesterday."
answer: got
```

```yaml
# Two blanks: the learner provides two values
prompt: "Darren ___ ___ yesterday."
answer:
  - got
  - home
```

```yaml
# Sentence transformation: the learner provides one complete sentence
answer: "I used to live in London when I was a child."
```

A sentence containing many words is still one input if the learner is required to provide one complete sentence.

The answer does not describe how the learner response is evaluated. Case, whitespace, punctuation, alternative valid responses, normalization, and other equivalence rules belong to evaluation and are outside the Expected Answer model.

For multiple-choice Challenges, the answer must identify one of the provided option values by content, and therefore:

```text
answer ∈ options
```

The extractor must not invent an answer. If source evidence is insufficient to establish a specific expected answer, the occurrence is incomplete/unresolved and must not be treated as a fully valid Challenge Candidate.

## 9. extra

`extra` contains metadata that is not part of the Challenge's semantic assessment task.

At minimum, it may contain source information and maintenance information.

For a source-derived Challenge, source information is represented as:

```yaml
extra:
  source:
    source_id: destination-c1-c2
    page_number: 42
    segment_id: unit-1
    exercise_name: "Exercise 3"
    item_number: 2
  notes: ...
```

The source fields duplicate information encoded in the ID for explicit machine-readable source information. They do not replace the ID.

### 9.1 Source fields

The canonical source fields are:

- `source_id`: the source registered in the source registry.
- `page_number`: the page number in the original source artifact, not a page number relative to the Source Segment or a PDF viewer's zero/one-based page index.
- `segment_id`: the Source Segment containing the Challenge occurrence.
- `exercise_name`: the name or label of the exercise as it appears in the source material.
- `item_number`: the item number or label within the exercise.

`page_number` refers to the page numbering of the original source itself. If the source artifact is a scanned or paginated book, this means the printed/book page number when one exists, rather than the technical page index of the digital artifact.

`exercise_name` preserves the source exercise's name or label rather than introducing a system-generated exercise identity.

`item_number` identifies the item within the exercise for source information purposes; it is not a separately persisted Challenge entity.

The source structure is explicit machine-readable origin information. It does not define a second identity for the Challenge.

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
3. It has exactly one target_atom_id.
4. target_atom_id identifies exactly one Knowledge Atom.
5. target_atom_id is a single scalar Atom ID; array-valued or plural target fields are invalid.
6. It has a concrete instruction.
7. It has a concrete prompt.
8. options is optional and, when present, contains the finite semantic choices presented to the learner.
9. A supported valid Challenge has a specific expected answer.
10. An input is one distinct thing the Challenge requires the learner to provide.
11. If the Challenge requires one input, answer is a string.
12. If the Challenge requires multiple inputs, answer is an array of strings whose elements correspond to the inputs in order.
13. The number of answer values MUST equal the number of inputs required by the Challenge.
14. For a multiple-choice Challenge, answer identifies one of the values in options.
15. Evaluation rules are outside the Expected Answer model.
16. Source information, when present, is metadata that supplements the ID.
17. Learner/runtime data is outside the Challenge structure.
18. Candidate and Official representations use the same Challenge ID.
19. No persisted form field is required by the canonical Challenge structure.
20. Rare duplicate/special source cases are handled through human review rather than by automatic ID-level deduplication.
21. Extraction is fail-closed and does not silently invent or repair essential assessment content.
22. Source evidence is preserved faithfully when deriving the Challenge.
23. Under a fixed source, contextual input, and extraction-rule version, extraction is reproducible.

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

A later post-extraction step must not be required to guess which Atom a Challenge assesses. A Challenge Candidate is not valid until contextual analysis establishes exactly one target Atom. If the analysis identifies multiple independent knowledge points but cannot determine one assessed Atom, the occurrence is unresolved/incomplete rather than a multi-target Candidate.

The same extraction analysis also determines the concrete instruction, prompt, optional options, and answer from the source evidence.

## 14. Source preservation and fail-closed behavior

This section is retained as the canonical cross-reference for the extraction rules introduced in Section 6. The requirements apply to the entire Challenge extraction process, not only to schema validation.

## 15. Status of the structure

The canonical Challenge structure is now intentionally small:

```text
Challenge
├── id
├── target_atom_id
├── instruction
├── prompt
├── options?
├── answer
└── extra
```

This structure is the basis for the Candidate and Official Challenge schemas.

The schema should be derived from this structure rather than introducing a separate form taxonomy.

Future work may refine the internal representation of prompt, options, answer, and source information where real source material demonstrates a genuine structural need. Such refinement should not introduce a Challenge Form field unless there is a clear semantic requirement that cannot be represented by the existing structure.
