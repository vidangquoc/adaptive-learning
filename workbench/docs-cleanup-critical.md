# Critical Documentation / Architecture Issues

> This workbench file tracks the five core architecture issues found during the full documentation consistency audit.
>
> These issues affect the canonical data model, representation, or invariants and should be resolved before treating the affected architecture as complete.
>
> Resolved decisions must be transferred to the appropriate canonical documentation and schemas.

## 1. Define Representation and Identity for AI-Created Challenges

### Problem

The current model says that source-derived Challenges have source provenance and source-occurrence identity, while AI-created/source-independent Challenges may exist without a source.

At the same time, the Candidate and Official Challenge schemas require `extra.source` and all of its source-specific fields.

### Current inconsistency

Source-derived Challenge identity is:

```text
<source-id>_<segment-id>_<exercise>_<item-number>
```

and the schemas require:

```yaml
extra:
  source:
    source_id:
    page_number:
    segment_id:
    exercise_name:
    item_number:
```

An AI-created Challenge without a source occurrence cannot legitimately provide these fields.

### What must be decided

Define the canonical model for source-independent / AI-created Challenges, including:

- Challenge identity and ID format when there is no source occurrence;
- whether source provenance is optional at the schema level or conditionally required only for source-derived Challenges;
- what metadata distinguishes generated Challenges from source-derived Challenges;
- whether the same Candidate/Official physical representation is retained for both kinds;
- whether generated Challenges need a different identity component or generation metadata;
- how officialization and later correction work for AI-created Challenges;
- whether a source-independent Challenge may be persisted as Official without external/source provenance.

### Acceptance condition

The Challenge conceptual documentation and Candidate/Official schemas agree on one representation for both source-derived and AI-created Challenges, with source-specific provenance required exactly when a Challenge is derived from a source.

---

## 2. Define Provenance for Source-Stated vs Inferred Atom Attributes

### Problem

The Knowledge Atom documentation requires inferred attributes to remain distinguishable from attributes explicitly supported by the source.

The current Atom schemas do not provide a representation for that distinction.

### Current inconsistency

The docs discuss:

- source-stated attributes;
- contextually inferred attributes;
- evidence supporting those interpretations.

But the canonical atom fields remain ordinary scalar values such as:

```yaml
meaning:
part_of_speech:
pronunciation:
structure:
```

The `extra.source.origin` and `extra.source.atom_decision` structures provide source provenance for the Atom, but they do not identify which individual field is inferred versus explicitly stated.

### What must be decided

Define how attribute-level provenance or evidence status is represented, or explicitly decide that the distinction belongs only in review/evidence records rather than in the persisted Atom itself.

The decision must cover:

- which fields require source-stated/inferred distinction;
- whether the distinction is persisted;
- how multiple supporting sources are represented;
- how a reviewer can determine why a field has its current value;
- how generated enrichment is distinguished from source-grounded content.

### Acceptance condition

The canonical Atom representation either preserves the required source-stated/inferred distinction in a defined machine-readable way, or the documentation is changed to no longer require a distinction that the canonical representation does not preserve.

---

## 3. Define Participating Atom References for Relation Atoms

### Problem

A `relation` Atom represents knowledge about a relationship between two or more independent Knowledge Atoms, but the current canonical structure does not define how the participating Atoms are identified.

### Current inconsistency

The model deliberately rejected a generic `related_atoms` graph field.

However, the current relation examples identify participants only through free text such as:

```yaml
name: present perfect vs simple past
structure: present perfect ↔ simple past
```

Neither the schema nor the canonical structure defines a structured participant reference.

### What must be decided

Define the canonical representation of relation participants while preserving the distinction between:

- knowledge about a relationship; and
- arbitrary graph edges.

The decision must specify:

- whether relation participants are persisted;
- the field name and shape, if persisted;
- whether participant order is semantically meaningful;
- whether a relation may involve two or more participants;
- how relation identity incorporates participant information, if at all;
- how participant IDs are validated against the Knowledge Atom store.

### Acceptance condition

Every valid relation Atom has a canonical, machine-readable way to identify the independent Atoms participating in the learned relationship, without reintroducing an unspecified generic graph model.

---

## 4. Make Example Provenance Representable

### Problem

The Atom documentation says examples may be source-derived or generated and that their provenance must remain distinguishable.

The current schema stores examples only as strings.

### Current inconsistency

Current representation:

```yaml
examples:
  - "..."
  - "..."
```

The schema therefore cannot tell which example came from the source and which was generated.

Atom-level `extra.source` provenance does not provide provenance for individual examples.

### What must be decided

Define the canonical representation for examples and their provenance, including:

- whether each example needs an origin marker;
- whether source references attach to individual examples;
- whether generated examples require generation metadata;
- whether the distinction is required for every example or only for source-derived examples;
- how the representation remains compatible with the shared Atom structure.

### Acceptance condition

The canonical representation either makes example origin machine-readable, or the documentation no longer requires a distinction that cannot be represented.

---

## 5. Fix the Challenge True/False Representation to Match the Schema

### Problem

The Challenge Structure documentation gives a True/False example using YAML booleans, while both Challenge schemas require string options and string answers.

### Current inconsistency

The documentation currently shows:

```yaml
options:
  - true
  - false
answer: true
```

Under YAML semantics, these are boolean values, but the schema requires strings.

### Required correction

The canonical example must use strings:

```yaml
options:
  - "true"
  - "false"
answer: "true"
```

The surrounding documentation should continue to state that True/False is not a separate Challenge type or form.

### Acceptance condition

Documentation examples and both Challenge schemas accept exactly the same True/False representation.
