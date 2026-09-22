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

Example:

```markdown
## vocabulary.lexical_sense.assume.verb

```yaml
id: vocabulary.lexical_sense.assume.verb
domain: vocabulary
type: lexical_sense
name: assume
part_of_speech: verb
pronunciation: /əˈsuːm/
meaning: ...
mother_says: giả định
explanation: ...
structure: ...
examples: []
extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: null
review_status: pending
```
```

This representation keeps Candidate data human-reviewable while preserving a direct machine-validation boundary at the individual atom block.

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

Confirm how the existing canonical fields are physically persisted:
- `extra.source.origin`
- `extra.source.atom_decision`
- `extra.is_tested`
- `extra.test_evidence`

Questions:
- Are these stored directly in every atom?
- What repository-relative paths or IDs are referenced?
- How are missing/not-applicable values represented?

Status: OPEN

## 7.5 Learner state boundary

Define the physical boundary between static knowledge and learner-specific state.

Questions:
- exact location of learner-state data;
- relationship between Official Store and learner state;
- whether review queue belongs under learner data;
- whether learner state references atom IDs only.

Status: OPEN

## 7.6 Data format and validation strategy

Decide the implementation conventions for persisted data:
- YAML vs JSON vs other formats;
- schema validation scope;
- whether every stored atom must validate independently;
- how collections are validated;
- naming conventions for files.

Status: OPEN

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
