# Step 7 — Define the physical data architecture

This is a temporary working document for Step 7.

Step 7 will be resolved one issue at a time. This document records the questions that must be discussed and the decisions we make. It is not a canonical specification.

## 7.1 Physical location of Knowledge Atom stores

**Decision: FINALIZED**

Official:
```text
data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atoms.md
```

Candidates:
```text
data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atom_candidates.md
```

Rules:
- `<source-id>` is the canonical `source_id` from the Source Registry.
- `<segment-id>` is the canonical `segment_id` from source segmentation.
- `<domain>` is the Knowledge Atom domain.
- The path is storage organization, not semantic atom identity.
- No additional `official/` or `candidates/` directory layer.

## 7.2 Physical representation of Candidate Atoms

**Decision: FINALIZED — Option A**

`knowledge_atom_candidates.md` is a Markdown collection containing multiple fenced YAML blocks. Each YAML block represents exactly one complete Candidate Atom and directly corresponds to `schemas/candidate-atom.schema.json`.

Rules:
- The file may contain multiple Candidate Atoms.
- Each Candidate Atom is represented by one fenced YAML block.
- Each YAML block contains the complete Candidate Atom; there is no partial or presentation-only representation.
- There is no collection-level YAML wrapper such as `candidates:`.
- `review_status` is a top-level lifecycle field in each Candidate Atom and is not placed under `extra`.
- A newly created Candidate starts with `review_status: pending`.
- The YAML content of each block must validate as one Candidate Atom against `schemas/candidate-atom.schema.json`.
- Markdown headings may identify or separate atoms for human review, but they are not part of the atom data and are not an alternative schema.

## 7.3 Physical representation of Official Atoms

**Decision: FINALIZED — Option A**

`knowledge_atoms.md` is a Markdown collection containing multiple fenced YAML blocks. Each YAML block represents exactly one complete Official Atom and directly corresponds to `schemas/official-atom.schema.json`.

Rules:
- The file may contain multiple Official Atoms.
- Each Official Atom is represented by one fenced YAML block.
- Each YAML block contains the complete Official Atom; there is no partial or presentation-only representation.
- There is no collection-level YAML wrapper such as `atoms:`.
- Official Atoms have no lifecycle field such as `official_status`.
- The YAML content of each block must validate as one Official Atom against `schemas/official-atom.schema.json`.
- Markdown headings may identify or separate atoms for human review, but they are not part of the atom data and are not an alternative schema.
- An Official Atom keeps the same semantic ID as the Candidate from which it was officialized.

Officialization is a storage transition:

```text
Candidate YAML block
        │
        │ officialize
        ▼
Official YAML block
        │
        ▼
knowledge_atoms.md
```

Candidate and Official physical representations are therefore the same except that a Candidate has the top-level `review_status` lifecycle field.

Status: FINALIZED

## 7.4 Source provenance and evidence in stored atoms

**Decision: FINALIZED**

The canonical provenance and assessment fields are persisted directly in every stored atom, using the common atom structure.

The persisted structure is:

```yaml
extra:
  source:
    origin:
      - source_id: destination-c1-c2
        segment_id: <segment-id>
        location:
          page: <page>
          section: <section>
          line: <line>
    atom_decision:
      - source_id: destination-c1-c2
        segment_id: <segment-id>
        location:
          page: <page>
          section: <section>
          line: <line>
  is_tested: true
  test_evidence:
    - "Exercise A, item 5, line 100"
  notes: null
```

Rules:
- `extra.source.origin` records where the knowledge point originates.
- `extra.source.atom_decision` records the source evidence supporting the decision to represent the knowledge point as a Knowledge Atom.
- Each provenance entry references the canonical `source_id` and `segment_id`; location fields are optional.
- `source_id` is resolved through the Source Registry. The atom does not store a repository path to the source artifact.
- `extra.is_tested` is `true` when the Atom is directly tested or practised in the learning material, and `false` otherwise.
- An exercise may test multiple Atoms; each directly tested Atom may therefore have `is_tested: true` and may reference the same test location.
- `extra.test_evidence` records locations in the learning material where the Atom is directly tested or practised.
- `source.origin`, `source.atom_decision`, `is_tested`, and `test_evidence` are provenance/assessment metadata, not knowledge content and do not affect semantic identity.
- When a collection is structurally required but there is no applicable evidence, use an empty array `[]`; do not omit the field.
- `notes` may be `null` when there is no note.

