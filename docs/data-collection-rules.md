# PTNK Advanced English Dataset — Data Collection Rules

> Version: v0.3
> Status: Working specification
> Project: PTNK
> Purpose: Define the rules for collecting, classifying, enriching, and maintaining English lexical data for PTNK specialized-English preparation.

---

# 1. Purpose

This document defines the rules for building the PTNK Advanced English Dataset.

The dataset is intended to support preparation for the English specialized entrance examination of Trường Phổ thông Năng khiếu (PTNK), ĐHQG-HCM.

The dataset is:

- PTNK-oriented
- evidence-based
- focused on advanced general English
- designed for vocabulary learning and spaced repetition
- suitable for integration with the project's Google Sheets flashcard system

The dataset is **not** intended to be:

- a generic English dictionary
- a generic C1/C2 vocabulary list
- an AI training dataset
- a collection of every difficult English word
- a collection based solely on subjective difficulty

The main principle is:

> Collect what is useful for PTNK, not simply what is difficult.

---

# 2. Core Design Principles

## 2.1 PTNK relevance comes first

An item should have a clear reason for being included.

Strong evidence includes:

1. It appeared in an actual PTNK specialized-English examination.
2. It is part of a recurring lexical pattern found in PTNK exams.
3. It is important advanced general English relevant to the type of language tested by PTNK.
4. It is a useful collocation, idiom, fixed expression, phrasal verb, or word family connected to the target vocabulary.
5. It is supported by reliable lexical resources or corpus evidence and has clear learning value for PTNK.

Do not include an item merely because:

- it looks advanced
- it is labelled C1/C2 somewhere
- it is rare
- it is unfamiliar to the learner

---

# 3. What Counts as a Lexical Item?

The dataset treats the following as lexical items:

- single words
- multiword expressions
- collocations
- idioms
- phrasal verbs
- useful fixed phrases
- selected word-formation results

All of these are stored in the same Lexicon structure.

Examples:

- `errand` → word
- `run errands` → expression/collocation
- `stick to one's guns` → idiom
- `cotton on to` → phrasal expression
- `live up to` → phrasal verb

The fact that an expression contains a word already present in the dataset does **not** make the expression redundant.

For example:

- `errand` is one lexical item.
- `run errands` is another lexical item.

They serve different learning purposes.

---

# 4. Word vs Expression

This distinction must be maintained.

## 4.1 Single word

A single lexical word is stored as a word entry.

Example:

`errand`

Type:

`n`

Meaning:

A short journey made to do or get something.

---

## 4.2 Expression

A multiword lexical unit that is useful as a fixed or semi-fixed combination is stored as an expression.

Example:

`run errands`

Type:

`exp`

Do not force the expression into the entry for `errand`.

---

# 5. Word Type

The `word_type` field uses simple labels.

Current standard labels:

| Code | Meaning |
|---|---|
| `n` | noun |
| `v` | verb |
| `adj` | adjective |
| `adv` | adverb |
| `exp` | expression / fixed phrase / collocation |
| `idi` | idiom |

Do not create unnecessary subcategories unless the project later requires them.

The goal is a simple, consistent dataset rather than an overly complicated linguistic taxonomy.

---

# 6. Pronunciation

All pronunciation should use:

> American English (US) IPA

The learner is accustomed to American English pronunciation.

Therefore:

- use American pronunciation consistently
- use IPA
- do not mix British and American pronunciation without a specific reason
- expressions and idioms should also receive pronunciation where practical

If pronunciation has not been verified, do not invent it.

---

# 7. English Definition

Every normal lexical item should have an English definition.

The definition should:

- be accurate
- be understandable
- explain the intended sense
- match the sense relevant to the PTNK evidence
- avoid unnecessary dictionary-style complexity

Do not simply copy a long dictionary definition.

Prefer a concise learner-friendly definition.

---

# 8. Vietnamese Meaning

Every normal lexical item should also have a Vietnamese meaning.

The Vietnamese meaning should:

- match the specific sense being taught
- be concise
- avoid misleading literal translations
- reflect the meaning in the PTNK context when relevant

When one English word has several unrelated senses, do not combine all meanings into one vague Vietnamese translation.

---

# 9. Examples

Every lexical item should have:

> At least 3 examples.

More than 3 examples are allowed when they add meaningful variation.

Examples should generally be:

- short
- natural
- useful
- easy to understand
- approximately 5–10 words when possible

Avoid unnecessarily long sentences.

The purpose of examples is fast comprehension and retention, not reading practice.

---

# 10. Example Formatting

The Google Sheet stores all examples in a single cell.

Use:

`|`

