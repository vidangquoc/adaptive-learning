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

Knowledge atoms are **flat and independent by default**. If several meanings, senses, constructions, patterns, or usages can be independently learned, assessed, rejected, approved, or tracked, they should be represented as separate atoms.

In particular, **one lexical sense = one knowledge atom by default**. A single spelling may therefore produce multiple atoms when the source distinguishes multiple senses. Each sense atom must have its own evidence and review decision so that one sense can be approved while another is rejected or held.

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

## Evidence Must Be First-Class

Every knowledge-atom proposal must carry enough evidence to allow a reviewer to reconstruct **why the atom exists and which sense is being proposed**.

At minimum, preserve:

- source identifier;
- exact or sufficiently precise source location;
- source section/subsection;
- the source text/span containing the relevant item;
- the definition or explanation supporting the sense, when available;
- a source example sentence containing the item, when available;
- any additional context needed to distinguish the sense;
- whether each claim is source-stated or inferred.

If an example sentence exists in the source, prefer that sentence over an invented example for the evidence layer. A generated example may be added later as enrichment, but it must never replace the original evidence.

When the source provides a definition but no example, record the definition evidence and leave the source-example field null. When neither is available, do not fabricate evidence.

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

For polysemous lexical items, split **each independently documented sense into its own atom**. This is the default because each sense may have different evidence, examples, patterns, assessment value, and human-review outcome.

Merge evidence only when it supports the same underlying knowledge item **and the same sense**.

Do not merge merely because spellings are identical, meanings overlap, items share a word family, or one expression contains another.

False deduplication is more damaging than controlled redundancy.

## Accuracy Over Completeness

Never fill a field merely because the schema contains it. If a claim cannot be verified from an appropriate reliable source, leave it blank, mark it unverified/pending, or omit it when the schema permits.

> **Do not optimize for filled rows. Optimize for trustworthy rows.**

## Definitions, Pronunciation, Examples, Patterns, and Word Formation

Definitions and meanings must be grounded in reliable lexical evidence. Pronunciation must never be guessed. Examples must be grammatical, natural, meaningful, and compatible with the verified sense.

When the source contains a sentence or example containing the target item, preserve it as source evidence and associate it with the specific atom/sense it supports. Do not replace it with a generic invented sentence during extraction.

Generated examples may be added later as enrichment and must be explicitly marked as generated rather than source evidence.

Patterns must represent genuine usage information rather than synonyms, paraphrases, translations, or arbitrary combinations.

A derived form that is useful as an independent lexical item may become its own atom, while the derivational relationship is preserved explicitly.

## Deduplication and Relationships

Deduplicate only when records represent the same underlying knowledge item and the same sense.

Do not collapse records merely because spellings are similar, meanings overlap, one is a component of another expression, or they belong to the same word family.

False deduplication is more damaging than controlled redundancy.
