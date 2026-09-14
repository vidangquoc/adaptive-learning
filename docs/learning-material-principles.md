# Learning Material Construction Principles

> **Canonical source of truth for constructing structured learning material in the PTNK Adaptive Preparation System.**
>
> This document is the project's **single, ultimate rulebook for learning-material construction and its directly supporting data/pipeline rules**. Other documents may specify implementation details, learner state, scheduling, competencies, or source-specific procedures, but they must not silently introduce competing learning-material rules.

---

## 1. Purpose and governing philosophy

The project builds a **knowledge system**, not a vocabulary list, textbook summary, or pile of exercises.

The objective is to turn trustworthy source material into structured evidence and knowledge that can support:

- diagnostic challenges;
- targeted instruction;
- practice;
- discrimination;
- transfer;
- delayed retention;
- adaptive review;
- next-best-activity selection.

Governing principle:

> **Build the smallest trustworthy representation that preserves the useful knowledge and evidence needed for adaptive learning.**

Accuracy and validity take precedence over extraction volume, row counts, or apparent completeness.

---

## 2. Destination C1 & C2 is the backbone

Destination C1 & C2 is the initial backbone from which the project's broad knowledge and competency universe is constructed.

The goal is **not** to force the learner through the books page by page. The goal is to extract and model the knowledge and assessment evidence so the adaptive system can determine what the learner actually needs.

"Master Destination" means demonstrated mastery of the relevant extracted knowledge and competencies, including retention and transfer where required—not completion of every page or exercise.

Additional books are **expansion sources**. They should be introduced selectively when the current model shows a concrete need for additional breadth, depth, precision, or transfer.

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
- retesting should use different contexts when transfer matters;
- challenge difficulty should expose useful gaps rather than create arbitrary difficulty.

> **Test → fail → discover → learn → beat the challenge.**

Instruction is evidence-driven, not page-driven.

---

## 4. Extract the whole taught knowledge universe

Do **not** extract only words that appear in exercises.

Capture relevant knowledge explicitly taught, explained, modeled, or exemplified, including where present:

- words and multiword vocabulary;
- idioms;
- phrasal verbs;
- collocations and fixed/semi-fixed expressions;
- grammar rules and constructions;
- lexical and grammatical contrasts;
- word formation;
- usage and register restrictions;
- meaning distinctions;
- examples and contextual evidence;
- exercises and assessment tasks.

Instructional content forms the knowledge base; exercises provide evidence about how that knowledge is tested.

A knowledge item should therefore be represented even when it has not yet appeared in a question.

---

## 5. Preserve distinctions

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

---

## 6. Knowledge atoms

A **knowledge atom** is the smallest useful, independently referenceable piece of knowledge that can be linked to evidence, competencies, and questions.

An atom may represent:

- a lexical item and verified sense;
- an idiom and its meaning/usage;
- a phrasal-verb sense and pattern;
- a collocation;
- a grammar construction or rule;
- a word-formation relationship;
- a lexical/grammatical contrast;
- a usage or register restriction.

The atom should be granular enough that a failed question can be traced to a useful gap, but not so fragmented that one meaningful concept becomes artificial micro-records.

### 6.1 Flat ontology

Knowledge atoms are **flat and independent by default**.

If several meanings, senses, constructions, patterns, or usages can be independently learned, assessed, or tracked, they may be represented as separate atoms.

Do **not** impose a mandatory hierarchy such as:

```text
word → sense → pattern → expression
```

Instead, keep independently useful units independent and use explicit typed relationships only when they provide real learning, assessment, or querying value.

A relationship is **not ownership, ancestry, or inherited mastery**.

For example, these may all be separate atoms:

```text
take — sense A
take — sense B
take responsibility
take something for granted
```

Learner mastery belongs to learner-state data, not to the static atom. One atom must not inherit mastery merely because it is related to another.

Typical identity/evidence concepts include:

```text
knowledge_atom_id
source_id
source_location
source_section
atom_type
canonical_form
content
provenance
relationships
```

The exact schema may evolve, but stable identity and provenance are mandatory concepts.

