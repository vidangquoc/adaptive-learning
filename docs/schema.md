# Knowledge Atom Schema

## Purpose

This document defines the common schema for all knowledge atoms in Adaptive Learning.

All knowledge atom types use the same field names and structure. Fields that do not apply to a particular atom type should remain present and use an appropriate empty value such as `null` or `[]` rather than introducing a different schema.

The schema separates the knowledge represented by an atom from additional metadata and provenance. Learner mastery and learner state do not belong in a knowledge atom.

## Schema

```yaml
id:
domain:
type:
subtype:

name:

meaning:
mother_says:
explanation:
structure:
usage:
constraints:

examples:
related_atoms:

extra:
  source:
  is_tested:
  test_evidence:
  notes:
```

## Fields

### `id`

A unique, stable identifier for the atom.

The ID identifies the atom independently of its wording, source location, or learner state. It should remain stable when the explanatory content of the atom is edited.

Example:

```yaml
id: gram.present-perfect-continuous.01
```

### `domain`

The high-level knowledge domain to which the atom belongs.

Allowed values:

- `vocabulary`
- `grammar`

`domain` answers the question: **Is this atom vocabulary knowledge or grammar knowledge?**

Examples:

```yaml
domain: vocabulary
```

```yaml
domain: grammar
```

`word_formation` belongs to `grammar` because the atom represents morphological/word-formation knowledge rather than a learner-state category.

### `type`

The specific kind of knowledge represented by the atom.

Examples include:

- `lexical_sense`
- `collocation`
- `phrasal_verb`
- `idiom`
- `grammar`
- `word_formation`

`type` must describe the knowledge itself, not how it is tested or how well the learner knows it.

### `subtype`

A more specific classification within `type`, when one is useful and supported by the knowledge model.

Use `null` when no meaningful subtype is needed.

Examples:

```yaml
subtype: verb
```

```yaml
subtype: tense
```

```yaml
subtype: derivational_family
```

A subtype should not be invented merely to avoid leaving the field empty.

### `name`

The standard name of the knowledge object that the atom describes.

It identifies **what the atom is about** in a concise, stable form.

Examples:

```yaml
name: assess
```

```yaml
name: present perfect continuous
```

```yaml
name: strike a balance
```

`name` should identify the knowledge object itself rather than describe the learner's task or mastery of it.

### `meaning`

A concise description of the meaning or function represented by the atom.

For vocabulary, this normally describes the relevant sense. For grammar, it describes the grammatical meaning or function.

Example:

```yaml
meaning: evaluate something
```

or:

```yaml
meaning: an activity continuing up to the present with emphasis on duration
```

`meaning` should be concise. Further explanation belongs in `explanation`.

### `mother_says`

A learner-facing expression of the atom's meaning in the learner's mother tongue.

For the current learner, this field contains Vietnamese. It is the only schema field whose content is intentionally written in the learner's mother tongue; all other field content should normally be in English.

For grammar atoms, this field is not necessary and should use `null` so that the common schema remains consistent across atom types.

Example:

```yaml
mother_says: đánh giá, thẩm định
```

`mother_says` is not required to be a word-for-word translation. It should communicate the relevant concept naturally and accurately in Vietnamese.

### `explanation`

A fuller explanation of the knowledge represented by the atom.

This field provides the detail needed to understand, teach, distinguish, or diagnose the atom beyond the concise `meaning` field.

Example:

```yaml
explanation: >
  Assess is used when making a considered judgment about the quality,
  value, condition, ability, risk, or importance of something, usually
  based on available evidence or criteria.
```

`explanation` should remain grounded in source evidence and should not contain unsupported additions or learner-specific mastery judgments.

### `structure`

The structural, formal, or pattern representation of the knowledge.

The exact content depends on the atom type.

Examples:

```yaml
structure: assess + noun
```

```yaml
structure: have/has + been + V-ing
```

```yaml
structure: strike + a balance + between A and B
```

For a knowledge type where no meaningful structural representation applies, use `null` rather than forcing unrelated information into this field.

### `usage`

The contexts, situations, functions, or conditions in which the knowledge is used.

Examples for vocabulary:

```yaml
usage:
  - evaluating quality
  - evaluating risk
  - evaluating ability
```

Examples for grammar:

```yaml
usage:
  - continuing activity up to the present
  - expressing duration
  - recently stopped activity with present relevance
```

`usage` describes how the knowledge is used, not how frequently the learner has used it.

