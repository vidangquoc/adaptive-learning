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

The project does not use an extracted `sections/` directory or `MANIFEST.tsv` as a source-of-truth layer.

Do not:

- derive Unit boundaries from section files;
- use section files as required inputs to discovery;
- use section filenames as canonical provenance;
- require a section manifest for validation;
- recreate the old section-based extraction pipeline.

Textbook headings, topic labels, grammar labels, exercise labels, and similar divisions remain content inside the Unit.

## Unit Validation Gate

Before downstream evidence discovery begins, validate every Unit boundary:

1. Unit start is correct.
2. Unit end is correct.
3. No content is missing.
4. No content from adjacent Units is included.
5. Unit order is preserved.
6. The Unit can be read as complete source context for downstream analysis.

If any condition fails:

```text
FAIL → stop extraction → repair Unit boundary → revalidate
```

Do not continue with known-invalid Unit input.

## Unit-Based Provenance

For Unit-based extraction, source provenance identifies:

```text
source
  ↓
Unit
  ↓
precise location/span within Unit
  ↓
source evidence
```

A textbook heading or exercise label may be recorded as descriptive context, but it does not replace Unit provenance or become a separate source layer.

## Downstream Discovery

Evidence discovery operates directly on Unit content. It may identify vocabulary, phrases, patterns, collocations, idioms, phrasal verbs, word formation, grammar, contrasts, examples, explanations, and assessment evidence.

Discovery output is evidence location, not canonical knowledge. Knowledge interpretation and atomization are defined elsewhere.

One Unit may contain many knowledge domains and evidence types. Do not split the Unit into artificial repository sections merely to simplify extraction.

## Assessment Evidence

Exercises and questions inside a Unit are source evidence for assessment. They may be linked to knowledge atoms, but answer choices, fill-in rows, and generic exercise markers must not automatically become knowledge atoms.

## Migration Rule

The former section-based extraction artifacts are historical and superseded. New pipeline code, schemas, provenance rules, and recovery instructions must not depend on them.

If an old script still expects `sections/`, update or retire it before using it in the current pipeline.