---

## 7. Source extraction is not learning design

Never mix transcription, interpretation, normalization, and adaptive teaching decisions into one uncontrolled operation.

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

Raw extraction is evidence and should be immutable.

Cleaning and normalization belong downstream. Never rewrite raw source merely to make it look nicer.

---

## 8. Provenance is mandatory

Every knowledge atom and source-derived question must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve where applicable:

- source ID and type;
- source quality/title/reference;
- unit/section/page/source location;
- exercise/question identifier;
- year and exam section when relevant;
- source context/role;
- uncertainty;
- license/usage information.

Keep provenance dimensions separate:

```text
source evidence → source_id / source_type / source_quality
PTNK relevance  → ptnk_evidence
CEFR evidence   → cefr_status / cefr_source
project state   → official_status
```

No one field should silently substitute for another.

---

## 9. Accuracy over completeness

Never fill a field merely because the schema contains it.

If a claim cannot be verified from an appropriate reliable source:

- leave it blank;
- mark it unverified/pending; or
- omit it when the schema permits.

This applies especially to definitions, Vietnamese meanings, pronunciation, examples, patterns, collocations, CEFR, domain, and provenance.

> **Do not optimize for filled rows. Optimize for trustworthy rows.**

---

## 10. Definitions and meanings

Definitions must be grounded in reliable lexical evidence.

Context may determine **which documented sense is intended**, but context alone is not authority for inventing a definition.

Workflow:

1. identify the item and intended sense;
2. find reliable evidence for that sense;
3. use or carefully paraphrase the evidence without changing its meaning;
4. retain provenance.

Do not infer a dictionary definition from a sentence alone, merge unrelated senses, or present an AI-generated definition as source-verified.

Vietnamese meanings must accurately represent the verified intended sense. If suitable evidence is unavailable, keep the field pending rather than guessing.

---

## 11. Pronunciation

Pronunciation must never be guessed from spelling, intuition, or generated phonetic attempts.

For US IPA, use US IPA only when independently verified from a reliable pronunciation source documenting the relevant lexical item and variant.

If multiple established pronunciations exist, preserve the relevant variant and evidence rather than silently selecting one.

If reliable evidence is unavailable, leave pronunciation pending.

---

## 12. Examples

Examples support learning but must not reduce accuracy.

Preferred evidence order:

1. reliable dictionary/lexical-source examples;
2. reliable corpus/documented usage;
3. carefully constructed learner examples based on verified sense and pattern.

Examples must be grammatical, natural, meaningful, and compatible with the verified sense.

A numerical example quota is not a quality rule. Never invent examples merely to fill a target count.

---

## 13. Patterns, collocations, and usage

Patterns should contain genuine usage information such as:

- collocations;
- grammatical frames;
- lexical frames;
- fixed/semi-fixed combinations;
- selectional or structural restrictions.

Do not use a pattern field for synonyms, paraphrases, definitions, translations, or arbitrary combinations.

Include a pattern only when it is natural, useful, and sufficiently supported.

Usage notes may record register, grammatical restriction, countability, semantic limitation, or important usage warnings.

---

## 14. Word formation

Word formation is part of the knowledge model, not merely an answer list.

A derived form that is useful as an independent lexical item may become its own knowledge atom, while the derivational relationship is preserved explicitly.

```text
culture → counterculture
```

Do not treat a word-formation answer as intrinsically more important merely because it is an answer.

---

## 15. Domain and specialist context

Domain describes meaningful subject/topic context when it adds useful information.

Do not force a specialized domain when the item is broadly transferable. If uncertain, leave the field pending.

Domain does not determine CEFR or learner priority.

---

## 16. CEFR and external metadata

Do not invent CEFR levels.

Do not infer C1/C2 merely because an item looks advanced, occurs in a difficult question, or feels difficult.

Record CEFR only when independently verified and preserve its source separately from lexical provenance and PTNK evidence.

CEFR may apply to a particular sense or use; do not automatically generalize it to every sense of a headword.

---

## 17. No intrinsic vocabulary priority

