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

## Candidate Knowledge Atom Representation

Candidate knowledge is the reviewable intermediate representation between source-grounded analysis and official promoted knowledge.

The candidate contract is defined separately in:

```text
schemas/knowledge-atom-candidate.schema.json
```

The candidate must preserve **all candidate fields even when some values are not yet established**. A missing value is represented as blank, `null`, or an empty array according to the field type. Fields must not be removed merely because no reliable value is currently available.

The candidate contract includes:

```text
atom_type
canonical_form
part_of_speech
sense
definition
mother_says
patterns
usage_note
source_status
source_location
evidence
source_example
context_status
review_status
```

`mother_says`, `patterns`, and `usage_note` are therefore part of the candidate proposal and must be visible during human review. They are not fields that should first be invented during officialization.

### Candidate interpretation rules

- `definition` preserves a source-provided definition verbatim when available; do not paraphrase it merely to make the candidate look complete.
- `mother_says` is the learner-facing Vietnamese meaning of the proposed sense. If explanatory wording is needed beyond the concise equivalent, put it in parentheses immediately after the equivalent(s). Never guess it merely because the field exists.
- `mother_says` is an interpretation for the learner; it is **not source evidence** and must not be represented as though it were a source quote or source-stated definition.
- `patterns` records genuine usage patterns that are verified or strongly supported by source context. It must not contain synonyms, translations, arbitrary word combinations, or patterns invented only to populate the field. If no reliable pattern is established, keep `[]`.
- `usage_note` records verified or strongly context-supported usage restrictions, register, nuance, contrasts, or other important usage information. If none is established, keep it blank/null.
- `source_status`, `context_status`, and `review_status` are separate concerns. `source_status` describes the quality/availability of source evidence; `context_status` describes the strength of contextual interpretation; `review_status` records the human decision. Strong source/context status does not imply `APPROVED`.
- `patterns` and `usage_note` should be proposed before human review whenever the evidence supports them, so the reviewer can approve, reject, or hold the interpretation explicitly.
- Officialization must **not silently add new semantic interpretation** to an approved candidate. Promotion primarily copies the approved candidate into the official representation, applying only the explicit official-schema transformation and separately authorized enrichment.
- If a pattern or usage note is not sufficiently supported at candidacy time, it remains unresolved rather than being automatically inferred during promotion.

This makes candidacy a complete reviewable proposal rather than a minimal placeholder whose meaning changes during promotion.

## Official Knowledge Atom Representation

Official knowledge is the canonical promoted layer consumed downstream by competency, diagnostic, challenge, and adaptive-learning systems.

The official atom contract is defined separately in:

```text
schemas/official-knowledge-atom.schema.json
```

The current canonical fields, in order, are:

| Field | Role |
|---|---|
| `id` | Positional identifier in the official knowledge base. It identifies the atom's position and must not encode the lexical item or sense. |
| `knowledge_domain` | High-level learning domain: `grammar` or `vocabulary`. It answers which broad learning domain the atom belongs to. |
| `atom_type` | Type of knowledge represented by the atom. It answers what kind of knowledge the atom is. |
| `canonical_form` | Canonical lexical/constructional form represented by the atom. |
| `pronunciation` | Verified pronunciation, preferably in IPA. Pronunciation must not be guessed. |
| `part_of_speech` | Part of speech when applicable and supported by the source. |
| `definition` | Source-provided definition, preserved verbatim when the source supplies one. Do not paraphrase it during promotion. |
| `mother_says` | Meaning in the learner's mother language. In the current project this means the Vietnamese meaning of the verified atom; it is **not** a usage explanation, native-speaker intuition note, or paraphrase of `definition`. |
| `examples` | One or more source or explicitly marked enriched example sentences supporting the atom. |
| `patterns` | Verified usage patterns genuinely associated with the atom. |
| `usage_note` | Verified usage restriction, register, nuance, contrast, or other important usage note. |
| `candidate_ref` | Single pointer to the reviewed candidate record from which the official atom was promoted. |

For vocabulary atoms, `mother_says` should answer **“Nghĩa tiếng Việt của từ/cụm này là gì?”** It should contain the concise Vietnamese equivalent(s) of the verified sense. If additional wording is needed to explain or clarify the meaning rather than provide another equivalent, put that explanation in parentheses `()` immediately after the equivalent(s). Do not present explanatory wording as if it were a synonym. For example:

```text
suy ngẫm (suy nghĩ rất kỹ về điều gì đó trong một thời gian dài)
```

Information about register, broader usage restrictions, contrasts, or other usage-specific notes belongs in `usage_note` instead.

Fields such as `pronunciation`, `mother_says`, `patterns`, and `usage_note` remain present in the representation even when reliable evidence is not available; use a blank value or empty array as appropriate. Do not fill them by guessing merely because they exist in the schema.

Official atoms intentionally do **not** carry candidate-review metadata, source-analysis metadata, evidence arrays, confidence, promotion status, or learner-state fields. Those concerns remain in their corresponding layers. `candidate_ref` is the explicit lineage pointer back to the reviewed candidate.

Official atom IDs use the canonical component separator `__` rather than `/`, for example:

```text
<book>__<unit>__<section>__<position>
```

The position may change only through an intentional knowledge-base reorganization; the ID must not be designed to encode lexical meaning or sense.

The field contract is a knowledge representation contract, not a learning-priority model. No intrinsic priority belongs in an official atom.

## Evidence Extraction Is Not Knowledge Interpretation

Parsing, evidence discovery, contextual interpretation, normalization, and learning design are separate operations.

A parser is an **evidence-location tool**, not a knowledge-authoring tool. Its output is a set of source spans or evidence signals that require contextual analysis. A pattern match must never silently become a canonical atom.

The system should not require an artificial permanent candidate layer when it adds no value. A parser may create temporary candidates internally, but **any candidate that enters human review must be materialized as a persistent record under `data/candidates/`**. Not every temporary parser candidate needs to be persisted.

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
PERSIST REVIEWABLE CANDIDATE
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

If an example sentence exists in the source, prefer that sentence over an invented example for the evidence layer. A generated example may be added later as enrichment, but it must never replace the original evidence or be presented as source evidence.

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

Generated examples may be added later as enrichment and must be explicitly marked as generated rather than source evidence. Enrichment may add examples, verified patterns, competency mappings, or assessment mappings when those additions have their own provenance. Enrichment must not silently change the core semantic identity of an approved candidate; if the identity, sense, definition, or other core interpretation changes, it must return to candidacy/review rather than being patched into official knowledge.

Patterns must represent genuine usage information rather than synonyms, paraphrases, translations, or arbitrary combinations.

A derived form that is useful as an independent lexical item may become its own atom, while the derivational relationship is preserved explicitly.

## Deduplication and Relationships

Deduplicate only when records represent the same underlying knowledge item and the same sense.

Do not collapse records merely because spellings are similar, meanings overlap, one is a component of another expression, or they belong to the same word family.

False deduplication is more damaging than controlled redundancy.
