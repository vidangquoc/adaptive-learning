# Step 7 — Define the physical data architecture

This is a temporary working document for Step 7.

Step 7 will be resolved one issue at a time. This document records the questions that must be discussed and the decisions we make. It is not a canonical specification.

## 7.1 Physical location of Knowledge Atom stores

Decide where the two atom stores live in the repository:

- Candidate Store
- Official Store

Questions to settle:
- Should both live under `data/`?
- Should they be separated by lifecycle (`candidates/` and `official/`)?
- Should they be separated by domain/type, or remain flat?
- What file format should the stores use?
- Is one file per atom or a collection file more appropriate?
- What is the canonical destination for Official Atoms?

Status: OPEN

## 7.2 Physical representation of Candidate Atoms

After 7.1, decide:
- exact directory/file layout;
- whether Candidate Atoms are stored individually or in collections;
- how `review_status` is represented;
- how candidate creation/update is performed;
- validation requirements against `schemas/candidate-atom.schema.json`.

Status: BLOCKED BY 7.1

## 7.3 Physical representation of Official Atoms

Decide:
- exact directory/file layout;
- individual atom vs collection;
- whether atoms are grouped by domain/type;
- how Official Store is validated against `schemas/official-atom.schema.json`;
- how officialization writes to this store.

Status: BLOCKED BY 7.1

## 7.4 Relations between Knowledge Atoms

Decide where and how relations are stored.

Questions:
- Separate relation store or another structure?
- What identifies the source and target atoms?
- How are relation types represented?
- Are relations global or grouped by domain?
- How does this interact with the flat atom model?

Status: BLOCKED BY 7.1

## 7.5 Source provenance and evidence in stored atoms

Confirm how the existing canonical fields are physically persisted:
- `extra.source.origin`
- `extra.source.atom_decision`
- `extra.is_tested`
- `extra.test_evidence`

Questions:
- Are these stored directly in every atom?
- What repository-relative paths or IDs are referenced?
- How are missing/not-applicable values represented?

Status: BLOCKED BY 7.1

## 7.6 Learner state boundary

Define the physical boundary between static knowledge and learner-specific state.

Questions:
- exact location of learner-state data;
- relationship between Official Store and learner state;
- whether review queue belongs under learner data;
- whether learner state references atom IDs only.

Status: BLOCKED BY 7.1

## 7.7 Data format and validation strategy

Decide the implementation conventions for persisted data:
- YAML vs JSON vs other formats;
- schema validation scope;
- whether every stored atom must validate independently;
- how collections are validated;
- naming conventions for files.

Status: BLOCKED BY 7.1

## 7.8 Scripts and pipeline integration

After the storage model is settled, identify required changes to:
- extraction scripts;
- validation scripts;
- candidate creation;
- review/promotion;
- officialization.

Do not change scripts before the underlying storage model is agreed.

Status: BLOCKED BY 7.1

## 7.9 Documentation synchronization

After decisions are finalized, update only the canonical documents that are actually affected.

Potential documents:
- `docs/knowledge/overall.md`
- `docs/knowledge/atom-structure.md`
- `docs/knowledge/atom-pipeline.md`
- `docs/knowledge/atom-types.md`
- `docs/learner/learning-state.md`
- relevant learning-material principles/procedures
- `README.md`

Status: BLOCKED BY 7.1

## 7.10 Final Step 7 verification

Verify:
- physical stores match the agreed architecture;
- schemas match stored data;
- pipeline references are consistent;
- no obsolete paths or structures remain;
- canonical documentation is synchronized.

Status: BLOCKED BY 7.1
