# Learning Material Construction Principles

> **Canonical index for the learning-material rulebook of Adaptive Learning.**
>
> The detailed principles are split into focused documents by conceptual ownership. The index does not redefine those principles.

## Rulebook Structure

### 1. Purpose and Learning Strategy

`01-purpose-and-learning-strategy.md`

Owns the purpose of learning-material construction, the initial source backbone, challenge-first learning, and whole-knowledge extraction.

### 2. Knowledge Model and Interpretation

`02-knowledge-model-and-interpretation.md`

Owns how source evidence is interpreted into knowledge distinctions and independent atoms, including semantic/linguistic reasoning and inference boundaries.

### 3. Evidence, Provenance, and Governance

`03-evidence-provenance-and-governance.md`

Owns provenance policy, candidate review and promotion, governance, quality gates, and fail-closed behavior.

### 4. Assessment and Learning-Material Construction

`04-assessment-and-learning-material.md`

Owns source-derived questions, question-to-knowledge linkage, generated assessment material, assessment dimensions, and assessment validity.

### 5. Source Scope and Metadata

`05-source-scope-and-metadata.md`

Owns source selection/scope, domain, proficiency metadata, priority boundaries, and copyright/source-boundary policy.

### 6. Source Unit Boundary

`06-source-unit-boundary.md`

Owns the canonical source boundary and validation rules for Unit-based source extraction.

## Ownership Rule

A principle is defined in the document that owns its conceptual role. Other documents may reference that rule but should not restate it in full.

```text
methodology
    ↓
learning-material principles
    ├── purpose / strategy
    ├── interpretation
    ├── provenance / governance
    ├── assessment
    ├── source scope / metadata
    └── source boundary
```

Knowledge ontology, atom structure, atom taxonomy, atom pipeline, data architecture, and learner-state rules are owned by their respective documents outside this rulebook.

## Global Invariants

The following invariants are surfaced here because they affect the whole rulebook:

1. Build a knowledge system, not a vocabulary list.
2. Preserve raw evidence separately from interpretation and learning design.
3. A parser discovers evidence; it does not author canonical knowledge.
4. Preserve source context and provenance.
5. Prefer accuracy over completeness.
6. Do not fabricate unsupported knowledge.
7. Keep static knowledge separate from learner state.
8. Automated analysis is advisory; human review governs promotion.
9. Generated material must add instructional value.
10. Fail closed when required structural, provenance, semantic, or validation evidence is insufficient.

## Maintenance Rule

Add new learning-material rules to the most conceptually appropriate child document first. Update this index only when ownership or rulebook structure changes, or when a genuinely global invariant needs to be surfaced.
