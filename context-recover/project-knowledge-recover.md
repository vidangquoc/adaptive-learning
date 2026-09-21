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

1. Read `docs/foundation/methodology.md` for project purpose, methodology, and governing rules.
2. Read `docs/data/architecture.md` for the authoritative data architecture and domain boundaries.
3. Read the relevant documents under `docs/` for the specific subsystem involved in the current task.
4. Read `docs/knowledge/overall.md` for the conceptual knowledge model when the task involves knowledge representation.
5. Read `docs/knowledge/atom-types.md` and `docs/knowledge/atom-structure.md` when the task involves Knowledge Atom taxonomy or structure.
6. Read `docs/knowledge/step-3-review.md` when the task involves the current Step 3 review; this is the working discussion and decision log, not the canonical model.
7. Read `docs/learner/learning-state.md` for learner-state concepts when the task involves adaptive learner behavior.
8. Read relevant implementation files for the behavior currently implemented.
9. Inspect Git history when the task depends on why a design or rule exists.
10. Use the current repository state rather than relying on remembered project knowledge.

Do not reconstruct project knowledge from this file. Use it only to locate and prioritize authoritative sources.

## Learning-Material / Knowledge-Data Recovery

To understand what learning materials and knowledge data currently exist:

1. Inspect `data/knowledge/` for current structured learning data when present.
2. Inspect `sources/` for source and evidence material when present and when provenance or source content is required.
3. Read `docs/learning-material/principles/overall.md` for the overall learning-material rulebook.
4. Read the relevant focused principle under `docs/learning-material/principles/` for the specific rule involved.
5. Read `docs/learning-material/sources/source-registry.md` and `docs/learning-material/sources/books.md` when source identity, scope, or catalog information is required.
6. Read `docs/learning-material/procedures/source-extraction-sop.md` when the task involves source extraction procedure.
7. Read `docs/learning-material/rules/lexical-definition-rules.md` when the task involves lexical-definition rules.
8. Read `docs/knowledge/overall.md` for the conceptual knowledge model.
9. Read `docs/knowledge/atom-types.md` for atom taxonomy.
10. Read `docs/knowledge/atom-structure.md` for the formal/common atom structure.
11. Read `docs/knowledge/atom-pipeline.md` for knowledge-atom discovery, validation, and promotion workflow.
12. Read `docs/data/architecture.md` when interpreting the relationship between source, knowledge, assessment, and learner data.
13. Use the actual repository data for current inventories, counts, structures, and values.

### Current Step 3 recovery note

When recovering the current Step 3 discussion:

- Treat docs/knowledge/overall.md, docs/knowledge/atom-types.md, and docs/knowledge/atom-structure.md as canonical knowledge-model sources.
- Treat docs/knowledge/step-3-review.md as the working review/discussion source.
- Do not treat review proposals as canonical unless explicitly adopted and reflected in the canonical docs.
- multiword_expression is currently being treated as a fallback for multi-word lexical units that are not phrasal_verb, idiom, or collocation.
- word_formation and morphological_form have been moved to the Grammar domain; their detailed boundary with other Grammar subtypes remains open.
- A grammar rule may itself be an Atom when it is a learning target; this does not imply a dedicated rule field in the common Atom structure.
- Step 3 remains open.

Do not infer current knowledge inventories, atom counts, source contents, or other data from conversation memory or from this recovery file.

## Learner / User Learning-Data Recovery

To recover the learner data currently stored in the repository:

1. Inspect `data/learner/` for the current learner data when present.
2. Read `docs/learner/learning-state.md` to understand the meaning of learner-state concepts and fields.
3. Read `docs/data/architecture.md` to understand the boundary between static knowledge and learner data.
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

Do **not** treat a separate verification file as an automatic recovery procedure. User-facing verification questions are maintained in `context-recover/context-recovery-prompt.md`.

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
