# Open Architectural Issues

> This workbench file tracks the remaining architecture issue identified during the documentation consistency review.
>
> Resolved architecture decisions belong in the appropriate canonical documentation, not here.

## 1. Define Representation and Identity for AI-Created Challenges

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