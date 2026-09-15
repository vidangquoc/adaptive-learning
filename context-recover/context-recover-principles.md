# Context Recovery Principles

## 1. Purpose

These principles define how context recovery works in the Adaptive Learning repository.

They govern the separation between:

- **Project knowledge** — what the project is and how it works.
- **Conversation context** — what the current conversation is doing and what must be preserved to continue it.

This file defines the principles only. Detailed project knowledge belongs in `project-knowledge.md` and the project documentation it points to.

## 2. Core Principles

### CR-01 — Separate Project Knowledge from Conversation Context

Project knowledge and current conversation context MUST be treated as different kinds of information.

- `project-knowledge.md` answers: **What is this project and what do its data mean?**
- `context-recover.md` answers: **What are we doing now and what context is needed to continue?**

### CR-02 — `project-knowledge.md` Is the Knowledge Baseline

`project-knowledge.md` MUST provide the entry point for recovering the knowledge required to understand:

1. the project itself;
2. the learning-material / knowledge domain;
3. the learner-data domain.

It MUST point to authoritative detailed documentation and data rather than duplicating them unnecessarily.

### CR-03 — `context-recover.md` Is Conversation-Specific

`context-recover.md` MUST contain only the context necessary to resume the current line of work.

It MAY contain, for example:

- current task or objective;
- decisions made in the current work;
- active constraints;
- files or components currently under discussion;
- unresolved questions;
- immediate next steps.

It MUST NOT become a complete project history or a substitute for project documentation.

### CR-04 — No Duplication of Authoritative Knowledge

Information that belongs in project documentation MUST NOT be copied into recovery files merely for convenience.

Recovery files should **point to knowledge; they should not become another source of knowledge**.

### CR-05 — Repository Is the Source of Truth

The current repository is authoritative for project state and documented knowledge.

Previous conversations, model memory, and inferred assumptions are secondary context and MUST be verified against the repository when correctness matters.

### CR-06 — Preserve Domain Separation

The following domains MUST remain conceptually distinct:

- project knowledge;
- learning-material / knowledge data;
- learner data;
- current conversation context.

In particular, knowledge about what can be learned MUST NOT be confused with data about what a learner has done, knows, or needs to review.

### CR-07 — Progressive and Task-Driven Recovery

Context SHOULD be recovered progressively rather than by reading the entire repository indiscriminately.

The recovery process SHOULD move from:

1. current conversation context;
2. project knowledge baseline;
3. task-relevant authoritative documentation;
4. task-relevant source, data, and implementation details.

### CR-08 — Recover Enough Context, Not Everything

The objective is to recover **sufficient context to perform the current task correctly**, not to reconstruct the entire historical conversation or load every repository file into context.

### CR-09 — Verify Before Inferring

When information is missing, ambiguous, or contradictory, the system MUST verify it from authoritative repository sources before treating an assumption as fact.

### CR-10 — Current Context Must Not Rewrite History

Conversation recovery MUST preserve the distinction between:

- historical facts and records;
- current project state;
- current conversation decisions.

A current conversation context is a working snapshot, not a replacement for historical records.

### CR-11 — Recovery Must Be Reproducible

A new AI session with no access to the previous conversation SHOULD be able to follow the recovery protocol and reconstruct the context required to continue the work without relying on undocumented assumptions.

### CR-12 — Keep Recovery Files Stable and Minimal

Recovery files SHOULD change only when the recovery protocol, context structure, or current working context changes.

Project evolution SHOULD normally update the authoritative project documentation, not cause project knowledge to accumulate inside `context-recover.md`.

## 3. Boundary Rule

The simplest boundary is:

> **`project-knowledge.md` describes what must be understood. `context-recover.md` describes what must be remembered to continue the current conversation.**

If information is needed by every future conversation to understand the project, it belongs in project knowledge or authoritative documentation.

If information is needed only to continue the current conversation, it belongs in conversation recovery context.

If information is neither, it should not be added to the recovery files.
