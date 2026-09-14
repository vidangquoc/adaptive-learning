# Learning Material Construction Principles

> **Canonical source of truth for constructing structured learning material in the PTNK Adaptive Preparation System.**
>
> This document is the project's single, ultimate rulebook for learning-material construction and its directly supporting data/pipeline rules.

---

## 1. Purpose and governing philosophy

The project builds a **knowledge system**, not a vocabulary list, textbook summary, or pile of exercises.

The objective is to turn trustworthy source material into structured evidence and knowledge that can support diagnostic challenges, targeted instruction, practice, discrimination, transfer, delayed retention, adaptive review, and next-best-activity selection.

> **Build the smallest trustworthy representation that preserves the useful knowledge and evidence needed for adaptive learning.**

Accuracy and validity take precedence over extraction volume, row counts, or apparent completeness.

---

## 2. Destination C1 & C2 is the backbone

Destination C1 & C2 is the initial backbone from which the project's broad knowledge and competency universe is constructed.

The goal is not to force the learner through the books page by page. The goal is to extract and model knowledge and assessment evidence so the adaptive system can determine what the learner actually needs.

"Master Destination" means demonstrated mastery of relevant extracted knowledge and competencies, including retention and transfer where required—not completion of every page or exercise.

Additional books are expansion sources, introduced selectively when the current model shows a concrete need for additional breadth, depth, precision, or transfer.

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

Reliable success should lead to compression, skipping, greater discrimination, greater complexity, or transfer. Failure should trigger targeted learning rather than restarting an entire chapter.

> **Test → fail → discover → learn → beat the challenge.**

Instruction is evidence-driven, not page-driven.

---

## 4. Extract the whole taught knowledge universe

Do not extract only words that appear in exercises.

Capture relevant knowledge explicitly taught, explained, modeled, or exemplified, including:

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

An atom may represent a lexical item and verified sense, idiom, phrasal-verb sense and pattern, collocation, grammar construction/rule, word-formation relationship, lexical/grammatical contrast, or usage/register restriction.

### 6.1 Flat ontology

Knowledge atoms are **flat and independent by default**.

If several meanings, senses, constructions, patterns, or usages can be independently learned, assessed, or tracked, they may be represented as separate atoms.

Do not impose a mandatory hierarchy such as:

```text
word → sense → pattern → expression
```

Use explicit typed relationships only when they provide real learning, assessment, or querying value. A relationship is not ownership, ancestry, or inherited mastery.

For example, these may all be separate atoms:

```text
take — sense A
take — sense B
take responsibility
take something for granted
```

Learner mastery belongs to learner-state data, not to the static atom. One atom must not inherit mastery merely because it is related.

Stable identity and provenance are mandatory concepts.

---

## 7. Evidence extraction is not knowledge interpretation

**Parsing, interpretation, normalization, and learning design are separate operations.**

A parser is an **evidence-discovery tool**, not a knowledge-authoring tool.

A parser may reliably discover headings, tables, POS markers, word boxes, candidate expressions, exercise boundaries, source spans, and provenance locations. It must not be assumed to have determined the final knowledge atom merely because a pattern matched.

Use layered processing:

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
  ↓
QUESTIONS / EXERCISES
  ↓
COMPETENCY MAPPING
  ↓
