# Context Recovery

## 1. Purpose

This file is the entry point for recovering the **current conversation context** of `vidangquoc/adaptive-learning`.

It does not contain the project's full knowledge. For the stable knowledge required to understand the project, learning materials, and learner data, read:

- `context-recover/project-knowledge.md`

The governing recovery rules are defined in:

- `context-recover/context-recover-principles.md`

Verification is defined in:

- `context-recover/context-recover-verification.md`

## 2. Current Conversation Context

### Current task

Establish a clean, reproducible context-recovery system for the repository.

### Current objective

Separate:

1. **Project knowledge** — stable knowledge required to understand the project and its data.
2. **Conversation context** — temporary context required to continue the current line of work.
3. **Verification** — questions used to test whether the required context has actually been recovered.

### Current decisions

- `context-recover/project-knowledge.md` is the compact baseline for recovering knowledge about:
  - the Adaptive Learning project;
  - learning-material / knowledge data;
  - learner data.
- `context-recover/context-recover.md` is conversation-specific and should contain only the context needed to continue the current work.
- `context-recover/context-recover-principles.md` defines the governing principles and boundaries.
- `context-recover/context-recover-verification.md` defines the recovery verification questions.
- Detailed project knowledge remains authoritative in `docs/` and the repository's actual data/source/code.
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
├── context-recover-principles.md
├── context-recover-verification.md
└── project-knowledge.md
```

### Immediate next step

Use `context-recover/context-recover-verification.md` to verify that the recovered context is sufficient and correct. If verification exposes a gap, inspect the relevant authoritative documentation/data and update `project-knowledge.md` or the current conversation context as appropriate.

## 3. Recovery Procedure

For a new conversation or lost context:

1. Read this file to recover the current conversation context.
2. Read `context-recover/context-recover-principles.md` to apply the recovery rules.
3. Read `context-recover/project-knowledge.md` to recover the stable project/knowledge/learner baseline.
4. Read only the authoritative `docs/`, data, sources, and implementation files relevant to the current task.
5. Run the verification questions when context correctness needs to be established.
6. Only then continue the task.

## 4. Boundary

> **`project-knowledge.md` describes what must be understood. `context-recover.md` describes what must be remembered to continue the current conversation.**

This file should remain short. When stable project knowledge changes, update the authoritative documentation and the relevant summary in `project-knowledge.md`; do not copy that knowledge into this file.
