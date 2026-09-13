# PTNK Advanced English Dataset — Data Collection Rules

> Version: v0.5
> Status: Working specification / source of truth
> Project: PTNK
> Purpose: Define how lexical data is collected, evidenced, normalized, curated, and promoted into the official PTNK learning dataset.

---

# 0. Accuracy over completeness

**Accuracy is more important than completeness.**

The project must never fill a field merely because the schema expects a value. If a claim cannot be verified confidently from an appropriate reliable source, leave it blank, mark it as unverified/pending, or omit it where the schema permits.

This rule applies especially to:

- definitions and meanings
- Vietnamese meanings
- pronunciation / IPA
- examples
- collocations and patterns
- CEFR
- domain
- priority
- provenance and source quality

A smaller dataset with trustworthy information is preferable to a larger dataset containing guesses, fabricated metadata, forced examples, or unsupported claims.

> **Do not optimize for filled rows. Optimize for trustworthy rows.**

---

# 1. Purpose

This document is the **source of truth** for collecting and maintaining the PTNK Advanced English Dataset.

The dataset supports preparation for the English specialized entrance examination of Trường Phổ thông Năng khiếu (PTNK), ĐHQG-HCM.

The dataset is:

- PTNK-oriented
- evidence-based
- focused on advanced general English and useful topic vocabulary
- designed for vocabulary learning and spaced repetition
- suitable for the project's Google Sheets flashcard system

It is **not**:

- a generic English dictionary
- a generic C1/C2 list
- an AI training dataset
- a list of every difficult English word
- a collection based only on subjective difficulty

> **Core principle: collect what is useful for PTNK, not simply what is difficult.**

---

# 2. Data Lifecycle: Raw → Curated → Official

PTNK data must distinguish between **source data** and **official learning data**.

The project uses three logical layers:

```text
External sources
      ↓
RAW / EVIDENCE
      ↓  extract + preserve provenance
CURATED / NORMALIZED
      ↓  review + validate + approve
OFFICIAL LEXICON
      ↓
P1 / P2 / P3 / P4 learning views
```

## 2.1 Raw / Evidence layer

Raw data is the material captured from an external source with minimal transformation.

Examples:

- official exam material
- verified exam transcription
- published answer key
- dictionary entry
- corpus evidence
- English Profile / EVP evidence

Raw data should preserve the original wording, source identity, location, and uncertainty.

Do **not** silently rewrite raw evidence to make it look cleaner.

## 2.2 Curated / Normalized layer

Curated data is produced from raw evidence after normalization and editorial review.

Typical transformations include:

- choosing a canonical lexical form
- assigning `word_type`
- selecting the relevant sense
- writing concise English/Vietnamese meanings **only from reliable lexical evidence**
- adding US IPA **only when verified**
- adding learner examples when reliable evidence is sufficient
- recording genuine patterns
- assigning `domain`
- evaluating PTNK priority
- linking word-formation relationships

Curated data may improve presentation, but it must retain a link to its source evidence.

## 2.3 Official Lexicon layer

The Official Lexicon is the **approved learning dataset** used by the PTNK learning system.

An item should enter the Official Lexicon only after the required fields and provenance have been checked.

Official does **not** mean that every field came from an official PTNK source. It means the item has been reviewed and approved as part of the project's authoritative learning dataset.

A transcription can therefore be a valid source for an official curated item, provided the source quality and uncertainty are explicitly recorded.

---

# 3. Source vs Evidence vs Official Status

These concepts must not be conflated.

| Concept | Question answered | Example |
|---|---|---|
| `source_id` | Where did this evidence come from? | `ptnk-2026-q37` |
| `source_type` | What kind of source is it? | `ptnk_exam`, `transcription`, `dictionary`, `corpus` |
| `source_quality` | How trustworthy/verified is the source? | `official_exam`, `transcription`, `verified` |
| `ptnk_evidence` | Why is this item relevant to PTNK? | `2026 · Reading · Q37 · correct_answer` |
| `cefr_source` | Where was CEFR information verified? | `English Profile` |
| official status | Has the curated item been approved for the Official Lexicon? | `official` |

