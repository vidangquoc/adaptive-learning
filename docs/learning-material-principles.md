# Learning Material Construction Principles

> **Canonical source of truth for constructing structured learning material in the PTNK Adaptive Preparation System.**
>
> This is the project's **single, ultimate rulebook for learning-material construction and its supporting pipeline**. Other documents may describe source acquisition, learner state, competency models, or implementation mechanics, but they must not introduce competing learning-material rules.

---

## 1. Purpose and governing philosophy

The project builds a **knowledge system**, not a collection of vocabulary lists, textbook summaries, or isolated exercises.

The objective is to convert high-quality source material into a structured representation that can support:

- diagnostic challenges;
- targeted instruction;
- practice;
- discrimination;
- transfer;
- delayed retention;
- adaptive review;
- next-best-activity selection.

The governing principle is:

> **Build the smallest trustworthy representation that preserves the useful knowledge and evidence needed for adaptive learning.**

Accuracy takes precedence over extraction volume or field completeness.

---

## 2. Destination C1 & C2 is the backbone

Destination C1 & C2 is the initial backbone from which the project's first broad knowledge and competency universe is constructed.

The goal is **not** to make the learner read or complete the book from page 1 to the end. The goal is to extract and model the knowledge and assessment evidence contained in it so the adaptive system can determine what the learner needs.

"Master Destination" means demonstrated mastery of the relevant extracted knowledge and competencies, including retention and transfer where required—not completion of every page or exercise.

Additional books are expansion sources. They should be introduced selectively when the current knowledge/competency model exposes a concrete need for additional breadth, depth, precision, or transfer.

---

## 3. Challenge-first learning interface

When prior knowledge is plausible, the learner should normally encounter a meaningful challenge before routine instruction.

```text
Challenge
   ↓
Correct → compress / skip / extend
   ↓
Wrong or uncertain
   ↓
Trace the smallest useful gap
   ↓
Targeted learning
   ↓
Different-context retest
```

Therefore:

- do not force textbook-order instruction when a challenge can reveal the actual need;
- reliable success should lead to compression, skipping, greater discrimination, greater complexity, or transfer;
- failure should trigger targeted learning rather than restarting an entire chapter;
- retesting should use sufficiently different contexts when transfer matters;
- challenge difficulty should expose useful gaps without becoming uninformative noise.

The intended learning loop is:

> **Test → fail → discover → learn → beat the challenge.**

Instruction is evidence-driven, not page-driven.

---

## 4. Extract the whole taught knowledge universe

Do **not** extract only words that occur in exercises.

For Destination and other instructional sources, capture the relevant knowledge explicitly taught, explained, modeled, or exemplified, including where present:

- single-word vocabulary;
- multiword vocabulary;
- idioms;
- phrasal verbs;
- collocations;
- fixed and semi-fixed expressions;
- grammar rules and patterns;
- lexical and grammatical contrasts;
- word-formation relationships;
- usage and register information;
- meaning distinctions and restrictions;
- examples and contextual evidence;
- exercises and assessment tasks.

The instructional content forms the knowledge base; exercises are evidence about how that knowledge is tested.

```text
Instructional content ──→ Knowledge Base
                              ↑
Exercises ────────────────────┘
```

A knowledge item should therefore be extracted even when it has not yet appeared in a question.

---

## 5. Preserve lexical distinctions

Do not flatten all lexical material into a single `word` category.

At minimum distinguish:

```text
word
multiword expression
idiom
phrasal verb
collocation
fixed expression
word-formation relation
```

A surface form may participate in multiple relationships. Preserve those relationships rather than forcing an artificial single category.

---

## 6. Knowledge atoms

The canonical unit of structured knowledge is the **knowledge atom**: the smallest useful, independently referenceable piece of knowledge that can be linked to evidence, competencies, and questions.

A knowledge atom may represent:

- a lexical item and a verified sense;
- an idiom and its meaning/usage;
- a phrasal-verb sense and its pattern;
- a collocation;
- a grammar rule or construction;
- a word-formation relationship;
- a contrast between commonly confused forms;
- a usage/register restriction.

A knowledge atom should be granular enough that a failed question can be traced to a useful gap, but not so fragmented that one meaningful rule becomes dozens of artificial records.

Typical fields include:

```text
knowledge_atom_id
source_id
source_location
source_section
atom_type
canonical_form
content
patterns
usage_note
provenance
```

