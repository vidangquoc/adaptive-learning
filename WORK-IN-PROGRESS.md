# Work in Progress — Before Knowledge Atom Extraction

> Temporary working checklist. This file is for coordinating the current cleanup phase and can be deleted after the prerequisites are resolved.

## Goal

Make the repository's **source layer, atom model, and schemas agree with each other** before continuing large-scale knowledge-atom extraction.

## Order of work

### 0. Lock the source of truth
- [x] Treat `docs/knowledge/overall.md` as the canonical conceptual model for knowledge atoms and their relationships.
- [x] Treat `docs/knowledge/atom-structure.md` as the canonical common field structure and field semantics.
- [x] Treat `docs/knowledge/atom-types.md` as the canonical atom taxonomy.
- [x] Do not introduce a second atom model in other documentation or schemas; later schema work must conform to these three documents.

The authority chain is:

```text
Knowledge model / concepts
        ↓
docs/knowledge/overall.md
        ↓
common structure
        ↓
docs/knowledge/atom-structure.md
        ↓
taxonomy
        ↓
docs/knowledge/atom-types.md
        ↓
schemas / data / extraction
```

Step 0 locks the locations of the authoritative definitions. It does not prevent those documents from being refined during their dedicated checklist steps.

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
- [x] Update `docs/learning-material/procedures/source-extraction-sop.md` to match the final Segment-based source architecture.
- [x] Ensure the pipeline is unambiguous:

```text
Source PDF → Segmentation → Segment validation → Evidence → Candidate atoms → Validation → Official atoms
```

The SOP now treats the original source PDF as the source of truth, `source-segments.yaml` as the segmentation manifest, Segment PDFs as the canonical structural source artifacts, and `segment-text/` as derived machine-readable text. It no longer uses an obsolete whole-source text layer or separate `units/` / `sections/` layers.

### 3. Finalize atom taxonomy + structure
- [x] Make `docs/knowledge/atom-types.md` and `docs/knowledge/atom-structure.md` use one coherent taxonomy.
- [x] Confirm exactly what belongs in `type` vs an atom's properties.
- [x] Preserve the finalized common atom field structure:

```yaml
id:
domain:
type:
name:
part_of_speech:
pronunciation:
meaning:
mother_says:
explanation:
structure:
examples:
extra:
  source:
  is_tested:
  test_evidence:
  notes:
```

- [x] Confirm semantic-ID rules (`<domain>.<type>.<name>`, with the part-of-speech / meaning slug added for lexical senses when needed).

Step 3 decisions:

- `domain` is currently `vocabulary` or `grammar`.
- Vocabulary has explicit types: `lexical_sense`, `multiword_expression`, `phrasal_verb`, `idiom`, `collocation`, `word_formation`, and `morphological_form`.
- Grammar has explicit types: `rule`, `use`, `exception`, `word_formation`, and `morphological_form`.
- `part_of_speech` and `pronunciation` are common fields but apply only to `vocabulary.lexical_sense`.
- Descriptive properties are not atoms unless the knowledge point is directly taught/tested and therefore needs its own atom.
- Semantic relationships are relations, not atom fields or atom types.
- Source structure and assessment entities are not atom types.
- Learner state is outside the atom model.

### 4. Rebuild the JSON schemas
- [x] Update `candidate-atom.schema.json` to the finalized model.
- [x] Update `official-atom.schema.json` to the finalized model.
- [x] Remove obsolete legacy/PTNK schemas and fields.
- [x] Inline the complete atom schema into both Candidate and Official schemas so neither depends on a shared common schema.
- [x] Ensure Candidate adds only the lifecycle-specific `review_status` field.

Step 4 is complete. The `schemas/` directory now contains only the two canonical schemas:
- `schemas/candidate-atom.schema.json`
- `schemas/official-atom.schema.json`

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
