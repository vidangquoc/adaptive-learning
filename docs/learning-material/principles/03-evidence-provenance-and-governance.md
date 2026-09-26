# Evidence, Provenance, and Governance

## Provenance Is Mandatory

Every source-derived Knowledge Atom and Challenge must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve source identity, source boundary, precise location, relevant source context, uncertainty, and licensing/usage information where applicable.

The canonical source-boundary and provenance coordinates are defined by the Source documentation, especially `docs/source/source-structure.md`. Knowledge-specific provenance fields are defined by the canonical Knowledge Atom documentation, and Challenge provenance is defined by the canonical Assessment documentation.

External evidence such as proficiency frameworks must remain distinguishable from source evidence and project status.

## Candidate and Official Governance

Discovery, review, and officialization are distinct stages.

For Knowledge Atoms, the detailed Candidate/Official representation, review statuses, validation boundary, and officialization transition are owned by `docs/knowledge/atom-pipeline.md`.

For Challenges, the corresponding Candidate/Official structure and lifecycle are owned by `docs/assessment/challenge-extraction/pipeline.md` and `docs/assessment/challenge-extraction/structure.md`.

The cross-domain governance principle is:

```text
SOURCE EVIDENCE
      ↓
CANDIDATE
      ↓
HUMAN REVIEW
      ↓
approved Candidate
      ↓
OFFICIALIZE
      ↓
OFFICIAL
```

Automated discovery and analysis are advisory. They do not independently officialize source-derived knowledge or assessment objects.

## Human Review Is the Officialization Gate

Human review is the semantic gate between extracted Candidates and Official representations.

Structural validation does not replace human review. A schema can establish whether a representation is structurally valid, but it cannot by itself establish that the source was interpreted correctly.

Detailed review statuses and transition rules belong to the canonical Knowledge and Assessment lifecycle documents.

## Knowledge Admission and Learner State

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

> **Do not officialize. Preserve the Candidate and require review or an explicit extraction report according to the owning pipeline.**

## Pipeline Governance

Evidence should be preserved before interpretation. Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, Challenges, or learner-state data without rewriting raw evidence.

Transformations should be reproducible and idempotent where practical. Do not silently repair source evidence; record repairs or downstream normalization explicitly.

Keep these concerns separable:

```text
source evidence
candidate knowledge / assessment
human review decision
official representation
learning design
learner state
```

Detailed implementation rules belong to the canonical documentation for each concern rather than being copied into this cross-domain principle document.
