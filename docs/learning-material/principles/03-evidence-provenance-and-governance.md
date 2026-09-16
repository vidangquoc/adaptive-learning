# Evidence, Provenance, and Governance

## Provenance Is Mandatory

Every knowledge atom and source-derived question must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve source ID/type, source quality/title/reference, **source Unit or equivalent source boundary**, precise location within that boundary, exercise/question identifier when applicable, source context/role, uncertainty, and license/usage information where applicable.

The **Unit is the canonical source boundary** for Destination learning-material extraction. The project does not use a pre-cut `sections/` layer as a source boundary or provenance layer.

Keep source evidence, external proficiency evidence, and project status as separate provenance dimensions.

## Knowledge-Atom Discovery and Promotion

Discovery and promotion are different states.

A **candidate** is an evidence-backed hypothesis about a possible knowledge atom. It is not yet canonical knowledge. Candidate data must be preserved so that analysis, review, and promotion remain traceable and reproducible.

```text
EVIDENCE FROM SOURCE
   ↓
CANDIDATE
   ↓
HUMAN REVIEW
   ↓
APPROVED
   ↓
PROMOTION / COPY
   ↓
OFFICIAL KNOWLEDGE
```

Automated discovery and analysis may identify candidates, collect evidence, perform linguistic/semantic analysis, assess curricular evidence, calculate confidence, and flag warnings. These outputs are advisory and must not independently promote a candidate to official knowledge.

## Human Review Is the Final Promotion Gate

A candidate becomes eligible for official learning-material knowledge only after explicit human approval.

The reviewer may:

- `APPROVE`
- `REJECT`
- `HOLD`

The human decision and its rationale must be preserved with provenance. Candidate records and official atoms must remain distinguishable so that every official atom can be traced back to its evidence and final human decision.

A candidate with `APPROVED` status is eligible for officialization. A candidate with any other status is left untouched by the officialization process.

A previous `REJECT` or `HOLD` does not permanently prevent later review. If a candidate is intentionally reviewed again and its current status is changed to `APPROVED`, it becomes eligible for officialization.

> **Officialization reads the current candidate status. `APPROVED` → eligible; anything else → leave it alone.**

> **Machine proposes. Human decides.**

Automated curricular signals are inputs to human review, not authoritative promotion rules.

## Official Knowledge Is a Promoted Copy

Official knowledge must be produced by a **promotion process** from approved candidates.

The promotion process must:

1. select candidate records whose current status is explicit `APPROVED`;
2. if that candidate has already been officialized, skip it;
3. copy the approved knowledge into the official knowledge hierarchy;
4. preserve provenance linking each official atom to its candidate and source evidence;
5. leave the original candidate data intact;
6. never officialize a candidate whose current status is `REJECTED`, `HOLD`, `PENDING`, or any other non-`APPROVED` state.

Officialization is intentionally simple and idempotent: **approved and not-yet-officialized → promote; already officialized → skip; anything not approved → do nothing.**

Official knowledge must not be created by moving, deleting, or destructively transforming candidate records. The candidate layer preserves the proposal/review data; the official knowledge layer is the canonical learning-material snapshot consumed by downstream systems.

## Knowledge Data and Learner Review Data Are Separate

Static official learning material and dynamic learner-state data must remain separate concerns.

```text
DATA/
├── candidates/   ← proposed knowledge atoms
├── knowledge/    ← approved / official knowledge
└── review/       ← learner review and adaptive-learning data
```

`knowledge/` contains canonical official knowledge organized by source and source boundary. It must not depend on extracted section files. `review/` contains learner-specific attempts, learning state, review history, review queue, and related adaptive-learning data. Learner review data must not determine whether static material is admitted into official knowledge.

## Back-Matter Evidence

Author-curated back matter such as word lists, phrasal-verb databases, collocation databases, and idiom databases is strong curricular evidence that a source treats an item as part of its target learning scope.

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

Quality gates should cover source-boundary validity, provenance, semantic plausibility, answer uniqueness, schema validity, duplication, unsupported inference, and source/license constraints as appropriate.

If evidence is insufficient or competing interpretations remain unresolved:

> **Do not promote. Preserve the candidate and mark it for review.**

## Pipeline Governance

Evidence should be preserved before interpretation.

Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting the raw evidence layer.

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
