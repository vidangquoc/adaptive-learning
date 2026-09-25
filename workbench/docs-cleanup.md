# Open Architectural Issues

> This workbench file tracks the two architecture issues identified during the documentation consistency review.
>
> These issues require a design decision before the affected canonical specifications are changed.

## 1. Separate Challenge Extraction from Knowledge Atom Extraction

### Problem

The current Challenge Extraction documents still describe Challenge Extraction and Knowledge Atom extraction as sharing the same contextual analysis, and the Challenge Extraction Pipeline currently produces both Knowledge Atom Candidates and Challenge Candidates.

That is inconsistent with the current architecture:

> **Knowledge Atoms are not part of the Challenge Extraction Pipeline.**

Challenge extraction must remain focused on extracting and validating Challenges and their single target_atom_id.

### Current inconsistency

docs/assessment/challenge-extraction/pipeline.md currently contains a flow in which contextual analysis produces:

```text
Knowledge Atom Candidates
Exercise Items
      ↓
Challenge Candidates
```

docs/assessment/challenge-extraction/principles.md likewise states that a Challenge may identify or create a Knowledge Atom during the same analysis.

### What must be decided

Define the boundary and coordination between the two pipelines, including:

- how Challenge Extraction obtains target_atom_id;
- whether the target Atom must already exist as Candidate or Official before a Challenge Candidate is emitted;
- how a Challenge that reveals previously unidentified knowledge is handed to the Knowledge Atom pipeline;
- how the two pipelines share contextual evidence without making Knowledge Atom creation an output of Challenge Extraction;
- which document owns the coordination rule.

### Acceptance condition

The canonical Challenge Extraction documentation must no longer define Knowledge Atom Candidates as an output of Challenge Extraction or imply that Challenge Extraction creates Knowledge Atoms.

The final design must preserve the one-Challenge-to-one-Atom invariant while keeping Knowledge Atom creation in the Knowledge pipeline.

---

## 2. Define Representation and Identity for AI-Created Challenges

### Problem

The current model says that source-derived Challenges must have source provenance and source-occurrence identity, while AI-created/source-independent Challenges may exist without a source.

At the same time, the current Candidate and Official Challenge schemas require extra.source and all of its source-specific fields.

Therefore the model does not yet provide a consistent physical representation for AI-created Challenges.

### Current inconsistency

Source-derived Challenge identity is currently:

```text
<source-id>_<segment-id>_<exercise>_<item-number>
```

and the schemas require source-specific provenance under extra.source:

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