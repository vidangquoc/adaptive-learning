# Assessment and Learning-Material Construction

## Source-Derived Challenges

Exercises contained in a selected source may form the initial canonical seed Challenge collection for that source.

Extract source-derived Challenges faithfully and retain the source information required by the canonical Challenge model. The detailed Challenge structure, source-occurrence identity, extraction scope, fail-closed rules, and Candidate/Official lifecycle are owned by `docs/assessment/challenge.md` and `docs/assessment/challenge-extraction/`.

Generated Challenges are a separate layer for targeted practice, discrimination, transfer, retention, and retesting.

## Challenge ↔ Knowledge Linkage

A source-derived Challenge must have a defensible relationship to the knowledge it assesses.

The canonical invariant is that one Challenge assesses exactly one Knowledge Atom. The detailed target-Atom rule and extraction handling for unresolved or multi-target occurrences are owned by the Assessment documentation.

If a Challenge assesses knowledge about a relationship between independent Knowledge Atoms, that relationship is represented according to the canonical Knowledge model rather than by adding multiple targets to the Challenge.

## Generated Material Must Add Instructional Value

Generate follow-up Challenges or explanations only for a concrete instructional reason, such as:

- isolating a gap;
- distinguishing close alternatives;
- increasing contextual complexity;
- testing transfer;
- verifying delayed retention;
- preventing memorization;
- providing a needed task format.

Generated content must remain distinguishable from source-derived content. The detailed representation and lifecycle of generated Challenges are defined by the canonical Assessment documentation.

## Competency Mapping

Challenges may be linked to competencies and target-domain task types when the relationship is supported by the learning design.

Do not force a competency label when evidence is insufficient.

## Assessment Validity

Assessment validity is a cross-domain learning-material concern, but the detailed rules for Challenge extraction and structure belong to `docs/assessment/`.

In particular, source-derived Challenges must preserve their source task faithfully, and extraction must fail closed when essential assessment information cannot be established. Grammar-specific validity rules, expected-answer handling, and source-answer-key interpretation are defined by the canonical Assessment documentation rather than repeated here.

## Relationship to Knowledge Construction

This document defines how source material participates in assessment-oriented learning-material construction. It does not define the atom ontology or atom schema. Those are owned by `docs/knowledge/`.