A source is not automatically official learning data.

A PTNK transcription may be raw evidence. After review, a normalized lexical item derived from that transcription may become official dataset content.

---

# 4. Provenance Is Mandatory

Every item must retain enough provenance to answer:

> **Why is this item here, and where did it come from?**

At minimum, preserve when available:

- source ID
- source type
- source quality
- PTNK year
- section
- question number
- exam role/context
- source note or location

Never remove provenance during cleaning, deduplication, or restructuring.

If evidence is uncertain, preserve the uncertainty instead of upgrading the claim.

---

# 5. PTNK Relevance

An item should have a clear reason for inclusion.

Strong reasons include:

1. It appeared in an actual PTNK specialized-English examination.
2. It belongs to a recurring lexical pattern found in PTNK exams.
3. It is important advanced general English relevant to PTNK.
4. It is a useful collocation, idiom, fixed expression, phrasal verb, or word family connected to target vocabulary.
5. It is supported by reliable lexical/corpus evidence and has clear PTNK learning value.

Do not include an item merely because it looks advanced, is unfamiliar, is rare, or is labelled C1/C2 somewhere.

---

# 6. Lexical Items

The main Lexicon may contain:

- single words
- multiword expressions
- collocations
- idioms
- phrasal verbs
- useful fixed phrases
- selected word-formation results

All are lexical items in one unified Lexicon.

Examples:

- `errand` → `n`
- `run errands` → `exp`
- `stick to one's guns` → `idi`
- `live up to` → `exp`

An expression is not redundant merely because one of its component words is already present.

---

# 7. Word Type

Use only these standard codes unless the project explicitly changes the specification:

| Code | Meaning |
|---|---|
| `n` | noun |
| `v` | verb |
| `adj` | adjective |
| `adv` | adverb |
| `exp` | expression / fixed phrase / collocation / phrasal verb |
| `idi` | idiom |

Keep the taxonomy simple.

---

# 8. Lexicon Schema

The current learner-facing Lexicon schema is:

```text
id
word
word_type
pronunciation
meaning_en
meaning_vi
examples
patterns
usage_note
domain
priority
word_formation
ptnk_evidence
source_id
source_type
source_quality
official_status
cefr_status
cefr_source
```

### Field roles

- `id` — stable unique identifier.
- `word` — canonical lexical item.
- `word_type` — lexical category using the standard codes.
- `pronunciation` — US IPA **only when independently verified**.
- `meaning_en` — concise learner-friendly English definition grounded in a reliable lexical source.
- `meaning_vi` — concise Vietnamese meaning for the intended sense, grounded in reliable lexical evidence.
- `examples` — short natural examples when sufficient reliable evidence exists; 3–5 is preferred, but 3 is **not** a hard requirement.
- `patterns` — genuine useful collocations/grammatical or lexical patterns only.
- `usage_note` — optional usage/register/grammar warning.
- `domain` — subject/topic context; use `general` when broadly transferable and justified.
- `priority` — PTNK learning value: P1/P2/P3/P4.
- `word_formation` — derivational/family relationship when relevant.
- `ptnk_evidence` — specific PTNK evidence and role/context.
- `source_id` — identifier for the underlying source/evidence record.
- `source_type` — nature of the source.
- `source_quality` — honest verification/quality label.
- `official_status` — lifecycle status of the curated item.
- `cefr_status` — verified CEFR information only; otherwise `not_verified`.
- `cefr_source` — source used to verify the CEFR information.

---

# 9. Raw Data Schema

Raw records may use a source-specific schema. They do **not** have to match the Official Lexicon schema.

A raw record should preserve, where applicable:

```text
source_id
source_type
source_title
source_url_or_reference
raw_text
year
section
question
role
source_quality
source_note
```

