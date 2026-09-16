# Evidence, Provenance, and Governance

## Provenance Is Mandatory

Every source-derived knowledge atom and question must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve source identity, source boundary, precise location, relevant source context, uncertainty, and licensing/usage information where applicable.

External evidence such as proficiency frameworks must remain distinguishable from source evidence and project status.

The detailed Unit-boundary rules are owned by `06-source-unit-boundary.md`.

## Candidate and Promotion States

Discovery and promotion are different states.

A **candidate** is an evidence-backed hypothesis about possible canonical knowledge. It is not official knowledge. Candidate data must remain reviewable so analysis, review, and promotion are traceable and reproducible.

```text
SOURCE EVIDENCE
      ↓
CANDIDATE
      ↓
HUMAN REVIEW
      ↓
APPROVED
      ↓
PROMOTION
      ↓
OFFICIAL KNOWLEDGE
```

Automated discovery and analysis are advisory. They may locate evidence, analyze linguistic/semantic properties, calculate confidence, and flag warnings, but they do not independently promote knowledge.

## Human Review Is the Promotion Gate

A candidate becomes eligible for official learning material only after explicit human approval.

```text
APPROVE
REJECT
HOLD
```

The human decision and rationale must be preserved with provenance.

A candidate may be reviewed again later. Promotion always reads the current review status:

```text
APPROVED → eligible for promotion
anything else → do nothing
```

> **Machine proposes. Human decides.**

## Officialization

Official knowledge is a promoted representation of approved candidate knowledge.

Promotion must:

1. select candidates whose current status is `APPROVED`;
2. skip candidates already officialized;
3. create the official representation without destroying the candidate record;
4. preserve links to candidate and source evidence;
5. never promote `REJECTED`, `HOLD`, `PENDING`, or other non-approved candidates.

The exact official atom structure is defined by the knowledge-layer schema documentation.

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

> **Do not promote. Preserve the candidate and mark it for review.**

## Pipeline Governance

Evidence should be preserved before interpretation. Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting raw evidence.

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

Implementation details for discovering, validating, and promoting atoms belong in `docs/knowledge/atom-pipeline.md`.