The exact schema may evolve, but provenance and stable identity are mandatory concepts.

---

## 7. Source extraction must be separated from learning design

Never mix source transcription, interpretation, normalization, and adaptive teaching decisions into one uncontrolled operation.

Use layered processing:

```text
SOURCE
  ↓
RAW / EVIDENCE
  ↓
CLEAN / NORMALIZED
  ↓
CURATED KNOWLEDGE
  ↓
KNOWLEDGE ATOMS
  ↓
QUESTIONS / EXERCISES
  ↓
COMPETENCY MAPPING
  ↓
CHALLENGES / LEARNING ACTIVITIES
```

Raw extraction is evidence and should be treated as immutable.

Cleaning and normalization belong in later layers. Never manually rewrite raw source text merely to make it look nicer.

---

## 8. Provenance is mandatory

Every knowledge atom and source-derived question must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve, where applicable:

- source ID;
- source type;
- source quality;
- source title/reference;
- unit/section;
- page or source location;
- exercise/question identifier;
- year and exam section when relevant;
- role/context;
- uncertainty.

Never remove provenance during cleaning, deduplication, normalization, or restructuring.

Keep provenance dimensions separate:

```text
lexical/source evidence → source_id / source_type / source_quality
PTNK relevance          → ptnk_evidence
CEFR evidence           → cefr_status / cefr_source
project lifecycle       → official_status
```

No one field should silently substitute for another.

Source authority and dataset approval are different concepts. A record may be approved for the project's learning system even when its underlying evidence is a verified transcription rather than an official document, provided provenance and uncertainty remain explicit.

---

## 9. Accuracy over completeness

Never fill a field merely because the schema contains it.

If a claim cannot be verified confidently from an appropriate reliable source:

- leave it blank;
- mark it unverified/pending; or
- omit it when the schema permits.

Prefer a smaller trustworthy dataset to a larger dataset containing guesses, fabricated metadata, forced examples, or unsupported claims.

This rule applies especially to definitions, Vietnamese meanings, pronunciation/IPA, examples, collocations, patterns, CEFR, domain, provenance, and source quality.

> **Do not optimize for filled rows. Optimize for trustworthy rows.**

---

## 10. Definitions and meanings

Definitions must be grounded in a reliable lexical source.

Context may determine **which documented sense is intended**, but context alone is not authority for inventing a definition.

Correct workflow:

1. identify the lexical item and intended sense from context;
2. find a reliable source documenting that sense;
3. use or carefully paraphrase the source definition without changing its meaning;
4. retain definition provenance.

Do not infer a new dictionary definition from a sentence, merge unrelated senses, or present an AI-generated definition as source-verified.

Vietnamese learner meanings must represent the verified intended sense accurately. A literal translation is not automatically correct. Use reliable bilingual evidence where appropriate or derive concise Vietnamese wording from a verified English sense without adding unsupported meaning.

If no suitable lexical evidence exists, keep the field pending rather than fabricating it.

---

## 11. Pronunciation

Pronunciation/transcription must never be guessed from spelling, context, intuition, or a generated phonetic attempt.

If the project specifies US IPA, use **US IPA only when independently verified** from a reliable source documenting the actual lexical item and relevant pronunciation variant.

Correct workflow:

1. identify the exact lexical item and relevant pronunciation variant;
2. find a reliable pronunciation source;
3. record or normalize the pronunciation without changing its phonetic content;
4. retain pronunciation provenance.

If no reliable pronunciation source is available, leave pronunciation unverified/pending.

If multiple established pronunciations exist, preserve the relevant variant and its evidence rather than silently choosing one.

---

## 12. Examples

Examples support learning but are not allowed to reduce accuracy.

Preferred evidence order:

1. reliable dictionary/lexical-source examples;
2. reliable corpus or documented natural usage;
3. carefully constructed learner examples based on a verified sense and verified pattern.

Examples should be grammatical, natural, meaningful, reasonably concise, and compatible with the verified intended sense.

A numerical quota is **not** a quality rule. Fewer examples are preferable when additional examples would require guessing, awkward construction, unsupported usage, forced repetition, or an uncertain sense.

Never create examples merely to fill a target count.

---

## 13. Patterns, collocations, and usage

Patterns should contain genuine useful usage information, such as:

- collocations;
- grammatical frames;
- lexical frames;
- natural fixed/semi-fixed combinations;
- important selectional or structural restrictions.

Do not use a pattern field for synonyms, paraphrases, definitions, translations, or arbitrary combinations.

Include a pattern only when it is natural, semantically appropriate, useful for learning, and sufficiently supported by evidence.

A short list of trustworthy patterns is better than a long list of guessed combinations.

Usage notes may record register, grammatical restriction, countability, semantic limitation, or important natural-usage warnings. They should not merely repeat the definition.

---

## 14. Word formation

Word formation is part of the knowledge model, not merely a separate answer list.

A derived form that is useful as an independent lexical item should become a normal knowledge/lexicon entry, while the derivational relationship is preserved explicitly.

Example:

```text
culture → counterculture
```

Do not assume that being a word-formation answer automatically makes an item intrinsically more important.

---

## 15. Domain and specialist context

Domain describes a meaningful subject/topic context when that context adds useful information.

Examples include academic, agriculture, linguistics, social science, and general.

Do not force a specialized domain when the item is broadly transferable. If domain assignment is uncertain, leave it pending rather than guessing.

Domain does not determine CEFR or learner priority.

---

## 16. CEFR and other external metadata

Do not invent CEFR levels.

Do not infer C1/C2 merely because an item looks advanced, appears in a difficult question, or feels difficult to the learner.

Record CEFR only when independently verified from an appropriate reliable source, and preserve the CEFR source separately from lexical provenance and PTNK provenance.

CEFR may apply to a particular sense or use; do not automatically generalize a level to every sense of a headword.

The same evidence discipline applies to other externally sourced metadata.

---

## 17. No intrinsic vocabulary priority

Individual vocabulary items must **not** receive an intrinsic learning-priority score merely because they appeared more often in PTNK papers, appear difficult, or seem useful.

The working principle is:

> **C1/C2 knowledge represented in the selected backbone is legitimate learning material unless evidence shows that it is outside the target scope.**

Adaptive urgency belongs to the learner's current state and task-selection system, not to the lexical item itself.

Therefore the material-construction layer must not encode a `priority` field as an intrinsic property of a word.

---

## 18. PTNK papers: calibration, not curriculum selection

PTNK papers are used primarily to calibrate and validate:

- competency coverage;
- task formats;
- difficulty and discrimination;
- how advanced knowledge is operationalized;
- transfer requirements.

Do not construct the backbone by reverse-engineering a vocabulary list from past-paper frequency.

A C1/C2 item represented in the selected knowledge base remains legitimate learning material whether or not it has appeared in an observed PTNK paper.

PTNK evidence may be attached to a knowledge atom or question when available, but past appearance does not determine intrinsic lexical importance.

---

## 19. Destination exercises are the canonical seed question bank

Exercises already contained in Destination are the initial **canonical seed questions**.

They should be extracted faithfully and retain provenance such as source, unit, section/exercise, source location, question number/identifier, and original task type.

Do not replace source exercises with automatically generated questions.

Generated questions are a second layer for targeted practice, discrimination, transfer, delayed retention, and retesting.

---

## 20. Question ↔ knowledge linkage is mandatory

Each source-derived question should be linked to the knowledge atom(s) it tests whenever the relationship can be defended.

Typical fields include:

```text
question_id
source_id
source_location
exercise_id
question_type
prompt
options
answer
knowledge_atom_ids
competency_id
skill
provenance
```

A question-to-knowledge link must be evidence-based, not inferred merely because the same word appears nearby.

This linkage allows a wrong answer to produce an actionable diagnosis rather than only a score.

---

## 21. Generated material must add instructional value

Generated questions or explanations must exist for a concrete instructional reason, not merely to increase item counts.

Generate follow-up material when it can:

- isolate a knowledge gap;
- test a different mastery dimension;
- distinguish close alternatives;
- increase contextual complexity;
- test transfer;
- verify delayed retention;
- prevent memorization of the source question;
- provide a missing task format required by the competency model.

Generated content must be clearly distinguished from source-derived content.

---

## 22. Knowledge must support multiple mastery dimensions

A knowledge record is not automatically a mastery record.

Where applicable, learning material should support:

- recognition;
- recall;
- meaning precision;
- form and pattern;
- collocation;
- contextual usage;
- discrimination from near alternatives;
- transformation/production;
- transfer;
- delayed retention.