Raw data should be as close as practical to the source material.

Do not overwrite raw records with normalized wording.

---

# 10. Curated Data Rules

Curated records are normalized from one or more raw/evidence records.

Normalization may include:

- canonicalizing the lexical item
- choosing the relevant sense
- standardizing word type
- translating the intended sense **from reliable lexical evidence**
- adding verified pronunciation
- adding learner examples only when evidence is sufficient
- identifying genuine patterns
- assigning domain and priority only when defensible

Every curated record must retain `source_id` and provenance.

If a field cannot be verified, leave it blank or mark it as unverified according to the field's rules. Do not fabricate data to make the row look complete.

---

# 11. Official Status

`official_status` describes the dataset lifecycle, not source authority.

Recommended values:

- `raw` — source material, not curated.
- `curated` — normalized and reviewed, but not yet approved as official learning content.
- `official` — approved for the Official Lexicon.
- `deprecated` — no longer recommended for active use but retained for audit/history.

A source can be official while a derived record is still curated; conversely, a transcription can support an official lexical item without being an official exam document.

---

# 12. Pronunciation

Use American English (US) IPA.

**Pronunciation/transcription must never be invented, guessed, reconstructed from spelling, inferred from context, or generated from intuition.**

The pronunciation must come from a reliable source that documents the actual lexical item and relevant pronunciation variant.

If no reliable pronunciation source is available, leave `pronunciation` blank or explicitly unverified/pending. Do not block a trustworthy record merely to force a pronunciation value into the row.

If multiple valid pronunciations exist, preserve the relevant variant and its source rather than silently choosing one without evidence.

Formatting/normalization of verified IPA is allowed only when it preserves the source-supported phonetic content and follows the project's US-IPA convention.

---

# 13. Meanings

Every normal lexical item should have, when evidence is sufficient:

- a concise English definition
- a concise Vietnamese meaning

Definitions must come from reliable lexical sources. The PTNK passage/question may determine **which documented sense is intended**, but context alone is not an authority for inventing a definition.

Do not:

- read the PTNK sentence and invent a new definition from context
- turn a contextual implication into a dictionary definition
- merge unrelated senses into one vague translation
- present an AI-generated definition as source-verified

Paraphrasing is allowed only when the source meaning is preserved accurately.

If a reliable lexical source for the intended sense cannot be found, leave the curated/official meaning pending rather than fabricating it.

---

# 14. Examples

Examples are important, but **accuracy takes priority over completeness**.

3–5 examples are preferred when sufficient reliable, natural evidence exists. However, **3 examples is not a hard minimum**.

It is explicitly acceptable to have fewer than 3 examples when adding more would require:

- guessing
- awkward or unnatural construction
- unsupported usage
- forced repetition
- demonstrating a different or uncertain sense

Preferred evidence order:

1. reliable dictionary / lexical-source examples
2. reliable corpus or otherwise documented natural usage
3. carefully constructed learner examples based on a verified sense and verified pattern

Never create additional examples solely to satisfy a numeric quota.

Examples should be:

- grammatical
- natural
- short
- meaningful
- easy to understand
- approximately 5–10 words when possible
- clearly compatible with the verified intended sense

Use `|` to separate examples in the Google Sheet.

Avoid awkward AI-generated sentences, unnecessary obscure vocabulary, and examples that accidentally demonstrate another sense.

---

# 15. Patterns and Collocations

`patterns` must contain genuine, useful usage patterns.

Valid patterns may include:

- collocations
- grammatical frames
- lexical frames
- natural fixed/semi-fixed combinations

Do **not** use `patterns` for:

- synonyms
- paraphrases
- definitions
- translations
- semantic explanations
- arbitrary combinations

Include a pattern only when it is natural, semantically appropriate, useful for learning, and supported by reliable evidence where verification is necessary.

A short list of verified patterns is better than a long list of guessed combinations.

When uncertain, leave the pattern out.

---

# 16. Usage Notes

`usage_note` is optional.