Individual vocabulary items must **not** receive intrinsic learning-priority scores based on frequency in PTNK papers, perceived difficulty, usefulness, or any other heuristic.

Working principle:

> **C1/C2 knowledge represented in the selected backbone is legitimate learning material unless evidence shows that it is outside the target scope.**

Adaptive urgency belongs to learner state and task selection, not to the lexical item itself.

The material layer must not encode `priority` as an intrinsic property of a word.

---

## 18. PTNK papers are calibration evidence

PTNK papers are used primarily to calibrate and validate:

- competency coverage;
- task formats;
- difficulty/discrimination;
- how advanced knowledge is operationalized;
- transfer requirements.

Do not construct the curriculum by reverse-engineering a frequency-based vocabulary list from past papers.

A C1/C2 item in the selected backbone remains legitimate learning material whether or not it has appeared in an observed PTNK paper.

---

## 19. Destination exercises are canonical seed questions

Exercises already contained in Destination are the initial **canonical seed question bank**.

Extract them faithfully and retain source, unit, section/exercise, location, question identifier, and task type.

Do not replace source exercises with generated questions.

Generated questions are an additional layer for targeted practice, discrimination, transfer, retention, and retesting.

---

## 20. Question ↔ knowledge linkage is mandatory

Each source-derived question should be linked to the knowledge atom(s) it actually tests whenever that relationship can be defended.

Typical concepts:

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

A linkage must be evidence-based, not inferred merely because the same word appears nearby.

---

## 21. Generated material must add instructional value

Generate follow-up questions or explanations only for a concrete instructional reason, such as:

- isolating a knowledge gap;
- testing another mastery dimension;
- distinguishing close alternatives;
- increasing contextual complexity;
- testing transfer;
- verifying delayed retention;
- preventing memorization of a source question;
- providing a needed task format.

Generated content must remain distinguishable from source-derived content.

---

## 22. Multiple mastery dimensions

A knowledge record is not automatically a mastery record.

Where applicable, learning material should support:

- recognition;
- recall;
- meaning precision;
- form/pattern;
- collocation;
- contextual usage;
- discrimination;
- transformation/production;
- transfer;
- delayed retention.

Mastery is learner-state evidence, not a static property of the atom.

---

## 23. Competency mapping

Knowledge and questions should ultimately be linkable to competencies and, where useful, PTNK skill/task categories.

The mapping should answer:

> **What capability does this knowledge or question help assess?**

Do not force a competency label when evidence is insufficient.

---

## 24. Deduplication and relationships

Deduplicate only when records represent the same underlying knowledge item and sense.

Do not collapse records merely because spellings are similar, meanings overlap, one is a component of another expression, or they belong to the same word family.

Preserve useful typed relationships such as:

```text
word ↔ expression
word ↔ idiom
word ↔ phrasal verb
word ↔ collocation
base form ↔ derived form
knowledge atom ↔ question
knowledge atom ↔ competency
```

False deduplication is more damaging than controlled redundancy.

---

## 25. Grammar is a modeling problem, not a transcription problem

Grammar knowledge requires interpretation of **form, meaning, function, constraints, discourse context, and contrasts** where relevant.

Do not create a grammar atom merely by copying a heading such as `past perfect`. Model the smallest useful construction/rule that can support instruction and valid assessment.

A grammar representation should distinguish:

```text
source evidence
      ↓
interpreted construction / rule
      ↓
meaning or discourse function
      ↓
constraints / contrasts
      ↓
assessable knowledge atom
```

If the source does not provide enough evidence to determine a rule or constraint, preserve the evidence and mark the interpretation pending/review-needed. Do not invent it.

### 25.1 Grammaticality is not contextual appropriateness

Grammar assessment must distinguish:

```text
grammaticality
contextual appropriateness
intended meaning
```

A candidate can be grammatically correct while expressing a different interpretation from the intended one.

Therefore, "the answer key says B" is not sufficient evidence that B is uniquely correct.

### 25.2 Answer uniqueness is mandatory

Before a grammar question enters the canonical question bank, evaluate every candidate:

