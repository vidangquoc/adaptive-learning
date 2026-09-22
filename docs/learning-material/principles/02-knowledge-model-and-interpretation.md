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

A knowledge atom is an independently useful, source-grounded unit of knowledge.

Knowledge atoms are flat and independent by default. If several meanings, senses, constructions, patterns, or usages are directly tested or practised as distinct knowledge points in the source, they should be represented as separate atoms.

One lexical sense is one atom by default. For other knowledge distinctions, direct source-level testing/practice is the trigger for separate atom representation.

Do not impose hierarchies such as:

```text
word → sense → pattern → expression
grammar heading → grammar use → example
```

Atom-to-atom relationships are not persisted because they are not used by the Adaptive Learning system.

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

Context may support inference of attributes such as part of speech, intended sense, usage, or meaning.

Use this hierarchy:

```text
explicit source statement
        ↓
strong contextual inference
        ↓
weak / ambiguous inference
        ↓
null / pending / review-needed
```

Inferred attributes must remain distinguishable from source-stated attributes and retain appropriate evidence/provenance. A sentence can identify an intended sense without being sufficient authority for inventing a dictionary definition.

## Atom Boundaries

One source span does not necessarily equal one atom:

```text
one evidence span → multiple atoms
multiple evidence spans → one atom
one evidence span → no atom
```

Split when the source supports a knowledge distinction and the corresponding knowledge point is directly tested or practised as a distinct target.

Merge evidence only when it supports the same underlying knowledge item and the same sense/use.

Do not merge merely because forms are identical or similar, meanings overlap, items share a word family, or one expression contains another.

False deduplication is more damaging than controlled redundancy.

## Linguistic and Semantic Reasoning

For lexical knowledge, consider sense, lexicalization, idiomaticity, syntactic behavior, patterns, derivation, register, semantic contrasts, and restrictions where the source supports them.

For grammar, consider form, meaning, function, discourse context, constraints, and contrasts. Do not create a grammar atom merely because a textbook heading exists. Represent a grammatical knowledge point as a separate atom when the source directly tests or practises that point as a distinct target.

## Accuracy over Completeness

Never fill a field merely because a representation allows it. Unsupported definitions, pronunciation, examples, patterns, proficiency labels, domains, or relationships remain unresolved.

> **Do not optimize for filled records. Optimize for trustworthy knowledge.**

## Learning-State Boundary

The knowledge model describes stable knowledge. Learner mastery, attempts, confidence, retention, review status, and progress belong to the learner layer and must not be embedded in the knowledge definition.