Use it for information such as register, grammatical restriction, countability, semantic limitation, or important natural-usage warnings.

Do not repeat the definition.

---

# 17. Word Formation

Word Formation is not a separate Lexicon data type.

A word-formation answer becomes a normal Lexicon item, with the relationship recorded in `word_formation`.

Example:

```text
culture → counterculture
```

The derived item `counterculture` is a normal Lexicon entry.

Being a Word Formation answer does not automatically make an item P1.

---

# 18. Domain

`domain` describes the subject/topic context in which the item is especially relevant.

Examples:

- `academic`
- `agriculture`
- `linguistics`
- `social_science`
- `general`

Assign a domain only when there is a clear basis in the source/context and the classification adds useful information.

Do not force a specialized domain when the word is broadly transferable.

`domain` does not determine priority or CEFR.

A word may appear in a specialist PTNK passage while still being `general` because its learning value transfers broadly.

If domain assignment is uncertain, leave it blank or mark it pending rather than guessing.

---

# 19. PTNK Evidence and Roles

Preserve PTNK evidence whenever available.

At minimum record:

- year
- section
- question number
- role/context when useful

Useful roles include:

- `correct_answer`
- `distractor`
- `reading_only`
- `word_formation`

Distractors can be retained and evaluated independently. Being a distractor does not automatically make an item low priority.

---

# 20. Source Type and Source Quality

`source_type` describes what the source is.

Examples:

- `ptnk_exam`
- `transcription`
- `answer_key`
- `dictionary`
- `corpus`
- `evp`
- `learner_dictionary`
- `other_documented`

`source_quality` describes the verification status/nature of the evidence.

Examples:

- `official_exam`
- `transcription`
- `dictionary`
- `corpus`
- `verified`

Do not claim an official source when the actual source is a transcription.

These fields are complementary and must not be collapsed into a single vague `source` field.

---

# 21. CEFR Rules

Do not invent CEFR levels.

Do not infer C1/C2 merely because an item looks advanced, appears in a difficult PTNK question, or feels difficult to the learner.

CEFR information should be recorded only when independently verified from a reliable source.

`cefr_source` answers:

> **Where was this CEFR information verified?**

It is not the source of the lexical item itself and is not a substitute for PTNK provenance, definition source, or pronunciation source.

If CEFR is not verified:

```text
cefr_status: not_verified
cefr_source:
```

CEFR information should be treated carefully because lexical levels may apply to particular meanings/uses rather than automatically to every sense of a headword.

---

# 22. Priority System

Priority measures **PTNK learning value**, not linguistic difficulty.

Priority must be evidence-based and defensible. If the evidence is insufficient to distinguish levels confidently, do not manufacture precision merely to fill the field.

## P1 — Core

High-value items that should normally enter the default learning queue.

Typical cases: advanced general vocabulary, important idioms, useful phrasal verbs, high-value collocations, recurring patterns, and important word families.

## P2 — Important

Useful items that should be learned after the core set.

## P3 — Recognition / Lower Priority

Useful mainly for recognition, reading comprehension, or lower-frequency/topic-specific coverage.

## P4 — Low / Specialized

Retained for completeness/reference but normally excluded from the default learning queue.

P4 items are not deleted.

A difficult item can be P1. An easy but low-value item can be P4.

---

# 23. Specialized Vocabulary

Specialist vocabulary from biology, forestry, technology, psychology, linguistics, education, culture, etc. should not automatically become P1.

Ask:

1. Is it useful beyond this passage?
2. Is it advanced general English?
3. Is it transferable to other PTNK texts?
4. Is it part of a recurring lexical pattern?
5. Is its main value only topic recognition?

Topic-specific recognition items will often be P3/P4 unless stronger evidence supports a higher priority.

---

# 24. Idioms and Phrasal Verbs

Idioms, fixed expressions, and phrasal verbs are first-class lexical items.

Preserve their canonical form, natural grammatical variation, meaning, examples, patterns, and provenance.

