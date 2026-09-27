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

The current work is focused on the **Challenge / assessment extraction** part of Adaptive Learning.

The Knowledge Atom framework is substantially defined and the work has moved into applying and validating the Challenge Extraction model against real source material.

### Current objective

Keep these layers distinct:

1. **Project knowledge** — stable knowledge required to understand the project and its architecture.
2. **Conversation context** — temporary decisions and current work position needed to continue the task.
3. **Recovery instructions** — procedures telling AI where and how to recover context.
4. **User prompts** — prompts used to start recovery and verify the result.

### Current Challenge work

The canonical Challenge model is documented under `docs/assessment/`.

Current settled points relevant to continuing the work:

- Assessment uses a Challenge to obtain evidence about exactly one Knowledge Atom.
- One Challenge has exactly one `target_atom_id`.
- If the assessed knowledge is a relationship between independent Atoms, the relationship itself is represented by a `relation` Atom and is the Challenge target.
- Challenge extraction is based on actual source assessment/exercise material.
- The current extraction scope is Atom-level Challenges.
- An exercise item is the default Challenge candidate boundary when contextual analysis shows that it is an independent, evaluable learner task.
- Multiple blanks/actions inside one independent item can still form one Challenge.
- Shared-context exercises are currently skipped and reported rather than artificially decomposed.
- Long integrated/composite exercises and long Cloze passages are currently outside Atom-level extraction and are skipped/reported.
- A Challenge cannot cross Source Segment boundaries.
- Source-derived Challenge identity is the source occurrence, encoded in the Challenge ID.
- Extracted Challenges require source traceability and a specific expected answer supported by source evidence.
- Extraction is fail-closed: do not invent or silently repair essential instruction, prompt, options, learner response elements, target Atom, boundaries, source information, or expected answer.
- Candidate and Official Challenges use the same Challenge ID; officialization is a storage transition.
- There is no `difficulty` concept and no persisted Challenge Form field.

For exact definitions, always verify the authoritative Challenge documentation rather than treating this summary as canonical.

### Recent extraction state

Unit 1 has been extracted from the current source material into Candidate stores:

- Grammar Knowledge Atom Candidates: 22
- Vocabulary Knowledge Atom Candidates: 25
- Challenge Candidates: 93
- Challenge extraction reports: 4 occurrences

The Unit 1 extraction currently reports/skips:

- A1 — source item contains two independently assessed tense choices; one Challenge cannot target both and the source occurrence cannot be safely split without changing its boundary.
- A12 — same one-Challenge/one-Atom boundary problem with two independently assessed tense choices.
- Exercise C — shared-context exercise, skipped under the current extraction scope.
- Exercise J — long integrated Cloze exercise, skipped under the current extraction scope.

The extracted Unit 1 files are current working data, not a substitute for rechecking the source when extraction quality is under review.

When reviewing or changing this extraction, verify the actual source evidence, answer key, canonical Segment IDs, source page convention, target Atom, prompt/options, and answer values against the repository.

### Current Atom work relevant to Challenge extraction

The Knowledge Atom model currently has:

- flat atoms; no parent/child hierarchy;
- `domain + type` taxonomy with no subtype layer;
- `vocabulary` and `grammar` domains;
- vocabulary types including `lexical_sense`, `multiword_expression`, `phrasal_verb`, `idiom`, and `collocation`;
- grammar types including `rule`, `usage`, `exception`, `word_formation`, `morphological_form`, and `relation`;
- relation knowledge represented by `type: relation` with a relation-specific `relation_type`;
- Candidate and Official Atom stores kept separate;
- Candidate and Official use the same Atom ID;
- Candidate review status is `pending | approved | rejected`;
- officialization is a storage transition, not a review status.

Atom admission remains domain-specific: Grammar knowledge can be admitted when directly taught, explained, or clearly represented; Vocabulary knowledge must be directly tested/assessed by the source. Source grounding remains mandatory.

Do not use this summary instead of the canonical Atom docs when exact field semantics or taxonomy details matter.

### Current work position

The previous Step 3 taxonomy review is historical context, not the current active task.

Recent assessment design cleanup has also resolved several earlier open design points. Do not recreate an assessment `open-issues.md` file merely to hold temporary discussion.

The immediate working direction is **Challenge Extraction implementation/review against real source material**, including verifying the Unit 1 extraction and then continuing extraction work only when the current rules are satisfied.

### Authoritative current documentation

For the current Challenge work, start with:

- `docs/assessment/overall.md`
- `docs/assessment/challenge.md`
- `docs/assessment/challenge-extraction/principles.md`
- `docs/assessment/challenge-extraction/pipeline.md`
- `docs/assessment/challenge-extraction/structure.md`
- `schemas/candidate-challenge.schema.json`
- `schemas/official-challenge.schema.json`

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
├── context-recover.md
├── project-knowledge-recover.md
├── context-recovery-prompt.md
└── context-recovery-authoring-principles.md
```

The authoring-principles file is meta-level and is not part of normal recovery.

## 3. Recovery Procedure

For a new conversation or lost context:

1. Read this file to recover the current conversation context.
2. Read `context-recover/project-knowledge-recover.md` to determine the authoritative project/data sources relevant to the task.
3. Read only the authoritative documentation, data, source material, and implementation relevant to the current task.
4. For current extraction work, inspect the actual source material and current extracted data before modifying it.
5. Recover missing context progressively.
6. Verify important facts against repository evidence.
7. Continue the task only after sufficient context has been recovered.

Do not read `context-recover/context-recovery-authoring-principles.md` as a normal recovery step.

## 4. Boundary

> `context-recover.md` describes how to recover the current conversation context. `project-knowledge-recover.md` describes how to recover project, learning-material / knowledge, and learner-data understanding. `context-recovery-prompt.md` provides user-facing recovery and verification prompts. `context-recovery-authoring-principles.md` governs how the recovery system itself is authored and maintained.

Stable project knowledge belongs in authoritative documentation and data. Recovery instructions belong in the appropriate recovery file. User-facing prompts belong in `context-recovery-prompt.md`.
