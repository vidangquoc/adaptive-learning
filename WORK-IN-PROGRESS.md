# Work in Progress — Before Knowledge Atom Extraction

> Temporary working checklist. This file is for coordinating the current cleanup phase and can be deleted after the prerequisites are resolved.

## Goal

Make the repository's **source layer, atom model, and schemas agree with each other** before continuing large-scale knowledge-atom extraction.

## Order of work

### 1. Fix the source segmentation / Segment boundary
- [x] Establish `Segment` as the canonical structural source boundary.
- [x] Make the actual `sources/` structure agree with `docs/learning-material/principles/06-source-unit-boundary.md`.
- [x] Define the roles of `segments/`, `segment-text/`, and `source-segments.yaml`.
- [x] Remove the obsolete `raw/` layer and the superseded whole-book text extraction artifact.

The canonical source flow is:

```text
Original source PDF
      ↓
source-segments.yaml
      ↓
Segment PDFs
      ↓
Segment text
      ↓
Evidence discovery
```

A Unit is a `type: unit` Segment. There is no separate canonical `units/` directory and no `raw/` layer.

### 2. Align the extraction SOP
- [ ] Update `docs/learning-material/procedures/source-extraction-sop.md` to match the final Segment-based source architecture.
- [ ] Ensure the pipeline is unambiguous:

```text
Source PDF → Segmentation → Segment validation → Evidence → Candidate atoms → Validation → Official atoms
```

### 3. Finalize atom taxonomy + structure
- [ ] Make `docs/knowledge/atom-types.md` and `docs/knowledge/atom-structure.md` use one coherent taxonomy.
- [ ] Confirm exactly what belongs in `type` vs `subtype` vs an atom's properties.
- [ ] Preserve the common atom field structure:

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

- [ ] Confirm semantic-ID rules (`<domain>.<concept>.<case>`, with the case omitted when unnecessary).

### 4. Rebuild the JSON schemas
- [ ] Update candidate-atom schema to the finalized model.
- [ ] Update official-atom schema to the finalized model.
- [ ] Update/remove obsolete `knowledge-atom.schema.json` if it conflicts with the new candidate/official model.
- [ ] Remove all obsolete PTNK naming/fields from schemas.
- [ ] Ensure schemas do not silently introduce a second atom model.

### 5. Clean stale references and verify source registry
- [ ] Remove stale references such as `docs/knowledge/model.md`.
- [ ] Search for other obsolete pre-reorganization paths.
- [ ] Verify `source-registry.csv`, `source-registry.md`, source files, and source metadata agree on source identity/version.
- [ ] Search the repository for `PTNK` and confirm no unwanted docs/schema references remain.

### 6. Revalidate the Unit 1 test extraction
- [ ] Keep `unit-1-sources/test-atoms.md` as a working/historical extraction, not the canonical schema.
- [ ] Recheck Unit 1 scope: **Grammar — Present time**.
- [ ] Map its useful extraction evidence into the finalized atom structure.
- [ ] Resolve any atom-boundary decisions exposed by the test extraction.

### 7. Establish the canonical atom destination
- [ ] Decide where official atoms live under the target data architecture.
- [ ] Keep knowledge data separate from learner state.
- [ ] Do not mix learner mastery/attempts into knowledge atoms.

## Definition of done

Before large-scale atom extraction, all of the following should be true:

- Source segmentation / Segment boundary is unambiguous.
- Extraction SOP matches that boundary.
- Atom taxonomy and structure agree.
- Candidate and official schemas agree with the documented atom model.
- No obsolete PTNK/schema/path references remain where they should not.
- Unit 1 test extraction has been reconciled with the final model.
- Canonical destination for official atoms is known.

## Current rule

**Do not start large-scale knowledge-atom extraction until the Definition of Done above is satisfied.**

We solve the checklist **one item at a time**, starting from **1. Fix the source segmentation / Segment boundary**.