Examples:

- `stick to one's guns`
- `make headway`
- `live up to`
- `rule someone/something out`

Do not reduce them to their component words.

---

# 25. Canonical Forms

Use canonical forms for variable pronouns or grammar where appropriate.

Examples:

- `stick to one's guns`
- `write someone off`
- `rule someone/something out`

Examples may use natural forms such as `her guns`, `him off`, or `them out`.

Never force a canonical form into an unnatural sentence.

---

# 26. Quality Control

Before an item becomes official, verify:

- lexical form is correct
- word type is correct
- intended sense is correct
- English meaning is accurate and source-backed
- Vietnamese meaning is accurate and source-backed
- pronunciation is independently verified or explicitly left unverified
- examples are grammatical and natural
- no example was added solely to satisfy a numeric quota
- patterns are genuine, useful, and evidence-supported where necessary
- domain is justified or left unverified
- priority reflects defensible PTNK value
- provenance is preserved
- source quality is honest
- CEFR is not invented
- lifecycle status is correct

If uncertain, preserve uncertainty or omit the field rather than guessing.

---

# 27. Official Promotion Rule

A record may be promoted to `official` only when:

1. its source/evidence is recorded;
2. its provenance is preserved;
3. the lexical form and intended sense are reviewed;
4. required learner-facing fields are complete **to the extent justified by available evidence**;
5. definitions and meanings are source-backed;
6. pronunciation is source-backed or explicitly left unverified;
7. examples and patterns pass quality control without fabricated completeness;
8. priority/domain decisions are defensible, or are left pending where the schema permits;
9. unsupported CEFR claims have been removed;
10. the record is not merely a raw transcription copied into the learning dataset.

**Optional or evidence-limited fields must not be fabricated merely to satisfy a preferred schema shape.**

Official promotion is an editorial decision by the project, not a claim that the source itself is official.

---

# 28. Learning-Facing Architecture

The learner-facing Google Sheet remains organized by priority:

```text
PTNK Google Sheet
├── P1
├── P2
├── P3
└── P4
```

There should not be separate learner tabs for Vocabulary / Idioms / Phrasal Verbs / Word Formation.

`word_type` identifies what an item is.

`priority` identifies how worthwhile it is to study.

This keeps the learning system simple.

---

# 29. Separation of Concerns

The following distinctions are mandatory:

```text
source data      = what the external source says
provenance       = where and why we got it
after extraction = raw/evidence record
curation         = normalization + enrichment + review
official lexicon = approved learning content
CEFR source      = independent evidence for CEFR only
priority         = PTNK learning value
domain            = topic/subject context
```

Do not use one field as a substitute for another.

---

# 30. Migration Rule for Existing Data

Existing files may use older schemas or separate directories such as:

```text
data/vocabulary/
data/idioms/
data/phrasal_verbs/
data/collocations/
data/word_formation/
```

These are historical/working source structures and should not be interpreted as the final learner-facing architecture.

When migrating them:

1. preserve the original files as historical evidence;
2. map source-specific fields into the unified Lexicon schema;
3. preserve provenance and source quality;
4. add `source_id`, `source_type`, and `official_status` where applicable;
5. do not silently upgrade `transcription` to `official_exam`;
6. do not invent CEFR;
7. do not invent definitions or pronunciation;
8. do not manufacture examples or patterns to fill preferred quotas;
9. promote records to `official` only after review.

---

# 31. Final Principle

The dataset should optimize for:

> **evidence → traceability → accurate curation → useful learning data**

not:

> **maximum number of words → maximum metadata → artificial completeness**

**Accuracy is more important than completeness.**

A missing field is acceptable when the evidence is missing.

A short verified example list is better than three invented examples.

A blank pronunciation is better than guessed IPA.

A pending definition is better than a fabricated definition.

A short verified pattern list is better than a long guessed list.

PTNK relevance is more important than generic difficulty.

Provenance must survive every transformation.
