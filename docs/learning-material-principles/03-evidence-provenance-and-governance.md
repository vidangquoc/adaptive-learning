# Evidence, Provenance, and Governance

## Provenance Is Mandatory

Every knowledge atom and source-derived question must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve source ID/type, source quality/title/reference, unit/section/page/source location, exercise/question identifier, relevant exam/year metadata, source context/role, uncertainty, and license/usage information where applicable.

Keep source evidence, PTNK relevance, CEFR evidence, and project status as separate provenance dimensions.

## Knowledge-Atom Discovery and Promotion

Discovery and promotion are different states.

A **candidate** is an evidence-backed hypothesis about a possible knowledge atom. It is not yet canonical knowledge.

```text
EVIDENCE
   ↓
CANDIDATE
   ↓
VERIFIED
   ↓
ENRICHED
```

Automated discovery and analysis may identify candidates, collect evidence, perform linguistic/semantic analysis, assess curricular evidence, calculate confidence, and flag warnings. These outputs are advisory and must not independently promote a candidate to official knowledge.

## Human Review Is the Final Promotion Gate

A candidate becomes an official learning-material knowledge atom only after explicit human approval.

The reviewer may:

- `APPROVE`
- `REJECT`
- `HOLD`

The human decision and its rationale must be preserved with provenance. Candidate records and official atoms must remain distinguishable so that every official atom can be traced back to its evidence and final human decision.

> **Machine proposes. Human decides.**

Automated curricular signals—including instructional evidence, back-matter presence, linguistic confidence, and related evidence—are inputs to human review, not authoritative promotion rules.

## Back-Matter Evidence

Author-curated back matter such as word lists, phrasal-verb databases, collocation databases, and idiom databases is strong curricular evidence that the source treats an item as part of the target learning scope.

Back-matter evidence informs human review but does not by itself prove semantic identity, meaning, or official atom status.

## Learner State Must Not Govern Material Admission

Learning-material admission must be determined independently of learner state.

Learner mastery, scheduling urgency, opportunity cost, and other learner-specific signals belong to downstream adaptive learning and must not determine whether a candidate becomes an official knowledge atom.

## Quality Gates and Fail-Closed Behavior

Every transformation stage must have explicit quality gates.

```text
PASS → continue
WARN → continue only when explicitly acceptable
FAIL → stop / preserve evidence / require review
```

Quality gates should cover structural validity, provenance, semantic plausibility, answer uniqueness, schema validity, duplication, unsupported inference, and source/license constraints as appropriate.

If evidence is insufficient or competing interpretations remain unresolved:

> **Do not promote. Preserve the candidate and mark it for review.**

## Pipeline Governance

Evidence should be preserved before interpretation.

Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting the raw evidence layer.

Transformations should be reproducible and idempotent where practical. Do not silently repair source evidence; record repairs or downstream normalization explicitly.

Keep these concerns separable:

```text
source evidence
interpretation
validation
enrichment
learning design
learner state
```
