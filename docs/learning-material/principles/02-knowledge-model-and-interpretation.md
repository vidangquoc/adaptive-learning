# Knowledge Model and Interpretation

> This document defines how source evidence is interpreted into useful knowledge distinctions. The formal atom structure is owned by `docs/knowledge/atom-structure.md`; the taxonomy is owned by `docs/knowledge/atom-types.md`; discovery and promotion are owned by `docs/knowledge/atom-pipeline.md`.

## Preserve Knowledge Distinctions

Do not flatten different kinds of knowledge into a generic record. Preserve distinctions whenever they matter for meaning, usage, learning, or assessment.

Relevant distinctions may include:

```text
lexical sense
multiword expression
idiom
phrasal verb
collocation
fixed expression
grammatical construction / rule
lexical or grammatical contrast
word formation
usage restriction
discourse / pragmatic function
```

The taxonomy document determines which categories are available; this document determines how to reason about whether source evidence represents a meaningful distinction.

## Flat Knowledge-Atom Principle

A knowledge atom is a source-grounded unit of knowledge admitted under the domain-specific Knowledge Atom rules.

Knowledge atoms are flat and independent by default. Admission differs by domain:

- For **Grammar**, a knowledge point may be represented as an Atom when the source directly teaches, explains, or clearly represents it. Direct testing is not required.
- For **Vocabulary**, a vocabulary item must be directly tested or assessed by the source to become a Candidate. Every vocabulary item directly assessed by the source must be proposed as a Candidate.

This applies across the vocabulary taxonomy, including `lexical_sense`, `multiword_expression`, `phrasal_verb`, `idiom`, and `collocation`.

Direct testing is therefore not a general trigger for Atom admission. Where an Atom is tested, assessment evidence is recorded through the existing `extra.is_tested` and test-evidence mechanisms.

Do not impose hierarchies such as:

```text
word → sense → pattern → expression
grammar heading → grammar use → example
```

Raw Atom-to-Atom relationships are not persisted merely as graph edges. When knowledge about a relationship between independent Knowledge Atoms is itself an independently learnable or testable target, that knowledge is represented as a `relation` Atom.

## Evidence versus Interpretation

Extraction, contextual interpretation, normalization, and learning design are separate operations.

A source example, heading, table row, or exercise may provide evidence for knowledge, but it does not automatically define the atom boundary or ontology.

```text
source evidence
      ↓
contextual interpretation
      ↓
knowledge distinction
      ↓
atom proposal
```

Interpretation must remain grounded in the available evidence. If the source does not support a reliable distinction, preserve the uncertainty rather than inventing one.

## Source Order and Context

Interpret relevant source content in its original instructional order and inspect the surrounding context before making semantic or grammatical judgments.

Context may include:

- headings and subheadings;
- lexical tables or word boxes;
- definitions and explanations;
- example sentences;
- usage notes and patterns;
- contrast sets;
- task instructions and framing;
- nearby source spans.

These are source-content features, not separate repository source layers.

## Context-Grounded Inference

AI inference is currently permitted only for the following knowledge attributes:

- `meaning`;
- `part_of_speech`;
- `mother_says`.

All other knowledge attributes must be grounded in explicit source evidence and must not be inferred by AI. If a required non-inferable attribute is not supported by the source, do not invent it; preserve the uncertainty or leave the extraction unresolved as appropriate.

For attributes that may be inferred, the inference must remain grounded in the available source context and reviewable through the existing evidence/provenance model. The special `(ai-generated)` convention remains applicable to inferred vocabulary `meaning` where defined by the canonical Knowledge Atom model. No equivalent marker is added for `part_of_speech` or `mother_says`.

Use this hierarchy for attributes that are allowed to be inferred:

```text
explicit source statement
        ↓
strong contextual inference
        ↓
weak / ambiguous inference
        ↓
null / pending / review-needed
```

## Atom Boundaries

One source span does not necessarily equal one atom:

```text
one evidence span → multiple atoms
multiple evidence spans → one atom
one evidence span → no atom
```

Split when the source supports a distinct knowledge point and the resulting parts satisfy the applicable domain-specific Knowledge Atom admission rule.

Merge evidence only when it supports the same underlying knowledge item and the same sense/use.

Do not merge merely because forms are identical or similar, meanings overlap, items share a word family, or one expression contains another.

False deduplication is more damaging than controlled redundancy.

## Linguistic and Semantic Reasoning

For lexical knowledge, consider sense, lexicalization, idiomaticity, syntactic behavior, patterns, derivation, register, semantic contrasts, and restrictions where the source supports them.

For grammar, consider form, meaning, function, discourse context, constraints, and contrasts. Do not create a grammar atom merely because a textbook heading exists. Represent a grammatical knowledge point as a separate atom when the source directly teaches, explains, or clearly represents that point.

## Accuracy over Completeness

Never fill a field merely because a representation allows it. Unsupported definitions, pronunciation, examples, patterns, proficiency labels, domains, or relationships remain unresolved.

> **Do not optimize for filled records. Optimize for trustworthy knowledge.**

## Learning-State Boundary

The knowledge model describes stable knowledge. Learner mastery, attempts, confidence, retention, review status, and progress belong to the learner layer and must not be embedded in the knowledge definition.
