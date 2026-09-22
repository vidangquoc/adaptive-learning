# Knowledge Model

> Canonical conceptual model for knowledge atoms and their relationships. Formal field structure is defined in `atom-structure.md`; taxonomy is defined in `atom-types.md`; discovery and promotion are defined in `atom-pipeline.md`.

## 1. Purpose

A **Knowledge Atom is a unit of knowledge that has its own meaning and can be identified, learned, and assessed as a separate learning target.**

The key criterion is whether the knowledge itself is a learning target that the system may want to teach and evaluate separately. An atom does not need to be completely independent from all other knowledge. It may depend on, overlap with, or be closely related to other atoms and still be a separate atom.

A knowledge atom may be:

- grounded in source evidence;
- identified as a distinct learning target;
- learned independently as a target;
- assessed independently or together with other atoms;
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

**Knowledge atoms are flat. There is no parent/child hierarchy between atoms.**

An atom may be related to another atom, depend on another atom, overlap with another atom, or be more specific in content, but these relationships do not create an atom hierarchy and do not make one atom the parent of another.

For example, the following are separate atoms in the same flat knowledge set:

```text
present perfect
present perfect + since
present perfect + for
present perfect + ever
present perfect + never
```

The fact that `present perfect + since` is related to `present perfect` does **not** mean that it is a child atom of `present perfect`.

The relationship can instead be represented explicitly:

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

The practical question for deciding whether something should be an atom is:

> **Is this a learning target that we want to identify, learn, and assess separately?**

If yes, it can be a separate atom even when another atom is closely related to it.

## 4. Atom versus Property versus Relation

The system distinguishes:

```text
knowledge atom
property
metadata
```

A **property** is information that describes an existing atom. By itself, a property does not create another atom.

If a knowledge point represented by a property is **directly tested or practised in the learning material**, that knowledge point is represented as a separate Knowledge Atom. Otherwise, it remains descriptive information about the existing atom.

For example, the form `have/has + past participle` may be recorded as a property of the `present perfect` atom. If the learning material directly tests or practises that form as a knowledge point, the form itself is represented as a separate atom as well.

The existence of a property therefore does not automatically create another atom. The trigger for separate representation is source-level direct testing/practice of that knowledge point.

**Metadata** describes source, provenance, system, or other contextual information. It is not part of the knowledge itself.

Therefore, the practical distinction is:

```text
Does it describe an existing atom?
    → Property

Can it itself be a meaningful learning target?
    → It may be an Atom

Does it describe source/system context?
    → Metadata
```

The important point is that **Property versus Atom is not decided only by whether the information describes another atom**. The same knowledge may be a property in one context and a separately represented atom when source evidence shows that it is a distinct learning target worth assessing separately.

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

- Knowledge atoms are flat; do not create parent/child hierarchies between atoms.
- Atom-to-atom relationships are not persisted because they are not used by the Adaptive Learning system.
- Preserve lexical and grammatical distinctions that matter for learning.
- Do not require hierarchy merely to group related or overlapping atoms.
- Do not confuse an assessment structure with the underlying knowledge ontology.
- Do not assign learner mastery or adaptive priority to static knowledge.
- Do not invent unsupported knowledge.
