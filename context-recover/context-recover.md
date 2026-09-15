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

Establish a clean, reproducible context-recovery system for the repository.

### Current objective

Separate:

1. **Project knowledge** — stable knowledge required to understand the project and its data.
2. **Conversation context** — temporary context required to continue the current line of work.
3. **Recovery instructions** — procedures telling the AI how to recover the required context.
4. **User prompts** — prompts used to start recovery and to test whether recovery succeeded.

### Current decisions

- `context-recover/context-recover.md` contains instructions for recovering current conversation context.
- `context-recover/project-knowledge-recover.md` contains instructions for recovering project knowledge, learning-material / knowledge data, and learner / user learning data.
- `context-recover/context-recovery-prompt.md` contains two groups of user-facing prompts: prompts for recovery and prompts for verification after recovery.
- `context-recover/context-recovery-authoring-principles.md` defines how the recovery files themselves should be created, updated, and maintained. It is not a normal recovery step.
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
├── context-recovery-prompt.md
├── context-recover.md
├── project-knowledge-recover.md
└── context-recovery-authoring-principles.md
```

### Immediate next step

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
