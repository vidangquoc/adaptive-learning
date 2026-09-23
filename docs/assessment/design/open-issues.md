# Challenge Open Issues

This document records unresolved design questions and documentation gaps identified by comparing the Challenge model with the Knowledge Atom model.

These are design issues, not implementation tasks. They should be resolved before the corresponding Challenge schema and implementation are finalized.

## 1. Define the canonical Challenge structure

Knowledge Atoms have a dedicated `atom-structure.md` defining their canonical fields and field semantics. Challenges currently have only a conceptual structure:

```text
Challenge
├── task
├── form
├── target_atom_id
└── answer
```

Need to define a dedicated `challenge-structure.md` that specifies:

- canonical top-level fields;
- required versus nullable fields;
- field semantics;
- Candidate versus Official representation;
- provenance structure;
- expected-answer structure;
- semantic identity rules;
- relationship between task, form, target Atom, and answer.

## 2. Define Challenge semantic identity and ID

Challenge identity is based on the concrete assessment task, not merely its target Knowledge Atom, and not its source occurrence.

Need to specify:

- what constitutes the semantic identity of a Challenge;
- how the Challenge ID is constructed;
- which task changes preserve identity;
- which changes require a new Challenge ID;
- that source page, exercise number, item number, extraction order, candidate status, and learner state must not be encoded in the canonical ID;
- that Candidate and Official Challenge use the same semantic ID;
- how identical or equivalent Challenges from different source occurrences can be recognized as the same semantic Challenge.

The distinction must remain explicit:

```text
Challenge semantic identity
        ≠
source occurrence
        ≠
learner attempt
```

## 3. Define Challenge provenance structure

Challenge extraction requires exact traceability to the source assessment occurrence, but the canonical provenance structure has not yet been defined.

Need to specify the canonical provenance fields, including as applicable:

- `source_id`;
- `segment_id`;
- source location;
- exercise identifier;
- item identifier;
- other information needed to identify the exact assessment occurrence.

Consider whether provenance should distinguish:

- where the Challenge occurrence originates; and
- the source evidence supporting the decision that the occurrence is a Challenge, its boundary, form, target Atom, or expected answer.

Provenance must remain metadata and must not define Challenge semantic identity.

## 4. Define Challenge metadata

Knowledge Atoms have an explicit `extra` metadata structure. Challenge metadata has not yet been fully specified.

Need to determine the canonical metadata structure and which metadata is permitted.

At minimum, provenance and maintenance notes may need explicit representation.

The structure must explicitly exclude learner/runtime data such as:

- attempts;
- learner responses;
- correctness history;
- mastery;
- review state;
- aggregate performance statistics;
- adaptive selection state.

## 5. Define the Challenge Form taxonomy

Extraction principles require Challenges to be classified using a defined set of Challenge forms, but the canonical form taxonomy has not yet been documented.

Need to define the supported forms and their semantics.

Potential forms already discussed include:

- multiple choice;
- fill in the blank;
- sentence completion;
- matching;
- error correction;
- sentence transformation;
- reordering;
- word formation;
- cloze.

The list above is not yet a finalized taxonomy.

The taxonomy should provide a decision rule for classifying source tasks and should allow an unclassified/unresolved Candidate when no existing form is appropriate.

## 6. Fully specify the expected-answer model

The current model requires a supported Challenge to have a specific expected answer, but `answer` is only conceptually defined.

Need to specify:

- the canonical representation of `answer`;
- how answers differ by Challenge form;
- whether an answer is a scalar, object, list, or another structured value;
- how multiple response elements within one Challenge are represented;
- how source answer keys map to the canonical expected answer;
- what constitutes sufficient evidence for an answer;
- how incomplete/unresolved Challenges are represented when the source does not establish a specific answer.

The extractor must never invent an expected answer.

The distinction should remain explicit:

```text
task
    learner-facing assessment content

answer
    expected outcome used for assessment

source
    provenance
```

## 7. Enforce the one-Challenge-to-one-Atom invariant

The current conceptual model states that one Challenge assesses exactly one Knowledge Atom, but this invariant should be made explicit in the canonical Challenge structure and schema.

Need to specify:

- a Challenge has exactly one `target_atom_id`;
- `target_atom_id` is not a list;
- a Challenge cannot silently target several independent Atoms;
- when the assessed knowledge is a relationship between independent Atoms, that relationship must first be represented as a `relation` Knowledge Atom and the Challenge targets that relation Atom;
- structural relationships among grammar components remain part of the relevant grammar Atom/rule rather than becoming relation targets.

## 8. Standardize the target Atom field name — Resolved

The canonical field name is `target_atom_id`.

A Challenge assesses exactly one Knowledge Atom, and `target_atom_id` stores the ID of that Atom.

The canonical name and semantics are now defined consistently across the Challenge model:

- `target_atom_id` is a required scalar Atom ID;
- it is not a list and there is no plural `target_atom_ids` field;
- it identifies the single Knowledge Atom assessed by the Challenge;
- a Challenge testing a relationship between independent Atoms targets the corresponding `relation` Atom through `target_atom_id`;
- Candidate and Official Challenge representations use the same field name.

