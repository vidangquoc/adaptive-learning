# Challenge Structure

This document defines the canonical structural model of a Challenge.

It complements [Challenge](../challenge.md), which defines the conceptual model. This document focuses on what information a Challenge must contain and how the fields relate to one another.

## 1. Canonical structure

A Challenge is a concrete assessment task that targets exactly one Knowledge Atom and has a specific expected answer.

Conceptually:

\`\`\`text
Challenge
├── id
├── task
├── form
├── target_atom_id
├── answer
└── extra
\`\`\`

The canonical structure deliberately separates:

- **semantic identity** (\`id\`);
- **learner-facing assessment content** (\`task\`);
- **assessment form** (\`form\`);
- **the knowledge being assessed** (\`target_atom_id\`);
- **the expected outcome** (\`answer\`);
- **metadata and provenance** (\`extra\`).

This document defines the structure, not the JSON Schema. The schema should be derived only after the structural decisions here are stable.

## 2. Field definitions

### 2.1 \`id\`

\`id\` is the stable semantic identifier of the Challenge.

It identifies the concrete assessment task, not its source occurrence.

The following do not define Challenge identity:

- source;
- source page or location;
- exercise number;
- item number;
- extraction order;
- Candidate/Official status;
- learner attempts;
- learner performance;
- adaptive selection state.

Candidate and Official representations of the same Challenge use the same \`id\`.

If a modification changes the assessment task semantically, the modified task requires a new Challenge ID.

### 2.2 \`task\`

\`task\` contains the learner-facing assessment task.

It should contain enough information to reconstruct what the learner is expected to do, including when applicable:

- instructions;
- prompt;
- necessary context;
- answer options;
- response elements;
- other information that is part of the concrete task.

\`task\` must not contain information that belongs only to the answer key or internal provenance.

The exact internal structure of \`task\` may depend on the Challenge \`form\`.

For example, a multiple-choice task may need:

\`\`\`yaml
task:
  instruction: "Choose the correct answer."
  prompt: "Darren ___ home at eight yesterday."
  options:
    - "gets"
    - "got"
    - "has got"
\`\`\`

A fill-in-the-blank task may instead contain a prompt and one or more response elements.

The examples are illustrative; the complete form-specific task structures remain to be defined by the Challenge Form taxonomy.

### 2.3 \`form\`

\`form\` identifies the kind of assessment task represented by the Challenge.

Examples include:

- multiple choice;
- fill in the blank;
- sentence completion;
- matching;
- error correction;
- sentence transformation;
- sentence reordering;
- word formation;
- cloze.

The canonical taxonomy and exact values are not finalized by this document.

A Challenge should use a defined form whenever the task can be classified reliably. If no defined form is appropriate, the extraction process must preserve the task as unresolved/unclassified rather than inventing a misleading form.

### 2.4 \`target_atom_id\`

\`target_atom_id\` identifies the single Knowledge Atom assessed by the Challenge.

It is mandatory for a valid Challenge.

\`\`\`text
Challenge
    │
    │ target_atom_id
    ▼
Knowledge Atom
\`\`\`

The field contains an Atom ID, not a copy of Atom content.

A Challenge must not contain a list of independent target Atom IDs.

If the assessment concerns a relationship between independent Knowledge Atoms, the relationship itself must be represented as a \`relation\` Knowledge Atom, and \`target_atom_id\` points to that relation Atom.

Structural relationships among components of a grammar construction remain part of the relevant grammar rule and do not become relation targets merely because a Challenge tests them.

### 2.5 \`answer\`

\`answer\` contains the specific expected answer for the Challenge.

The answer is intrinsic to the current Challenge model because a supported Challenge must have a specific expected outcome.

It is distinct from learner-facing task content:

\`\`\`text
task
  ↓
what the learner is asked to do

answer
  ↓
the expected outcome used to assess the response
\`\`\`

The representation may be scalar or structured according to the Challenge \`form\`.

Examples:

- multiple choice → selected option;
- fill in the blank → expected word/form;
- sentence transformation → expected transformed sentence;
- sentence reordering → expected ordering;
- matching → expected set of pairings.

When a Challenge contains multiple response elements, \`answer\` may contain the corresponding structured set of expected outcomes.

The extractor must not invent an answer. If source evidence is insufficient to establish a specific expected answer, the occurrence is incomplete/unresolved and must not be treated as a fully valid Challenge Candidate.

### 2.6 \`extra\`

\`extra\` contains metadata that is not part of the Challenge's semantic assessment task.

At minimum, it may contain provenance and maintenance information.

A source-derived Challenge may use:

\`\`\`yaml
extra:
  source:
    source_id: destination-c1-c2
    segment_id: ...
    exercise_id: ...
    item_id: ...
  notes: ...
\`\`\`

The exact provenance structure remains to be finalized separately.

\`extra\` must not contain learner/runtime state such as:

- learner responses;
- attempts;
- correctness history;
- mastery;
- review state;
- review scheduling;
- aggregate performance statistics;
- adaptive selection state.

## 3. Candidate and Official representation

Candidate and Official Challenges share the same semantic structure and ID.

A Candidate additionally carries review lifecycle information.

Conceptually:

\`\`\`text
Candidate Challenge
├── canonical Challenge fields
└── review_status
\`\`\`

where:

\`\`\`text
review_status ∈ { pending, approved, rejected }
\`\`\`

Official Challenges do not carry Candidate review status.

Officialization is a storage transition:

\`\`\`text
Challenge Candidate
      │
      │ approved + officialize
      ▼
Official Challenge
\`\`\`

The semantic Challenge ID remains unchanged during this transition.

## 4. Structural invariants

A valid Challenge must satisfy these invariants:

1. It has exactly one stable \`id\`.
2. It has exactly one \`target_atom_id\`.
3. \`target_atom_id\` identifies a Knowledge Atom.
4. It has a concrete \`task\`.
5. It has a defined \`form\`, or is explicitly preserved as unresolved/unclassified during extraction.
6. A supported valid Challenge has a specific \`answer\`.
7. Source provenance, when present, is metadata and does not define identity.
8. Learner/runtime data is outside the Challenge structure.
9. Candidate and Official representations use the same semantic Challenge ID.
10. A semantic change to the assessment task requires a new Challenge identity.

## 5. Source occurrence versus Challenge identity

A source occurrence is evidence from which a Challenge Candidate is extracted.

It is not the Challenge itself.

The distinction is:

\`\`\`text
Source occurrence
      ↓
Challenge Candidate
      ↓
semantic Challenge
\`\`\`

Multiple source occurrences may later be recognized as the same semantic Challenge. In that case, provenance may retain multiple origins while the Challenge continues to have one semantic ID.

Conversely, two source occurrences that are similar but represent semantically different assessment tasks must remain different Challenges.

Deduplication and reuse are therefore separate processes from extraction.

## 6. Relationship to extraction

Challenge extraction and Knowledge Atom extraction use the same contextual analysis of a Source Segment.

The extractor should determine the target Atom while determining the Challenge itself.

\`\`\`text
Source Segment
      ↓
Contextual Analysis
      ├── Knowledge Atom Candidates
      └── Challenge Candidates
                 │
                 └── target_atom_id
\`\`\`

The target Atom may be:

- an existing Knowledge Atom Candidate;
- an existing Official Knowledge Atom;
- a Knowledge Atom identified and created during the same contextual analysis.

A later post-extraction step must not be required to guess which Atom a Challenge assesses.

## 7. Form-specific structure

This document intentionally does not freeze the detailed structure of every Challenge form.

Form-specific definitions should determine, as necessary:

- the shape of \`task\`;
- the shape of \`answer\`;
- required response elements;
- constraints needed to interpret the response;
- how source answer information maps to the canonical answer.

For example:

\`\`\`text
multiple choice
    task.options
    answer.selected_option

matching
    task.items + task.matches
    answer.pairings

sentence transformation
    task.original_sentence + instruction
    answer.transformed_sentence
\`\`\`

These are structural examples, not the final schema.

## 8. Source preservation and fail-closed behavior

Challenge structure must preserve source evidence faithfully.

Extraction must not silently invent or repair:

- missing task text;
- missing options;
- missing response elements;
- exercise/item boundaries;
- target Atom;
- expected answer.

If an essential structural element cannot be established from the source, the extraction result must explicitly represent the uncertainty or omission rather than silently producing a normal valid Challenge.

## 9. What does not belong in the structure

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
- source occurrence as semantic identity.

These belong to assessment runtime, learner state, adaptive-system data, extraction metadata, or implementation mechanisms as appropriate.

## 10. Status of unresolved details

This document establishes the canonical conceptual structure but does not yet finalize:

- the complete Challenge Form taxonomy;
- the exact form-specific \`task\` structures;
- the exact form-specific \`answer\` structures;
- the complete provenance structure;
- the final Challenge ID generation algorithm;
- the Candidate and Official JSON Schemas.

Those decisions should be resolved before the corresponding schemas are finalized.
