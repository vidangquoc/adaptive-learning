# Knowledge Atom Structure

## Purpose

This document defines the canonical common structure for all knowledge atoms in Adaptive Learning.

All knowledge atoms use the same top-level fields. A field that does not apply to a particular atom remains present and uses the appropriate empty value, normally `null` or `[]`, rather than introducing a second atom schema.

The taxonomy of valid `domain` and `type` combinations is defined in `atom-types.md`.

Learner mastery, attempts, confidence, retention, review state, and other learner-specific state do not belong in a knowledge atom.

---

## 1. Canonical structure

```yaml
id:
domain:
type:

name:

meaning:
mother_says:
explanation:
structure:
constraints:

examples:
related_atoms:

extra:
  source:
  is_tested:
  test_evidence:
  notes:
```

This is the single common atom structure. Atom type must not cause a different top-level field layout.

---

## 2. Identity fields

### `id`

A unique, stable semantic identifier for the atom.

General pattern:

```text
<namespace>.<concept>.<case>
```

The final `case` is optional and is used only when a semantic distinction is needed to separate atoms that would otherwise share the same concept name.

The namespace is a compact semantic identifier for the domain:

- `lex` for vocabulary knowledge;
- `gram` for grammar knowledge.

Examples:

```yaml
id: lex.compelling
id: lex.assume
id: gram.present-perfect-continuous.duration
id: gram.present-perfect-continuous.continuing-activity
id: gram.present-perfect-continuous.recently-stopped-activity
```

The namespace is an ID convention; it does not replace the `domain` field.

Rules:

- IDs must be semantic rather than arbitrary sequence numbers;
- use the shortest stable concept name that remains unambiguous;
- add a semantic case only when necessary;
- do not encode source page, exercise number, extraction order, or learner state into the canonical ID;
- do not use `.01`, `.02`, etc. as semantic distinctions.

Changing an atom's semantic identity is a model change, not a formatting change.

### `domain`

The broad knowledge domain.

Canonical values:

- `vocabulary`
- `grammar`

The valid domain/type combinations are controlled by `atom-types.md`.

### `type`

The primary knowledge type defined by the taxonomy.

Examples include:

- `lexical_sense`
- `multiword_expression`
- `phrasal_verb`
- `idiom`
- `collocation`
- `word_formation`
- `morphological_form`
- `rule`
- `use`
- `exception`
- `word_formation`
- `morphological_form`

`type` describes what the knowledge is. It must not encode assessment format, source location, learner performance, or pedagogical activity.

There is no `subtype` field. A further distinction must be represented through the atom's content/properties or, if it is independently meaningful knowledge, through a separate atom type approved by the taxonomy.

---

## 3. Knowledge content fields

### `name`

The concise, stable name of the knowledge object represented by the atom.

Examples:

- `assess`
- `present perfect continuous`
- `strike a balance`

`name` identifies the learning object; it is not a definition or explanation.

### `meaning`

A concise statement of the relevant meaning or grammatical function.

For vocabulary, it normally states the specific sense represented by the atom. For grammar, it normally states the relevant grammatical meaning or function.

Keep `meaning` concise. Further teaching detail belongs in `explanation`.

### `mother_says`

The learner-facing Vietnamese rendering or explanation of the relevant meaning.

This field is intentionally in the learner's mother tongue and is part of the common schema.

For grammar atoms, use `null` when a concise Vietnamese rendering would not add useful semantic information or when the grammar atom is better explained through `meaning` and `explanation`.

Do not use this field for learner feedback, hints about a specific attempt, or learner-state information.

### `explanation`

The fuller explanation required to understand, teach, distinguish, or diagnose the atom beyond the concise `meaning`.

This may include semantic nuance, contrasts, why a pattern works, or other source-supported explanation.

Do not use it to hide unsupported claims or learner state.

### `structure`

The structural or formal representation of how the knowledge is formed or expressed.

It answers: **How is this knowledge formed or structured?**

Examples:

- `assess + noun`
- `have/has + been + V-ing`
- a lexical frame;
- a morphological formation pattern.

Use `null` when no meaningful structural representation applies.

Keep `structure` focused on form/pattern, not on when or why the knowledge is used.

### `constraints`

Restrictions, conditions, exceptions, contrasts, or limitations needed for accurate use.

Examples include:

- semantic restrictions;
- grammatical restrictions;
- transitivity or separability conditions;
- fixedness or allowed variation;
- source-supported exceptions.

A constraint that merely describes an existing atom normally belongs here rather than becoming a separate atom.

If a specific knowledge point represented by a constraint is directly tested in the learning material, that knowledge point is represented as a separate Knowledge Atom rather than remaining merely a constraint of the original atom.

---

## 4. Evidence and relationship fields

### `examples`

Examples that demonstrate the knowledge represented by the atom.

Examples may be source-derived or generated, but their provenance must remain distinguishable.

Do not treat every example sentence as an independent atom. An example becomes an atom only when it expresses independently meaningful knowledge supported by the taxonomy.

Use `[]` when no example is available or appropriate.

### `related_atoms`

Explicit relationships to other independent knowledge atoms.

Canonical conceptual form:

```yaml
related_atoms:
  - id: lex.assume
    relation: contrasts_with
  - id: lex.infer
    relation: related_to
```

A relationship:

- connects independent atoms;
- does not imply parent/child hierarchy;
- does not imply inherited meaning;
- does not imply inherited mastery;
- must be supported by source evidence or an explicitly justified knowledge-model relation.

