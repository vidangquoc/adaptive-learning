# Evidence, Provenance, and Governance

## Provenance Is Mandatory

Every source-derived Knowledge Atom and Challenge must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve source identity, source boundary, precise location, relevant source context, uncertainty, and licensing/usage information where applicable.

External evidence such as proficiency frameworks must remain distinguishable from source evidence and project status.

The detailed source-boundary rules are owned by `docs/source/source-structure.md`.

## Candidate and Official Stores

Discovery, review, and officialization are distinct stages of the knowledge pipeline.

A **Candidate** is a complete Knowledge Atom stored in the Candidate Store. It is not official knowledge yet. Candidate and Official use the same semantic ID and the same canonical atom structure; Candidate additionally carries the lifecycle field `review_status`.

```text
SOURCE EVIDENCE
      ↓
CANDIDATE STORE
      ↓
HUMAN REVIEW
      ↓
approved Candidate
      ↓
OFFICIALIZE
      ↓
OFFICIAL STORE
```

Candidate and Official are stored separately. Officialization is a storage transition, not a new ontology type and not a reviewer decision.

Automated discovery and analysis are advisory. They may locate evidence and analyze linguistic/semantic properties, but any tool-generated confidence scores or warnings are advisory tooling output and are not persisted Atom fields. They do not independently officialize Candidates.

## Human Review Is the Officialization Gate

Candidate review status has exactly three values:

```text
pending
approved
rejected
```

- `pending`: newly created Candidate or unchanged by reviewer;
- `approved`: accepted for officialization, but still a Candidate;
- `rejected`: rejected by reviewer and still reviewable later.

The reviewer may leave `pending`, set `approved`, or set `rejected`. There is no `hold` state.

> **Machine proposes. Human decides.**

## Officialization

Officialization processes only Candidates whose current status is `approved`.

For each approved Candidate:

1. write the Official Atom to the separate Official Store;
2. keep the same semantic ID;
3. preserve the canonical atom content and provenance;
4. delete the Candidate from the Candidate Store.

Therefore the Candidate Store has no `officialized` status. Candidates that are `pending` or `rejected` are not affected.

A rejected Candidate may be reviewed again. An Official Atom does not return to Candidate/rejected lifecycle states.

## Knowledge Admission Is Independent of Learner State

Static learning-material admission must not be controlled by learner mastery, review urgency, opportunity cost, or other learner-specific signals.

Learner evidence may influence adaptive activity selection, but it must not rewrite source evidence or determine whether static knowledge is canonical.

## Quality Gates

Every transformation stage should have explicit gates:

```text
PASS → continue
WARN → continue only when explicitly acceptable
FAIL → stop / preserve evidence / require review
```

Gates should cover applicable structural validity, provenance, semantic plausibility, schema validity, duplication, unsupported inference, answer validity, and source/license constraints.

If evidence is insufficient or competing interpretations remain unresolved:

> **Do not officialize. Preserve the Candidate and mark it for review.**

## Pipeline Governance

Evidence should be preserved before interpretation. Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, Challenges, or learner-state data without rewriting raw evidence.

Transformations should be reproducible and idempotent where practical. Do not silently repair source evidence; record repairs or downstream normalization explicitly.

Keep these concerns separable:

```text
source evidence
candidate knowledge
human review decision
official knowledge
learning design
learner state
```

Implementation details for discovering, validating, reviewing, and officializing atoms belong in `docs/knowledge/atom-pipeline.md`.