1. Is it grammatical?
2. What interpretation does it permit?
3. Does the supplied context license or exclude that interpretation?
4. Is exactly one candidate compatible with the intended meaning/task?

If two or more candidates are grammatical **and** contextually compatible, **reject or rewrite the item**.

Example of an invalid item:

```text
When I arrived at the lab, Sarah ___ the results.
A. checked
B. was checking
C. had checked
D. has checked
```

Without additional context, both `was checking` and `had checked` can describe coherent situations. The item therefore lacks a uniquely defensible answer.

A valid rewrite must encode the intended interpretation explicitly, for example with context equivalent to `was still checking` or `had already finished checking` when that distinction is what is being assessed.

### 25.3 Answer keys do not override demonstrated ambiguity

A source answer key is evidence of the author's intended answer, not proof that the item is objectively valid.

If independent review demonstrates another grammatical and contextually compatible answer, the item must be flagged, rejected, or rewritten rather than forcing the learner to accept the key.

### 25.4 Prefer context-rich and contrastive assessment

When several constructions are close competitors, prefer formats that make the semantic/discourse distinction explicit:

- context-conditioned multiple choice;
- contrast selection with explicit meaning cues;
- error identification with objectively constrained errors;
- meaning-preserving transformation;
- controlled production;
- explanation/justification when the competency requires it.

Do not force every grammar distinction into a single-answer MCQ.

### 25.5 Grammar question quality gate

```text
Question generated
       ↓
Check grammaticality of all candidates
       ↓
Check interpretation of each grammatical candidate
       ↓
Does context license exactly one answer?
       ↓
   NO ─────────→ REJECT / REWRITE
   YES
       ↓
Check knowledge-atom linkage
       ↓
Check competency / skill
       ↓
      ACCEPT
```

This gate applies to both source-derived and generated grammar questions.

---

## 26. Quality gates before canonical use

Before knowledge or questions enter the canonical learning dataset, verify:

1. provenance is known;
2. extraction is faithful enough for the intended use;
3. lexical/grammatical type is correctly classified;
4. meanings and pronunciation are evidence-backed where present;
5. examples and patterns are natural and defensible;
6. CEFR and external metadata are independently sourced;
7. question-to-knowledge links are defensible;
8. grammar questions have uniquely defensible answers under their stated context;
9. duplicates and false splits are controlled;
10. generated material is clearly distinguished from source material;
11. uncertainty is preserved rather than silently upgraded.

Accuracy and assessment validity take precedence over extraction volume.

---

## 27. Copyright and source-use boundaries

Copyrighted books may be used as source material for the private learning system subject to applicable rights and repository constraints, but the repository should not redistribute copyrighted books or wholesale copied content without permission.

Prefer preserving:

- canonical source URL/reference;
- acquisition method/script where appropriate;
- retrieval timestamp;
- checksum;
- license/usage notes;
- extraction notes;
- provenance metadata.

Generated original material must be clearly distinguished from source-derived material.

---

# Pipeline and Data-Governance Rules

## 28. Canonical pipeline

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
      ↓
LEARNING STATE
      ↓