to separate examples.

Preferred number:

3–5

More may be used when the item has important usage variation.

---

# 11. Patterns and Collocations

The `patterns` field is an important part of the dataset.

Patterns should help the learner understand how the lexical item is actually used.

Examples:

For `errand`:

```text
run errands|do an errand|run a few errands|go on an errand
```

For `stick to one's guns`:

```text
stick to your guns|stick to one's guns
```

---

# 12. Critical Rule for Patterns

The `patterns` field is **not** a dumping ground for:

- synonyms
- paraphrases
- definitions
- translations
- semantic explanations
- arbitrary combinations

For example:

`stick to one's guns`

Meaning:

> Refuse to change one's opinion or decision.

The phrase:

`refuse to change one's mind`

is a paraphrase of the meaning.

It is **not** a pattern.

Therefore it must NOT be placed in `patterns`.

---

# 13. Evidence Rule for Patterns

A pattern should be included only when it is:

1. grammatically natural
2. semantically appropriate
3. useful for learning
4. supported by evidence where verification is necessary

Useful evidence may include:

- PTNK exam context
- reputable dictionaries
- established learner dictionaries
- corpus evidence
- Cambridge/English Profile resources
- other reliable lexical sources

Do not invent a pattern simply because it sounds possible.

When uncertain, leave the pattern out rather than guessing.

---

# 14. Usage Notes

`usage_note` is optional.

Use it only when the learner benefits from additional information.

Good uses include:

- register
- grammatical restriction
- common usage distinction
- American/British difference
- countability
- common semantic limitation
- important warning about natural usage

Do not repeat the English definition in `usage_note`.

---

# 15. Word Formation

Word Formation is **not a separate data type**.

A word-formation answer becomes a normal lexical item in the main Lexicon.

Example:

`culture → counterculture`

The resulting lexical item:

`counterculture`

is stored as a normal word.

The relationship is recorded in:

`word_formation`

For an item that is not derived from a specific PTNK word-formation question, this field may be blank.

---

# 16. Word Formation Priority

A word-formation answer is **not automatically P1**.

Priority must be evaluated independently.

The question is:

> How valuable is this lexical item for PTNK preparation?

A very useful advanced word may be P1.

A highly specialized or low-frequency word-formation result may be P3 or P4.

The fact that an item appeared in Word Formation does not automatically determine its priority.

---

# 17. PTNK Evidence

Every item should preserve its PTNK evidence whenever available.

At minimum, record:

- year
- section
- question number
- role/context where useful

Example:

`2026 · Language Use · Q1 · correct answer`

The evidence should make it possible to understand why the item entered the dataset.

---

# 18. Role

When useful, distinguish the role of an item in the exam.

Examples:

- `correct_answer`
- `distractor`
- `reading_only`
- `word_formation`

A distractor can still be valuable.

However:

> Being a distractor does not automatically make an item low priority.

Evaluate its independent learning value.

---

# 19. Source Quality

Record the quality/nature of the source honestly.

Examples:

- `official_exam`
- `transcription`
- `dictionary`
- `corpus`
- `EVP`
- `verified`

Do not claim that something came from an official source if it was actually obtained from a transcription.

If an exam item has not been independently verified, preserve that uncertainty.

---

# 20. CEFR Rules

Do not invent CEFR levels.

In particular:

- do not label a word C1 merely because it looks advanced
- do not label a word C2 because it appeared in a difficult PTNK question
- do not infer CEFR solely from personal judgement

Cambridge English exams at B2 and above do not have official vocabulary lists.

English Profile / English Vocabulary Profile can provide useful lexical information, but CEFR levels apply to specific meanings/uses and should not be treated as an automatic label for an entire headword.

If CEFR has not been verified:

> Do not assign a CEFR level.

If CEFR is later verified from a reliable source, record the verification explicitly.

---

# 21. Priority System

Priority represents:

> How worthwhile the item is to study for PTNK.

Priority is **not difficulty**.

The current priority levels are:

## P1 — Core

High-value items that should be learned first.

Typical examples:

- advanced general vocabulary
- important idioms
- common fixed expressions
- useful phrasal verbs
- high-value collocations
- important word families
- recurring patterns relevant to PTNK

P1 items should normally enter the default flashcard learning queue.

## P2 — Important

Useful advanced items that are worth learning after the core set.

They may be:

- less central than P1
- less frequent
- somewhat more specialized
- useful extensions of P1 knowledge

## P3 — Recognition / Lower Priority

Items that are useful to recognize but have lower learning priority.

Typical cases:

- topic-specific vocabulary
- less common advanced words
- useful but lower-frequency expressions
- items whose main value is reading comprehension

