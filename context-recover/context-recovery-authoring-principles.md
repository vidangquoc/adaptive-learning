# Context Recovery Authoring Principles

## 1. Purpose

This file defines the principles that govern the **creation, modification, and maintenance of the context-recovery instruction system** in this repository.

It is a **meta-level authoring specification**. It is not a recovery instruction and MUST NOT be treated as a required step of normal context recovery.

These principles apply when an AI is asked to create, update, review, redesign, or restructure the files that make up the context-recovery system.

## 2. Context-Recovery Files

The context-recovery system consists of the following files:

### `context-recover/context-recover.md`

The entry-point instructions for recovering the **current conversation context**.

It tells an AI what current conversational information must be recovered and where to continue from. It is concerned with the work currently being continued, not with storing the complete project knowledge base.

### `context-recover/project-knowledge-recover.md`

Instructions for recovering the information required to understand:

1. the Adaptive Learning project;
2. learning-material / knowledge data;
3. learner / user learning data.

It is a navigation and recovery procedure, not a project-knowledge database. Authoritative project documentation, data, source material, implementation, and history remain the sources of truth.

### `context-recover/context-recover-verification.md`

A set of **verification questions written for the user to ask the AI** after context recovery.

It is not an instruction that the AI must automatically execute during recovery. Its purpose is to test whether the AI has recovered the required context correctly and can demonstrate that understanding.

## 3. Authoring Principles

### CR-01 — Recovery Files Are Instructions, Not Knowledge Stores

Recovery files MUST primarily tell an AI:

- what to recover;
- where to look;
- which sources are authoritative;
- how to distinguish relevant domains;
- what to verify;
- what to do when information is missing or contradictory.

They MUST NOT become parallel repositories of detailed project knowledge.

### CR-02 — Separate Authoring from Execution

The principles in this file govern the **authoring and maintenance** of the recovery system.

Normal context recovery should execute the relevant recovery instructions without requiring this file to be read as part of the recovery procedure.

### CR-03 — Preserve File Roles

Each recovery file MUST have one clear responsibility:

- `context-recover.md` → recover current conversation context.
- `project-knowledge-recover.md` → recover project, learning-material / knowledge, and learner-data understanding.
- `context-recover-verification.md` → provide questions for testing whether recovery succeeded.

A file MUST NOT silently take over another file's role.

### CR-04 — Repository Is the Source of Truth

Recovery instructions MUST direct the AI to authoritative repository sources whenever correctness depends on current project state, data, implementation, provenance, or documented rules.

Conversation memory and inference are secondary and MUST NOT override repository evidence.

### CR-05 — No Duplication of Authoritative Knowledge

Authoring a recovery file MUST NOT copy detailed project documentation, data inventories, learner state, or historical records merely for convenience.

Recovery files should point to authoritative information rather than reproduce it.

### CR-06 — Preserve Domain Separation

Recovery instructions MUST keep these domains distinct:

- project knowledge;
- learning-material / knowledge data;
- learner / user learning data;
- current conversation context.

In particular, static knowledge MUST NOT be confused with learner state or historical learning activity.

### CR-07 — Progressive and Task-Driven Recovery

Recovery instructions SHOULD direct the AI to recover context progressively, starting with the minimum information needed for the current task and expanding only when required.

They SHOULD identify authoritative entry points and task-relevant sources rather than instructing the AI to read the entire repository indiscriminately.

### CR-08 — Recover Enough Context, Not Everything

The goal of recovery is to provide sufficient information to perform the current task correctly.

Authoring SHOULD avoid unnecessary recovery steps that increase context size without improving task correctness.

### CR-09 — Specify Verification and Failure Handling

Recovery instructions SHOULD explicitly state how the AI should behave when:

- information is missing;
- sources conflict;
- current repository state differs from remembered context;
- exact data cannot be determined;
- an authoritative source cannot be located.

The instructions SHOULD prefer verification and explicit uncertainty over guessing.

### CR-10 — Current Context Must Not Rewrite History

Recovery instructions MUST preserve the distinction between historical records, current repository state, and current conversation decisions.

A recovered conversation snapshot MUST NOT be treated as an authoritative historical record.

### CR-11 — Recovery Must Be Reproducible

A new AI session with no access to the previous conversation SHOULD be able to follow the recovery instructions and reconstruct the context required to continue the work without undocumented assumptions.

### CR-12 — Keep the Recovery System Stable and Minimal

Recovery files SHOULD change only when their roles, recovery procedures, verification requirements, or relevant context structure change.

Normal project evolution SHOULD primarily update authoritative project documentation and data, not accumulate project knowledge inside recovery files.

## 4. Authoring Boundary

When creating or modifying a recovery file, ask:

1. **What is this file responsible for?**
2. **What does the AI need to do?**
3. **Where should the AI obtain the required information?**
4. **Which source is authoritative?**
5. **How should ambiguity or missing information be handled?**
6. **Is this content an instruction, a verification question, or actual project knowledge?**

If the content is actual project knowledge, it normally belongs in the appropriate authoritative documentation or data rather than in a recovery file.

If the content is a question used to test recovered context, it belongs in `context-recover-verification.md`.

If the content is an instruction for recovering context, it belongs in the appropriate recovery-instruction file.
