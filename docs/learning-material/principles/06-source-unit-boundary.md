# Source Unit Boundary

## Canonical Rule

For Destination C1 & C2, **Unit is the canonical source boundary**.

The authoritative learning-material inputs are:

```text
sources/destination-c1-c2/units/
├── unit-01.txt
├── unit-02.txt
├── unit-03.txt
└── ...
```

Each `unit-XX.txt` must contain the complete source content belonging to that Unit and must not contain content from another Unit.

## No `sections/` Layer

The project does **not** use an extracted `sections/` directory or `MANIFEST.tsv` as a source-of-truth layer.

Do not:

- derive Unit boundaries from section files;
- use section files as required inputs to discovery;
- use section filenames as canonical provenance;
- require a section manifest for validation;
- recreate the old section-based extraction pipeline.

A textbook may contain internal headings, topic labels, grammar labels, exercise labels, or other divisions. Those are **content inside the Unit**, not mandatory structural files in the repository.

## Unit Validation Gate

Before evidence discovery begins, validate every Unit boundary.

At minimum verify:

1. Unit start is correct.
2. Unit end is correct.
3. No content is missing.
4. No content from the next/previous Unit is included.
5. Unit order is preserved.
6. The Unit can be read as the complete source context for downstream analysis.

If any condition fails:

```text
FAIL → stop extraction → repair Unit boundary → revalidate
```

Do not continue into candidate generation with a known-invalid Unit.

## Provenance

Every source-derived candidate and official atom must be traceable to:

```text
source
  ↓
Unit
  ↓
precise location/span within Unit
  ↓
source evidence
```

A textbook heading may be recorded as descriptive metadata when useful, but it does not replace Unit provenance.

## Discovery

Evidence discovery operates directly on Unit content.

The discovery layer may identify:

- vocabulary entries;
- topic vocabulary;
- phrases, patterns, and collocations;
- idioms;
- phrasal verbs;
- word formation;
- grammar rules and constructions;
- lexical/grammatical contrasts;
- examples and explanations;
- exercises and assessment evidence.

Discovery output is evidence location, not canonical knowledge.

One Unit may contain many knowledge domains and evidence types. Do not split the Unit into artificial repository sections merely to make extraction easier.

## Knowledge Atom Implication

Unit boundaries and knowledge-atom boundaries are different concepts.

A single Unit may produce many independent atoms, and one atom may be supported by multiple evidence spans within the same Unit or, where explicitly allowed, across source records.

The flat-atom rule remains:

> **Each independently useful knowledge unit is represented as its own atom.**

This applies equally to lexical and grammatical knowledge.

## Assessment Evidence

Exercises and questions inside a Unit are primarily assessment evidence. They may be linked to knowledge atoms, but answer choices, fill-in rows, and generic exercise markers must not automatically become knowledge atoms.

## Migration Rule

The former section-based extraction artifacts are historical and superseded. New pipeline code, schemas, provenance rules, validation, and recovery instructions must not depend on them.

If an old script still expects `sections/`, update or retire the script before using it in the new pipeline.