## P4 — Low / Specialized

Items retained for completeness or reference but not normally part of the default learning queue.

Important:

> P4 items are NOT deleted.

They remain in the dataset.

---

# 22. Priority Is Not Difficulty

Do not interpret:

`P1 = easy`

or:

`P4 = difficult`

This is incorrect.

An item can be:

- difficult but P1 because it is highly valuable
- easy but P4 because it has little PTNK value
- difficult and P4 because it is highly specialized

Priority measures learning value, not linguistic difficulty.

---

# 23. Specialized Vocabulary

PTNK reading passages may contain specialized vocabulary.

Examples can come from:

- biology
- forestry
- technology
- psychology
- linguistics
- education
- culture

Do not automatically promote specialized vocabulary to P1.

Ask:

1. Is the word useful beyond this specific passage?
2. Is it part of advanced general English?
3. Is it likely to transfer to other PTNK texts?
4. Is it a useful recurring lexical pattern?
5. Is its main value simply recognizing one topic?

If its value is mainly topic-specific recognition, P3 or P4 may be more appropriate.

---

# 24. Distractors

Distractors should not automatically be ignored.

A distractor can provide evidence of:

- lexical discrimination
- synonym/near-synonym knowledge
- collocation knowledge
- semantic precision
- register
- phrase selection

However, not every distractor deserves P1.

Evaluate its independent learning value.

---

# 25. Idioms and Fixed Expressions

Idioms and fixed expressions are first-class lexical items.

They should not be reduced to individual component words.

Examples:

- `stick to one's guns`
- `in the offing`
- `cut one's losses`
- `dead in the water`
- `par for the course`
- `make headway`

For these items, preserve:

- exact expression
- natural grammatical variation
- meaning
- Vietnamese meaning
- at least 3 short examples
- genuine patterns when available
- PTNK evidence

---

# 26. Phrasal Verbs

Phrasal verbs should be treated as lexical items when they have independent learning value.

Examples:

- `live up to`
- `cotton on to`
- `write someone off`
- `rule something out`
- `churn out`
- `run afoul of`

Do not automatically split them into unrelated entries for the individual verb and particle.

The lexical unit being learned is the phrasal verb itself.

---

# 27. Canonical Form

When a lexical item has variable pronouns or grammatical forms, store a canonical form.

Examples:

- `stick to one's guns`
- `write someone off`
- `rule someone/something out`

Examples can then use natural forms:

- `She stuck to her guns.`
- `He wrote him off too quickly.`
- `They ruled out several possibilities.`

Do not force the canonical form into unnatural example sentences.

---

# 28. Example Quality Control

Before accepting an example, check:

- Is it grammatical?
- Is it natural?
- Does it demonstrate the intended meaning?
- Is the lexical item used correctly?
- Is it reasonably short?
- Does it add information rather than merely repeat another example?

Avoid:

- awkward AI-generated sentences
- unnatural collocations
- unnecessarily sophisticated contexts
- examples that introduce obscure vocabulary unnecessarily
- examples that demonstrate a different sense without explanation

---

# 29. Pattern Quality Control

Before accepting a pattern, ask:

> Would a good learner actually benefit from memorizing this combination?

Then verify:

- Is it natural?
- Is it commonly used?
- Is it relevant to the item's intended sense?
- Is it genuinely a pattern/collocation?
- Is it supported by evidence where necessary?

If the answer is uncertain:

> Do not invent it.

---

# 30. Provenance

Every item should retain provenance.

The dataset should make it possible to answer:

> Why is this item here?

Possible provenance:

- PTNK 2026
- PTNK 2025
- PTNK 2024
- official exam material
- verified exam transcription
- Cambridge/English Profile
- dictionary
- corpus
- other documented source

Do not remove provenance during cleaning or restructuring.

---

# 31. Current Google Sheets Architecture

The learner-facing data is organized by priority.

```text
PTNK Google Sheet
├── P1
├── P2
├── P3
└── P4
```

There should NOT be separate tabs such as:

```text
Vocabulary
Idioms
Phrasal Verbs
Word Formation
```

The reason is that priority has direct meaning for the learning system.

`word_type` identifies what the item is.

The sheet/tab identifies how important it is to study.

This keeps the structure simple.

---

# 32. Final Google Sheet Schema

Each P1/P2/P3/P4 tab uses the same columns:

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
word_formation
ptnk_evidence
source_quality
```

Priority is represented by the tab itself.

Therefore there is no need to duplicate priority in every row unless the architecture is changed later.

`study_mode` is intentionally excluded.

---

# 33. Field Definitions

## id

Unique identifier for the lexical item.

IDs must remain stable once assigned.

## word

The lexical item being learned.

Examples:

- `errand`
- `run errands`
- `stick to one's guns`
- `live up to`