A definition-only representation is useful knowledge data, but it is not sufficient evidence of mastery.

---

## 23. Competency mapping

Knowledge and questions should ultimately be linkable to competencies and, where useful, PTNK skill/task categories.

The mapping should answer:

> **What capability does this knowledge or question help assess?**

Examples include lexical precision, collocation, idiom use, phrasal-verb control, advanced grammar, word formation, reading inference, discourse, error identification, and sentence transformation.

Do not force a competency label when the evidence is insufficient. A pending mapping is better than a false diagnosis.

---

## 24. Deduplication and relationships

Deduplicate only when two records represent the same underlying knowledge item and sense.

Do not collapse items merely because their spellings are similar, one is a component of another expression, their meanings overlap, or they belong to the same word family.

Preserve meaningful relationships such as:

```text
word ↔ expression
word ↔ idiom
word ↔ phrasal verb
word ↔ collocation
base form ↔ derived form
knowledge atom ↔ question
knowledge atom ↔ competency
```

False deduplication is more damaging than retaining a small amount of controlled redundancy.

---

## 25. Quality gates before canonical use

Before knowledge or questions enter the canonical learning dataset, verify:

1. provenance is known;
2. extraction is faithful enough for the intended use;
3. lexical/grammatical type is correctly classified;
4. meanings and pronunciation are evidence-backed where present;
5. examples and patterns are natural and defensible;
6. CEFR and other external metadata are independently sourced;
7. question-to-knowledge links are defensible;
8. duplicates and false splits are controlled;
9. generated material is clearly distinguished from source material;
10. uncertainty is preserved rather than silently upgraded.

Accuracy takes precedence over extraction volume.

---

## 26. Copyright and source-use boundaries

Copyrighted books may be used as source material for the private learning system subject to applicable rights and repository constraints, but the repository should not redistribute copyrighted books or wholesale copied content without permission.

Prefer preserving:

- canonical source URL/reference;
- acquisition script where appropriate;
- retrieval timestamp;
- checksum;
- license/usage notes;
- extraction notes;
- provenance metadata.

Generated original material should be clearly distinguished from source-derived material.

---

# Pipeline and Data-Governance Rules

## 27. Canonical pipeline

All learning-material construction should follow this conceptual pipeline:

```text
External sources
      ↓
RAW / EVIDENCE
      ↓
CLEAN / NORMALIZED
      ↓
CURATED KNOWLEDGE
      ↓
KNOWLEDGE BASE
 ├── knowledge atoms
 └── source exercises / questions
       ↓
Question ↔ Knowledge
       ↓
Competency / Challenge
```

A more detailed implementation pipeline is:

```text
SOURCE
  ↓
RAW / EVIDENCE
  ↓
CLEAN / NORMALIZED
  ↓
CURATED KNOWLEDGE
  ↓
KNOWLEDGE ATOMS
  ↓
QUESTIONS / EXERCISES
  ↓
COMPETENCY MAPPING
  ↓
CHALLENGES / LEARNING ACTIVITIES
```

The layers are conceptually distinct even when implementation combines some processing steps.

---

## 28. Raw / Evidence layer

Raw records represent what was obtained from a source with minimal transformation.

Examples include:

- instructional book material;
- PTNK exam documents;
- verified transcriptions;
- answer keys;
- dictionary evidence;
- corpus evidence;
- English Profile / EVP evidence.

Raw data should preserve source identity, location, original text where applicable, context, source quality, and uncertainty.

Raw records must not be rewritten merely to fit a final learner-facing schema.

For extracted PDFs and similar sources:

- preserve the original source file when legally and operationally appropriate;
- preserve raw text extraction separately;
- treat raw extraction as immutable evidence;
- perform encoding cleanup, structural normalization, and parsing in later layers;
- never manually edit raw text just to make it look nicer.

---

## 29. Clean / Normalized layer

Cleaning and normalization are separate from raw evidence.

Typical implementation work includes:

- encoding cleanup;
- structural normalization;
- whitespace and line normalization;
- canonicalization;
- controlled deduplication;
- segmentation into units/sections/exercises;
- normalization of machine-readable representations.

The raw layer remains the evidence baseline and must remain recoverable.

Normalization must not destroy information needed to reconstruct or audit the source.

---

## 30. Curated Knowledge and Knowledge Base

