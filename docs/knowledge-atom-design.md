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

**Working decision: do not build a hierarchical word/sense ontology.**

For a lexical item, each distinct teachable or assessable knowledge variant is treated as its **own knowledge atom**. We do not create parent/child/grandparent relationships merely to represent the fact that several atoms are related to the same surface lexical item.

For example, instead of:

```text
take
└── sense A
    └── pattern
        └── collocation
```

we can simply have separate atoms:

```text
Atom A: take — meaning/sense A
Atom B: take — meaning/sense B
Atom C: take responsibility
Atom D: take something for granted
```

These are independent knowledge atoms. They may be related when the relationship is useful, but **relatedness does not imply hierarchy**.

This deliberately avoids building a complicated ontology of lexical families, senses, sub-senses, components, descendants, and ancestors. The system should remain flat at the knowledge-atom level.

### 5.1 What counts as a separate lexical atom?

A separate atom is justified when the knowledge can reasonably have its own:

- meaning or interpretation;
- form or expression;
- usage constraint;
- assessment target;
- mastery state;
- source evidence;
- or instructional value.

Thus the following may all be separate atoms when the source supports them:

```text
word / lexical form
word + distinct meaning
phrasal verb
idiom
collocation
fixed expression
usage pattern
word-formation item
```

The important point is not whether linguists would classify these as different theoretical levels. The important point is whether the learning system needs to **teach, test, track, or retrieve them independently**.

### 5.2 No mandatory parent atom

If several atoms share the same surface form, the system does **not** require a separate parent atom merely to group them.

For example:

```text
bank — financial institution
bank — side of a river
```

can simply be two independent atoms.

Likewise:

```text
stick to your guns
stick — physical action
stick — remain attached
```

may be represented as independent atoms without constructing a hierarchy between them.

### 5.3 Relationships are optional, not ancestry

If useful, atoms can have explicit typed relationships such as:

```text
related_to
contrasts_with
confused_with
used_in
part_of_expression
derived_from
supports_competency
```

But these relationships must not silently turn into a parent/child ontology.

The rule is:

> **Flat atoms first; explicit relationships only when they provide real learning or querying value.**

### 5.4 Why this is intentional

The flat model keeps the system simpler and makes adaptive learning easier to reason about:

```text
Knowledge Atom A
Knowledge Atom B
Knowledge Atom C
        ↓
independent learner states
        ↓
questions target whichever atom is actually weak
```

The system does not need to infer that mastery of one atom automatically implies mastery of another merely because they share a word form or lexical family.

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

Under the flat-atom decision in Section 5, these are **relationships between independent atoms**, not evidence that one atom must be a parent or child of another.

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

1. What is the minimum information required for an atom to be considered valid?
2. Should patterns/collocations be atoms themselves or typed relationships/components of another atom? The current default is to allow them to be independent atoms when they are independently teachable/assessable.
3. Which knowledge types require distinct schemas rather than one polymorphic schema?
4. What is the minimum information required for an atom to be considered valid?
5. Which fields are source evidence, which are normalized canonical data, and which are derived metadata?
6. How should conflicting source evidence be represented?
7. How should grammar knowledge be represented alongside lexical knowledge?
8. Which relationships should be first-class and queryable?
9. Which fields are allowed to be unknown rather than inferred?
10. What constitutes promotion from discovered candidate to verified atom?
11. How should atom versioning work when the ontology evolves?

The previous question about whether a lexical sense should be a parent entity has been resolved: **no parent lexical entity is required merely to organize related atoms**.

## 13. Current non-negotiable constraints

- Preserve provenance.
- Preserve raw source evidence separately from normalized knowledge.
- Never invent definitions, meanings, pronunciation, examples, CEFR, or relationships.
- Preserve lexical distinctions.
- Treat independently teachable/assessable lexical variants as independent atoms.
- Do not require parent/child/grandparent hierarchies among lexical atoms.
- Use explicit relationships only when they provide real learning or querying value.
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

The current ontology decision for lexical knowledge is intentionally simple: **knowledge atoms are flat, independently assessable units; lexical relatedness is represented through optional explicit relationships rather than ancestry.**

The next design work should focus on the remaining ontology questions before large-scale semantic enrichment or canonical promotion.