REVIEW / NEXT-BEST ACTIVITY
```

The layers are conceptually distinct even when implementation combines processing steps.

---

## 29. Raw / Evidence layer

Raw records represent what was obtained from a source with minimal transformation.

Raw data should preserve source identity, location, original text where applicable, context, source quality, and uncertainty.

For extracted PDFs and similar sources:

- preserve the original source when legally and operationally appropriate;
- preserve raw text extraction separately;
- treat raw extraction as immutable evidence;
- perform encoding cleanup, structural normalization, and parsing downstream;
- never manually edit raw text merely to make it look nicer.

---

## 30. Clean / Normalized layer

Cleaning and normalization are separate from raw evidence.

Typical work includes:

- encoding cleanup;
- whitespace/line normalization;
- canonicalization;
- controlled deduplication;
- segmentation into units/sections/exercises;
- machine-readable normalization.

The raw layer must remain recoverable.

Normalization must not silently turn uncertain interpretation into fact.

---

## 31. Curated Knowledge and Knowledge Base

Curated knowledge is an evidence-backed interpretation of raw material suitable for the learning system.

Promotion into canonical knowledge is a **quality-gated decision**, not an automatic consequence of extraction.

Candidate records may remain pending, rejected, or review-needed.

Destination exercises remain canonical seed questions and should be linked to the knowledge they test.

---

## 32. Source acquisition and caching

For external sources, preserve enough acquisition metadata to make the dataset reproducible and auditable where legally and technically appropriate.

Where legally permissible, cache raw source data so future modeling changes do not require unnecessary re-downloading.

For copyrighted/restricted sources, preserve metadata such as:

- canonical URL;
- retrieval timestamp;
- checksum;
- license/usage status;
- acquisition method/script;
- extraction notes;
- handling restrictions.

A generated CSV is not a substitute for provenance.

---

## 33. Structural extraction rules

Structural extraction should be deterministic, validated, and fail-closed.

Recommended workflow:

```text
DISCOVER
   ↓
VALIDATE PLAN
   ↓
COMMIT EXTRACTION
   ↓
POST-EXTRACTION VALIDATION
```

Rules:

- validate major structural boundaries before mass parsing;
- distinguish real section boundaries from repeated headers/footers;
- preserve unit/section/exercise/question locations;
- keep exercises and knowledge extraction separable where practical;
- do not silently guess ambiguous boundaries;
- do not overwrite validated outputs with speculative extraction.

The raw source remains the recovery point.

---

## 34. Canonical data shapes

The exact schemas may evolve, but these concepts should remain stable.

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
relationships
```

Not every field is required for every atom. Evidence rules determine whether a field is populated.

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

Source-derived and generated questions must remain distinguishable.

---

## 35. What this file does not control

This file is the single source of truth for **learning-material construction and directly supporting pipeline/data-governance rules**.

It does not replace specialized specifications for:

- learner learning state;
- review scheduling algorithms;
- competency definitions;
- application/runtime behavior;
- source-specific acquisition instructions.

Those documents may define implementation details, but if they make a claim about how learning material should be constructed, classified, evidenced, linked, or promoted, this document takes precedence.

---

## 36. Non-negotiable rules

1. **Build a knowledge system, not a vocabulary list.**
2. **Destination C1 & C2 is the initial backbone.**
3. **Challenge first when prior knowledge is plausible.**
4. **Extract the whole taught knowledge universe, not only exercise answers.**
5. **Keep raw evidence separate from normalization, interpretation, and learning design.**
6. **Preserve provenance.**
7. **Accuracy beats completeness.**
8. **Never invent definitions, pronunciation, examples, patterns, CEFR, provenance, or unsupported metadata.**
9. **Preserve distinctions among words, expressions, idioms, phrasal verbs, collocations, grammar, word formation, and usage.**
10. **Knowledge atoms are flat independent units by default; relationships do not imply hierarchy or inherited mastery.**
11. **Do not assign intrinsic vocabulary priority.**
12. **Use PTNK papers for calibration/validation, not frequency-based curriculum selection.**
13. **Use Destination exercises as canonical seed questions.**
14. **Link questions to the knowledge they actually test.**
15. **Generate new material only when it adds measurable instructional value.**
16. **Grammar must be modeled through form, meaning, function, constraints, and context where relevant.**
17. **A grammar question is invalid if multiple answers are grammatical and contextually compatible with the intended meaning. Reject or rewrite it.**
18. **An answer key does not override demonstrated ambiguity.**
19. **Preserve uncertainty and fail closed when evidence or answer validity is insufficient.**
20. **Adaptive task urgency belongs to learner state/task selection, not intrinsic lexical value.**
21. **Implementation documents must not silently create competing learning-material rules.**
22. **When in doubt, prefer a smaller trustworthy representation over a larger speculative one.**

---

## Maintenance rule

When a new learning-material rule is discovered during extraction, modeling, question validation, or learner testing, update this document first. Other implementation documents should reference this rule rather than independently redefining it.
