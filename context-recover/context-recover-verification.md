# Context Recovery Verification

## Purpose

This file defines a small verification checklist to determine whether the required context has been recovered correctly before continuing work.

Verification is a **test of recovered context**, not a replacement for reading the authoritative sources.

## Recovery Input

Before answering the verification questions, the AI should have read:

1. `context-recover/context-recover.md` — current conversation context.
2. `context-recover/context-recover-principles.md` — recovery rules.
3. `context-recover/project-knowledge.md` — stable project, learning-material, and learner-data knowledge.
4. Any authoritative `docs/`, data, sources, or implementation files required to verify the answers.

## Verification Questions

### 1. Project Understanding

**Question:**

> Give a brief preliminary summary of the Adaptive Learning project. What is the project trying to accomplish, what are its main conceptual components, and how do those components relate to one another?

**Verification goal:**

The answer should demonstrate a coherent high-level understanding of the project without relying on unsupported assumptions or confusing historical/domain-specific material with the project as a whole.

---

### 2. Knowledge-Atom Understanding

**Question:**

> Summarize the knowledge-atom inventory currently available in the repository. Report the number of knowledge atoms and break them down by the relevant atom categories/types. Identify the authoritative data locations used to obtain these counts.

**Verification goal:**

The answer should be based on the current repository data, not on remembered numbers from previous conversations. The AI should be able to distinguish knowledge data from source material, generated assessments, and learner state.

If the repository does not contain enough information to produce an exact count, the AI must explicitly say so rather than estimate or invent one.

---

### 3. Learner-Data Understanding

**Question:**

> Give a concise summary of the learner data currently stored in the repository. What learner information exists, what learning activity/history is recorded, what learner-state information is maintained, and how does it relate to the knowledge atoms?

**Verification goal:**

The answer should demonstrate that the AI understands learner data as a separate domain from static knowledge. It should identify the relevant authoritative data locations and distinguish current learner state from historical attempts or sessions.

## Verification Rules

1. **Use repository evidence.** Answers must be grounded in the current repository.
2. **Do not use remembered values.** Previous conversation context may guide recovery but must not substitute for verification.
3. **Do not invent missing data.** Unknown, unavailable, or ambiguous information must be reported as such.
4. **Distinguish domains.** Project knowledge, learning-material knowledge, and learner data must not be conflated.
5. **Prefer exact counts from data.** Statistics must be derived from the current authoritative data sources whenever possible.
6. **Verify before continuing.** If one or more answers reveal that context has not been recovered correctly, return to the relevant authoritative sources before continuing the task.

## Pass Condition

Context recovery passes when the AI can answer all three questions coherently, with repository-grounded evidence, without unsupported assumptions, and with the three context domains correctly separated.
