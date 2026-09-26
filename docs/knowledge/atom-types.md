# Knowledge Atom Taxonomy

## Purpose

This document defines the canonical taxonomy for knowledge atoms in the current Adaptive Learning learning-material pipeline.

The taxonomy is intentionally scoped to the knowledge domains currently represented by the source material:

- `vocabulary`
- `grammar`

It does not define learner skills, learner state, assessment entities, mastery, review state, learning strategies, or other learner-side concepts.

The taxonomy answers **what kind of knowledge an atom represents**. The common field structure and field semantics are defined in `atom-structure.md`. The conceptual model is defined in `overall.md`.

---

## 1. Taxonomy model

The hierarchy is:

```text
atom
├── domain
│   ├── vocabulary
│   └── grammar
└── type
```

### `domain`

`domain` identifies the broad knowledge area.

Current canonical values:

- `vocabulary`
- `grammar`

A new domain must not be introduced merely because existing knowledge is inconvenient to represent. It requires an explicit taxonomy decision.

### `type`

`type` identifies the primary kind of independently meaningful knowledge represented by the atom.

`type` must describe the knowledge ontology, not the source location, exercise format, learner performance, or pedagogical activity.

Current canonical types are:

| Domain | Type | Meaning |
|---|---|---|
| `vocabulary` | `lexical_sense` | One independently meaningful sense of a lexical item |
| `vocabulary` | `multiword_expression` | A multi-word lexical unit taught as a unit |
| `vocabulary` | `phrasal_verb` | A verb + particle/preposition functioning as a lexical unit |
| `vocabulary` | `idiom` | A fixed or semi-fixed expression with non-compositional or strongly conventional meaning |
| `vocabulary` | `collocation` | A conventional word combination whose natural use is independently learnable |
| `grammar` | `word_formation` | Knowledge of a productive or source-supported morphological formation pattern |
| `grammar` | `morphological_form` | A grammatical/inflectional form of a lexical item that is independently useful to represent |

### Taxonomy level

There is intentionally no `subtype` layer. If a distinction is important enough to represent as an independently meaningful kind of knowledge, it should be represented as an atom type or as the content of an atom, not as an additional taxonomy level.

The two taxonomy questions are deliberately simple:

```text
domain → knowledge belongs to which broad area?
type   → what kind of knowledge is it?
```

Do not use `type` to encode source location, exercise format, learner performance, pedagogical activity, or descriptive properties such as register or constraint.

---

## 2. Vocabulary knowledge

### 2.1. `lexical_sense`

A specific, independently meaningful sense of a lexical item.

Examples:

- `assess` → evaluate or estimate something
- `assume` → accept something as true without sufficient evidence
- `infer` → reach a conclusion from evidence

One independently meaningful sense should normally be one atom.

If the source teaches distinct senses of the same surface form, represent them as separate atoms when they can be independently understood or assessed.

Semantic distinctions between senses belong in the atom content; they do not require a parent atom.

### 2.2. `multiword_expression`

A multi-word lexical unit taught or used as a unit.

Examples:

- `by and large`
- `in the long run`

Use this type when the expression is not better represented by the more specific `phrasal_verb`, `idiom`, or `collocation` type.

### 2.3. `phrasal_verb`

A verb plus particle or preposition functioning as a lexical unit.

Examples:

- `carry out`
- `come across`
- `put off`

A phrasal verb is also a multi-word expression in the ordinary linguistic sense, but it receives a dedicated type because its grammatical and semantic behavior is often independently important.

### 2.4. `idiom`

A fixed or semi-fixed expression whose meaning is not adequately predicted from the meanings of its individual words.

Examples:

- `spill the beans`
- `hit the nail on the head`

Fixedness, variation, register, and usage constraints are descriptive properties by default. If the learning material directly teaches or assesses one of these as an independent knowledge point, represent that knowledge point as a separate atom when an existing canonical type can represent it; do not create a dedicated property-based subtype merely to accommodate it.

### 2.5. `collocation`

A conventional combination of words that is independently useful to learn because knowing the individual words is insufficient to reproduce the taught combination naturally.

Examples:

- `assess the risk`
- `strong evidence`
- `draw a conclusion`

A collocation should become an atom only when the source supports it as meaningful knowledge rather than merely as an incidental phrase in an example.

## 3. Grammar knowledge

All grammar atoms use `domain: grammar`. The `type` identifies the kind of grammatical knowledge represented.

The currently agreed grammar type set is:

### 3.1. `rule`

A fixed or systematic grammatical relationship, transformation, formation principle, or structural rule governing how grammar is formed or operates.

This includes knowledge that might otherwise be described as `form` or `pattern`; those are not separate subtypes for now.

Examples:

- `I/you/we/they → do`; `he/she/it → does`
- present perfect → `have/has + past participle`

### 3.2. `usage`

Knowledge about when, in what context, or for what communicative purpose a grammatical construction is used.

