# Context Recovery

## 1. Purpose

This file is the entry point for recovering the **current conversation context** of `vidangquoc/adaptive-learning`.

It does not contain the project's full knowledge. To recover the project, learning-material / knowledge, and learner-data understanding required for the current task, follow:

- `context-recover/project-knowledge-recover.md`

The context-recovery authoring principles are defined in:

- `context-recover/context-recovery-authoring-principles.md`

That file governs the creation and maintenance of recovery files. It is **not** part of the normal recovery procedure.

Verification questions are provided in:

- `context-recover/context-recover-verification.md`

These questions are intended for the user to ask the AI after recovery; they are not an automatic recovery step.

## 2. Current Conversation Context

### Current task

Establish a clean, reproducible context-recovery system for the repository.

### Current objective

Separate:

1. **Project knowledge** — stable knowledge required to understand the project and its data.
2. **Conversation context** — temporary context required to continue the current line of work.
3. **Recovery instructions** — procedures telling the AI how to recover the required context.
4. **Verification** — questions used by the user to test whether the required context has actually been recovered.

### Current decisions

- `context-recover/context-recover.md` contains instructions for recovering current conversation context.
- `context-recover/project-knowledge-recover.md` contains instructions for recovering project knowledge, learning-material / knowledge data, and learner / user learning data.
- `context-recover/context-recovery-authoring-principles.md` defines how the recovery files themselves should be created, updated, and maintained. It is not a normal recovery step.
- `context-recover/context-recover-verification.md` contains questions for the user to ask the AI to verify recovery quality. It is not a recovery procedure.
- Detailed project knowledge remains authoritative in `docs/` and the repository's actual data, source material, implementation, and history.
- Do not recreate `PROJECT-CONTEXT.md` or `PROJECT-STATUS.md` as parallel recovery files.

### Current constraints

- Do not duplicate detailed project documentation into recovery files.
- Do not turn conversation recovery into a complete project history.
- Do not treat old conversation memory as authoritative when repository evidence is available.
- Keep project knowledge, learning-material knowledge, learner data, and current conversation context distinct.
- When information is missing or contradictory, verify it from authoritative repository sources rather than guessing.

### Relevant files

```text
context-recover/
├── context-recover.md
├── project-knowledge-recover.md
├── context-recovery-authoring-principles.md
└── context-recover-verification.md
```

### Immediate next step

When context has been recovered, use `context-recover/context-recover-verification.md` as a set of questions to test whether the recovery is sufficient and correct. If a question exposes a gap, inspect the relevant authoritative documentation/data and recover the missing context before continuing.

## 3. Recovery Procedure

For a new conversation or lost context:

1. Read this file to recover the current conversation context.
2. Read `context-recover/project-knowledge-recover.md` to determine which authoritative project, learning-material, and learner-data sources are relevant.
3. Read only the authoritative `docs/`, data, sources, and implementation files relevant to the current task.
4. Recover the required project/knowledge/learner context progressively rather than reading the entire repository indiscriminately.
5. Continue the task once sufficient context has been recovered.

After recovery, the user may use `context-recover/context-recover-verification.md` to test whether the recovered context is correct.

Do **not** read `context-recover/context-recovery-authoring-principles.md` as a normal recovery step. Consult it when creating, updating, reviewing, or redesigning the recovery system itself.

## 4. Boundary

> **`context-recover.md` describes how to recover the current conversation context. `project-knowledge-recover.md` describes how to recover the project, learning-material / knowledge, and learner-data understanding required for the task. `context-recover-verification.md` provides questions for the user to test the result. `context-recovery-authoring-principles.md` governs how these recovery files are authored and maintained.**

This file should remain focused on the current conversation. Stable project knowledge belongs in authoritative documentation and data; recovery instructions belong in the appropriate recovery file; verification questions belong in the verification file.
