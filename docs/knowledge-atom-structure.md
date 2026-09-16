# Knowledge Atom Structure

## Purpose

This document defines the common structure for all knowledge atoms in Adaptive Learning.

All knowledge atom types use the same field names and structure. Fields that do not apply to a particular atom type should remain present and use an appropriate empty value such as `null` or `[]` rather than introducing a different structure.

The structure separates the knowledge represented by an atom from additional metadata and provenance. Learner mastery and learner state do not belong in a knowledge atom.

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

## Field Semantics by Atom Type

The common structure is shared across all atom types, but the meaning and expected content of individual fields depend on the type of knowledge being represented.

The purpose of this section is to define those type-specific semantics so that extraction remains consistent without creating a different schema for each atom type.

### Overview

| Type | `meaning` | `explanation` | `structure` | `usage` | `constraints` |
|---|---|---|---|---|---|
| `lexical_sense` | Relevant lexical sense | Semantic nuance and boundaries | Optional lexical/syntactic pattern | Contexts and functions | Semantic, syntactic, or usage limits |
| `collocation` | Meaning/function of the combination | Why/how the combination works | Lexical or syntactic pattern | Contexts in which the combination occurs | Combination, word-choice, or grammatical restrictions |
| `phrasal_verb` | Meaning of the phrasal verb | Semantic behavior and distinctions | Verb + particle/preposition pattern | Contexts and functions | Transitivity, separability, register, or other restrictions |
| `idiom` | Idiomatic meaning | Figurative meaning and interpretation | Fixed or semi-fixed form | Contexts and register | Fixedness, variation, or usage restrictions |
| `grammar` | Grammatical meaning/function | How the grammatical system works | Grammatical form/construction | Situations and functions | Conditions, exceptions, contrasts, or form restrictions |
| `word_formation` | Meaning/function of the derived form or formation | How the formation works | Morphological pattern | Productive or contextual use | Formation, spelling, category, or productivity restrictions |

The table is a quick reference. The detailed rules below take precedence when a field needs type-specific interpretation.

### `lexical_sense`

A `lexical_sense` represents one independently meaningful sense of a lexical item.

- `name`: the lemma or lexical item identifying the sense.
- `meaning`: the concise meaning of this specific sense.
- `mother_says`: a natural Vietnamese expression of the relevant sense.
- `explanation`: semantic nuance, boundaries, and distinctions needed to understand this sense accurately.
- `structure`: a lexical or syntactic pattern when the sense has a meaningful one; otherwise `null`.
- `usage`: contexts, functions, register, or typical situations supported by the source.
- `constraints`: restrictions or distinctions that prevent incorrect use or confusion with another sense.
- `examples`: examples that demonstrate this specific sense.
- `related_atoms`: other senses or knowledge items with an evidenced semantic or structural relationship.

Do not combine multiple independently diagnosable senses into one atom merely because they share the same spelling or lemma.

### `collocation`

A `collocation` represents a conventional combination of words whose relationship is useful as an independently learnable knowledge item.

- `name`: the collocation itself.
- `meaning`: the meaning or function of the combination when it cannot be adequately represented by treating the words independently.
- `mother_says`: a natural Vietnamese rendering of the relevant combined meaning when useful.
- `explanation`: why the combination is conventional, what it conveys, or how it differs from plausible alternatives when the source provides such information.
- `structure`: the lexical or syntactic pattern of the combination.
- `usage`: contexts, functions, register, and situations in which the collocation is used.
- `constraints`: restrictions on word choice, grammatical form, variation, or contexts.
- `examples`: examples showing the collocation in natural use.
- `related_atoms`: component lexical items or other collocations that are explicitly related.

Do not create a collocation merely because two words happen to co-occur in a source example. The combination should have evidence of being treated as a meaningful or conventional unit.

### `phrasal_verb`

A `phrasal_verb` represents a verb-particle or verb-preposition construction whose combined meaning or grammatical behavior is independently relevant.

- `name`: the phrasal verb.
- `meaning`: its combined meaning.
- `mother_says`: a natural Vietnamese rendering of that meaning.
- `explanation`: semantic behavior, nuance, or distinctions from related verbs/phrasal verbs.
- `structure`: the verb + particle/preposition pattern, including separability or complement pattern when supported.
- `usage`: contexts, functions, register, and typical situations.
- `constraints`: transitivity, separability, object placement, preposition/particle requirements, register, or other restrictions.
- `examples`: examples demonstrating the construction and its grammatical behavior.
- `related_atoms`: related verbs, particles, phrasal verbs, or contrasting expressions.

### `idiom`

An `idiom` represents a conventional expression whose overall meaning is not adequately derived from the literal meanings of its individual words.

- `name`: the idiomatic expression.
- `meaning`: its idiomatic meaning.
- `mother_says`: a natural Vietnamese explanation or equivalent where appropriate.
- `explanation`: the figurative interpretation and relevant nuance.
- `structure`: the fixed or semi-fixed form of the expression.
- `usage`: contexts, functions, register, and typical situations.
- `constraints`: fixedness, permitted variation, grammatical restrictions, register, or conditions of use.
- `examples`: examples showing natural use of the idiom.
- `related_atoms`: semantically or structurally related expressions.

### `grammar`

A `grammar` atom represents an independently diagnosable grammatical meaning, function, construction, contrast, or usage pattern.

- `name`: the grammatical construction or phenomenon.
- `meaning`: the concise grammatical meaning or function.
- `mother_says`: `null` under the current common schema.
- `explanation`: the detailed grammatical explanation needed to understand the construction and distinguish it from related constructions.
- `structure`: the grammatical form or construction pattern.
- `usage`: the situations, functions, discourse contexts, or temporal relationships in which the construction is used.
- `constraints`: form restrictions, conditions, exceptions, contrasts, or cases where another construction is required or preferred.
- `examples`: examples demonstrating the construction or contrast.
- `related_atoms`: grammatically related, contrasting, broader, narrower, or prerequisite atoms.

A grammar atom should represent a knowledge distinction that can be independently diagnosed or taught. Do not collapse distinct grammatical uses into one atom merely because they share a surface form when the source treats them as meaningfully different.

### `word_formation`

A `word_formation` atom represents knowledge about how words are formed, transformed, or related through morphological processes.

- `name`: the formation pattern, derivational relationship, or word-formation phenomenon.
- `meaning`: the meaning or function contributed by the formation.
- `mother_says`: a natural Vietnamese explanation where useful.
- `explanation`: how the formation works and what semantic or grammatical effect it produces.
- `structure`: the morphological pattern, such as affix + base or a transformation pattern.
- `usage`: contexts or productive uses supported by the source.
- `constraints`: restrictions on bases, word classes, spelling, meaning, productivity, or other formation conditions.
- `examples`: examples of the formation in use.
- `related_atoms`: related bases, derived forms, affixes, or contrasting formation patterns.

Do not use `word_formation` as a general-purpose category for vocabulary relationships that are not actually about word formation.

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