Curated knowledge is derived from raw/evidence only after the evidence requirements in this document have been satisfied.

The knowledge base may contain lexical, grammatical, word-formation, usage, and other knowledge atoms, together with provenance and relationships.

Destination exercises are retained as canonical seed questions and linked to the knowledge atoms they test.

A curated record is not merely a cleaned record: it is an evidence-backed interpretation suitable for the learning system.

---

## 31. Source extraction, acquisition, and caching

When external source material is acquired for the project, preserve enough information to make the acquisition reproducible and auditable.

Where legally permissible, cache raw source data so future aggregation or modeling changes do not require unnecessary re-downloading.

For copyrighted or restricted sources, preserve metadata such as:

- canonical URL;
- acquisition/retrieval timestamp;
- checksum;
- license or usage status;
- acquisition script or method;
- extraction notes;
- local/repository handling restrictions.

Do not treat a generated CSV or normalized dataset as a substitute for source provenance.

---

## 32. Structural extraction rules

When parsing instructional books or similar structured sources:

1. extract the source to an immutable raw layer first;
2. validate major structural boundaries before mass parsing;
3. distinguish real section boundaries from repeated page headers/footers;
4. preserve unit, section, exercise, and question locations;
5. parse exercises independently from knowledge extraction where possible;
6. retain source identifiers throughout every downstream layer.

For example, a PDF-to-text workflow may be:

```text
PDF
 ↓
pdftotext -layout
 ↓
RAW TXT (immutable)
 ↓
cleaning / normalization
 ↓
Unit / Section parser
 ↓
Exercise parser
 ↓
Knowledge atoms
 ↓
Question bank
```

Parser safety requirements:

- fail rather than silently overwrite existing parsed outputs;
- validate expected unit counts and boundaries;
- preserve the raw source as the recovery point;
- make parsing deterministic where practical.

---

## 33. Canonical data shapes

The exact database schema may evolve, but the following concepts should remain stable.

### Knowledge atom

```text
knowledge_atom_id
source_id
source_location
source_section
atom_type
canonical_form
content
meaning/function
pronunciation
register
grammar_behavior
patterns
collocations
usage_note
examples
word_formation
domain
provenance
```

Not every field is mandatory for every atom. Evidence rules determine whether a field is populated.

### Source-derived question

```text
question_id
source_id
source_location
exercise_id
question_type
prompt
options
answer
knowledge_atom_ids
competency_id
skill
difficulty
provenance
license_note
```

Questions must remain distinguishable as source-derived versus generated.

---

## 34. What this file does not control

This file is the single source of truth for **learning-material construction** and the pipeline rules that directly support it.

It does not replace specialized specifications for:

- learner learning state;
- review scheduling algorithms;
- competency definitions;
- application/runtime behavior;
- source-specific acquisition instructions.

Those documents may define implementation details, but if they make a claim about how learning material itself should be constructed, classified, evidenced, linked, or promoted, this document takes precedence.

---

## 35. Non-negotiable rules

1. **Build a knowledge system, not a vocabulary list.**
2. **Destination C1 & C2 is the initial backbone.**
3. **Challenge first when prior knowledge is plausible.**
4. **Extract the whole taught knowledge universe, not only exercise answers.**
5. **Keep raw evidence separate from normalization and learning design.**
6. **Preserve provenance.**
7. **Accuracy beats completeness.**
8. **Never invent definitions, pronunciation, examples, patterns, CEFR, provenance, or source quality.**
9. **Preserve distinctions among words, expressions, idioms, phrasal verbs, collocations, grammar, and word formation.**
10. **Do not assign intrinsic vocabulary priority.**
11. **Use PTNK papers for calibration and validation, not for constructing a frequency-based vocabulary curriculum.**
12. **Use Destination exercises as canonical seed questions.**
13. **Link questions to the knowledge they actually test.**
14. **Generate new material only when it adds measurable instructional value.**
15. **Do not confuse source authority, PTNK relevance, CEFR evidence, and project approval status.**
16. **Preserve uncertainty instead of silently upgrading weak evidence.**
17. **Keep generated content distinguishable from source-derived content.**
18. **Adaptive task urgency belongs to learner state/task selection, not to intrinsic lexical value.**
19. **Never allow pipeline implementation documents to silently create competing learning-material rules.**
20. **When in doubt, prefer a smaller trustworthy representation over a larger speculative one.**
