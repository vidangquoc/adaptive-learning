# Learning Material Construction Principles

> Canonical principles for converting Destination C1 & C2 and later sources into structured learning material for the PTNK Adaptive Preparation System.

## 1. Build a knowledge system, not a collection of lists

Learning material must represent the knowledge and competencies taught by a source, not merely extract vocabulary or reproduce pages.

The system should capture, where present and relevant:

- single-word vocabulary;
- multiword vocabulary;
- idioms;
- phrasal verbs;
- collocations;
- fixed expressions;
- grammar rules and patterns;
- word-formation relationships;
- lexical/grammatical contrasts;
- usage, register, meaning, and restriction information;
- examples and contextual evidence;
- exercises and assessment tasks.

## 2. Separate source extraction from learning design

The source should first be represented faithfully. Only after extraction should the system transform that material into learner-facing challenges, modules, reviews, or generated practice.

```text
SOURCE
  ↓
RAW / EVIDENCE
  ↓
CURATED KNOWLEDGE
  ↓
KNOWLEDGE ATOMS
  ↓
EXERCISES / QUESTIONS
  ↓
COMPETENCY MAPPING
  ↓
CHALLENGES / LEARNING ACTIVITIES
```

Do not mix source transcription, interpretation, and adaptive teaching decisions in one uncontrolled step.

## 3. Destination exercises are canonical seed questions

Exercises already contained in Destination C1 & C2 are the initial canonical question bank.

They should be extracted and linked to the knowledge they test rather than replaced by automatically generated questions.

A question should retain provenance such as:

- source;
- unit;
- section/exercise;
- source location;
- question number or identifier;
- original task type.

Original generated questions are a second layer used for targeted practice, discrimination, transfer, and retesting.

## 4. Every knowledge atom should be linkable to evidence

A knowledge atom should retain enough provenance to answer:

> Where did this knowledge come from, and what evidence supports it?

Typical provenance fields include:

```text
knowledge_atom_id
source_id
source_location
source_section
atom_type
canonical_form
content
provenance
```

Never invent definitions, pronunciation, examples, patterns, register, CEFR, or other metadata merely to fill a field.

## 5. Extract the whole taught knowledge universe

Do not extract only words that appear in exercises.

For Destination, extraction should cover the knowledge explicitly taught or exemplified in the instructional material, including vocabulary boxes, grammar explanations, examples, collocations, idioms, phrasal verbs, word formation, and other relevant sections.

Exercises are then linked back to that knowledge universe.

```text
Instructional content ──→ Knowledge Base
                              ↑
Exercises ────────────────────┘
```

## 6. Preserve distinctions between lexical types

Do not flatten all lexical material into a single `word` field.

The system should distinguish at least:

```text
word
multiword expression
idiom
phrasal verb
collocation
fixed expression
word-formation relation
```

The same surface form may participate in more than one relation; preserve those relations rather than forcing one artificial category.

## 7. No intrinsic vocabulary priority ranking

Individual vocabulary items should not receive an intrinsic importance/priority score merely because they appeared more often in PTNK papers or seem more useful.

The working principle is:

> C1/C2 knowledge represented in the selected backbone is legitimate learning material unless evidence shows that it is outside the target scope.

Adaptive priority belongs to the **learner state and task-selection system**, not to the lexical item itself.

## 8. Knowledge must be usable, not merely recognizable

Material should support multiple dimensions of mastery when applicable:

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

A definition-only record is therefore a knowledge representation, not a complete mastery representation.

## 9. Challenge-first learner interface

The learner should normally meet a challenge before receiving routine instruction when prior knowledge is plausible.

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

Learning material should therefore be designed so that each knowledge atom can support appropriate challenges, not merely passive reading.

## 10. Question ↔ knowledge linkage is mandatory

Questions should be linked to one or more knowledge atoms and, where appropriate, to a competency and PTNK skill.

```text
Question
  ├── knowledge_atom_ids
  ├── competency_id
  ├── skill
  ├── question_type
  └── provenance
```

This linkage is what allows a wrong answer to produce an actionable learning diagnosis rather than simply a score.

## 11. Generated material must add instructional value

Generated questions should not exist merely to increase item counts.

Generate follow-up material when it provides a concrete function such as:

- isolating a knowledge gap;
- testing a different dimension of the same knowledge;
- distinguishing close alternatives;
- increasing contextual complexity;
- testing transfer;
- verifying delayed retention;
- preventing memorization of a source question.

## 12. Preserve the source, normalize separately

Raw extraction is immutable evidence. Cleaning, normalization, and interpretation belong in later layers.

```text
RAW → CLEAN → CURATED → KNOWLEDGE / QUESTIONS
```

Do not manually "fix" raw source text in place merely to make it look nicer.

## 13. Copyright and provenance

Copyrighted books may be used as source material for the private learning system subject to applicable rights and repository constraints, but the repository should not redistribute copyrighted books or wholesale copied content without permission.

Prefer storing:

- source metadata;
- provenance;
- extraction scripts;
- structured mappings;
- permitted answers/analysis;
- generated original practice;
- licensing/usage notes.

## 14. Quality gates

Before material enters the canonical knowledge base, verify:

1. source provenance is known;
2. extraction is faithful enough for the intended use;
3. lexical/grammatical type is correctly classified;
4. metadata is evidence-backed;
5. question-to-knowledge links are defensible;
6. duplicates and false splits are controlled;
7. generated material is clearly distinguished from source material.

Accuracy takes precedence over extraction volume.

## 15. Destination-first implementation order

The first complete implementation should use Destination C1 & C2 to establish:

1. source structure;
2. knowledge extraction;
3. exercise/question extraction;
4. question ↔ knowledge links;
5. competency mapping;
6. challenge generation;
7. learning-state integration.

Additional books are expansion sources and should be integrated selectively after the Destination backbone exposes a concrete need.
