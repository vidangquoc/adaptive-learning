# Knowledge Model and Interpretation

> This document defines cross-domain principles for interpreting source evidence into useful knowledge distinctions. The canonical Knowledge Atom model is owned by `docs/knowledge/`: `overall.md` defines the conceptual model, `atom-structure.md` defines the formal structure, `atom-types.md` defines the taxonomy, and `atom-pipeline.md` defines discovery and officialization.

## Preserve Knowledge Distinctions

Do not flatten different kinds of knowledge into a generic record. Preserve distinctions whenever they matter for meaning, usage, learning, or assessment.

Relevant distinctions may include:

```text
lexical sense
multiword expression
idiom
phrasal verb
collocation
grammatical construction / rule
lexical or grammatical contrast
word formation
usage restriction
discourse / pragmatic function
```

The canonical Knowledge Atom taxonomy determines which categories can be represented as Atom types. This document focuses on the reasoning process, not on redefining that taxonomy.

## Interpretation versus Representation

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

## Atom Boundaries

One source span does not necessarily equal one atom:

```text
one evidence span → multiple atoms
multiple evidence spans → one atom
one evidence span → no atom
```

Use the canonical Knowledge Atom admission and splitting rules rather than redefining them here. In particular, admission criteria and vocabulary/grammar-specific rules belong to the Knowledge documentation.

When splitting or merging evidence, preserve independently meaningful knowledge distinctions and avoid false deduplication. Do not merge merely because forms are similar, meanings overlap, items share a word family, or one expression contains another.

## Accuracy over Completeness

Never fill a field merely because a representation allows it. Unsupported definitions, pronunciation, examples, patterns, proficiency labels, domains, or relationships remain unresolved.

> **Do not optimize for filled records. Optimize for trustworthy knowledge.**

The formal Atom structure, field semantics, taxonomy, provenance representation, and Candidate/Official lifecycle are canonical elsewhere and should not be redefined in this document.

## Learning-State Boundary

The knowledge model describes stable knowledge. Learner mastery, attempts, confidence, retention, review status, and progress belong to the learner layer and must not be embedded in the knowledge definition.