### `constraints`

Restrictions, conditions, distinctions, exceptions, or limitations that are necessary to use the knowledge accurately.

Examples:

```yaml
constraints:
  - stative verbs are normally not used in the continuous form
```

or:

```yaml
constraints:
  - normally takes a direct object
```

This field is especially important for knowledge where a superficially similar alternative would lead to an error.

### `examples`

Examples that demonstrate the knowledge represented by the atom.

Examples should be traceable to source evidence when they are presented as source-derived examples. Generated practice examples should not be treated as source evidence merely because they illustrate the atom.

Use `[]` when no examples are available or appropriate.

### `related_atoms`

Relationships between this atom and other knowledge atoms.

An atom may have zero, one, or multiple relationships. Each relationship should identify the related atom and the type of relationship.

Example:

```yaml
related_atoms:
  - id: lex.assume.01
    relation: contrasts_with
  - id: lex.infer.01
    relation: related_to
```

Possible relation types include `synonym`, `near_synonym`, `antonym`, `contrasts_with`, `broader_than`, `narrower_than`, `derived_from`, `variant_of`, `part_of`, `requires`, `commonly_used_with`, and `grammatically_related`.

Only relationships supported by evidence or by an explicit knowledge-model decision should be added.

## `extra`

`extra` contains information about the atom that is useful for provenance, validation, testing, or maintenance but is **not itself the knowledge represented by the atom**.

### `extra.source`

The provenance of the atom: where the knowledge was obtained or supported.

It should preserve enough information to trace the atom back to its source evidence.

Example:

```yaml
extra:
  source:
    - source_id: destination-c1-c2
      source_type: textbook
      unit: 1
      section: Present time
      location: exercise A
      evidence: present perfect continuous usage
```

Multiple source entries may be used when the same atom is supported by multiple sources.

### `extra.is_tested`

A boolean indicating whether the source explicitly tests or practises the knowledge represented by the atom.

```yaml
is_tested: true
```

or:

```yaml
is_tested: false
```

This field means **source-level testing/practice evidence**. It does **not** mean that the learner has mastered the atom.

### `extra.test_evidence`

Evidence supporting the value of `is_tested`.

This should identify the relevant exercise, question, task, section, or other source location that explicitly tests or practises the atom.

Example:

```yaml
extra:
  is_tested: true
  test_evidence:
    - exercise: A
      item: 3
      evidence: distinguishes present perfect simple from continuous
```

If the source does not explicitly test or practise the atom, use an empty list.

### `extra.notes`

Additional information useful for maintaining or interpreting the atom that does not belong in the core knowledge fields or other `extra` fields.

It may contain extraction notes, unresolved issues, or implementation notes.

Notes must not be used as a place to hide learner state or unsupported knowledge claims.

## What Does Not Belong in an Atom

A knowledge atom represents relatively stable knowledge and source evidence. It should not contain learner-specific state such as:

- mastery level
- recall strength
- retention estimate
- last seen time
- review due date
- number of attempts
- learner accuracy
- learner confidence

These belong under the learner-state architecture and should reference the atom by `id`.

Similarly, generated questions and learner responses are not source evidence merely because they concern the atom. Assessment definitions belong to the knowledge/assessment layer, while attempts and outcomes belong to the learner layer.

## Domain and Type Examples

```yaml
id: lex.assess.01
domain: vocabulary
type: lexical_sense
subtype: verb

name: assess

meaning: evaluate something
mother_says: đánh giá, thẩm định
explanation: >
  Assess means evaluating something systematically using available
  information or criteria.
structure: assess + noun
usage:
  - evaluation
constraints: []
examples: []
related_atoms: []

extra:
  source: []
  is_tested: true
  test_evidence: []
  notes: null
```

```yaml
id: gram.present-perfect-continuous.01
domain: grammar
type: grammar
subtype: tense

name: present perfect continuous

meaning: activity continuing up to the present with emphasis on duration or process
mother_says: null
explanation: >
  The present perfect continuous is formed with have/has + been + V-ing
  and is used especially to emphasize duration or an ongoing process.
structure: have/has + been + V-ing
usage:
  - continuing activity up to the present
  - duration
  - recently stopped activity with present relevance
constraints:
  - stative verbs are normally not used in the continuous form
examples: []
related_atoms: []

extra:
  source: []
  is_tested: true
  test_evidence: []
  notes: null
```