Semantic relationships such as synonymy, near-synonymy, antonymy, semantic distinction, and derivation normally belong here rather than becoming separate atoms.

---

## 5. `extra` metadata

`extra` contains provenance, source-level testing evidence, and maintenance metadata. It must not become a hidden second knowledge schema.

### `extra.source`

The provenance record needed to trace the atom back to its supporting source evidence.

At minimum, provenance should identify the source and the relevant Segment/location when available. It should make the following chain recoverable:

```text
source PDF
  ↓
Segment
  ↓
segment PDF
  ↓
segment text / source span
  ↓
evidence
  ↓
atom
```

The exact machine-readable provenance shape is finalized by the later schema step; this document defines the semantic requirement, not every serialization detail.

Do not use source provenance to encode learner history.

### `extra.is_tested`

A boolean indicating whether the source explicitly tests or practises the atom.

This is **source-level evidence** only. It is not learner mastery, confidence, correctness, or frequency.

### `extra.test_evidence`

The source exercise, question, task, or other assessment/practice evidence supporting `is_tested`.

Use `[]` when the source does not explicitly test or practise the atom.

### `extra.notes`

Maintenance or extraction notes that do not belong in the core knowledge fields.

Do not use `notes` as a place to hide:

- learner state;
- unsupported knowledge claims;
- alternative schemas;
- arbitrary taxonomy labels.

---

## 6. Type-specific interpretation

The structure is shared, but fields are interpreted according to the atom taxonomy.

| Type | `meaning` | `explanation` | `structure` | `constraints` |
|---|---|---|---|---|---|
| `lexical_sense` | Specific lexical sense | Semantic nuance, boundaries, and relevant usage | Lexical/syntactic pattern when relevant | Semantic/syntactic/usage limits |
| `multiword_expression` | Expression meaning/function | Meaning, conventional behavior, and relevant usage | Fixed or semi-fixed form | Variation/fixedness restrictions |
| `phrasal_verb` | Combined meaning | Semantic behavior, distinctions, and relevant usage | Verb + particle/preposition | Transitivity/separability/register |
| `idiom` | Idiomatic meaning | Figurative interpretation and relevant usage | Fixed/semi-fixed form | Fixedness/variation restrictions |
| `collocation` | Meaning/function of combination | Why/how the combination is conventional and used | Lexical or syntactic pattern | Combination or grammatical restrictions |
| `word_formation` | Meaning/function of formation | Formation behavior and relevant use | Morphological pattern | Formation/spelling/category restrictions |
| `morphological_form` | Relevant lexical-form information | Form/function explanation and relevant use | Inflectional or irregular form | Form or distribution restrictions |
| `rule` | Grammatical rule/relationship | How the rule works, including relevant contexts when needed | Grammatical form/pattern | Conditions/exceptions/contrasts |
| `use` | Grammatical meaning/function | How the construction is used, including relevant contexts | Grammatical form/pattern when relevant | Conditions/exceptions/contrasts |
| `exception` | Exceptional grammatical behavior | Why it differs from the general rule and where it applies | Exceptional form/pattern | Scope/conditions of the exception |
| `word_formation` | Meaning/function of formation | Formation behavior | Morphological pattern | Productive/contextual use | Formation/spelling/category restrictions |
| `morphological_form` | Relevant lexical-form information | Form/function explanation | Inflectional or irregular form | Context/use | Form or distribution restrictions |

The taxonomy document determines whether a record is valid as one of these types. This table does not create additional types.

---

## 7. Atom versus property versus relation

The conceptual boundary is:

```text
knowledge independently meaningful and independently diagnosable
        ↓
      atom

characteristic used only to describe an existing atom
        ↓
     property

explicit connection between independent atoms
        ↓
     relation
```

Properties are descriptive information about an atom; they are not Knowledge Atoms themselves.

When a knowledge point represented by a Property or Constraint is directly tested in the learning material, that knowledge point is represented as a separate Knowledge Atom rather than as a Property/Constraint of the original atom.

Likewise, a Relation describes a connection between independent atoms. If the learning material directly tests a knowledge point about that connection, the tested knowledge point is represented as a separate Knowledge Atom.

Examples:

```text
assess
→ lexical_sense atom

formal
→ property of an existing atom

assess ↔ evaluate
→ relation

assume ↔ infer
→ semantic-distinction / contrast relation

present simple
→ atom

present simple + habitual actions
→ separate atom when the corresponding knowledge point is directly tested
```

This boundary prevents both atom inflation and the loss of independently useful distinctions.

---

## 8. Representation invariants

1. Every atom uses the same top-level field structure.
2. `domain` and `type` must conform to the canonical taxonomy.
3. `type` describes the knowledge ontology, not the source or learner.
4. One lexical sense is one atom by default when the source supports that distinction.
5. Independently useful grammar distinctions may be separate atoms according to the grammar taxonomy.
6. Properties describe existing atoms; they are not Knowledge Atoms themselves. If a knowledge point represented by a Property or Constraint is directly tested in the learning material, that knowledge point is represented as a separate Atom.
7. Relations connect independent atoms; they are not disguised parent/child records.
8. Source provenance remains recoverable for every official atom.
9. `extra.is_tested` and `extra.test_evidence` describe source-level practice/testing only.
10. Learner mastery, attempts, confidence, retention, review state, and progress never belong in the atom.
11. Source Segment IDs, page locations, exercise IDs, and extraction details are provenance/assessment data, not semantic identity.
12. Canonical atom meaning remains independent of learner state.
13. The formal JSON schema may constrain representation details later, but it must not introduce a second conceptual model.
