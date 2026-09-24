# Context Recovery

## 1. Purpose

This file is the entry point for recovering the **current conversation context** of `vidangquoc/adaptive-learning`.

It does not contain the project's full knowledge. To recover project, learning-material / knowledge, and learner-data understanding required for the current task, follow:

- `context-recover/project-knowledge-recover.md`

The context-recovery authoring principles are defined in:

- `context-recover/context-recovery-authoring-principles.md`

That file governs creation and maintenance of the recovery system. It is **not** part of normal recovery.

User-facing recovery and verification prompts are provided in:

- `context-recover/context-recovery-prompt.md`

That file contains prompts for the user; it is not an automatic recovery step.

## 2. Current Conversation Context

### Current task

The current work is focused on the **Challenge / assessment extraction design** of Adaptive Learning.

The Knowledge Atom framework has already been substantially defined. The current discussion has moved from Atom taxonomy review to Challenge extraction. The recovery system itself is also being updated because the previous recovery snapshot had become stale.

### Current objective

Keep these layers distinct:

1. **Project knowledge** — stable knowledge required to understand the project and its architecture.
2. **Conversation context** — temporary decisions and work position needed to continue the current task.
3. **Recovery instructions** — procedures telling AI where and how to recover context.
4. **User prompts** — prompts used to start recovery and verify the result.

### Current Challenge work

The canonical Challenge model is already documented under `docs/assessment/`.

Current settled points relevant to continuing the work:

- Challenge is the concrete assessment task used to assess a Knowledge Atom.
- One Challenge targets exactly one Knowledge Atom.
- A Challenge that assesses knowledge about a relationship targets a `relation` Knowledge Atom; it does not directly target multiple independent Atoms.
- Challenge extraction is based on actual source assessment/exercise material.
- Long integrated/composite exercises, including long Cloze passages, are currently outside atom-level Challenge extraction.
- Shared-context exercises are currently skipped rather than split into artificial atom-level Challenges.
- A Challenge cannot belong to two Source Segments; such occurrences are skipped/reported.
- A source exercise item normally provides the default Challenge boundary when contextual analysis shows that it is an independent evaluable learner task.
- Multiple blanks or actions inside one independent item can still belong to one Challenge.
- A supported extracted Challenge requires a specific expected answer supported by source evidence; the extractor must not invent an answer.
- Essential missing information causes an occurrence to be incomplete/unresolved/skipped rather than silently repaired.
- Challenge identity for source-derived Challenges is the source occurrence, encoded in the Challenge ID.
- Candidate and Official Challenges use the same ID; officialization is a storage transition.
- There is no `difficulty` concept in the Challenge model.
- There is no `retired` lifecycle state.
- There is no persisted Challenge Form field.
- `options` are semantic option values, not A/B/C presentation labels.
- Whitespace constraints apply to every option and answer string: no leading/trailing whitespace, exactly one ASCII space between words, and no tabs or line breaks.

These are context-level summaries of the current work. For exact canonical definitions, always verify the authoritative Challenge documentation.

### Current Atom work relevant to Challenge extraction

The Knowledge Atom model currently has:

- flat atoms; no parent/child atom hierarchy;
- `domain + type` taxonomy with no subtype layer;
- `vocabulary` and `grammar` domains;
- relation knowledge represented as `type: relation` with a relation-specific `relation_type`;
- grammar structural relationships inside one construction represented as rules, not relation atoms;
- Candidate and Official atom stores kept separate;
- Candidate and Official use the same Atom ID;
- Candidate review status is `pending | approved | rejected`;
- officialization is a storage transition, not a review status.

Do not use this summary instead of the canonical Atom docs when exact field semantics or taxonomy details matter.

### Current work position

The previous Step 3 taxonomy review should **not** be treated as the current active task. Its historical discussion may still be relevant when Challenge extraction needs Atom context, but it must not be revived as the current task merely because an older recovery file mentioned it.

There is no current `open-issues.md` file for assessment. Do not recreate one merely to hold temporary discussion.

### Authoritative current documentation

For the current Challenge work, start with:

- `docs/assessment/assessment.md`
- `docs/assessment/challenge.md`
- `docs/assessment/challenge-extraction/challenge-structure.md`

For Knowledge Atom context, use:

- `docs/knowledge/overall.md`
- `docs/knowledge/atom-types.md`
- `docs/knowledge/atom-structure.md`
- `docs/knowledge/atom-pipeline.md`

For learning-material/source context, use the relevant files under:

- `docs/learning-material/principles/`
- `docs/learning-material/procedures/`
- `docs/learning-material/rules/`
- `docs/learning-material/sources/`

For learner state, use:

- `docs/learner/learning-state.md`

### Current constraints

- Repository state is authoritative for current project rules, data, source material, implementation, and history.
- Do not promote conversation summaries into canonical project rules.
- Do not use obsolete paths from older recovery snapshots.
- Do not recreate deleted review/WIP files merely because they appeared in earlier context.
- When a current decision is uncertain, inspect the relevant authoritative file or Git history instead of guessing.
- Recovery should be progressive and task-driven; do not read the entire repository unnecessarily.

### Recovery-system files

```text
context-recover/
├── context-recovery-prompt.md
├── context-recover.md
├── project-knowledge-recover.md
└── context-recovery-authoring-principles.md
```

The authoring-principles file is meta-level and is not part of normal recovery.

## 3. Recovery Procedure

For a new conversation or lost context:

1. Read this file to recover the current conversation context.
2. Read `context-recover/project-knowledge-recover.md` to determine the authoritative project/data sources relevant to the task.
3. Read only the authoritative documentation, data, source material, and implementation relevant to the current task.
4. Recover missing context progressively.
5. Verify important facts against repository evidence.
6. Continue the task only after sufficient context has been recovered.

Do not read `context-recover/context-recovery-authoring-principles.md` as a normal recovery step.

## 4. Boundary

> `context-recover.md` describes how to recover the current conversation context. `project-knowledge-recover.md` describes how to recover project, learning-material / knowledge, and learner-data understanding. `context-recovery-prompt.md` provides user-facing recovery and verification prompts. `context-recovery-authoring-principles.md` governs how the recovery system itself is authored and maintained.

Stable project knowledge belongs in authoritative documentation and data. Recovery instructions belong in the appropriate recovery file. User-facing prompts belong in `context-recovery-prompt.md`.