Status: FINALIZED

## 7.5 Learner review data

**Decision: FINALIZED**

Each learner has exactly one review-data file:

```text
data/learners/<learner-id>/review-data.yaml
```

`review-data.yaml` contains only the learner's **latest review state**. It does not store attempts or review history.

Each review record contains exactly these fields:

```yaml
- atom_id:
  total_review_times:
  effective_review_times:
  last_review_date:
  next_review_date:
```

Field semantics:
- `atom_id` identifies the Knowledge Atom being tracked.
- `total_review_times` is the total number of times the learner has reviewed the Atom, regardless of whether the learner answered correctly or incorrectly.
- `effective_review_times` is the number of times the learner answered the question correctly when that question was presented to test the Atom.
- `last_review_date` stores the date and time of the learner's most recent review.
- `next_review_date` stores the calendar date on which the Atom is scheduled for its next review.

Rules:
- Review data references Knowledge Atoms by `atom_id`; it does not copy Atom content.
- `last_review_date` is a datetime; `next_review_date` is a date only.
- Attempts and historical review records are outside the scope of `review-data.yaml`.
- Review data is learner-specific and may change as the learner performs reviews.


- A Knowledge Atom is reviewed as one unit: the review checks whether the learner remembers the Atom; no separate recognition, recall, usage, collocation, discrimination, transfer, or retention dimensions are stored for an Atom.

Status: FINALIZED

## 7.6 Data format and validation strategy

### 7.6.1 Persisted data format

**Decision: FINALIZED**

YAML is the persistence format for the project's structured persisted data, including Knowledge Atoms and learner review data.

### 7.6.2 Schema validation scope

**Decision: FINALIZED**

Learner review data has its own JSON Schema:

`schemas/review-data.schema.json`

The schema defines `review-data.yaml` as a top-level YAML sequence. Each item is one learner review record containing exactly:
- `atom_id`
- `total_review_times`
- `effective_review_times`
- `last_review_date`
- `next_review_date`

The schema enforces:
- no additional fields in a review record;
- non-negative integer review counts;
- `last_review_date` as `date-time`;
- `next_review_date` as `date`.

The semantic integrity rule `effective_review_times <= total_review_times` remains a data-integrity rule and is not encoded using non-standard JSON Schema features.

Status: PARTIALLY FINALIZED

### 7.6.3 Independent validation of stored Knowledge Atoms

**Decision: FINALIZED**

Each Knowledge Atom stored in a collection must be validated independently against the schema corresponding to its store:
- Candidate Atom → `schemas/candidate-atom.schema.json`
- Official Atom → `schemas/official-atom.schema.json`

A collection file such as `knowledge_atoms.md` is not itself validated as one Atom or one YAML document. Its individual YAML blocks are extracted and validated one by one.

Status: FINALIZED

## 7.7 Scripts and pipeline integration

After the storage model is settled, identify required changes to:
- extraction scripts;
- validation scripts;
- candidate creation;
- review/promotion;
- officialization.

Do not change scripts before the underlying storage model is agreed.

Status: OPEN

## 7.8 Documentation synchronization

After decisions are finalized, update only the canonical documents that are actually affected.

Potential documents:
- `docs/knowledge/overall.md`
- `docs/knowledge/atom-structure.md`
- `docs/knowledge/atom-pipeline.md`
- `docs/knowledge/atom-types.md`
- `docs/learner/learning-state.md`
- relevant learning-material principles/procedures
- `README.md`

Status: OPEN

## 7.9 Final Step 7 verification

Verify:
- physical stores match the agreed architecture;
- schemas match stored data;
- pipeline references are consistent;
- no obsolete paths or structures remain;
- canonical documentation is synchronized.

Status: OPEN
