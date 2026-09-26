# Documentation Cleanup

## Open Issues

### 1. Align Knowledge Atom admission and splitting rules

**Status:** Open

`docs/knowledge/overall.md` defines the finalized admission criterion: an independently useful, source-grounded knowledge point that is directly taught, explained, or explicitly represented by the source can become a Knowledge Atom. Direct testing is not required for Atom admission.

However, `docs/learning-material/principles/02-knowledge-model-and-interpretation.md` still states that direct source-level testing/practice is the trigger for separate atom representation and uses direct testing/practice as a splitting condition.

**Required resolution:**
- Align the learning-material principle with the canonical Knowledge Atom admission rule.
- Distinguish Atom admission from assessment metadata:
  - independently useful + source-grounded + taught/explained/explicitly represented → Knowledge Atom
  - direct testing/practice → `extra.is_tested = true`
- Ensure the splitting guidance does not reintroduce direct testing as a mandatory admission condition.

### 2. Clarify handling of inferred attributes

**Status:** Open

`docs/learning-material/principles/02-knowledge-model-and-interpretation.md` says that inferred attributes must remain distinguishable from source-stated attributes.

The current atom model does not define a generic `inference_origin` or equivalent field. Vocabulary `meaning` has its own explicit `(ai-generated)` convention, but this is not a general mechanism for all inferred attributes.

**Required resolution:**
- Revise the principle wording so it does not imply that a generic source-vs-inferred marker exists.
- Require inferred attributes to remain grounded in source context and reviewable through the existing evidence/provenance model.
- Preserve the existing special `(ai-generated)` convention for inferred vocabulary meanings where it is already defined canonically.

### 3. Reduce duplicated ownership of canonical rules

**Status:** Open

Several files under `docs/learning-material/principles/` restate detailed rules whose canonical ownership belongs to the Knowledge, Assessment, or Source documentation.

This is not necessarily a direct contradiction, but duplicated detailed rules create a risk of future drift between multiple sources of truth.

**Required resolution:**
- Review the learning-material principle documents for duplicated canonical rules.
- Keep high-level principles and cross-domain guidance there.
- Where a detailed rule already has a canonical owner under `docs/knowledge/`, `docs/assessment/`, or `docs/source/`, prefer a concise reference to that canonical documentation instead of restating the full rule.
- Do not remove useful cross-domain principles merely because they overlap conceptually; the goal is to clarify ownership and avoid conflicting copies.
