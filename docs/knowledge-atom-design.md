# Knowledge Atom Design

> Status: **design workspace / ontology discussion**
>
> This document is the working place for defining what a `knowledge_atom` is, what belongs inside an atom, what must remain a separate entity, and how knowledge atoms connect to questions, competencies, and learner state.
>
> This document does **not** yet override `schemas/knowledge-atom.schema.json`. The schema should be updated only after the ontology is agreed.

## 1. Purpose

The PTNK system is building a knowledge system, not a vocabulary list. A knowledge atom should therefore represent a sufficiently small, identifiable unit of knowledge that can be:

- grounded in source evidence;
- referenced independently;
- tested by one or more assessment items;
- related to other knowledge;
- associated with multiple mastery dimensions;
- reused across modules and learning activities.

## 2. Working definition

A **knowledge atom** is a stable, source-grounded unit of knowledge that is small enough to assess and relate independently, but complete enough to have a meaningful interpretation in the target learning system.

The current working distinction is:

```text
Knowledge Atom
    = stable knowledge representation

Learning State
    = what this learner currently knows about that knowledge
```

Learner-specific mastery must not be embedded in the knowledge atom itself.

## 3. What a knowledge atom is not

A knowledge atom is not automatically:

- one orthographic word;
- one exercise question;
- one answer option;
- one page or textbook entry;
- one definition string;
- one competency;
- one learner state;
- one difficulty score;
- one intrinsic vocabulary-priority score.

In particular, **intrinsic lexical priority is not part of the ontology**. A lexical item appearing in the C1/C2 source material remains potentially relevant regardless of how frequently it appears in past PTNK papers.

## 4. Candidate ontology families

The initial ontology should support at least the following families without assuming that they all have identical internal structure:

```text
lexical
├── word
├── lexical_sense
├── phrasal_verb
├── idiom
├── collocation
└── fixed_expression

grammatical
├── grammatical_pattern
├── construction
└── transformation_pattern

word_formation

discourse_usage
```

These categories are provisional and require further design review.

## 5. The word-versus-sense problem

A surface form is not necessarily a complete knowledge unit.

For example:

```text
take
├── lexical item / surface form
├── sense A
├── sense B
├── pattern
├── collocation
└── fixed expression
```

The system should not force every meaning, pattern, collocation, or expression into one undifferentiated `take` atom if doing so prevents precise assessment or learner-state tracking.

A major design question remains:

> Should a lexical sense be the fundamental lexical atom, with the word form represented as a parent entity, or should word-level atoms remain primary and senses/patterns be attached components?

This must be resolved before the final schema is frozen.

## 6. Source evidence versus canonical knowledge

Extraction must preserve the distinction between:

```text
RAW SOURCE
    ↓
EVIDENCE
    ↓
DISCOVERED CANDIDATE
    ↓
VERIFIED KNOWLEDGE ATOM
    ↓
SEMANTIC ENRICHMENT
```

A discovered candidate is not automatically a canonical knowledge atom.

Every promoted atom should retain provenance sufficient to trace it back to the exact source evidence.

## 7. Knowledge atom versus question

Questions are assessment entities, not knowledge atoms.

The relationship should be many-to-many:

```text
Knowledge Atom A ─┐
Knowledge Atom B ─┼── Question Q
Knowledge Atom C ─┘
```

and one atom can be tested by many questions:

```text
Atom A
  ├── diagnostic question
  ├── context-selection question
  ├── collocation question
  ├── discrimination question
  └── transfer question
```

Book exercises are canonical seed questions, while generated follow-up questions should add instructional value.

## 8. Knowledge atom versus competency

A competency describes a capability; a knowledge atom describes knowledge that may contribute to that capability.

Example relationship:

```text
knowledge atoms
      ↓
competency
      ↓
assessment tasks
```

A competency may depend on many atoms, and an atom may support multiple competencies.

## 9. Knowledge atom versus learner state

The atom should be stable across learners.

Learner state should live separately:

```text
KnowledgeAtom
    └── stable definition, form, relations, provenance

LearningState
    ├── recognition
    ├── recall
    ├── usage
    ├── collocation
    ├── discrimination
    ├── transfer
    ├── retention
    └── review state
```

This allows the same knowledge base to support multiple learners and prevents learner performance from contaminating source knowledge.

## 10. Candidate relationships

The ontology may need explicit relationships such as:

- synonymy;
- antonymy;
- semantic_relatedness;
- derivation / word-formation relation;
- collocation relation;
- constituent-of-expression;
- prerequisite;
- contrast / easily-confused-with;
- broader-than / narrower-than;
- tested-by;
- supports-competency.

Relationships should be explicit entities or typed references where this is necessary for reliable querying and adaptive learning.

## 11. Mastery dimensions

Mastery dimensions belong to learner state and assessment, not to the static definition of an atom.

Potential dimensions include:

- recognition;
- recall;
- usage;
- collocation;
- discrimination;
- transfer;
- retention.

A learner can therefore know one dimension of an atom while remaining weak in another.

Example:

```text
recognition:       strong
recall:            strong
collocation:       strong
usage:             developing
transformation:    weak
```

The adaptive engine should respond to this state rather than repeatedly reteaching the entire atom.

## 12. Open design questions

The following questions must be resolved before the final schema is treated as canonical:

1. What is the fundamental unit for lexical knowledge: word, sense, expression, or a layered model?
2. Should patterns/collocations be atoms themselves or typed relations/components of another atom?
3. Which knowledge types require distinct schemas rather than one polymorphic schema?
4. What is the minimum information required for an atom to be considered valid?
5. Which fields are source evidence, which are normalized canonical data, and which are derived metadata?
6. How should conflicting source evidence be represented?
7. How should an atom with multiple senses be represented without losing source fidelity?
8. How should grammar knowledge be represented alongside lexical knowledge?
9. Which relationships should be first-class and queryable?
10. Which fields are allowed to be unknown rather than inferred?
11. What constitutes promotion from discovered candidate to verified atom?
12. How should atom versioning work when the ontology evolves?

## 13. Current non-negotiable constraints

- Preserve provenance.
- Preserve raw source evidence separately from normalized knowledge.
- Never invent definitions, meanings, pronunciation, examples, CEFR, or relationships.
- Preserve lexical distinctions.
- Do not assign intrinsic priority to individual vocabulary items.
- Do not confuse source authority with learner relevance.
- Do not promote extraction candidates without validation.
- Do not put learner-specific mastery state into the static knowledge atom.
- Do not let question-bank structure dictate the underlying knowledge ontology.

## 14. Current pipeline relationship

```text
Source sections
      ↓
Evidence-specific discovery
      ↓
Candidate knowledge atoms
      ↓
Stratified validation
      ↓
Verified knowledge atoms
      ↓
Semantic enrichment
      ↓
Knowledge base
      ↓
Question ↔ atom ↔ competency graph
      ↓
Learner state
      ↓
Adaptive next-best activity
```

## 15. Status

The current Destination C1/C2 discovery pipeline has demonstrated a promotion-gate PASS for evidence-specific candidate extraction. That does **not** mean the discovered candidates are already the final ontology.

The next design work should focus on the ontology questions above before large-scale semantic enrichment or canonical promotion.
