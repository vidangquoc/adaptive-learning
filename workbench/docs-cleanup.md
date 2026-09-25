# Open Architectural Issues

> This workbench file tracks the two architecture issues identified during the documentation consistency review.
>
> These issues require a design decision before the affected canonical specifications are changed.

## 1. Define the boundary and coordination of simultaneous Knowledge Atom and Challenge extraction

### Problem

Knowledge Atom extraction and Challenge extraction occur **simultaneously from the same contextual analysis of a Source Segment**. They are not two independent pipelines that must run sequentially or wait for one another to finish.

During analysis of a Segment, the process may identify both:

```text
Knowledge findings
Assessment occurrences
```

and use the relationship between them to establish which Knowledge Atom a Challenge assesses.

The current documents, however, blur this architecture by describing Knowledge Atom Candidates as an output of the Challenge Extraction Pipeline while also implying that Challenge Extraction should merely consume already-created Atoms.

Neither extreme is the intended model.

### Correct architectural principle

The extraction process should be understood as **one contextual analysis process with two related outputs**:

```text
Source Segment
      ↓
Shared contextual analysis
      ├── Knowledge Atom Candidates
      └── Challenge Candidates
                     │
                     └── target_atom_id
```

The fact that a Knowledge Atom already exists before a Challenge is analyzed is not a prerequisite.

When analysis identifies the knowledge assessed by a Challenge:

```text
existing Official Atom
        or
existing Candidate Atom
        or
new Knowledge Atom identified from the same context
```

the Challenge uses that Atom's semantic ID as `target_atom_id`.

Creating a new Candidate Atom in this situation does **not** mean inventing an Atom to fill the target field. The Atom must be inferred from the source context and must satisfy the canonical Knowledge Atom ontology, structure, semantic identity, provenance, and governance rules.

Challenge evidence may therefore reveal knowledge that is not yet represented elsewhere, and that knowledge can be created as a Candidate during the same contextual analysis.

### What must be decided

Define the precise contract for this simultaneous process, including:

- how the shared contextual analysis identifies knowledge findings and assessment occurrences together;
- how an identified knowledge finding becomes a Candidate Atom under the canonical Knowledge Atom rules;
- how the Challenge obtains the semantic ID of an existing or newly created Atom;
- what happens when the context is insufficient to determine the single target Atom reliably;
- how evidence discovered through the Challenge contributes to the Atom Candidate without allowing the Challenge to fabricate the Atom;
- where the coordination rule is canonically documented.

### Acceptance condition

The canonical documentation must describe Knowledge Atom and Challenge extraction as simultaneous, context-sharing activities rather than independent sequential pipelines.

The one-Challenge-to-one-Atom invariant must remain mandatory. A Challenge may target an existing Atom or an Atom Candidate created from the same contextual analysis, but it must never invent a Knowledge Atom merely to satisfy `target_atom_id`.

Knowledge Atom creation remains governed by the Knowledge Atom ontology, structure, identity, and review/officialization rules even when the Candidate is created during Challenge analysis.

---

## 2. Define Representation and Identity for AI-Created Challenges

### Problem

The current model says that source-derived Challenges must have source provenance and source-occurrence identity, while AI-created/source-independent Challenges may exist without a source.

At the same time, the current Candidate and Official Challenge schemas require `extra.source` and all of its source-specific fields.

Therefore the model does not yet provide a consistent physical representation for AI-created Challenges.

### Current inconsistency

Source-derived Challenge identity is currently:

```text
<source-id>_<segment-id>_<exercise>_<item-number>
```

and the schemas require source-specific provenance under `extra.source`:

```yaml
extra:
  source:
    source_id:
    page_number:
    segment_id:
    exercise_name:
    item_number:
```

But AI-created Challenges may legitimately have no source occurrence and therefore cannot provide those fields.

### What must be decided

Define the canonical model for source-independent / AI-created Challenges, including:

- Challenge identity and ID format when there is no source occurrence;
- whether source provenance is optional at the schema level or conditionally required only for source-derived Challenges;
- what metadata distinguishes generated Challenges from source-derived Challenges;
- whether the same Candidate/Official physical representation is retained for both kinds;
- whether generated Challenges need a different identity component or generation metadata;
- how officialization and later correction work for AI-created Challenges;
- whether any source-independent Challenge may be persisted as Official without external/source provenance.

### Acceptance condition

The Challenge conceptual documentation and Candidate/Official schemas must agree on one representation for both source-derived and AI-created Challenges, with source-specific provenance required exactly when a Challenge is derived from a source.

The final identity and lifecycle rules must be explicit and must not force fabricated source metadata onto AI-created Challenges.