CHALLENGES / LEARNING ACTIVITIES
```

> **Parser discovers evidence. Reasoning interprets evidence. Validation decides whether the interpretation is safe enough to become knowledge.**

A parser may produce one candidate from one evidence span, multiple atom candidates from one span, one atom from multiple spans, or no atom at all.

Therefore:

- never equate parser output count with knowledge-atom count;
- never let a regex match silently become a canonical atom;
- never force an atom when evidence is insufficient;
- preserve raw evidence so interpretation can be revised without re-extracting the source;
- keep generated interpretation distinguishable from source evidence.

### 7.1 Lexical knowledge requires interpretation too

Words, multiword expressions, phrasal verbs, idioms, collocations, and word-formation records are **not exempt** from semantic/linguistic analysis.

Examples of questions that may require reasoning rather than pattern matching:

- Does one headword represent multiple independently useful senses?
- Is a multiword sequence a lexicalized expression or merely a compositional phrase?
- Is an expression functioning idiomatically or literally in the supplied context?
- Does a phrasal verb have several independently assessable senses/patterns?
- Does a collocation encode a genuine lexical preference or merely a possible combination?
- Does a derived form deserve its own atom, and what exactly is the derivational relationship?
- Are two superficially similar strings actually distinct knowledge items?

For example, `look up` may support different independently useful senses/patterns, while `spill the beans` requires distinguishing idiomatic from literal use. A parser can surface these strings, but cannot by itself establish the correct atomization.

### 7.2 Context-grounded inference and missing evidence

The reasoning layer may infer attributes such as **part of speech, intended sense, usage, or meaning** from sufficiently informative source context. This is allowed even when the source does not state the attribute explicitly.

However, inferred attributes must remain distinguishable from directly source-stated attributes and must carry appropriate confidence/provenance. Context is evidence for interpretation; it is not permission to invent unsupported facts.

Use the following rule:

> **If context provides sufficient evidence, infer the attribute and record the inference. If context does not provide sufficient evidence, leave the field null/pending rather than guessing.**

Examples:

```text
estimate (v, n)
        ↓
verb atom + noun atom
```

The POS is directly source-supported, so it may be populated immediately.

If a sentence such as `The estimate was much higher than expected` clearly licenses the noun reading, the noun sense may be inferred from context. If the available source merely says `query (v, n)` with no informative context, the atom may retain POS while leaving meaning/sense unspecified.

A field being present in the schema is never a reason to fill it.

Inference should follow this evidence hierarchy where applicable:

```text
explicit source statement
        ↓
strong contextual inference
        ↓
