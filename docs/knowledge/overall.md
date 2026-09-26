# Knowledge Model

> Canonical conceptual model for knowledge atoms. Formal field structure is defined in `atom-structure.md`; taxonomy is defined in `atom-types.md`; discovery and promotion are defined in `atom-pipeline.md`.

## 1. Purpose

A **Knowledge Atom is a unit of knowledge that has its own meaning and can be identified, learned, and assessed as a separate learning target.**

The key criterion is whether the knowledge itself is a learning target that the system may want to teach and evaluate separately. An atom does not need to be completely independent from all other knowledge. It may depend on, overlap with, or be closely related to other atoms and still be a separate atom.

A knowledge atom may be:

- grounded in source evidence;
- identified as a distinct learning target;
- learned independently as a target;
- assessed through one or more Challenges;
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

**Knowledge atoms are flat. There is no parent/child hierarchy between atoms.**

An atom may be related to another atom, depend on another atom, overlap with another atom, or be more specific in content, but these relationships do not create an atom hierarchy and do not make one atom the parent of another. If knowledge about a relationship between two or more independent atoms is itself a learning target, that knowledge may be represented as a `relation` atom.

For example, the following are separate atoms in the same flat knowledge set:

```text
present perfect
present perfect + since
present perfect + for
present perfect + ever
present perfect + never
```

The fact that `present perfect + since` is related to `present perfect` does **not** mean that it is a child atom of `present perfect`.

The relationship can be described explicitly when useful, but a raw relationship is not itself persisted merely as graph metadata. When the relationship itself is independently learned or tested, it is represented as a `relation` atom:

```text
present perfect
        │
        ├── related_to → present perfect + since
        └── related_to → present perfect + for
```

The diagram shows a relationship, not a hierarchy.

Likewise, different meanings of the same surface form can be separate atoms:

```text
bank — financial institution
bank — side of a river
```

There is no requirement to create a parent atom for the shared form `bank`.

Atom admission is domain-specific:

- **Grammar:** a knowledge point may become a Knowledge Atom when the source directly teaches, explains, or clearly represents it. Direct testing is not required.
- **Vocabulary:** a vocabulary item must be directly tested or assessed by the source to become a Knowledge Atom Candidate. If the source directly tests a vocabulary item, it must be proposed as a Candidate.

This admission rule applies to the vocabulary taxonomy, including `lexical_sense`, `multiword_expression`, `phrasal_verb`, `idiom`, and `collocation`.

Source grounding is a separate requirement: an admitted Atom must remain traceable to concrete source evidence. Direct testing is assessment evidence and, where applicable, establishes `extra.is_tested: true`; it is not a general admission requirement for Grammar.

Examples and incidental mentions do not create Atoms by themselves. For Grammar, they may support an Atom when the source directly teaches, explains, or clearly represents the corresponding knowledge point. For Vocabulary, mere appearance or contextual mention is insufficient without direct assessment.

## 4. Atom versus Property versus Metadata

The system distinguishes:

```text
knowledge atom
property
metadata
```

A **property** is information that describes an existing atom. By itself, a property does not create another atom.

Whether a property becomes a separate Knowledge Atom follows the domain-specific admission rules in Section 3. It is not promoted merely because the property can be observed in an example.

**Metadata** describes source, provenance, system, or other contextual information. It is not part of the knowledge itself.

The important distinction is therefore:

```text
Describes an existing atom
    → Property

Meets the domain-specific admission rule
    → Knowledge Atom

Describes source/system context
    → Metadata
```

## 5. Knowledge versus Assessment

Challenges are assessment entities, not knowledge atoms.

A Challenge is a concrete assessment task that targets exactly one Knowledge Atom:

```text
Knowledge Atom
      │
      │ assessed by
      ▼
  Challenge
```

The cardinality is:

```text
One Challenge → exactly one Knowledge Atom
One Knowledge Atom → zero or many Challenges
```

If a Challenge tests knowledge about a relationship between independent Knowledge Atoms, that relationship is represented as a `relation` Atom and the Challenge targets that relation Atom. The Challenge does not directly target multiple independent Atoms.

Assessment construction rules belong to `docs/assessment/overall.md` and the Challenge documentation.

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

Source-boundary rules belong to `docs/source/source-structure.md`; source extraction and provenance procedures belong to `docs/source/extraction.md`. Broader learning-material governance remains in `docs/learning-material/principles/03-evidence-provenance-and-governance.md`. This document defines the conceptual role of provenance, not its extraction procedure.

## 8. Knowledge and Learner Independence

The same knowledge base should support multiple learners. Learner performance must not mutate the canonical meaning, source evidence, or ontology of an atom.

Learner review state and adaptive decisions belong to `docs/learner/learning-state.md`.

## 9. Design Constraints

- Knowledge atoms are flat; do not create parent/child hierarchies between atoms.
- Raw structural relationships between atoms are not persisted merely for graph purposes. A relationship becomes a `relation` atom only when the relationship between independent Knowledge Atoms is itself an independently learnable or testable knowledge target. Every Official `relation` atom specifies a non-empty `relation_type`. Candidate relation atoms may temporarily use `relation_type: null` while the relation type is being determined; non-relation atoms use `relation_type: null`.
- Preserve lexical and grammatical distinctions that matter for learning.
- Do not require hierarchy merely to group related or overlapping atoms.
- Do not confuse an assessment structure with the underlying knowledge ontology.
- Do not assign learner mastery or adaptive priority to static knowledge.
- Do not invent unsupported knowledge.
