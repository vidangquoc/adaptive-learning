# Context Recovery

## 1. Purpose

This file is the entry point for recovering the **current conversation context** of `vidangquoc/adaptive-learning`.

It does not contain the project's full knowledge. To recover the project, learning-material / knowledge, and learner-data understanding required for the current task, follow:

- `context-recover/project-knowledge-recover.md`

The context-recovery authoring principles are defined in:

- `context-recover/context-recovery-authoring-principles.md`

That file governs the creation and maintenance of recovery files. It is **not** part of the normal recovery procedure.

User-facing recovery and verification prompts are provided in:

- `context-recover/context-recovery-prompt.md`

That file contains prompts for the user to start recovery and prompts for the user to verify the result. It is not an automatic recovery step.

## 2. Current Conversation Context

### Current task

Recover enough current conversation context and repository understanding to continue the user's present task accurately.

The current work is a review of Step 3 — Knowledge Atom Taxonomy + Structure. The review is still open and must not be marked complete unless the user explicitly decides to do so.

The working discussion is in docs/knowledge/step-3-review.md. It is a review/discussion document, not the canonical source of truth.

### Current objective

Keep four distinct layers separate:

1. **Project knowledge** — stable knowledge required to understand the project and its data.
2. **Conversation context** — temporary context required to continue the current line of work.
3. **Recovery instructions** — procedures telling the AI how to recover the required context.
4. **User prompts** — prompts used to start recovery and to test whether recovery succeeded.

### Current decisions

For the current Step 3 review, the following points have been agreed in the conversation so far:

- Knowledge atoms are flat; there is no parent/child hierarchy between atoms.
- A knowledge unit may still be its own atom even when it relates to, depends on, or overlaps with another atom, when it is a distinct learning target.
- multiword_expression is the fallback for a multi-word lexical unit that is not a phrasal_verb, idiom, or collocation.
- word_formation and morphological_form belong to the Grammar domain, not Vocabulary. Their detailed boundary with other Grammar subtypes remains open.
- A grammar rule can itself be a Knowledge Atom when it is a learning target. The common Atom structure does not therefore need a dedicated rule property.
- The current Atom structure has no rule field; existing fields such as structure, usage, and constraints can describe aspects of an atom when appropriate.
- Step 3 remains open.

These are current conversation/review decisions. Do not silently promote them to canonical project rules; check the authoritative docs and the review file.

- `context-recover/context-recover.md` contains instructions for recovering current conversation context.
- `context-recover/project-knowledge-recover.md` contains instructions for recovering project knowledge, learning-material / knowledge data, and learner / user learning data.
- `context-recover/context-recovery-prompt.md` contains two groups of user-facing prompts: prompts for recovery and prompts for verification after recovery.
- `context-recover/context-recovery-authoring-principles.md` defines how the recovery files themselves should be created, updated, and maintained. It is not a normal recovery step.
- Detailed project knowledge remains authoritative in `docs/` and the repository's actual data, source material, implementation, and history.
- Do not recreate `PROJECT-CONTEXT.md` or `PROJECT-STATUS.md` as parallel recovery files.

### Current documentation structure

The main authoritative documentation domains are:

```text
docs/
├── foundation/
│   └── methodology.md
├── learning-material/
│   ├── principles/
│   │   ├── overall.md
│   │   ├── 01-purpose-and-learning-strategy.md
│   │   ├── 02-knowledge-model-and-interpretation.md
│   │   ├── 03-evidence-provenance-and-governance.md
│   │   ├── 04-assessment-and-learning-material.md
│   │   ├── 05-source-scope-and-metadata.md
│   │   └── 06-source-unit-boundary.md
│   ├── sources/
│   ├── procedures/
│   └── rules/
├── knowledge/
│   ├── overall.md
│   ├── atom-types.md
│   ├── atom-structure.md
│   └── atom-pipeline.md
├── data/
│   └── architecture.md
└── learner/
    └── learning-state.md
```

Recovery instructions must use these current paths rather than obsolete pre-reorganization paths.

### Current constraints

- Do not duplicate detailed project documentation into recovery files.
- Do not turn conversation recovery into a complete project history.
- Do not treat old conversation memory as authoritative when repository evidence is available.
- Keep project knowledge, learning-material knowledge, learner data, and current conversation context distinct.
- When information is missing or contradictory, verify it from authoritative repository sources rather than guessing.
- Treat the repository's current structure and file contents as authoritative; do not preserve obsolete paths merely because they appeared in earlier recovery instructions.

### Relevant files

```text
context-recover/
├── context-recovery-prompt.md
├── context-recover.md
├── project-knowledge-recover.md
└── context-recovery-authoring-principles.md
```

### Immediate next step

For the current task, continue the Step 3 review from docs/knowledge/step-3-review.md after reading the canonical knowledge-model files. Do not restart the discussion from scratch and do not mark Step 3 complete.

After context has been recovered, the user may use the **Prompt kiểm tra** section in `context-recover/context-recovery-prompt.md` to test whether the recovery is sufficient and correct. If a question exposes a gap, inspect the relevant authoritative documentation/data and recover the missing context before continuing.

## 3. Recovery Procedure

For a new conversation or lost context:

1. Read this file to recover the current conversation context.
2. Read `context-recover/project-knowledge-recover.md` to determine which authoritative project, learning-material, and learner-data sources are relevant.
3. Read only the authoritative `docs/`, data, sources, and implementation files relevant to the current task.
4. Recover the required project/knowledge/learner context progressively rather than reading the entire repository indiscriminately.
5. Continue the task once sufficient context has been recovered.

After recovery, the user may use the **Prompt kiểm tra** section in `context-recover/context-recovery-prompt.md` to test whether the recovered context is correct.

Do **not** read `context-recover/context-recovery-authoring-principles.md` as a normal recovery step. Consult it when creating, updating, reviewing, or redesigning the recovery system itself.

## 4. Boundary

> **`context-recover.md` describes how to recover the current conversation context. `project-knowledge-recover.md` describes how to recover the project, learning-material / knowledge, and learner-data understanding required for the task. `context-recovery-prompt.md` provides user-facing prompts for starting recovery and testing the result. `context-recovery-authoring-principles.md` governs how these recovery files are authored and maintained.**

This file should remain focused on the current conversation. Stable project knowledge belongs in authoritative documentation and data; recovery instructions belong in the appropriate recovery file; user-facing prompts belong in `context-recovery-prompt.md`.
