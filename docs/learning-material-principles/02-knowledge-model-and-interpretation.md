# Knowledge Model and Interpretation

## Preserve Knowledge Distinctions

Do not flatten different kinds of knowledge into a single generic `word` record.

At minimum distinguish:

```text
word
multiword expression
idiom
phrasal verb
collocation
fixed expression
grammar rule / construction
lexical or grammatical contrast
word-formation relation
usage restriction
```

Preserve distinctions whenever they matter for meaning, usage, learning, or assessment.

## Flat Knowledge-Atom Ontology

A **knowledge atom** is the smallest useful, independently referenceable piece of knowledge that can be linked to evidence, competencies, and questions.

Knowledge atoms are **flat and independent by default**. If several meanings, senses, constructions, patterns, or usages can be independently learned, assessed, or tracked, they may be represented as separate atoms.

Do not impose a mandatory hierarchy such as:

```text
word → sense → pattern → expression
```

Use explicit typed relationships only when they provide real learning, assessment, or querying value. A relationship is not ownership, ancestry, or inherited mastery.

Learner mastery belongs to learner-state data, not to the static atom.

## Evidence Extraction Is Not Knowledge Interpretation

Parsing, evidence discovery, contextual interpretation, normalization, and learning design are separate operations.

A parser is an **evidence-location tool**, not a knowledge-authoring tool. Its output is a set of source spans or evidence signals that require contextual analysis. A pattern match must never silently become a canonical atom.

The system should not require an artificial permanent candidate layer when it adds no value. A parser may create temporary candidates internally, but the substantive intermediate artifact is the context-grounded knowledge-atom proposal.

```text
SOURCE
  ↓
RAW / STRUCTURAL EVIDENCE
  ↓
EVIDENCE LOCATION
  ↓
CONTEXTUAL LINGUISTIC / SEMANTIC ANALYSIS
  ↓
KNOWLEDGE-ATOM PROPOSAL
  ↓
VALIDATION / QUALITY GATES
  ↓
HUMAN REVIEW
  ↓
VERIFIED KNOWLEDGE ATOM
```

Parser output count must never be equated with knowledge-atom count. One evidence span may produce multiple proposals, multiple spans may support one atom, or an evidence span may produce no atom.

## Source-Order and Context Are Part of Interpretation

Knowledge extraction must preserve the instructional order of the source and inspect the surrounding lesson content before making semantic or grammatical judgments.

Where available, analysis should consider:

- section and subsection headings;
- lexical table rows or word boxes;
- definitions and explanations;
- example sentences;
- usage notes and patterns;
- contrast sets;
- task instructions and framing;
- relevant nearby source spans.

Do not reduce a candidate to an isolated token when surrounding content may determine its part of speech, intended sense, usage, or atom type.

## Lexical and Grammatical Interpretation

Words, multiword expressions, phrasal verbs, idioms, collocations, word formation, and grammar require linguistic/semantic reasoning.

Consider sense distinctions, lexicalization, idiomaticity, syntactic behavior, patterns, derivational relationships, discourse function, constraints, and contrasts where relevant.

Do not create grammar atoms merely by copying textbook headings.

## Context-Grounded Inference

The reasoning layer may infer attributes such as **part of speech, intended sense, usage, or meaning** from sufficiently informative source context.

Inferred attributes must remain distinguishable from directly source-stated attributes and must carry appropriate confidence/provenance.

Use this evidence hierarchy:

```text
explicit source statement
        ↓
strong contextual inference
        ↓
weak / ambiguous inference
        ↓
null / pending / review-needed
```

> **If context provides sufficient evidence, infer the attribute and record the inference. If context does not provide sufficient evidence, leave the field null/pending rather than guessing.**

A field being present in the schema is never a reason to fill it.

Context may identify which documented sense is intended, but a sentence alone must not be treated as authority for inventing a dictionary definition.

## Atom Splitting and Evidence Aggregation

One source span does not necessarily represent one knowledge atom.

Analysis may determine that:

```text
one evidence span → multiple independent atoms
multiple evidence spans → one atom with multiple evidence links
one evidence span → no atom
```

Split when distinctions are independently useful for learning, assessment, querying, or learner-state tracking. Merge evidence only when it supports the same underlying knowledge item and sense.

Do not merge merely because spellings are similar, meanings overlap, items share a word family, or one expression contains another.

False deduplication is more damaging than controlled redundancy.

## Accuracy Over Completeness

Never fill a field merely because the schema contains it. If a claim cannot be verified from an appropriate reliable source, leave it blank, mark it unverified/pending, or omit it when the schema permits.

> **Do not optimize for filled rows. Optimize for trustworthy rows.**

## Definitions, Pronunciation, Examples, Patterns, and Word Formation

Definitions and meanings must be grounded in reliable lexical evidence. Pronunciation must never be guessed. Examples must be grammatical, natural, meaningful, and compatible with the verified sense. Patterns must represent genuine usage information rather than synonyms, paraphrases, translations, or arbitrary combinations.

A derived form that is useful as an independent lexical item may become its own atom, while the derivational relationship is preserved explicitly.

## Deduplication and Relationships

Deduplicate only when records represent the same underlying knowledge item and sense.

Do not collapse records merely because spellings are similar, meanings overlap, one is a component of another expression, or they belong to the same word family.

False deduplication is more damaging than controlled redundancy.