## word_type

One of the standard type codes:

- `n`
- `v`
- `adj`
- `adv`
- `exp`
- `idi`

## pronunciation

American English IPA.

## meaning_en

Short English definition for the intended sense.

## meaning_vi

Concise Vietnamese meaning.

## examples

At least 3 short examples.

Multiple examples are separated with:

`|`

## patterns

Natural collocations and grammatical structures.

Multiple patterns are separated with:

`|`

Do not include synonyms or paraphrases.

## usage_note

Optional usage information.

Leave blank when unnecessary.

## word_formation

Optional word-formation relationship.

Example:

`culture → counterculture`

Leave blank when not applicable.

## ptnk_evidence

PTNK source information.

Example:

`2026 · Language Use · Q1 · correct answer`

## source_quality

Describe the actual source.

Example:

`transcription`

Do not exaggerate source reliability.

---

# 34. Data Collection Workflow

## Step 1 — Collect raw evidence

Collect lexical material from actual PTNK exams and other approved sources.

Do not immediately assign priority.

## Step 2 — Normalize

Normalize:

- spelling
- canonical form
- word type
- grammatical form
- expression form

Do not change the meaning.

## Step 3 — Separate lexical units

Determine whether the evidence represents:

- a word
- an expression
- an idiom
- a phrasal verb
- a collocation
- a word-formation result

Example:

`run errands`

may produce:

- `errand` → `n`
- `run errands` → `exp`

when both have independent learning value.

## Step 4 — Enrich the item

Add:

- American IPA
- English definition
- Vietnamese meaning
- at least 3 examples
- useful patterns
- usage note when needed

## Step 5 — Verify

Check:

- spelling
- meaning
- pronunciation
- examples
- patterns
- provenance

Do not guess when evidence is uncertain.

## Step 6 — Assign Priority

Evaluate the item's PTNK learning value.

Assign:

- P1
- P2
- P3
- P4

## Step 7 — Store

Place the item into the appropriate P1/P2/P3/P4 sheet.

---

# 35. Deduplication

Duplicate lexical items should not be created unnecessarily.

However, related items may legitimately coexist.

Example:

- `errand`
- `run errands`

These are not duplicates.

Similarly:

- `live`
- `live up to`

are different lexical learning units.

Deduplication should operate at the lexical-unit level, not simply by matching individual words.

---

# 36. Sense Separation

A word may have several meanings.

Do not combine unrelated meanings into one entry if doing so would make the entry confusing.

The selected meaning should correspond to:

- the PTNK usage
- the intended learning objective

If a word has a second highly useful meaning that deserves independent study, it may later be represented separately according to the dataset's evolution.

---

# 37. Common Errors to Avoid

## Error 1 — Treating every difficult word as Core

Wrong:

`Difficult → P1`

Correct:

`PTNK learning value → priority`

## Error 2 — Putting expressions inside word entries

Wrong:

`errand → patterns: run errands`

when `run errands` itself is an important lexical item.

Correct:

- `errand` → `n`
- `run errands` → `exp`

They can coexist.

## Error 3 — Inventing patterns

Wrong:

`stick to one's guns → refuse to change one's mind`

This is a paraphrase, not a pattern.

## Error 4 — Inventing CEFR

Wrong:

`pretentious → C2`

without verification.

Correct:

Leave CEFR unassigned unless verified.

## Error 5 — Overloading examples

Wrong:

Long, complicated sentences containing several unknown words.

Correct:

Short, natural examples focused on the target item.

## Error 6 — Creating too many categories

Do not create a complicated taxonomy merely to describe linguistic differences.

Keep:

`n / v / adj / adv / exp / idi`

unless the project later demonstrates a real need for additional types.

## Error 7 — Treating P4 as useless

P4 is still part of the dataset.

It simply has lower default learning priority.

---

# 38. Quality Standard

A good entry should answer the following questions quickly:

1. What is the word/expression?
2. How is it pronounced?
3. What does it mean in English?
4. What does it mean in Vietnamese?
5. How is it used?
6. What common patterns go with it?
7. Why is it relevant to PTNK?
8. How important is it for learning?

If these questions cannot be answered, the entry may need more work.

---

# 39. Guiding Philosophy

The dataset should optimize for:

> High learning value with low cognitive overhead.

The learner should not need to think about:

- complex lexical classifications
- CEFR theory
- source methodology
- priority algorithms
- spaced-repetition calculations