weak / ambiguous inference → leave null or review-needed
```

Context-derived inference must never silently become source-verified fact.

### 7.3 Source-grounded meanings

Context may help identify **which documented sense is intended**, but a sentence alone must not be treated as authority for inventing a dictionary definition.

When the source context supports a meaning strongly enough to identify the intended sense but does not provide authoritative definitional wording, store the interpretation as an inferred/pending meaning and preserve the supporting evidence. Later enrichment may verify or refine it from an appropriate lexical source.

### 7.4 Grammar knowledge requires interpretation too

Grammar requires the same evidence-to-knowledge distinction, with reasoning over form, meaning, function, constraints, discourse context, and contrasts where relevant.

Do not create grammar atoms by merely copying textbook headings.

---

## 8. Provenance is mandatory

Every knowledge atom and source-derived question must retain enough provenance to answer:

> **Where did this come from, and what evidence supports it?**

Preserve source ID/type, source quality/title/reference, unit/section/page/source location, exercise/question identifier, relevant exam/year metadata, source context/role, uncertainty, and license/usage information where applicable.

Keep source evidence, PTNK relevance, CEFR evidence, and project status as separate provenance dimensions.

---

## 9. Accuracy over completeness

Never fill a field merely because the schema contains it.

If a claim cannot be verified from an appropriate reliable source, leave it blank, mark it unverified/pending, or omit it when the schema permits.

> **Do not optimize for filled rows. Optimize for trustworthy rows.**

This applies especially to definitions, Vietnamese meanings, pronunciation, examples, patterns, collocations, CEFR, domain, and provenance.

---

## 10. Definitions and meanings

Definitions must be grounded in reliable lexical evidence.

Context may determine which documented sense is intended, but context alone is not authority for inventing a definition.

Do not infer a dictionary definition from a sentence alone, merge unrelated senses, or present an AI-generated definition as source-verified.

Vietnamese meanings must accurately represent the verified intended sense. If suitable evidence is unavailable, keep the field pending rather than guessing.

---

## 11. Pronunciation

Pronunciation must never be guessed from spelling, intuition, or generated phonetic attempts.

Use US IPA only when independently verified from a reliable pronunciation source documenting the relevant lexical item and variant.

If multiple established pronunciations exist, preserve the relevant variant and evidence rather than silently selecting one.

---

## 12. Examples

Examples should be grammatical, natural, meaningful, and compatible with the verified sense.

Preferred evidence order:

1. reliable dictionary/lexical-source examples;
2. reliable corpus/documented usage;
3. carefully constructed learner examples based on verified sense and pattern.

Never invent examples merely to fill a target count.

---

## 13. Patterns, collocations, and usage

Patterns should contain genuine usage information such as collocations, grammatical frames, lexical frames, fixed/semi-fixed combinations, and selectional or structural restrictions.

Do not use a pattern field for synonyms, paraphrases, definitions, translations, or arbitrary combinations.

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

> **C1/C2 knowledge represented in the selected backbone is legitimate learning material unless evidence shows that it is outside the target scope.**

Adaptive urgency belongs to learner state and task selection, not to the lexical item itself.

---

## 18. PTNK papers are calibration evidence

PTNK papers are used primarily to calibrate and validate competency coverage, task formats, difficulty/discrimination, how advanced knowledge is operationalized, and transfer requirements.

Do not construct the curriculum by reverse-engineering a frequency-based vocabulary list from past papers.

---

## 19. Destination exercises are canonical seed questions

Exercises already contained in Destination are the initial **canonical seed question bank**.

Extract them faithfully and retain source, unit, section/exercise, location, question identifier, and task type.

Generated questions are an additional layer for targeted practice, discrimination, transfer, retention, and retesting.

---

## 20. Question ↔ knowledge linkage is mandatory

Each source-derived question should be linked to the knowledge atom(s) it actually tests whenever that relationship can be defended.

A linkage must be evidence-based, not inferred merely because the same word appears nearby.

---

## 21. Generated material must add instructional value

Generate follow-up questions or explanations only for a concrete instructional reason, such as isolating a gap, testing another mastery dimension, distinguishing close alternatives, increasing contextual complexity, testing transfer, verifying delayed retention, preventing memorization, or providing a needed task format.

Generated content must remain distinguishable from source-derived content.

---

## 22. Multiple mastery dimensions

Where applicable, learning material should support recognition, recall, meaning precision, form/pattern, collocation, contextual usage, discrimination, transformation/production, transfer, and delayed retention.

Mastery is learner-state evidence, not a static property of the atom.

---

## 23. Competency mapping

Knowledge and questions should ultimately be linkable to competencies and, where useful, PTNK skill/task categories.

Do not force a competency label when evidence is insufficient.

---

## 24. Deduplication and relationships

Deduplicate only when records represent the same underlying knowledge item and sense.

Do not collapse records merely because spellings are similar, meanings overlap, one is a component of another expression, or they belong to the same word family.

Preserve useful typed relationships, but relationships are not hierarchies or inherited mastery.

False deduplication is more damaging than controlled redundancy.

---

## 25. Grammar is a modeling problem, not a transcription problem

Grammar knowledge requires interpretation of **form, meaning, function, constraints, discourse context, and contrasts** where relevant.

Do not create a grammar atom merely by copying a heading such as `past perfect`. Model the smallest useful construction/rule that can support instruction and valid assessment.

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

### 25.2 Answer uniqueness is mandatory

Before a grammar question enters the canonical question bank, evaluate every candidate for grammaticality, interpretation, contextual licensing, and uniqueness.

If two or more candidates are grammatical **and** contextually compatible, **reject or rewrite the item**.

Example:

```text
When I arrived at the lab, Sarah ___ the results.
A. checked
B. was checking
C. had checked
D. has checked
```

Without additional context, both `was checking` and `had checked` can describe coherent situations. The item therefore lacks a uniquely defensible answer.

### 25.3 Answer keys do not override demonstrated ambiguity

A source answer key is evidence of the author's intended answer, not proof that the item is objectively valid.

If independent review demonstrates another grammatical and contextually compatible answer, flag, reject, or rewrite the item rather than forcing the learner to accept the key.

### 25.4 Prefer context-rich and contrastive assessment

When several constructions are close competitors, prefer context-conditioned multiple choice, explicit contrast selection, objectively constrained error identification, meaning-preserving transformation, controlled production, or explanation/justification when appropriate.

Do not force every grammar distinction into a single-answer MCQ.

---

## 26. Knowledge-atom discovery and promotion gates

Discovery and promotion are different states.

A **candidate** is an evidence-backed hypothesis about a possible knowledge atom. It is not yet canonical knowledge.

```text
EVIDENCE
   ↓
