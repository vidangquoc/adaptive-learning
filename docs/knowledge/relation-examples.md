# Grammar Relation Atom Examples

## Purpose

This document is a design experiment for evaluating whether different kinds of relationships between Knowledge Atoms can reasonably share one grammar atom type:

`domain: grammar`
`type: relation`

Each example represents **knowledge about a relationship**, not the raw relationship itself.

The examples use the same common atom structure and include `relation_type`. For now, the example values are intentionally left blank (`null`); when an atom candidate is created, the AI may determine the appropriate `relation_type` from the source evidence. `relation_type` identifies the semantic nature of the relationship; it is not a subtype and does not identify participating atoms.

---

## Example 1 — Contrast between two grammar constructions

```yaml
id: grammar.relation.present_simple.present_continuous_contrast
domain: grammar
type: relation
relation_type: null

name: present simple vs present continuous
part_of_speech: null
pronunciation: null

meaning: The present simple and present continuous contrast in how they present situations, especially habitual or general situations versus situations occurring around the present time.
mother_says: null
explanation: This relationship helps distinguish two separately represented grammar constructions that can both describe present-time situations but normally encode different temporal perspectives.
structure: present simple ↔ present continuous

examples:
  - "She works in Ho Chi Minh City." ↔ "She is working from home today."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: contrast relation between two grammar atoms."
```

---

## Example 2 — Dependency between a construction and a required form

```yaml
id: grammar.relation.modal_verb.bare_infinitive
domain: grammar
type: relation
relation_type: null

name: modal verb + bare infinitive
part_of_speech: null
pronunciation: null

meaning: A modal verb is followed by a bare infinitive rather than an ordinary to-infinitive.
mother_says: null
explanation: The modal construction and the bare infinitive form are independently identifiable knowledge objects, while their relationship determines the form required after the modal.
structure: modal verb → bare infinitive

examples:
  - "She can swim."
  - "You must leave now."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: dependency/selection relation."
```

---

## Example 3 — Subject–verb agreement

```yaml
id: grammar.relation.subject.verb_agreement
domain: grammar
type: relation
relation_type: null

name: subject–verb agreement
part_of_speech: null
pronunciation: null

meaning: The form of a finite verb is determined by relevant grammatical features of its subject.
mother_says: null
explanation: The subject and the verb are separate grammatical elements, but the agreement relationship between them determines which verb form is appropriate.
structure: subject ↔ finite verb

examples:
  - "She works every day."
  - "They work every day."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: agreement relation."
```

---

## Example 4 — Negation dependency

```yaml
id: grammar.relation.negation.auxiliary
domain: grammar
type: relation
relation_type: null

name: negation with auxiliary
part_of_speech: null
pronunciation: null

meaning: In standard English, negation of many finite verb constructions is expressed through not attached to an auxiliary, with do-support required in relevant simple-present and simple-past cases.
mother_says: null
explanation: The negative marker and the auxiliary system interact; the relation determines how the negative construction is formed rather than merely describing either element independently.
structure: finite verb construction → auxiliary + not

examples:
  - "She does not work here."
  - "They have not finished."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: dependency/formation relation."
```

---

## Example 5 — Inversion in questions

```yaml
id: grammar.relation.question.auxiliary_subject_inversion
domain: grammar
type: relation
relation_type: null

name: auxiliary–subject inversion in questions
part_of_speech: null
pronunciation: null

meaning: In many English interrogative constructions, the auxiliary precedes the subject.
mother_says: null
explanation: The interrogative construction and the auxiliary/subject ordering are distinct knowledge objects, while their structural relationship determines the word order of the question.
structure: auxiliary → subject

examples:
  - "Are you ready?"
  - "Did she call?"

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: ordering relation."
```

---

## Example 6 — Compatibility between a tense/aspect construction and a time expression

```yaml
id: grammar.relation.present_perfect.since
domain: grammar
type: relation
relation_type: null

name: present perfect with since
part_of_speech: null
pronunciation: null

meaning: The present perfect can combine with since to relate a situation continuing to the present to the point when it began.
mother_says: null
explanation: The relation connects the interpretation of the present perfect with the temporal function of since. Neither atom alone fully represents the fact that this combination expresses a starting point continuing toward the present.
structure: present perfect + since + starting point

examples:
  - "I have lived here since 2020."
  - "She has worked there since January."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: construction–marker compatibility relation."
```

---

## Example 7 — Form relation between comparative and than

```yaml
id: grammar.relation.comparative.than
domain: grammar
type: relation
relation_type: null

name: comparative + than
part_of_speech: null
pronunciation: null

meaning: A comparative construction commonly uses than to introduce the entity or quantity against which the comparison is made.
mother_says: null
explanation: The comparative form and than have distinct grammatical roles, but their relationship creates the standard comparative structure.
structure: comparative form + than + comparison target

examples:
  - "This book is cheaper than that one."
  - "She runs faster than me."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: structural compatibility relation."
```

---

## Example 8 — Condition/result relationship

```yaml
id: grammar.relation.conditional.consequence
domain: grammar
type: relation
relation_type: null

name: conditional clause and consequence
part_of_speech: null
pronunciation: null

meaning: A conditional clause establishes a condition whose fulfillment or hypothetical status is related to the proposition expressed by the consequence clause.
mother_says: null
explanation: The two clauses are independently meaningful, but the conditional relationship between them determines how the whole sentence connects a condition with its consequence.
structure: condition → consequence

examples:
  - "If it rains, we will stay home."
  - "If I had more time, I would travel."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: semantic dependency relation."
```

---

## Example 9 — Substitution relationship between forms

```yaml
id: grammar.relation.subject.pronoun_agreement
domain: grammar
type: relation
relation_type: null

name: subject pronoun and verb-form selection
part_of_speech: null
pronunciation: null

meaning: In constructions with present-tense be and in relevant present-tense verb forms, the subject pronoun influences which finite verb form is selected.
mother_says: null
explanation: The relation connects subject-person/number information with the selection of an appropriate finite verb form.
structure: subject pronoun features → finite verb form

examples:
  - "I am ready."
  - "He is ready."
  - "They are ready."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: feature-to-form selection relation."
```

---

## Example 10 — Coordination relationship

```yaml
id: grammar.relation.coordinate_clauses.and
domain: grammar
type: relation
relation_type: null

name: coordinated clauses with and
part_of_speech: null
pronunciation: null

meaning: The conjunction and can connect coordinated clauses or other coordinated constituents of equal grammatical status.
mother_says: null
explanation: The individual constituents remain separate grammar objects, while the coordination relationship describes how they are combined into a larger structure.
structure: constituent A + and + constituent B

examples:
  - "She called me and I answered."
  - "He opened the door and walked inside."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Design example: combination/coordination relation."
```

---

## Observation target

> Note: `relation_type` values are intentionally left blank in these design examples for now. The AI may determine the value when creating an atom candidate from source evidence. A canonical controlled vocabulary has not yet been finalized.


These examples deliberately cover different relational behaviors:

- contrast;
- dependency;
- agreement;
- ordering;
- compatibility;
- feature-to-form selection;
- semantic condition/consequence;
- combination/coordination.

They all use the same:

```yaml
domain: grammar
type: relation
```

The experiment is intended to answer two separate questions:

1. Is `relation` a coherent **knowledge type** despite the relationships having different semantic behaviors?
2. If yes, what additional representation is needed to identify the atoms participating in the relation without creating a subtype taxonomy?

This file does not attempt to settle the second question.
