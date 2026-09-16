# Knowledge Model

> Canonical conceptual model for knowledge atoms and their relationships. Formal field structure is defined in `atom-structure.md`; taxonomy is defined in `atom-types.md`; discovery and promotion are defined in `atom-pipeline.md`.

## 1. Purpose

A knowledge atom is a stable, source-grounded unit of knowledge that is small enough to assess and relate independently, but complete enough to have a meaningful interpretation in the learning system.

A knowledge atom may be:

- grounded in source evidence;
- referenced independently;
- tested by one or more assessment items;
- related to other knowledge;
- reused across competencies and learning activities.

## 2. Knowledge Atom versus Learner State

```text
Knowledge Atom
    = stable knowledge representation

Learning State
    = current evidence-based state of one learner
```

Learner-specific mastery never belongs in the static atom.

## 3. Flat Atom Model

Knowledge atoms are flat and independent by default.

If distinct senses, constructions, patterns, expressions, or uses can be independently learned or assessed, they may be represented as separate atoms. A shared surface form does not require a parent atom.

For example:

```text
bank — financial institution
bank — side of a river
```

can be two independent atoms.

Relatedness does not imply hierarchy or inherited mastery.

## 4. Atom versus Property versus Relation

The system distinguishes:

```text
knowledge atom
property
relation
metadata
```

A property describes an existing atom; a relation connects independent atoms; metadata describes source or system context.

Synonymy, antonymy, near-synonymy, semantic distinctions, derivation, prerequisite relationships, and competency support are normally relations rather than additional atoms.

Create an atom when the knowledge itself is independently meaningful and useful to teach, assess, track, or retrieve.

## 5. Knowledge versus Assessment

Questions are assessment entities, not knowledge atoms.

The relationship is many-to-many:

```text
Atom A ─┐
Atom B ─┼── Question Q
Atom C ─┘
```

One atom may be tested by multiple questions, and one question may test multiple atoms.

Assessment construction rules belong to `docs/learning-material/principles/04-assessment-and-learning-material.md`.

## 6. Knowledge versus Competency

A competency describes a capability. A knowledge atom describes knowledge that may contribute to that capability.

```text
knowledge atoms
      ↓
competency
      ↓
assessment tasks
```

An atom may support multiple competencies, and a competency may depend on multiple atoms.

## 7. Source Grounding

Canonical knowledge must remain traceable to source evidence. Source interpretation may distinguish sense, usage, construction, or other properties, but unsupported claims must not be introduced merely to complete a record.

Source-boundary and provenance rules belong to the learning-material principles; this document defines the conceptual role of provenance, not its extraction procedure.

## 8. Knowledge and Learner Independence

The same knowledge base should support multiple learners. Learner performance must not mutate the canonical meaning, source evidence, or ontology of an atom.

Learner mastery dimensions and adaptive decisions belong to `docs/learner/learning-state.md`.

## 9. Design Constraints

- Preserve lexical and grammatical distinctions that matter for learning.
- Do not require parent/child hierarchies merely to group related atoms.
- Use explicit relationships when they provide real learning or querying value.
- Do not confuse an assessment structure with the underlying knowledge ontology.
- Do not assign learner mastery or adaptive priority to static knowledge.
- Do not invent unsupported knowledge.
