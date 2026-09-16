# Learning Material Construction Principles

> **Canonical index for the learning-material rulebook of Adaptive Learning.**
>
> The detailed principles are intentionally split into focused documents. They are grouped by conceptual dependency rather than by arbitrary size.

## Rulebook Structure

### 1. Purpose and Learning Strategy

`01-purpose-and-learning-strategy.md`

Defines the project's purpose, Destination C1 & C2 as the initial backbone, challenge-first learning, and the requirement to extract the whole taught knowledge universe.

### 2. Knowledge Model and Interpretation

`02-knowledge-model-and-interpretation.md`

Defines knowledge distinctions, flat knowledge atoms, evidence-vs-interpretation boundaries, source-order and context-aware reasoning, lexical and grammatical reasoning, context-grounded inference, atom splitting/aggregation, accuracy over completeness, definitions, pronunciation, examples, patterns, word formation, and deduplication.

### 3. Evidence, Provenance, and Governance

`03-evidence-provenance-and-governance.md`

Defines provenance, candidate/promotion states, automated analysis as advisory evidence, the human final promotion gate, back-matter evidence, separation from learner state, quality gates, fail-closed behavior, and pipeline governance.

### 4. Assessment and Learning-Material Construction

`04-assessment-and-learning-material.md`

Defines Destination exercises as canonical seed questions, question-to-knowledge linkage, generated material, mastery dimensions, competency mapping, and grammar assessment/modeling rules including answer uniqueness.

### 5. Source Scope and Metadata

`05-source-scope-and-metadata.md`

Defines source scope, intrinsic vocabulary priority, domain, proficiency/external metadata, and copyright/source boundaries.

### 6. Source Unit Boundary

`06-source-unit-boundary.md`

Defines the authoritative Destination source boundary. Destination extraction uses **Units only**. The former extracted `sections/` layer and section manifest are superseded and must not be used as source-of-truth, provenance, or pipeline boundaries.

## Governing Principle

These documents are one rulebook. The split is organizational only: a principle should be maintained in the document that best matches its conceptual role.

When two principles interact, the more specific rule governs the specific operation, while the general principles remain applicable unless explicitly overridden.

## Non-Negotiable Rules

1. Build a knowledge system, not a vocabulary list.
2. Destination C1 & C2 is the initial knowledge backbone.
3. Challenge first when prior knowledge is plausible.
4. Extract the whole taught knowledge universe, not only exercise words.
5. Separate raw evidence from normalization, interpretation, and learning design.
6. A parser discovers evidence; it does not author canonical knowledge.
7. Lexical and grammatical atomization requires linguistic/semantic reasoning.
8. Preserve source order and inspect relevant surrounding **Unit** context before making semantic or grammatical judgments.
9. **Unit is the canonical Destination source boundary. Do not depend on an extracted `sections/` layer or section manifest.**
10. Context may support inference of attributes such as POS, sense, usage, or meaning, but inferred values must remain distinguishable from source-stated facts.
11. If evidence is insufficient, leave the field null/pending; never guess merely to fill the schema.
12. One source span does not necessarily equal one atom; split, aggregate, or reject evidence according to independently useful knowledge distinctions.
13. Preserve provenance for every source-derived atom and question, including Unit and precise location within Unit.
14. Prefer accuracy over completeness.
15. Preserve useful distinctions; do not flatten independently learnable knowledge.
16. Knowledge atoms are flat and independent; relationships are not ancestry or inherited mastery.
17. Automated analysis is advisory; human review is the final promotion gate.
18. Learner state must not determine admission into the static learning-material knowledge base.
19. Destination exercises are canonical seed questions.
20. Link questions to the knowledge they actually test.
21. Generated material must add instructional value.
22. Grammar questions must have a uniquely defensible answer.
23. Fail closed when Unit-boundary, structural, provenance, semantic, or validation gates fail.

## Maintenance Rule

New learning-material rules should be added to the most conceptually appropriate child document first. The index should be updated only when the rulebook structure changes or a new non-negotiable rule must be surfaced.

The former section-based Destination extraction is superseded. References to a textbook's internal section/topic/exercise labels may remain as descriptive source context, but `sections/` is not a canonical data layer.
