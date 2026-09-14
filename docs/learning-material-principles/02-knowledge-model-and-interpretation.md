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

Parsing, interpretation, normalization, and learning design are separate operations.

A parser is an **evidence-discovery tool**, not a knowledge-authoring tool. A pattern match must never silently become a canonical atom.

```text
SOURCE
  ↓
RAW / STRUCTURAL EVIDENCE
  ↓
EVIDENCE CANDIDATES
  ↓
LINGUISTIC / SEMANTIC ANALYSIS
  ↓
KNOWLEDGE-ATOM CANDIDATES
  ↓
VALIDATION / QUALITY GATES
  ↓
VERIFIED KNOWLEDGE ATOMS
```

Parser output count must never be equated with knowledge-atom count. One evidence span may produce multiple candidates, multiple spans may support one atom, or an evidence span may produce no atom.

## Lexical and Grammatical Interpretation

Words, multiword expressions, phrasal verbs, idioms, collocations, word formation, and grammar require linguistic/semantic reasoning.

Consider sense distinctions, lexicalization, idiomaticity, syntactic behavior, patterns, derivational relationships, discourse function, constraints, and contrasts where relevant.

Do not create grammar atoms merely by copying textbook headings.

## Context-Grounded Inference

The reasoning layer may infer attributes such as **part of speech, intended sense, usage, or meaning** from sufficiently informative source context.

Inferred attributes must remain distinguishable from directly source-stated attributes and must carry appropriate confidence/provenance.

> **If context provides sufficient evidence, infer the attribute and record the inference. If context does not provide sufficient evidence, leave the field null/pending rather than guessing.**

Use this evidence hierarchy:

```text
explicit source statement
        ↓
strong contextual inference
        ↓
weak / ambiguous inference → leave null or review-needed
```

A field being present in the schema is never a reason to fill it.

Context may identify which documented sense is intended, but a sentence alone must not be treated as authority for inventing a dictionary definition.

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