For now, grammatical meaning is also represented through `usage` when it can be expressed adequately this way.

Examples:

- present continuous for a temporary activity
- present simple for habitual or general situations
- a construction used to express a particular meaning in a given context

### 3.3. `exception`

Knowledge about a case that does not follow an established general grammatical rule in its default form, or a special case that must be learned separately.

Exceptions must be supported by source evidence; they must not be invented from generated examples or model intuition.

### 3.4. `word_formation`

Knowledge about forming a new lexical item from another lexical item or morphological unit, including derivation, compounding, conversion, or other source-supported formation processes.

Examples:

- `assume` → `assumption`
- `infer` → `inference`
- `accurate` → `accuracy`

### 3.5. `morphological_form`

Knowledge about a grammatical or inflectional form of a lexical item that is independently useful to represent, especially an explicitly taught form.

Examples:

- `love` → `loved`, `loves`, `loving`
- `think` → `thought`
- `write` → `written`


---

### 3.6. `relation`

Knowledge about a relationship between two or more independent Knowledge Atoms when the relationship itself is an independently learnable or testable target.

Every `relation` atom must specify `relation_type`. `relation_type` describes the semantic nature of the relationship being learned; it is a relation-specific field, not a taxonomy level or subtype. It does not identify the participating atoms.

`relation_type` applies only to relationships between independent Knowledge Atoms. It must not be used to model structural relationships between grammatical components inside a single Atom.

A relation is not created merely because a grammar construction contains multiple components. Components such as subject, verb, modal verb, auxiliary, and bare infinitive are structural components of a grammar Atom, not Knowledge Atoms for the purpose of creating a relation.

For example, subject–verb agreement and modal verb + bare infinitive are rules when they describe how a grammar construction is formed or operates. By contrast, a contrast between two independently represented grammar Atoms may be a relation when the contrast itself is the knowledge being learned or tested.

A relation describes knowledge about the relationship; it does not imply that the participating Atoms form a parent/child hierarchy.

## 4. What is not an atom type

Several useful kinds of information are deliberately represented as **properties or relations**, not as additional atom types.

### Descriptive information and relationships

Descriptive information about an existing atom is not a separate atom type. If such information is independently meaningful knowledge and is directly taught and tested, represent that knowledge point as a separate atom.

Raw structural relationships between atoms are not persisted merely for graph purposes. If the learning material directly teaches and tests knowledge about a relationship between two or more independent Knowledge Atoms as an independent knowledge point, represent that knowledge point as a `relation` atom.

### Assessment

Challenges, exercises, attempts, answer records, and assessment quality are not atom types. They belong to the assessment/learner layers and may reference atoms.

### Source organization

Units, reviews, assessment tasks, page ranges, Segment IDs, and other source structure are provenance or source metadata, not atom types.

---

## 5. Atom versus property

Use the following decision rule:

```text
Does it describe an existing atom?
        │
       yes
        ↓
    property

Is it an independently useful knowledge point that the source directly teaches or assesses?
        │
       yes
        ↓
      atom
```

Properties describe existing atoms; they are not Knowledge Atoms themselves. If a knowledge point represented by descriptive information is directly taught and tested, represent that knowledge point as a separate Knowledge Atom.

---

## 6. Taxonomy constraints

1. **Source evidence comes first.** Do not invent definitions, patterns, collocations, restrictions, distinctions, or exceptions from intuition. If an independently useful knowledge point is not represented by an existing canonical type, leave it outside the current taxonomy rather than silently creating a new type.
2. **One lexical sense = one atom by default.** Split distinct senses when the source supports them.
3. **Do not turn every example sentence into an atom.** An example is evidence unless it teaches an independently reusable pattern or knowledge object.
4. **Do not turn every descriptive detail into an atom.** A knowledge point becomes a separate atom when the learning material directly teaches or assesses it as an independent target. Direct testing is not required when the source explicitly teaches the knowledge point as an independently useful target.
5. **Do not infer unsupported grammar.** A generated Challenge or model intuition is not evidence for a grammatical pattern.
6. **Do not encode learner state in taxonomy.** Mastery, attempts, confidence, retention, review status, and learning progress belong to the learner layer.
7. **Do not encode source structure in taxonomy.** Segment, Unit, exercise, page, and source identifiers belong to provenance and assessment structures.
8. **Do not add taxonomy levels without a demonstrated need.** Keep the canonical model at `domain + type` unless source-grounded modeling work shows that another level is necessary.
9. **Avoid overlapping types without a decision rule.** Use the most specific applicable vocabulary type; otherwise use `multiword_expression`.
10. **Avoid atom inflation.** The goal is useful learning granularity, not the maximum number of records.
11. **Preserve uncertainty.** Candidate knowledge that has not passed human review must not silently become official knowledge.
12. **Preserve provenance.** Every official atom must remain traceable to its supporting source evidence.
