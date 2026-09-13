# PTNK Advanced English Dataset — Data Collection Rules

> Version: v0.4
> Status: Working specification / source of truth
> Project: PTNK
> Purpose: Define how lexical data is collected, evidenced, normalized, curated, and promoted into the official PTNK learning dataset.

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
- writing concise English/Vietnamese meanings
- adding US IPA when verified
- creating learner examples
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
- `pronunciation` — US IPA when verified.
- `meaning_en` — concise learner-friendly English definition.
- `meaning_vi` — concise Vietnamese meaning for the intended sense.
- `examples` — 3–5 short natural examples where possible, separated by `|`.
- `patterns` — genuine useful collocations/grammatical or lexical patterns only.
- `usage_note` — optional usage/register/grammar warning.
- `domain` — subject/topic context; use `general` when broadly transferable.
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
- translating the intended sense
- adding verified pronunciation
- writing learner examples
- identifying genuine patterns
- assigning domain and priority

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

Do not invent pronunciation. If unverified, leave it blank or explicitly mark it as unverified in the relevant workflow.

---

# 13. Meanings

Every normal lexical item should have:

- a concise English definition
- a concise Vietnamese meaning

Both must match the intended sense and PTNK context where relevant.

Do not merge unrelated senses into one vague translation.

---

# 14. Examples

Every normal lexical item should have at least 3 examples; 3–5 is preferred.

Examples should be:

- grammatical
- natural
- short
- meaningful
- easy to understand
- approximately 5–10 words when possible

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

Include a pattern only when it is natural, semantically appropriate, useful for learning, and supported by evidence where verification is necessary. When uncertain, leave it out.

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

Do not force a specialized domain when the word is broadly transferable.

`domain` does not determine priority or CEFR.

A word may appear in a specialist PTNK passage while still being `general` because its learning value transfers broadly.

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

It is not the source of the lexical item itself and is not a substitute for PTNK provenance.

If CEFR is not verified:

```text
cefr_status: not_verified
cefr_source:
```

CEFR information should be treated carefully because lexical levels may apply to particular meanings/uses rather than automatically to every sense of a headword.

---

# 22. Priority System

Priority measures **PTNK learning value**, not linguistic difficulty.

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
- English meaning is accurate
- Vietnamese meaning is accurate
- pronunciation is verified or left unverified
- examples are grammatical and natural
- patterns are genuine and useful
- domain is justified
- priority reflects PTNK value
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
4. required learner-facing fields are complete enough for the item's type;
5. patterns/examples pass quality control;
6. priority/domain decisions are defensible;
7. unsupported CEFR claims have been removed;
8. the record is not merely a raw transcription copied into the learning dataset.

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
domain           = topic/subject context
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
7. promote records to `official` only after review.

---

# 31. Final Principle

The dataset should optimize for:

> **evidence → traceability → accurate curation → useful learning data**

not:

> **maximum number of words → maximum metadata → artificial completeness**

Accuracy is more important than completeness.

Useful patterns are more important than long lists.

PTNK relevance is more important than generic difficulty.

Provenance must survive every transformation.