Those belong to the dataset/backend.

The learner-facing system should remain simple.

Core principle:

> Complexity belongs in the algorithm, not in the learner's interface.

---

# 40. Relationship With the Flashcard System

The dataset and flashcard system have different responsibilities.

## Dataset

Answers:

> What should the learner know?

It contains:

- words
- expressions
- idioms
- meanings
- examples
- patterns
- evidence
- priority

## Flashcard system

Answers:

> When should the learner review it?

It handles:

- review scheduling
- repetition
- learning progression
- learner responses
- retention

The two systems should remain conceptually separate.

---

# 41. Learner Interface Principle

The current flashcard system intentionally uses a very simple interface:

`Nhớ`

`Quên`

Do not introduce unnecessary learner-facing grading choices merely because other systems use them.

The backend can be sophisticated while the learner interface remains simple.

Core principle:

> Complexity belongs in the algorithm, not in the learner's interface.

---

# 42. Adaptive Testing vs Spaced Repetition

These are different concepts.

## Spaced repetition

Determines:

> When should this item appear again?

## Adaptive testing

Determines:

> What should be tested next based on the learner's current performance?

The current flashcard system is primarily a spaced-repetition system.

Adaptive testing is a separate future feature and should not complicate the current dataset.

---

# 43. Dataset vs AI Training Data

This project should use the terminology:

- study data
- learning dataset
- vocabulary dataset
- lexical dataset

Avoid calling it:

- AI training data

The dataset is designed to support the learner and the flashcard system.

It is not intended to train an AI model.

---

# 44. Future Expansion

The dataset may later incorporate:

- more PTNK exam years
- additional verified lexical sources
- recurring vocabulary analysis
- frequency information
- corpus evidence
- stronger collocation verification
- learner error data
- adaptive testing

However:

> New features must not unnecessarily complicate the current learner workflow.

---

# 45. Change Management

When modifying the dataset rules:

1. Update this document first.
2. Record the new rule clearly.
3. Apply the rule consistently to new data.
4. Review affected existing entries.
5. Do not silently change established conventions.

When a rule is uncertain, mark it as a decision to review rather than inventing a permanent rule.

---

# 46. Current Decisions — Quick Reference

These decisions are currently considered established:

- PTNK-specific dataset, not generic C1/C2 list
- Words, expressions, idioms coexist in one Lexicon
- `run errands` is an expression; `errand` is a noun
- English definition is required
- Vietnamese meaning is required
- American English IPA is the pronunciation standard
- Minimum 3 short examples
- Examples are stored in one cell separated by `|`
- Patterns are stored in one cell separated by `|`
- Patterns must be genuine collocations/structures
- Patterns must not contain synonyms or paraphrases
- Word Formation is metadata, not a separate tab
- Word Formation does not automatically imply P1
- P1/P2/P3/P4 represent learning priority, not difficulty
- P4 remains in the dataset
- `study_mode` is removed
- Priority is represented by the P1/P2/P3/P4 tabs
- No invented CEFR levels
- PTNK evidence/provenance must be preserved
- Specialized vocabulary does not automatically become P1
- Distractors may still be valuable
- Learner interface remains simple: `Nhớ / Quên`
- Complexity belongs in the backend/algorithm

---

# 47. Final Checklist Before Adding an Item

Before adding a lexical item, check:

- [ ] Is this a genuine lexical unit?
- [ ] Is there a reason it belongs in the PTNK dataset?
- [ ] Is the canonical form correct?
- [ ] Is the word type correct?
- [ ] Is American IPA verified?
- [ ] Is the English definition accurate?
- [ ] Is the Vietnamese meaning accurate?
- [ ] Are there at least 3 short natural examples?
- [ ] Are the examples grammatically correct?
- [ ] Are the patterns genuine?
- [ ] Have synonyms/paraphrases been kept out of `patterns`?
- [ ] Is the PTNK evidence recorded?
- [ ] Is the source quality honestly described?
- [ ] Has CEFR been left blank if unverified?
- [ ] Has priority been assigned based on learning value?
- [ ] Has specialized vocabulary been evaluated appropriately?
- [ ] Has word formation been recorded only as metadata where applicable?
- [ ] Has unnecessary duplication been avoided?

---

# 48. Golden Rule

When uncertain, prefer:

> evidence over intuition  
> accuracy over completeness  
> useful patterns over long lists  
> PTNK relevance over generic difficulty  
> simple learner experience over unnecessary complexity

The goal is not to build the biggest vocabulary database.

The goal is to build the **most useful and trustworthy lexical dataset for PTNK preparation**.
