# Knowledge Atom Structure

## Purpose

This document defines the canonical common structure for all knowledge atoms in Adaptive Learning.

All knowledge atoms use the same top-level fields. A field that does not apply to a particular atom remains present and uses the appropriate empty value, normally `null` or `[]`, rather than introducing a second atom schema.

The core schema contains knowledge content and descriptive metadata only. It does not use dedicated fields for `usage`, `constraints`, or `related_atoms`. Usage restrictions that constitute independently meaningful knowledge are represented as separate atoms; otherwise they do not require a dedicated atom field. Raw structural relationships between atoms are not persisted merely for graph purposes. When knowledge about a relationship between independent Knowledge Atoms is itself a learning target, that knowledge is represented as a `relation` atom.

The taxonomy of valid `domain` and `type` combinations is defined in `atom-types.md`.

Learner mastery, attempts, confidence, retention, and other learner-specific state do not belong in a knowledge atom. Candidate/Official is a pipeline lifecycle distinction and is stored in separate stores. It is not an additional ontology field or atom type.

---

## 1. Canonical structure

```yaml
id:
domain:
type:
relation_type:

name:
part_of_speech:
pronunciation:

meaning:
mother_says:
explanation:
structure:

examples:

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

Base pattern:

```text
<domain>.<type>.<name>
```

For `vocabulary.lexical_sense`, `part_of_speech` is part of the semantic identity and follows `name`:

```text
<domain>.lexical_sense.<name>.<part_of_speech>
```

If two `lexical_sense` atoms still cannot be distinguished by `name + part_of_speech`, append a short, stable form of `meaning` as the final semantic component.

Examples:

```yaml
id: vocabulary.lexical_sense.assume.verb
id: vocabulary.lexical_sense.compelling.adjective
id: vocabulary.lexical_sense.run.verb.move_quickly
id: vocabulary.lexical_sense.run.verb.operate_function
id: vocabulary.collocation.strike_a_balance
grammar.usage.present_simple.current_habit
grammar.usage.present_perfect.past_to_present
grammar.rule.present_perfect_continuous
```

Rules:

- IDs must be semantic rather than arbitrary sequence numbers;
- `domain` and `type` are always the first two components;
- for `lexical_sense`, `part_of_speech` follows `name`;
- for `lexical_sense`, append a short stable form of `meaning` only when `name + part_of_speech` is insufficient to distinguish the atom;
- for other atom types, use `name` and additional semantic components only when needed to express a precise distinction;
- use the shortest stable identity that remains unambiguous;
- do not encode source page, exercise number, extraction order, or learner state into the canonical ID;
- do not use `.01`, `.02`, etc. as semantic distinctions.

Changing an atom's semantic identity is a model change, not a formatting change.

Candidate and its resulting Official Atom use the same canonical semantic `id`. The semantic ID is created when the Candidate is created; it is not replaced or regenerated during officialization. A Candidate does not use a separate `candidate_id` or temporary ID in place of the canonical semantic ID. A Candidate rejected and later reviewed again keeps the same semantic ID. Once officialized, it does not return to Candidate/rejected lifecycle states. Review state is separate from identity.

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
- `usage`
- `exception`
- `relation`

`type` describes what the knowledge is. It must not encode assessment format, source location, learner performance, or pedagogical activity.

### `relation_type`

The semantic kind of relationship represented by a `relation` atom. For an Official Atom, it is required and non-empty for `type: relation`; it is `null` for other atom types. A Candidate Atom may temporarily leave it as `null` while the relation type is being determined.

`relation_type` describes the relationship itself, not the participating atoms. It is not a subtype and must not be used for structural relationships between grammatical components inside a single Atom.

A `relation` Atom is a knowledge statement about a relationship, not a generic graph edge. The canonical Atom structure does not persist a separate list of participant Atom IDs. The participating concepts are represented by the relation Atom's semantic content, including its `name`, `structure`, `meaning`, and `explanation` where applicable.

There is no `subtype` field. A further distinction must be represented through the atom's content or, if it is independently meaningful knowledge, through a separate `type` approved by the taxonomy.

---

## 3. Knowledge content fields

### `name`

The concise, stable name of the knowledge object represented by the atom.

Examples:

- `assess`
- `present perfect continuous`
- `strike a balance`

`name` identifies the learning object; it is not a definition or explanation.

### `part_of_speech` and `pronunciation`

These fields are part of the canonical common atom structure, but they apply only to atoms with `domain: vocabulary` and `type: lexical_sense`. For all other atom types, they remain present and use `null`.

- `part_of_speech`: the part of speech of the lexical sense, such as `noun`, `verb`, or `adjective`.
- `pronunciation`: the pronunciation transcription of the lexical sense, normally represented using IPA when available.

Both are descriptive properties of the lexical sense; they are not separate Knowledge Atoms.

### `meaning`

A concise statement of the relevant meaning or grammatical function.

For vocabulary, it normally states the specific sense represented by the atom. For grammar, it normally states the relevant grammatical meaning or function.

Keep `meaning` concise. Further teaching detail belongs in `explanation`.

### `mother_says`

The Vietnamese translation or mother-tongue rendering of `name`.

This field is especially useful for vocabulary atoms, where the learner needs a direct translation of the lexical item or expression represented by `name`.

For grammar atoms, use `null` when a direct translation of `name` would not add useful information.

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

---

## 4. Evidence fields

### `examples`

Examples that demonstrate the knowledge represented by the atom.

The meaning of this field is intentionally simple: it contains concrete examples of the knowledge represented by the atom.

Examples may be source-derived or generated. The canonical `examples` field does not encode per-example provenance; source provenance is represented at the Atom level when applicable.

Do not treat every example sentence as an independent atom. An example becomes an atom only when it expresses independently meaningful knowledge supported by the taxonomy.

Use `[]` when no example is available or appropriate.

## 5. `extra` metadata

`extra` contains provenance, source-level testing evidence, and maintenance metadata. It must not become a hidden second knowledge schema.

### `extra.source`

The source information for the atom, divided into two distinct provenance roles:

- `origin`: where the underlying knowledge point comes from in the learning material;
- `atom_decision`: the source evidence on which the decision to represent that knowledge point as a Knowledge Atom is based.

Both are source provenance. They answer different questions and must not be conflated.

The structure is:

```yaml
source:
  origin:
    - source_id:
      segment_id:
      location:
        page:
        section:
        line:
  atom_decision:
    - source_id:
      segment_id:
      location:
        page:
        section:
        line:
```

Both `origin` and `atom_decision` are arrays because an atom may have multiple source records.

- `source_id` identifies the source artifact.
- `segment_id` identifies the canonical Segment containing the evidence.
- `location` identifies where the evidence occurs within that Segment.
- `location.page` identifies the source page when available.
- `location.section` identifies the relevant source section when available.
- `location.line` identifies the starting line of the evidence in the segment text when available. It is not a line range.

The location fields are optional when the source does not provide that level of precision. `line` is intentionally only a starting line; the structure does not require an ending line or exact text span.

`origin` identifies where the knowledge point originates. `atom_decision` identifies the source evidence that supports the decision to represent that knowledge point as an atom. The two may point to the same source location.

`source` is provenance, not knowledge content. It must not be used to store the atom's definition, explanation, learner state, or other normalized knowledge merely because that information appears in the source.

`source` does not replace assessment evidence such as `extra.test_evidence`.

Do not use source provenance to encode learner history.

### `extra.is_tested`

A boolean indicating whether the source explicitly tests or practises the atom.

An atom is `true` as soon as that atom is directly tested/practised, regardless of how many atoms the same exercise, Challenge, task, or assessment tests at the same time.

This is **source-level evidence** only. It is not learner mastery, confidence, correctness, or frequency.

### `extra.test_evidence`

Locations in the learning material that provide evidence that the atom is tested/practised.

Each entry is a simple location reference, for example:

```yaml
test_evidence:
  - "Exercise A, item 5, line 100"
