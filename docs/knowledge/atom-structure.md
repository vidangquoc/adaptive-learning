# Knowledge Atom Structure

## Purpose

This document defines the common structure for all knowledge atoms in Adaptive Learning.

All knowledge atom types use the same field names and structure. Fields that do not apply to a particular atom type remain present and use an appropriate empty value such as `null` or `[]` rather than introducing a different structure.

Learner mastery and learner state do not belong in a knowledge atom.

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

## Core field semantics

### `id`

A unique, stable identifier for the atom. IDs should use semantic components rather than arbitrary sequential numbers whenever a broader concept has multiple atoms.

General pattern:

```text
<domain>.<concept>.<case>
```

The final `case` is the semantic distinction that separates atoms representing the same broader concept or situation. It is not tied to a particular schema field such as `usage`.

Examples:

```yaml
id: gram.present-perfect-continuous.duration
id: gram.present-perfect-continuous.continuing-activity
id: gram.present-perfect-continuous.recently-stopped-activity
id: lex.compelling
```

Avoid arbitrary identifiers such as `gram.present-perfect-continuous.01` and `.02`.

### `domain`

The high-level knowledge domain. Current values are:

- `vocabulary`
- `grammar`

### `type`

The specific kind of knowledge represented by the atom, for example:

- `lexical_sense`
- `collocation`
- `phrasal_verb`
- `idiom`
- `grammar`
- `word_formation`

It describes the knowledge itself, not learner performance or assessment format.

### `subtype`

A finer classification within `type` when useful and supported. Use `null` when no meaningful subtype is needed.

### `name`

The concise, stable name of the knowledge object the atom describes.

Examples: `assess`, `present perfect continuous`, `strike a balance`.

### `meaning`

A concise description of the relevant meaning or grammatical function. Further teaching detail belongs in `explanation`.

### `mother_says`

The learner-facing Vietnamese expression of the relevant meaning. This is the only field intentionally written in the learner's mother tongue. For grammar atoms, use `null` under the common schema.

### `explanation`

The fuller explanation needed to understand, teach, distinguish, or diagnose the atom beyond the concise `meaning`.

### `structure`

The structural, formal, or pattern representation of the knowledge. Examples include `assess + noun`, `have/has + been + V-ing`, or a lexical frame. Use `null` when no meaningful structure applies.

### `usage`

The contexts, situations, functions, or conditions in which the knowledge is used. It describes knowledge use, not how frequently the learner has used it.

### `constraints`

Restrictions, conditions, exceptions, distinctions, or limitations needed for accurate use.

### `examples`

Examples demonstrating the knowledge. Source-derived examples remain evidence; generated practice examples must not be mistaken for source evidence. Use `[]` when none is available or appropriate.

### `related_atoms`

Zero or more explicit relationships to other atoms:

```yaml
related_atoms:
  - id: lex.assume
    relation: contrasts_with
  - id: lex.infer
    relation: related_to
```

The relationship is not ancestry and does not imply inherited mastery.

## `extra`

`extra` contains provenance, testing, validation, and maintenance metadata rather than the knowledge itself.

### `extra.source`

Preserve enough provenance to trace the atom to its source evidence, including source ID/type, Unit, location, and relevant evidence when available.

### `extra.is_tested`

A boolean indicating whether the source explicitly tests or practises the atom. It is **source-level evidence**, not learner mastery.

### `extra.test_evidence`

The exercise, question, task, or other source location supporting `is_tested`. Use an empty list when the source does not explicitly test or practise the atom.

### `extra.notes`

Maintenance or extraction notes that do not belong in the core knowledge fields. Do not hide learner state or unsupported knowledge claims here.

## Type-specific semantics

The common structure is shared across all atom types, while the content of the fields depends on the type:

| Type | `meaning` | `explanation` | `structure` | `usage` | `constraints` |
|---|---|---|---|---|---|
| `lexical_sense` | Relevant sense | Semantic nuance and boundaries | Lexical/syntactic pattern if applicable | Contexts/functions | Semantic/syntactic/usage limits |
| `collocation` | Meaning/function of combination | Why/how it works | Lexical or syntactic pattern | Context/register | Combination or grammatical restrictions |
| `phrasal_verb` | Combined meaning | Semantic behavior/distinctions | Verb + particle/preposition | Context/functions | Transitivity/separability/register etc. |
| `idiom` | Idiomatic meaning | Figurative interpretation | Fixed/semi-fixed form | Context/register | Fixedness/variation restrictions |
| `grammar` | Grammatical meaning/function | How the construction works | Grammatical form | Situations/functions | Conditions/exceptions/contrasts |
| `word_formation` | Meaning/function of formation | How the formation works | Morphological pattern | Productive/contextual use | Formation/spelling/category restrictions |

## Representation rules

1. Use one common schema across atom types.
2. One lexical sense is one atom by default.
3. Independently useful grammar uses, constructions, rules, constraints, and contrasts may be separate atoms.
4. Use properties and relations instead of creating atoms for information that merely describes an existing atom.
5. Preserve source evidence and provenance.
6. Do not fabricate definitions, pronunciation, examples, patterns, CEFR, domains, or relationships.
7. Learner mastery, attempts, confidence, retention, review state, and progress belong in the learner layer.
8. `is_tested` means source-level testing/practice evidence, not mastery.
9. Static atom meaning must remain independent of learner state.
