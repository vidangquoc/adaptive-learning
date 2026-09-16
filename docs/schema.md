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

Atom IDs should use semantic components rather than arbitrary sequential numbers whenever multiple atoms share the same core concept. The final component should be a short description of the specific **case** represented by the atom when such a discriminator is needed.

General pattern:

```text
<domain>.<concept>.<case>
```

The `case` is not tied to a particular schema field such as `usage`. It is simply the semantic distinction that separates one atom from other atoms representing the same broader concept or situation.

Examples:

```yaml
id: gram.present-perfect-continuous.duration
```

```yaml
id: gram.present-perfect-continuous.continuing-activity
```

```yaml
id: gram.present-perfect-continuous.recently-stopped-activity
```

For a concept represented by only one atom, the case component may be unnecessary:

```yaml
id: lex.compelling
```

Avoid arbitrary sequential identifiers such as:

```yaml
id: gram.present-perfect-continuous.01
id: gram.present-perfect-continuous.02
```

The semantic case should describe the nature of the atom rather than its order in a source or exercise. Exercise numbers, source positions, and learner attempts should not be used as the semantic discriminator.

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
  - id: lex.assume
    relation: contrasts_with
  - id: lex.infer
    relation: related_to
```

Possible relation types include `synonym`, `near_synonym`, `antonym`, `contrasts_with`, `broader_than`, `narrower_than`, `derived_from`, `variant_of`, `part_of`, `requires`, `commonly_used_with`, and `grammatically_related`.

Only relationships supported by evidence or by an explicit knowledge-model decision should be added.

## Field Semantics by Atom Type

The common schema defines the same fields for every atom type, but the **meaning and expected content of those fields depend on the atom type**. This section is the semantic contract for extracting and maintaining atoms from knowledge sources.

The purpose is to prevent different atom types from using the same field for unrelated kinds of information while preserving one common schema for storage and processing.

### General rules

1. The field names and field count do not change between atom types.
2. A field should be populated only with information appropriate to its semantics for that atom type.
3. If a field has no meaningful content for a particular atom, use `null` or `[]` rather than inventing content merely for completeness.
4. Type-specific semantics do not create a type-specific schema. They only explain how the common fields are interpreted.
5. Source evidence takes priority over inferred completeness. Do not add unsupported definitions, structures, usages, constraints, examples, or relationships.
6. `extra` remains metadata and provenance; it must not be used to hide knowledge that belongs in the core fields.

### Field-role overview by type

| Type | `meaning` | `explanation` | `structure` | `usage` | `constraints` |
|---|---|---|---|---|---|
| `lexical_sense` | Relevant lexical sense | Semantic nuance, distinctions, and explanation | Lexical/syntactic pattern when meaningful | Contexts, functions, register, and typical use | Meaning, syntax, register, or selection restrictions | 
| `collocation` | Meaning/function of the combination | Why the combination works and what it expresses | Lexical or syntactic combination pattern | Contexts and functions where the combination is natural | Word choice, grammatical, or selection restrictions | 
| `phrasal_verb` | Meaning of the phrasal verb | Meaning, particle behavior, and important distinctions | Verb + particle pattern and object placement where relevant | Contexts, functions, and typical use | Transitivity, separability, object restrictions, register, or other limits | 
| `idiom` | Idiomatic meaning | Figurative meaning, interpretation, and important nuance | Fixed or semi-fixed form | Contexts, functions, and register | Fixedness, allowed variation, register, or usage restrictions | 
| `grammar` | Grammatical meaning/function | Detailed grammatical explanation and contrasts | Grammatical form/construction | Specific grammatical uses and contexts | Conditions, exclusions, exceptions, contrasts, and restrictions | 
| `word_formation` | Meaning/function of the derived form or formation | Formation process and semantic relationship between forms | Morphological formation pattern | Productive or contextual use of the formation | Formation restrictions, spelling changes, productivity limits, or semantic restrictions | 

The table is an overview. The detailed rules below take precedence when a type-specific question arises.

### `lexical_sense`

Represents one independently meaningful sense of a lexical item.

- `name`: The lexical item and, when useful, a concise sense label.
- `meaning`: The concise meaning of this specific sense, not the entire dictionary entry for the word.
- `mother_says`: A natural Vietnamese rendering of this sense.
- `explanation`: Semantic nuance, boundaries of the sense, and distinctions from nearby senses or near-synonyms when supported by evidence.
- `structure`: A meaningful lexical or syntactic pattern, such as a required complement or common construction. Use `null` when none is supported.
- `usage`: Contexts, situations, functions, register, and other information about when the sense is naturally used.
- `constraints`: Restrictions on meaning, syntax, register, selection, or interpretation that prevent common misuse.
- `examples`: Sentences or source examples that demonstrate this specific sense. Do not use an example of another sense merely because it contains the same word.
- `related_atoms`: Explicitly supported relationships to other senses, near-synonyms, contrasts, or other relevant atoms.

A `lexical_sense` atom should not combine multiple independently diagnosable senses merely because they share the same spelling or lemma.

### `collocation`

Represents a conventional lexical combination whose components have a meaningful relationship in use.

- `name`: The collocation in its canonical form.
- `meaning`: The meaning or communicative function of the combination as a whole when this is distinct from the meanings of its individual words.
- `mother_says`: A natural Vietnamese rendering of the relevant combined meaning or function.
- `explanation`: Why the combination is used as a unit, including relevant semantic or lexical nuance when supported.
- `structure`: The lexical/syntactic pattern, including slots or grammatical variation where useful, such as `make + a decision`.
- `usage`: Contexts and functions in which the collocation is natural.
- `constraints`: Selection restrictions, grammatical restrictions, or important lexical alternatives that affect correctness or naturalness.
- `examples`: Examples showing the combination in natural context.
- `related_atoms`: Component words, related collocations, contrasts, or other supported relationships.

Do not create a collocation atom merely because two words happen to occur next to each other in a source. The combination should be supported as a meaningful or conventional lexical relationship.

### `phrasal_verb`

Represents a verb-particle construction whose combined meaning or grammatical behavior is knowledge worth learning independently.

- `name`: The phrasal verb in its canonical form.
- `meaning`: The relevant meaning of the phrasal verb.
- `mother_says`: A natural Vietnamese rendering of that meaning.
- `explanation`: Semantic behavior, important nuances, and distinctions from similar verbs or phrasal verbs.
- `structure`: The verb + particle pattern, including transitivity, object placement, or separability when supported.
- `usage`: Contexts, functions, register, and typical situations of use.
- `constraints`: Transitivity, separability, pronoun placement, object restrictions, register, or other limitations.
- `examples`: Examples that demonstrate the phrasal verb and, where relevant, its structural behavior.
- `related_atoms`: Related verbs, particles, near-synonyms, contrasts, or other supported relationships.

Do not use `structure` to store general explanations of meaning; structural behavior belongs there, while semantic explanation belongs in `meaning` and `explanation`.

### `idiom`

Represents a conventional fixed or semi-fixed expression whose meaning cannot be fully derived from the literal meanings of its components.

- `name`: The canonical idiomatic expression.
- `meaning`: The concise idiomatic meaning.
- `mother_says`: A natural Vietnamese rendering of the idiomatic meaning, not necessarily a literal translation.
- `explanation`: Figurative interpretation, semantic nuance, and important contextual meaning.
- `structure`: The fixed or semi-fixed form, including variable slots or grammatical variation when supported.
- `usage`: Contexts, functions, register, and situations where the idiom is natural.
- `constraints`: Fixedness, allowed variation, grammatical restrictions, register, or contexts where the expression would be inappropriate.
- `examples`: Examples showing the idiom in natural context.
- `related_atoms`: Related idioms, contrasts, component relationships, or other explicitly supported links.

Literal examples should not be used as evidence for an idiomatic meaning unless the source explicitly treats the expression literally as well.

### `grammar`

Represents an independently diagnosable grammatical meaning, construction, contrast, or use.

- `name`: The grammatical construction or phenomenon being represented.
- `meaning`: The concise grammatical meaning or function.
- `mother_says`: Normally `null` under the current common schema.
- `explanation`: The detailed grammatical explanation needed to understand the construction, including important contrasts with related constructions when supported.
- `structure`: The grammatical form or construction pattern, such as `have/has + been + V-ing`.
- `usage`: The specific uses, contexts, or functions represented by the atom.
- `constraints`: Conditions, exclusions, exceptions, contrasts, or restrictions necessary for accurate use.
- `examples`: Source examples demonstrating the construction or use. Each example should support the specific grammatical atom represented.
- `related_atoms`: Related grammatical constructions, contrasts, dependencies, or lexical atoms where explicitly supported.

A grammar atom should represent a unit that can be independently diagnosed. Do not collapse distinct grammatical contrasts into one atom merely because they appear in the same textbook explanation.

### `word_formation`

Represents knowledge about how a word or lexical family member is formed and what the formation contributes to meaning or grammatical category.

- `name`: The formation or derived form being represented.
- `meaning`: The meaning or function contributed by the formation.
- `mother_says`: A natural Vietnamese rendering of the relevant meaning when useful.
- `explanation`: The relationship between the source form and derived form, including semantic or grammatical effects supported by evidence.
- `structure`: The morphological formation pattern, such as stem + suffix, including spelling or form changes when relevant.
- `usage`: Contexts or productive uses of the formation.
- `constraints`: Restrictions on productivity, spelling, semantic compatibility, grammatical category, or other formation limits.
- `examples`: Derived forms or source examples demonstrating the formation.
- `related_atoms`: Related forms in the same derivational family or explicitly supported morphological relationships.

A `word_formation` atom should represent an actual formation rule, relationship, or derived-form knowledge supported by the source, not merely a list of words that happen to share a root.

### Type-specific empty values

The common schema requires every field to remain present even when a field is not applicable.

Typical examples include:

```yaml
# Grammar
mother_says: null
```

```yaml
# Any type with no meaningful structural information
structure: null
```

```yaml
# No supported relationships
related_atoms: []
```

```yaml
# No source-level testing evidence
extra:
  is_tested: false
  test_evidence: []
```

These empty values mean **no applicable or supported information is currently represented**. They do not mean that the information is impossible to obtain or that the atom is deficient.

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
id: lex.assess.evaluate

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
id: gram.present-perfect-continuous.duration

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