```

The location should contain enough information to find and verify the relevant exercise, item, task, or other practice/testing evidence. `line` identifies the starting line of the evidence in the relevant segment text when available.

Multiple atoms may point to the same `test_evidence` location when one exercise tests several atoms.

Use `[]` when the source does not explicitly test or practise the atom.

### Candidate review status

Candidate review lifecycle uses exactly three values:

- `pending`: the Candidate has not received a review decision, or the reviewer leaves it unchanged;
- `approved`: the reviewer has accepted the Candidate for officialization, but it is still a Candidate until the officialization step runs;
- `rejected`: the reviewer has rejected the Candidate; it may be reviewed again later.

Reviewers may leave a Candidate in `pending`, or explicitly change it to `approved` or `rejected`.

The officialization operation considers **only Candidates whose `review_status` is `approved`**. Each approved Candidate is copied to the separate Official Store with the same semantic ID and then deleted from the Candidate Store. Candidates that are `pending` or `rejected` are not affected by officialization.

There is no `officialized` review status in the Candidate Store because an officialized Candidate no longer exists there. Officialization is a storage transition, not a fourth review status.

### `extra.notes`

Maintenance or extraction notes that do not belong in the core knowledge fields.

Do not use `notes` as a place to hide:

- learner state;
- unsupported knowledge claims;
- alternative schemas;
- arbitrary taxonomy labels.

---

## 6. Type-specific interpretation

The structure is shared, but some fields have type-specific applicability. In particular, `part_of_speech` and `pronunciation` apply only to `vocabulary.lexical_sense`; for other atom types they remain present as `null`.

The structure is interpreted according to the atom taxonomy.

| Type | `meaning` | `explanation` | `structure` |
|---|---|---|---|
| `lexical_sense` | Specific lexical sense | Semantic nuance, boundaries, and relevant usage | Lexical/syntactic pattern when relevant |
| `multiword_expression` | Expression meaning/function | Meaning, conventional behavior, and relevant usage | Fixed or semi-fixed form |
| `phrasal_verb` | Combined meaning | Semantic behavior, distinctions, and relevant usage | Verb + particle/preposition |
| `idiom` | Idiomatic meaning | Figurative interpretation and relevant usage | Fixed/semi-fixed form |
| `collocation` | Meaning/function of combination | Why/how the combination is conventional and used | Lexical or syntactic pattern |
| `word_formation` | Meaning/function of formation | Formation behavior and relevant use | Morphological pattern |
| `morphological_form` | Relevant lexical-form information | Form/function explanation and relevant use | Inflectional or irregular form |
| `rule` | Grammatical rule/relationship | How the rule works, including relevant contexts when needed | Grammatical form/pattern |
| `usage` | Grammatical meaning/function | How the construction is used, including relevant contexts | Grammatical form/pattern when relevant |
| `exception` | Exceptional grammatical behavior | Why it differs from the general rule and where it applies | Exceptional form/pattern |

The taxonomy document determines whether a record is valid as one of these types. This table does not create additional types.

---

## 7. Atom versus property

Properties are descriptive information about an atom; they are not Knowledge Atoms themselves.

When a knowledge point represented only as descriptive information is directly taught and tested in the learning material, that knowledge point is represented as a separate Knowledge Atom rather than remaining merely descriptive information about the original atom.

This boundary prevents both atom inflation and the loss of independently useful distinctions.

## 8. Representation invariants

1. Every Candidate and Official Atom uses the same canonical top-level knowledge field structure; a Candidate additionally carries `review_status` as lifecycle metadata.
2. `domain` and `type` must conform to the canonical taxonomy.
3. `type` describes the knowledge ontology, not the source or learner.
4. One lexical sense is one atom by default when the source supports that distinction.
5. Independently useful grammar distinctions may be separate atoms according to the grammar taxonomy.
6. Properties describe existing atoms; they are not Knowledge Atoms themselves. If descriptive information is directly taught and tested as an independent knowledge point, that knowledge point is represented as a separate Atom.
7. Raw structural relationships between atoms are not persisted merely for graph purposes. Knowledge about a relationship between two or more independent Knowledge Atoms may be represented as a `relation` atom when the relationship itself is an independently learnable or testable target. A relation Atom is not a graph edge and does not require persisted participant Atom references; its semantic content represents the learned relationship.
8. A `relation` atom has a non-null `relation_type`; all non-relation atoms have `relation_type: null`.
9. Source provenance remains recoverable for every official atom.
10. `extra.is_tested` and `extra.test_evidence` describe source-level practice/testing only.
11. Learner mastery, attempts, confidence, retention, and progress never belong in the atom.
12. Source Segment IDs, page locations, exercise IDs, and extraction details are provenance/assessment data, not semantic identity.
13. Canonical atom meaning remains independent of learner state.
14. Candidate and Official use the same semantic `id`; officialization does not create a new atom identity.
15. Candidate and Official are stored separately; Candidate Store contains Candidates and Official Store contains Official Atoms.
16. A Candidate has the same complete canonical atom structure as an Official Atom, with only the additional `review_status` lifecycle field.
17. Candidate review uses exactly `pending`, `approved`, and `rejected`.
18. A newly created Candidate starts as `pending`; a reviewer may leave it `pending` or change it to `approved` or `rejected`.
19. Officialization processes only Candidates with `review_status: approved`, writes the resulting Official Atom with the same semantic ID to the Official Store, and deletes the Candidate from the Candidate Store.
20. A rejected Candidate may be reviewed again; an Official Atom does not return to Candidate/rejected lifecycle states.
21. An Official Atom may be corrected or refined while retaining the same semantic identity.
22. The formal JSON schema may constrain representation details later, but it must not introduce a second conceptual model.
