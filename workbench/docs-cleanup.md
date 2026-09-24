# Docs Cleanup Workbench

## Goal

Reorganize the documentation structure so that each directory represents a clear system domain and each document has a clear responsibility, without creating unnecessary new files.

## Steps

### 1. Clean up Assessment structure

- Rename `docs/assessment/assessment.md` → `docs/assessment/overall.md`.
- Rename `docs/assessment/challenge-extraction/challenge-structure.md` → `docs/assessment/challenge-extraction/structure.md`.
- Review `docs/assessment/challenge-extraction/challenge-form-examples.md`.
  - The current Challenge model deliberately has no persisted Challenge Form taxonomy.
  - Remove this file if its useful content is already covered by `structure.md` / `principles.md`.
  - Preserve only examples that are still needed by the canonical model.

### 2. Create a dedicated Source documentation domain

Move source-related documentation out of `docs/learning-material/` into:

```text
docs/source/
├── overall.md
├── source-registry.md
├── source-structure.md
└── extraction.md
```

Use these responsibilities:

- `overall.md`: conceptual role of sources in the system.
- `source-registry.md`: Source Registry and its relationship to `sources/source-registry.yaml`.
- `source-structure.md`: Source, Source Segment, IDs, and segment boundaries.
- `extraction.md`: source-to-segment/evidence extraction model.

If the extraction procedure becomes substantial, a separate `docs/source/procedures/extraction-sop.md` may be introduced later. Do not create it merely for symmetry.

### 3. Clean up Learning Material documentation

After source documentation has been separated, keep `docs/learning-material/` focused on learning-material-specific concepts.

Review:

- `principles/`
- `rules/`
- `overall.md`

Do not use `learning-material/` as a general container for source management, assessment, or knowledge documentation.

### 4. Review Learner documentation

Current structure:

```text
docs/learner/
└── learning-state.md
```

Keep it for now.

Later, if the learner model grows, consider:

```text
docs/learner/
├── overall.md
├── learning-state.md
└── review-data.md
```

Do not create these files until there is sufficient canonical content.

### 5. Preserve the Knowledge documentation structure

Keep the current structure unless review reveals a concrete problem:

```text
docs/knowledge/
├── overall.md
├── atom-types.md
├── atom-structure.md
├── atom-pipeline.md
└── relation-examples.md
```

Do not restructure merely for consistency with other domains.

### 6. Keep schemas flat for now

Keep `schemas/` flat:

```text
schemas/
├── candidate-atom.schema.json
├── official-atom.schema.json
├── candidate-challenge.schema.json
├── official-challenge.schema.json
└── review-data.schema.json
```

Do not introduce `knowledge/`, `assessment/`, or `learner/` schema subdirectories unless the number of schemas later makes the flat structure impractical.

### 7. Separate documentation from source data

Keep actual source artifacts and source registry data under `sources/`.

Documentation about the source model belongs under `docs/source/`.

Do not mix source artifacts into `docs/`.

### 8. Reassess books.md

Review `docs/learning-material/sources/books.md`.

The current understanding is that it only stores book names and has no special semantic role.

If it is merely a catalog/data list, remove it from `docs/` and decide whether it belongs under source data instead. Do not preserve it as documentation without a clear documentation responsibility.

### 9. Keep process/recovery artifacts outside canonical docs

Do not move `context-recover/` into `docs/`.

Context-recovery files describe AI/recovery workflow rather than the Adaptive Learning system's canonical model.

Likewise, `analysis/` and other temporary/process artifacts should not be treated as canonical documentation.

### 10. Remove obsolete artifacts

Review the repository for obsolete testing/review/WIP artifacts.

Known candidate for removal:

```text
unit-1-sources/test-atoms.md
```

It is obsolete and must not be treated as a source of truth.

Also verify that old review/WIP files are not being used to store canonical decisions. Decisions belong in the appropriate permanent documentation.

## Target high-level structure

The intended direction is:

```text
adaptive-learning/
├── README.md
├── docs/
│   ├── foundation/
│   ├── source/
│   ├── knowledge/
│   ├── assessment/
│   ├── learner/
│   └── learning-material/
├── schemas/
├── sources/
├── data/
├── scripts/
├── analysis/
└── context-recover/
```

## Execution rule

Do this incrementally. After each structural move or rename:

1. update internal links/references;
2. verify no canonical content was lost;
3. verify the new location matches the document's responsibility;
4. remove obsolete duplicates only after the new location is confirmed.

This file is a workbench/checklist, not canonical project documentation.
