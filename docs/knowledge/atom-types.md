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

A new domain must not be introduced merely because a property or relation is inconvenient to represent. It requires an explicit taxonomy decision.

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

Semantic distinctions between senses belong in the atom content and/or explicit relations; they do not require a parent atom.

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

Fixedness, variation, register, and usage constraints belong in the normal atom properties rather than in additional atom types.

### 2.5. `collocation`

A conventional combination of words that is independently useful to learn because knowing the individual words is insufficient to reproduce the taught combination naturally.

Examples:

- `assess the risk`
- `strong evidence`
- `draw a conclusion`

A collocation should become an atom only when the source supports it as meaningful knowledge rather than merely as an incidental phrase in an example.

### 2.6. `word_formation`

knowledge about a morphological relationship or formation pattern that is independently useful to learn.

Examples:

- `assume` → `assumption`
- `infer` → `inference`
- `accurate` → `accuracy`

The related lexical forms remain lexical knowledge. A word-formation atom represents the formation knowledge itself when that knowledge is independently meaningful.

### 2.7. `morphological_form`

a grammatical or inflectional form of a lexical item that is independently useful to represent, especially an explicitly taught form.

Examples:

- `love` → `loved`, `loves`, `loving`
- `think` → `thought`
- `write` → `written`

Do not create a separate atom for every ordinary inflection. Use this type when the form itself is a meaningful learning object supported by the source.

---

## 3. Grammar knowledge

All grammar atoms use `domain: grammar`. The `subtype` identifies the kind of grammatical knowledge represented.

The currently agreed grammar type set is:

### 3.1. `rule`

A fixed or systematic grammatical relationship, transformation, formation principle, or structural rule governing how grammar is formed or operates.

This includes knowledge that might otherwise be described as `form` or `pattern`; those are not separate subtypes for now.

Examples:

- `I/you/we/they → do`; `he/she/it → does`
- present perfect → `have/has + past participle`

### 3.2. `use`

Knowledge about when, in what context, or for what communicative purpose a grammatical construction is used.

For now, grammatical meaning is also represented through `use` when it can be expressed adequately this way.

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

## 4. What is not an atom type

Several useful kinds of information are deliberately represented as **properties or relations**, not as additional atom types.

### Descriptive information and relationships

Descriptive information about an existing atom is not a separate atom type. If such information is independently meaningful knowledge and is directly taught and tested, represent that knowledge point as a separate atom.

A relation connects independent atoms. It is not stored as a field on the atom and is not itself automatically an atom. If the learning material directly teaches and tests knowledge about a relation, represent that knowledge point as a separate atom using an appropriate grammar type when the knowledge is grammatical.

### Assessment

Questions, exercises, attempts, answer records, and assessment quality are not atom types. They belong to the assessment/learner layers and may reference atoms.

### Source organization

Units, reviews, tests, page ranges, Segment IDs, and other source structure are provenance or source metadata, not atom types.

---

## 5. Atom versus property versus relation

Use the following decision rule:

```text
Is the knowledge independently meaningful and independently diagnosable?
        │
       yes
        ↓
     atom

Does it mainly describe an existing atom?
        │
       yes
        ↓
    property

Does it connect two independently meaningful atoms?
        │
       yes
        ↓
    relation
```

The guiding principle is:

> Create an atom when the knowledge itself is independently meaningful and useful to teach, assess, track, or retrieve. Use properties for characteristics of an existing atom and relations for explicit connections between independent atoms.

This prevents both atom inflation and loss of independently useful distinctions.

---

## 6. Taxonomy constraints

1. **Source evidence comes first.** Do not invent definitions, patterns, collocations, restrictions, distinctions, or exceptions from intuition.
2. **One lexical sense = one atom by default.** Split distinct senses when the source supports them.
3. **Do not turn every example sentence into an atom.** An example is evidence unless it teaches an independently reusable pattern or knowledge object.
4. **Do not turn every semantic relationship into an atom.** Relations connect atoms. A relation becomes a knowledge atom only when the learning material directly teaches and tests knowledge about that relation.
5. **Do not infer unsupported grammar.** A generated question or model intuition is not evidence for a grammatical pattern.
6. **Do not encode learner state in taxonomy.** Mastery, attempts, confidence, retention, review status, and learning progress belong to the learner layer.
7. **Do not encode source structure in taxonomy.** Segment, Unit, exercise, page, and source identifiers belong to provenance and assessment structures.
8. **Do not add taxonomy levels without a demonstrated need.** Keep the canonical model at `domain + type` unless source-grounded modeling work shows that another level is necessary.
9. **Avoid overlapping types without a decision rule.** Use the most specific applicable vocabulary type; otherwise use `multiword_expression`.
10. **Avoid atom inflation.** The goal is useful learning granularity, not the maximum number of records.
11. **Preserve uncertainty.** Candidate knowledge that has not passed validation must not silently become official knowledge.
12. **Preserve provenance.** Every official atom must remain traceable to its supporting source evidence.
