# Adaptive Learning — Context Recovery

> Canonical recovery guide for `vidangquoc/adaptive-learning`.

## Project identity

The current project is **Adaptive Learning**.

**PTNK is the predecessor project from which Adaptive Learning was split.** PTNK remains an important domain-specific evidence source and validation target. It is not the identity of this repository.

## Master recovery prompt

```text
Continue work on GitHub project `vidangquoc/adaptive-learning`.

This project is Adaptive Learning, split from the predecessor project PTNK.

Read first:
1. `PROJECT-CONTEXT.md`
2. `PROJECT-STATUS.md`
3. `docs/methodology.md`
4. `docs/learning-state-specification.md`
5. `docs/knowledge-atom-pipeline.md`
6. relevant `docs/learning-material-principles/`
7. relevant schemas, data, sources, and scripts.

Core model:
Goal → competency model → knowledge base → diagnostic/challenge → learner state → learning frontier → next-best activity → assessment → updated learner state.

Core rules:
- challenge-first when prior knowledge is plausible;
- instruction is evidence-driven, not page-driven;
- static knowledge and learner state are separate;
- knowledge atoms are flat and independently diagnosable;
- one lexical sense is one atom by default;
- preserve provenance and uncertainty;
- never fabricate evidence, definitions, pronunciation, examples, patterns, CEFR, or relationships;
- Destination C1 & C2 is the initial curriculum/knowledge backbone;
- PTNK papers are calibration/validation evidence, not the whole curriculum;
- PTNK-specific files may retain `ptnk-*` naming because they represent PTNK provenance/domain;
- 700h is a ceiling/learning budget, not a quota.

Inspect the current repository state before changing anything. If old conversation context conflicts with the repository, trust the repository and report the difference.
```

## Recovery checklist

1. Confirm repository: `vidangquoc/adaptive-learning`.
2. Read `PROJECT-CONTEXT.md` and `PROJECT-STATUS.md`.
3. Inspect relevant schemas and current data.
4. Inspect Git state/history when necessary.
5. Preserve flat-atom and candidate/official separation.
6. Preserve source boundaries and provenance.
7. Make incremental changes and verify consequential writes.

## PTNK boundary

Do not rename or delete PTNK-specific historical artifacts merely to make names uniform. PTNK is a valid predecessor/domain layer inside Adaptive Learning.

Do not, however, introduce new project-level documents as if the repository were still named PTNK.

## Maintenance rule

When a major architectural, ontology, data-layer, or governance decision becomes stable, update this recovery guide and the canonical project context. Remove obsolete instructions when decisions are superseded.