Therefore no separate `atom_id` field should be introduced for the Challenge target.

## 9. Define Candidate and Official physical representation

Knowledge Atom documentation specifies that Candidate and Official stores contain Markdown collections of fenced YAML blocks, with each block independently validating against its corresponding schema.

Challenge storage currently specifies:

```text
data/
└── challenges/
    └── <source-id>/
        └── <segment-id>/
            ├── challenges.md
            └── challenge_candidates.md
```

Need to explicitly define:

- `challenges.md` as the Official Challenge collection;
- `challenge_candidates.md` as the Candidate Challenge collection;
- one fenced YAML block per Challenge;
- Candidate `review_status`;
- Candidate/Official shared semantic ID;
- schema validation of individual blocks;
- absence of an additional `official/` or `candidates/` directory layer.

## 10. Define Challenge Candidate and Official schemas

After the canonical structure is settled, define corresponding schemas, analogous to:

```text
schemas/
├── candidate-atom.schema.json
└── official-atom.schema.json
```

The likely Challenge equivalents are:

```text
schemas/
├── candidate-challenge.schema.json
└── official-challenge.schema.json
```

The exact names remain open until the schema design is finalized.

## 11. Strengthen fail-closed and source-preservation rules

Knowledge Atom pipeline documentation explicitly defines fail-closed behavior, immutable source evidence, and reproducibility requirements. Challenge extraction currently expresses the same principles more informally.

Need to formalize that extraction must not silently repair or invent:

- task wording;
- missing options;
- missing response elements;
- exercise/item boundaries;
- target Atom;
- expected answer;
- other essential assessment content.

If the task, boundary, target Atom, or expected answer cannot be established sufficiently from source evidence, the occurrence should become an explicit incomplete/unresolved/skip result rather than a normal valid Challenge Candidate.

Challenge extraction should also adopt explicit reproducibility and source-preservation rules comparable to the Knowledge Atom pipeline.

## 12. Resolve source-independent Challenge storage

The Challenge model permits Challenges that are generated by the system or otherwise have no source provenance.

However, the current physical storage layout is source/segment-oriented:

```text
data/challenges/<source-id>/<segment-id>/
```

Need to define where a source-independent Challenge is stored and how its absence of source provenance is represented.

Do not assume a `generated/` directory until this is explicitly decided.

## 13. Clarify intrinsic difficulty versus operational estimates

The Challenge model currently excludes `difficulty` as an intrinsic Challenge property.

Need to document the distinction between:

- intrinsic Challenge content;
- a difficulty estimate derived from learner/system evidence;
- adaptive selection priority.

Only the first belongs to the canonical Challenge model. Difficulty estimates and selection priorities, if introduced, belong to operational/adaptive data.

## 14. Clarify source answer key versus learner-facing task

A source exercise may contain both the learner-facing task and an answer key.

Need to explicitly define that:

- task content contains what the learner is presented with or needs to perform the task;
- answer contains the specific expected outcome;
- answer-key material is not automatically learner-facing task content;
- answer remains intrinsic Challenge data because it is required to define the supported Challenge;
- source provenance remains separate from both task and answer.

This distinction will be important for rendering Challenges and evaluating learner responses later.

## 15. Define source occurrence versus Challenge reuse/deduplication

Extraction currently preserves every source occurrence as a separate Candidate, while later reuse/deduplication is a separate process.

Need to document the relationship between:

- source occurrence;
- extracted Challenge Candidate;
- semantic Challenge identity;
- later deduplication/reuse.

In particular, multiple source occurrences may provide provenance for one reusable semantic Challenge without making source location part of its identity.

## 16. Update Knowledge Atom documentation to use Challenge terminology

The Knowledge Atom documentation still contains an outdated assessment model describing Questions as assessment entities and showing a Question as potentially related to multiple Atoms.

The current Challenge model has replaced that design.

The outdated section should be updated so that it reflects:

```text
Knowledge Atom
      │
      │ assessed by
      ▼
Challenge
```

and:

```text
One Challenge → exactly one Knowledge Atom
One Knowledge Atom → zero or many Challenges
```

This update should also preserve the relation-Atom rule: a Challenge testing a relationship between independent Atoms targets the corresponding relation Atom rather than directly targeting multiple Atoms.

## 17. Keep Challenge and Knowledge Atom boundaries aligned

The Challenge model should remain consistent with the established Knowledge Atom model.

In particular:

- Challenge is an assessment entity, not a Knowledge Atom;
- Challenge form must not become part of Atom taxonomy;
- learner state must not become Challenge content;
- source structure must not become Challenge identity;
- raw Atom-to-Atom graph relationships must not be introduced merely to support Challenges;
- a relationship becomes a relation Atom only when the relationship itself is independently learnable or testable.

These cross-model invariants should be explicitly documented so future Challenge schema/design changes cannot accidentally reintroduce the earlier Question-based or many-to-many target model.
