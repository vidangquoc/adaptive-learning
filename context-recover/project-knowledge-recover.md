# Adaptive Learning — Project Knowledge Recovery

## Purpose

This file is part of the context-recovery system.

It does **not** contain project knowledge. It defines the navigation and recovery procedure an AI should use to reconstruct knowledge about:

1. the Adaptive Learning project;
2. learning-material / knowledge data;
3. learner / user learning data.

The repository's authoritative documentation, data, source material, implementation, and Git history remain the sources of truth.

## 1. Project Knowledge Recovery

To understand the project:

1. Read `docs/foundation/methodology.md` for project purpose, methodology, and governing rules.
2. Read the relevant documents under `docs/` for the subsystem involved in the current task.
3. When the task involves Knowledge Atoms, read:
   - `docs/knowledge/overall.md`
   - `docs/knowledge/atom-types.md`
   - `docs/knowledge/atom-structure.md`
   - `docs/knowledge/atom-pipeline.md`
4. When the task involves Assessment or Challenge, read:
   - `docs/assessment/assessment.md`
   - `docs/assessment/challenge.md`
   - `docs/assessment/challenge-extraction/challenge-structure.md`
5. When the task involves learner state, read `docs/learner/learning-state.md`.
6. Read relevant learning-material principles, procedures, rules, and source documentation under `docs/learning-material/` as needed.
7. Read relevant implementation files for behavior currently implemented.
8. Inspect Git history when the task depends on why a design or rule exists.
9. Use current repository state rather than remembered project knowledge.

Do not reconstruct detailed project knowledge from this file. Use it only to locate and prioritize authoritative sources.

## 2. Learning-Material / Knowledge-Data Recovery

To understand what learning materials and knowledge data currently exist:

1. Inspect the current `data/` and `sources/` locations relevant to the task.
2. For source identity and catalog information, read:
   - `docs/learning-material/sources/source-registry.md`
   - `docs/learning-material/sources/books.md`
3. Read `docs/learning-material/principles/overall.md` for the overall learning-material rulebook.
4. Read the relevant focused principle under `docs/learning-material/principles/`.
5. Read `docs/learning-material/procedures/source-extraction-sop.md` when the task involves source extraction.
6. Read `docs/learning-material/rules/lexical-definition-rules.md` when the task involves lexical-definition rules.
7. Read the canonical Knowledge Atom documents when interpreting knowledge representation.
8. Read the canonical Challenge documents when interpreting assessment extraction.
9. Use actual repository data for current inventories, counts, structures, and values.

### Knowledge-data locations

Do not assume a generic `data/atoms/` layout.

The current Atom storage model uses:

```text
data/knowledge/
└── <source-id>/
    └── <segment-id>/
        └── <domain>/
            ├── knowledge_atoms.md
            └── knowledge_atom_candidates.md
```

Official and Candidate Atom collections are separated by file name within the source/segment/domain structure.

Challenge storage uses:

```text
data/challenges/
└── <source-id>/
    └── <segment-id>/
        ├── challenges.md
        └── challenge_candidates.md
```

Learner review data uses:

```text
data/learners/
└── <learner-id>/
    └── review-data.yaml
```

These paths describe the current storage model. Verify actual files before making claims about what data exists.

## 3. Learner / User Learning-Data Recovery

To recover learner data currently stored in the repository:

1. Inspect `data/learners/` for current learner review data.
2. Read `docs/learner/learning-state.md` to understand the meaning of learner-state fields.
3. Distinguish current learner review state from historical attempts and sessions.
4. Trace `atom_id` references to the corresponding Official Knowledge Atoms when interpretation requires knowledge context.
5. Use actual learner data for current values; do not infer mastery, progress, history, or review state from conversation memory.

The current review model stores the latest state only. It does not store attempts or review history in `review-data.yaml`.

## 4. Assessment / Challenge Recovery

When the task involves Challenge extraction:

1. Read the canonical Challenge overview and structure first.
2. Determine the relevant source segment and inspect the actual source evidence.
3. Treat the source exercise/item as evidence; do not infer missing instruction, prompt, options, learner response elements, target Atom, or expected answer.
4. Determine the target Atom during contextual analysis rather than in a later guess-based step.
5. Preserve one-to-one Challenge-to-target-Atom linkage.
6. Skip or mark unresolved occurrences when essential information cannot be established.
7. Preserve source traceability and use the canonical source-occurrence ID format.
8. Keep source-derived Challenges distinct from generated Challenges when provenance requires it.

Current extraction boundaries include:

- long integrated/composite exercises and long Cloze passages are outside current atom-level extraction;
- shared-context exercises are currently skipped rather than artificially decomposed;
- a Challenge cannot cross Source Segment boundaries;
- a source exercise item normally defines the Challenge boundary when it is an independent evaluable learner task;
- multiple blanks/actions may still form one Challenge;
- every supported extracted Challenge needs a specific expected answer supported by evidence.

Do not treat these bullets as a substitute for the canonical Challenge docs; they are recovery navigation cues.

## 5. Domain Separation

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
      └── assessments / Challenges

Learner / user learning data
      │
      └── review state

Current conversation context
      │
      └── context-recover.md
```

Do not use one domain as a substitute for another.

## 6. Recovery Procedure

For a task requiring project or learning-state understanding:

1. Read `context-recover/context-recover.md`.
2. Read this file to determine which authoritative project/data sources must be inspected.
3. Read the relevant authoritative documentation.
4. Inspect the relevant current repository data, source material, and implementation.
5. Verify important facts against authoritative sources before relying on them.
6. Expand recovery only when the current task, missing information, or uncertainty requires it.
7. Only then continue the task.

Do not read `context-recover/context-recovery-authoring-principles.md` as part of normal recovery.

Do not treat user-facing verification prompts as an automatic recovery procedure. They are maintained in `context-recover/context-recovery-prompt.md`.

## 7. Verification Rules

- Repository evidence takes precedence over remembered context.
- Current data must be read from authoritative repository locations.
- Do not invent missing data.
- Do not estimate exact counts when authoritative data can be inspected.
- Preserve provenance when interpreting knowledge or assessment data.
- Preserve the distinction between historical learner evidence and current learner-state interpretation.
- If sources conflict or information is ambiguous, inspect the relevant authoritative source before inferring.
- Treat working discussion/review files as context, not as canonical project rules, unless the canonical documentation has been updated accordingly.

## 8. Recovery Boundary

This file describes **how an AI recovers project knowledge and learning data**.

It is not itself an authoritative source of project knowledge, learning-material data, learner data, or current conversation context.
