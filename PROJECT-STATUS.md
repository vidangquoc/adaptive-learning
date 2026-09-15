# Adaptive Learning — Project Status

**Last updated:** 2026-09-15  
**Branch:** `main`  
**Project:** Adaptive Learning  
**Predecessor/domain:** PTNK

---

## 1. Current state

🟡 **Architecture established; implementation of the executable adaptive learning loop is the next major phase.**

The repository has moved beyond the original PTNK vocabulary-focused project. PTNK is now a predecessor/domain-specific evidence layer inside the broader Adaptive Learning system.

Current mental model:

```text
Goal
 ↓
Competency model
 ↓
Knowledge base
 ↓
Diagnostic / Challenge
 ↓
Learning State
 ↓
Learning Frontier
 ↓
Review Queue
 ↓
Next-best Activity
 ↓
Assessment
 ↺
Learning State
```

## 2. Established architecture

### Knowledge / evidence

- [x] RAW / EVIDENCE / CURATED / OFFICIAL separation
- [x] Provenance and accuracy-over-completeness policy
- [x] Flat knowledge-atom model
- [x] Candidate vs official knowledge separation
- [x] Destination C1 & C2 identified as the initial curriculum backbone
- [x] PTNK evidence pipeline retained as a calibration/validation subsystem

### Adaptive learning

- [x] Challenge-first principle
- [x] Diagnostic-first approach
- [x] Learning State concept
- [x] Mastery dimensions
- [x] Learning-state progression model
- [x] Adaptive branching concept
- [x] Review queue concept
- [x] Expansion-gate concept
- [x] 700h treated as a ceiling/learning budget rather than a quota

### Continuity

- [x] Canonical `PROJECT-CONTEXT.md`
- [x] Context recovery documentation
- [x] Project identity migrated from PTNK to Adaptive Learning

## 3. PTNK relationship

PTNK is **not being deleted or renamed out of the repository**.

PTNK-specific files remain valid because they describe:

- the predecessor project;
- PTNK exam evidence;
- calibration/validation material;
- PTNK-specific datasets and source provenance.

The project-level identity is now:

> **Adaptive Learning** — with PTNK as one important predecessor/domain and validation target.

## 4. Current repository layers

```text
sources/
    ↓
data / evidence
    ↓
curated knowledge
    ↓
knowledge atoms
    ↓
competencies / modules
    ↓
learner state
    ↓
attempt history
    ↓
review queue
    ↓
next-best activity
```

Important documentation includes:

- `PROJECT-CONTEXT.md`
- `PROJECT-STATUS.md`
- `docs/context-recover.md`
- `context-recover.md`
- `docs/methodology.md`
- `docs/knowledge-atom-pipeline.md`
- `docs/learning-state-specification.md`
- `docs/learning-material-principles/`
- `docs/data-collection-rules.md`
- `docs/data-pipeline.md`

## 5. Immediate next work

### Priority 1 — make Learning State executable

- [ ] Define concrete learner-state schema
- [ ] Define attempt-history schema
- [ ] Define competency-state schema
- [ ] Define review-queue schema
- [ ] Define deterministic state-update rules
- [ ] Define deterministic review-priority rules

### Priority 2 — build a small adaptive pilot

- [ ] Select representative competencies
- [ ] Create challenge/diagnostic items
- [ ] Record learner attempts
- [ ] Update learner state
- [ ] Generate review queue
- [ ] Verify that each recommendation has an explicit reason

### Priority 3 — expand knowledge coverage

Only after the adaptive loop works:

- [ ] Expand lexical coverage
- [ ] Expand grammar competencies
- [ ] Expand reading/cloze competencies
- [ ] Expand word formation and transformation
- [ ] Expand additional domains as evidence requires

Do not collect large amounts of knowledge without a learning-state purpose.

## 6. Design rules

### Rule A — mastery beats exposure

Seeing an item is not evidence of mastery.

### Rule B — no punishment for mastery

If diagnostic evidence shows mastery, skip or compress instruction.

### Rule C — diagnose dimensions, not just totals

A high aggregate score does not imply mastery if a required dimension is weak.

### Rule D — target the bottleneck

Teach the smallest useful gap rather than restarting a whole module.

### Rule E — knowledge is not learner state

Static knowledge describes what can be learned. Learner state describes what this learner currently knows and can do.

### Rule F — PTNK is calibration, not the whole system

Do not rebuild Adaptive Learning as a PTNK-only vocabulary or paper-reconstruction project.

### Rule G — heuristics are provisional

Thresholds and review intervals are working rules until supported by project data.

### Rule H — preserve provenance

Knowledge and evidence must remain traceable to their sources where applicable.

## 7. Definition of success for the next phase

The adaptive loop should eventually be able to take an attempt such as:

```text
Learner answered a challenge incorrectly.
```

and deterministically produce:

```text
Attempt recorded
      ↓
Relevant competency identified
      ↓
Weak dimension updated
      ↓
Mastery gate evaluated
      ↓
Review queue entry created
      ↓
Reason recorded
      ↓
Next-best targeted activity selected
```

At that point Adaptive Learning has moved from a knowledge repository into a functioning closed-loop learning system.
