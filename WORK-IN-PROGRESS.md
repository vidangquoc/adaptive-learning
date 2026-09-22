# Work in Progress — Before Knowledge Atom Extraction

> Temporary working checklist. This file is for coordinating the current cleanup phase and can be deleted after the prerequisites are resolved.

## Goal

Make the repository's **source layer, atom model, and schemas agree with each other** before continuing large-scale knowledge-atom extraction.

## Order of work

### 0. Lock the source of truth
- [x] Treat `docs/knowledge/overall.md` as the canonical conceptual model for knowledge atoms.
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
- [x] Ensure the pipeline is unambiguous.

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
- Semantic relationships are not persisted because they are not used by the Adaptive Learning system.
- Source structure and assessment entities are not atom types.
- Learner state is outside the atom model.

### 4. Rebuild the JSON schemas
- [x] Update `candidate-atom.schema.json` to the finalized model.
- [x] Update `official-atom.schema.json` to the finalized model.
- [x] Remove obsolete legacy/PTNK schemas and fields.
- [x] Inline the complete atom schema into both Candidate and Official schemas so neither depends on a shared common schema.
- [x] Ensure Candidate adds only the lifecycle-specific `review_status` field.

Step 4 is complete. The `schemas/` directory contains the canonical Candidate, Official, and learner review schemas:
- `schemas/candidate-atom.schema.json`
- `schemas/official-atom.schema.json`
- `schemas/review-data.schema.json`

### 5. Clean stale references and verify source registry
- [x] Remove stale references and obsolete pre-reorganization paths.
- [x] Finalize the Source Registry as `sources/source-registry.yaml`, containing only source artifacts that actually exist in the repository.
- [x] Verify source identity and artifact-path consistency across the registry, source manifest, Segment metadata, and available downstream references.
- [x] Confirm that no obsolete schema names or legacy registry references remain.
- [x] Confirm that `books.md` is treated only as a bibliography/reference list, not as a source-identity authority.

### 6. Revalidate the Unit 1 test extraction
- [x] Close this step without revalidation: `unit-1-sources/test-atoms.md` was only an experimental extraction and is no longer a valid project artifact or source of evidence.
- [x] Do not use the experimental extraction to define Unit 1 scope, atom structure, or atom boundaries.
- [x] Treat the finalized atom model and future source-grounded extraction as the basis for subsequent work.

### 7. Establish the canonical atom destination
- [x] Decide the physical destination for Official and Candidate Knowledge Atom stores.
- [x] Keep knowledge data separate from learner state.
- [x] Do not mix learner mastery/attempts into knowledge atoms.
- [x] Define Candidate and Official physical representation as Markdown collections of independently validated fenced YAML blocks.
- [x] Define learner review data as the latest state only in `data/learners/<learner-id>/review-data.yaml`.
- [x] Finalize the Candidate creation, human review, and officialization flow.
- [x] Synchronize affected canonical documentation.
- [x] Complete final Step 7 verification.

The agreed Knowledge Atom storage layout is:

```text
data/
└── knowledge/
    └── <source-id>/
        └── <segment-id>/
            └── <domain>/
                ├── knowledge_atoms.md
                └── knowledge_atom_candidates.md
```

- Official Store: `data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atoms.md`
- Candidate Store: `data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atom_candidates.md`
- `<source-id>` is the canonical Source Registry identifier.
- `<segment-id>` is the canonical source-segmentation identifier.
- The path is storage organization, not semantic atom identity.
- No additional `official/` or `candidates/` directory layer.

## Definition of done

Before large-scale atom extraction, all of the following should be true:

- Source segmentation / Segment boundary is unambiguous.
- Extraction SOP matches that boundary.
- Atom taxonomy and structure agree.
- Candidate and official schemas agree with the documented atom model.
- No obsolete PTNK/schema/path references remain where they should not.
- The obsolete Unit 1 experimental extraction is no longer a prerequisite or source of truth.
- Canonical destination for official atoms is known.
- Learner review data is separated from Knowledge Atom data.

## Current rule

**Do not start large-scale knowledge-atom extraction until the Definition of Done above is satisfied.**

We solve the checklist **one item at a time**. Steps 0–7 above are now complete.
