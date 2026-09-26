# Documentation Cleanup

## Open Issues

### 1. Align Knowledge Atom admission and splitting rules

**Status:** Resolved

`docs/knowledge/overall.md` defines the finalized admission criterion: an independently useful, source-grounded knowledge point that is directly taught, explained, or explicitly represented by the source can become a Knowledge Atom. Direct testing is not required for Atom admission.

However, `docs/learning-material/principles/02-knowledge-model-and-interpretation.md` still states that direct source-level testing/practice is the trigger for separate atom representation and uses direct testing/practice as a splitting condition.

**Resolution:**
- Knowledge Atom admission is domain-specific:
  - Grammar: source directly teaches, explains, or clearly represents the knowledge point.
  - Vocabulary: the item is directly tested or assessed by the source; every directly assessed vocabulary item must be proposed as a Candidate.
- Source grounding remains mandatory for admitted Atoms.
- Direct testing is not a general admission condition; where applicable it is reflected in `extra.is_tested`.
- Splitting follows the applicable domain-specific admission rule and does not require direct testing for Grammar.

### 2. Clarify handling of inferred attributes

**Status:** Resolved

`docs/learning-material/principles/02-knowledge-model-and-interpretation.md` needed to define which knowledge attributes AI may infer and how those inferences are handled.

**Resolution:**
- AI inference is currently permitted only for `meaning`, `part_of_speech`, and `mother_says`.
- All other knowledge attributes must be grounded in explicit source evidence and must not be inferred by AI.
- Allowed inferences must remain grounded in source context and reviewable through the existing evidence/provenance model.
- Preserve the existing special `(ai-generated)` convention for inferred vocabulary `meaning`; do not extend it to `part_of_speech` or `mother_says`.
- No generic `inference_origin` field is introduced.

### 3. Reduce duplicated ownership of canonical rules

**Status:** Resolved

The learning-material principle documents were reviewed and their duplicated detailed rules were reduced to concise cross-domain guidance and references to the canonical Knowledge, Assessment, and Source documentation.

**Resolution:**
- `docs/learning-material/principles/02-knowledge-model-and-interpretation.md` now focuses on cross-domain interpretation, contextual analysis, inference boundaries, and evidence-grounded reasoning; detailed Knowledge Atom ownership is referenced rather than redefined.
- `docs/learning-material/principles/03-evidence-provenance-and-governance.md` now keeps only cross-domain provenance and governance principles; Candidate/Official lifecycle and source-boundary details are delegated to their canonical documents.
- `docs/learning-material/principles/04-assessment-and-learning-material.md` now keeps cross-domain assessment/learning-material guidance while delegating detailed Challenge structure, extraction, validity, and lifecycle rules to `docs/assessment/`.
- Useful cross-domain principles were retained rather than removed merely because they overlap conceptually.
- No canonical Knowledge, Assessment, or Source rule was moved into the learning-material rulebook.
