# Adaptive Learning — Project Knowledge Recovery

## Purpose

This file is part of the context-recovery system.

It does **not** contain project knowledge. It defines the instructions, navigation points, and recovery procedure an AI should use to reconstruct knowledge about:

1. the Adaptive Learning project;
2. learning-material / knowledge data;
3. learner / user learning data.

The repository's authoritative documentation, data, source material, implementation, and Git history remain the sources of truth.

## Project Knowledge Recovery

To understand the project:

1. Read `docs/methodology.md` for project purpose, methodology, and governing rules.
2. Read `docs/data-architecture.md` for the authoritative data architecture and domain boundaries.
3. Read relevant implementation files for the behavior currently implemented.
4. Inspect Git history when the task depends on why a design or rule exists.
5. Use the current repository state rather than relying on remembered project knowledge.

Do not reconstruct project knowledge from this file. Use it only to locate and prioritize authoritative sources.

## Learning-Material / Knowledge-Data Recovery

To understand what learning materials and knowledge data currently exist:

1. Inspect `data/knowledge/` for current structured learning data.
2. Inspect `sources/` for source and evidence material when provenance or source content is required.
3. Read `docs/knowledge-atom-pipeline.md` for the knowledge-atom extraction and promotion process.
4. Read relevant files under `docs/learning-material-principles/` for learning-material rules.
5. Read `docs/data-architecture.md` when interpreting the relationship between source, knowledge, assessment, and learner data.
6. Use the actual repository data for current inventories, counts, structures, and values.

Do not infer current knowledge inventories, atom counts, source contents, or other data from conversation memory or from this recovery file.

## Learner / User Learning-Data Recovery

To recover the learner data currently stored in the repository:

1. Inspect `data/learner/` for the current learner data.
2. Read `docs/learning-state-specification.md` to understand the meaning of learner-state fields.
3. Read `docs/data-architecture.md` to understand the boundary between static knowledge and learner data.
4. Distinguish current learner state from historical attempts and sessions.
5. Treat review queues as derived learner-facing recommendations unless authoritative documentation states otherwise.
6. Trace learner-state references back to the corresponding knowledge-atom IDs when interpretation requires knowledge context.

Do not infer learner mastery, progress, history, or current state from conversation memory when repository data is available.

## Domain-Separation Rules

During recovery, keep these domains distinct:

```text
Project knowledge
      │
      ├── project documentation
      ├── implementation
      └── historical decisions

Learning-material / knowledge data
      │
      ├── sources / evidence
      ├── knowledge atoms
      ├── relations
      └── assessments

Learner / user learning data
      │
      ├── profile
      ├── attempts
      ├── sessions
      ├── learner state
      └── review queue

Current conversation context
      │
      └── context-recover.md
```

Do not use one domain as a substitute for another.

## Recovery Procedure

For a task requiring project or learning-state understanding:

1. Read `context-recover/context-recover.md` to recover the current conversation context.
2. Read this file to determine which authoritative project/data sources must be inspected.
3. Read the relevant authoritative documentation.
4. Inspect the relevant current repository data, source material, and implementation.
5. Verify important facts against authoritative sources before relying on them.
6. Expand recovery only when the current task, missing information, or uncertainty requires it.
7. Only then continue the task.

Do **not** read `context-recover/context-recovery-authoring-principles.md` as part of normal recovery. That file governs the creation and maintenance of the recovery system itself.

Do **not** treat `context-recover/context-recover-verification.md` as an automatic recovery procedure. It contains questions for the user to ask the AI after recovery when verification is desired.

## Verification Rules

- Repository evidence takes precedence over remembered context.
- Current data must be read from authoritative repository locations.
- Do not invent missing data.
- Do not estimate exact counts when authoritative data can be inspected.
- Preserve provenance when interpreting knowledge data.
- Preserve the distinction between historical learner evidence and current learner-state interpretation.
- If sources conflict or information is ambiguous, inspect the relevant authoritative source before inferring.

## Recovery Boundary

This file describes **how an AI recovers project knowledge and learning data**.

It is not itself an authoritative source of project knowledge, learning-material data, learner data, or current conversation context.