CANDIDATE
   ↓
VERIFIED
   ↓
ENRICHED
```

Promotion from candidate to verified atom requires sufficient evidence for atom identity/type, relevant sense or construction, provenance, interpretation, absence of unresolved contradiction, required fields for the atom type, and validation against project quality rules.

If evidence is insufficient or competing interpretations remain unresolved:

> **Do not promote. Preserve the candidate and mark it for review.**

### 26.1 Lexical promotion is not regex promotion

A lexical candidate must not become canonical merely because it matched a POS pattern, word-box pattern, table row, expression-like string, phrasal-verb pattern, or exercise marker.

These are **evidence signals**, not semantic proof.

Promotion may require reasoning over sense, lexicalization, idiomaticity, syntactic behavior, pattern, and distinctions from related candidates.

### 26.2 Grammar promotion is not heading promotion

A grammar heading such as `Past time` or `Past perfect` is structural evidence, not itself a knowledge atom.

The final atom should represent a useful assessable construction/rule supported by the source.

### 26.3 One-to-many and many-to-one mappings are allowed

The evidence model must support:

```text
1 evidence span → 1 atom
1 evidence span → multiple atoms
multiple evidence spans → 1 atom
1 evidence span → no atom / review-needed
```

Source presentation structure and atom structure must remain independent.

---

## 27. Quality gates and fail-closed behavior

Every transformation stage must have explicit quality gates.

When a quality gate fails, do not silently continue with potentially corrupted or ambiguous data.

Prefer:

```text
PASS → continue
WARN → continue only when the warning is explicitly acceptable
FAIL → stop / preserve evidence / require review
```

Quality gates should cover structural validity, provenance, semantic plausibility, answer uniqueness, schema validity, duplication, unsupported inference, and source/license constraints as appropriate.

---

## 28. Copyright and source boundaries

Use copyrighted books as source material within applicable rights and project permissions.

Preserve provenance, canonical source references, extraction metadata, and checksums where appropriate, but do not redistribute copyrighted source text wholesale unless permitted.

Generated summaries, metadata, mappings, and original follow-up questions should not be treated as a substitute for source provenance.

---

## 29. Pipeline governance

Evidence should be preserved before interpretation.

Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting the raw evidence layer.

Transformations should be reproducible and idempotent where practical. Do not silently repair source evidence; record repairs or downstream normalization explicitly.

Keep at least these concerns separable:

```text
source evidence
interpretation
validation
enrichment
learning design
learner state
```

This separation allows the project to improve its reasoning and adaptive strategy without repeatedly downloading or re-extracting the source.

---

## 30. Non-negotiable rules

1. Build a knowledge system, not a vocabulary list.
2. Destination C1 & C2 is the initial knowledge backbone.
3. Challenge first when prior knowledge is plausible.
4. Extract the whole taught knowledge universe, not only exercise words.
5. Separate raw evidence from normalization, interpretation, and learning design.
6. A parser discovers evidence; it does not author canonical knowledge.
7. Lexical and grammatical atomization requires linguistic/semantic reasoning.
8. Context may support inference of attributes such as POS, sense, usage, or meaning, but inferred values must remain distinguishable from source-stated facts.
9. If evidence is insufficient, leave the field null/pending; never guess merely to fill the schema.
10. Preserve provenance for every source-derived atom and question.
11. Prefer accuracy over completeness.
12. Preserve useful distinctions; do not flatten independently learnable knowledge.
13. Knowledge atoms are flat and independent; relationships are not ancestry or inherited mastery.
14. Do not assign intrinsic vocabulary priority.
15. PTNK papers calibrate and validate the model; they are not the primary curriculum.
16. Destination exercises are canonical seed questions.
17. Link questions to the knowledge they actually test.
18. Generated material must add instructional value.
19. Grammar questions must have a uniquely defensible answer.
20. Answer keys do not override demonstrated ambiguity.
21. Fail closed when structural, provenance, semantic, or validation gates fail.
