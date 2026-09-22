# Source Extraction SOP

## Purpose

This document defines the operational procedure for extracting instructional books and similar structured learning sources into the Adaptive Learning knowledge pipeline.

It is an implementation SOP, not a competing learning-material policy. The canonical learning-material principles remain in `docs/learning-material/principles/`.

## Core rule

> Preserve evidence first; postpone interpretation rather than guessing.

The extraction pipeline must keep the original source recoverable, preserve structural provenance, and separate source extraction from evidence discovery, knowledge interpretation, validation, and learner-state design.

## Canonical pipeline

```text
SOURCE PDF
    ↓
source registration
    ↓
source-segments.yaml
    ↓
segment PDFs
    ↓
segment text
    ↓
segment validation
    ↓
evidence discovery
    ↓
candidate atoms
    ↓
validation / promotion gate
    ↓
official atoms
```

The key boundary is **Segment**. A Segment is a canonical structural source boundary defined by `source-segments.yaml` and represented by a segment PDF. A Unit is one Segment with `type: unit`; it is not a separate repository layer.

The canonical source layer is:

```text
sources/
├── <original-source>.pdf
└── <source-id>/
    ├── source-segments.yaml
    ├── segments/
    └── segment-text/
```

`segments/` contains structural source PDFs. `segment-text/` contains derived machine-readable text for those same segments. Neither layer replaces the original source PDF.

## 1. Register the source

Before extraction:

1. assign a stable `source_id`;
2. record title and edition/year when known;
3. record source type and acquisition method;
4. preserve canonical URL/reference when available;
5. record retrieval/acquisition timestamp;
6. compute and record a checksum for the acquired source file;
7. record license and usage restrictions;
8. record the extraction method intended for the source.

Do not begin segmentation or evidence discovery before source registration is complete.

## 2. Preserve the original source / source of truth

The acquired source PDF is the recovery point and source of truth for structural extraction.

```text
ORIGINAL SOURCE PDF
       ↓
segmentation + derived representations
```

Never overwrite or modify the original source to repair extraction problems.

If redistribution is restricted, preserve the source only where legally and operationally permitted, while retaining enough provenance and metadata to identify and reproduce the extraction.

The source PDF must remain independently recoverable from all derived segment and text files.

## 3. Define source segmentation

Segmentation converts the source PDF into explicit, deterministic structural boundaries.

The segmentation manifest is `source-segments.yaml`. It records the segment IDs, types, ordering, and source boundaries needed to reproduce the structural split.

Typical segment types may include:

- `unit`;
- `review`;
- `progress-test`;
- `database`;
- `revision-test`;
- `answer-key`;
- `header`;
- `footer`.

The exact set of segment types is source-dependent and must be defined by the segmentation manifest rather than inferred from a generic hierarchy.

A Unit is represented as a Segment with `type: unit`. Do not create a second Unit-specific storage layer.

Segmentation must preserve source order and page/boundary provenance. Segment boundaries must be based on structural evidence in the source, not on arbitrary text lengths or downstream knowledge topics.

## 4. Generate segment PDFs

After the segmentation manifest is defined and reviewed, generate one PDF for each canonical Segment.

Rules:

- each segment PDF must map to exactly one manifest segment;
- output naming must be deterministic and stable;
- source page ranges or equivalent boundary information must remain traceable;
- the original source PDF must remain unchanged;
- segmentation must be reproducible from the source PDF and manifest;
- an unexpected existing output must fail loudly rather than being silently overwritten.

The segment PDF is the canonical structural representation of that Segment. It is the primary source artifact used to inspect whether a boundary is correct.

## 5. Generate segment text

Generate machine-readable text from each segment PDF when text processing is required.

The relationship is:

```text
Original source PDF
      ↓
Segment PDF
      ↓
Segment text
```

`segment-text/` is a derived representation, not an independent source layer.

Record when practical:

- extraction tool;
- tool/version;
- command or configuration;
- extraction timestamp;
- input checksum;
- output checksum.

Do not construct the canonical text corpus by first extracting the entire book into one intermediate TXT file and then splitting it. The canonical segmentation boundary comes first.

## 6. Validate segment boundaries and text

Validate segmentation before evidence discovery.

For a representative sample, inspect:

1. the beginning of each selected Segment;
2. the end of each selected Segment;
3. the corresponding pages in the original source PDF;
4. the segment PDF against the manifest boundary;
5. the segment text against the segment PDF.

Check for:

- missing pages or content;
- content leaking across segment boundaries;
- duplicated or omitted pages;
- incorrect reading order;
- broken encoding;
- damaged tables or answer choices;
- corrupted symbols or diacritics;
- duplicated headers/footers;
- text extraction that materially changes meaning.

If a Segment is wrong, fix the segmentation or extraction process before discovering evidence from it. Do not silently repair source evidence during downstream parsing.

A segment is not ready for evidence discovery until its boundary and derived text are sufficiently trustworthy for the intended task.

## 7. Discover evidence

Evidence discovery identifies source-supported instructional and assessment evidence inside validated Segments.

The evidence-discovery process should work from segment text while remaining traceable to the segment PDF and original source PDF.

Every discovered evidence item should preserve enough provenance to answer:

```text
Which source?
Which Segment?
Which segment PDF?
Which text span or source location?
What does the source actually say or show?
```

Evidence discovery is not yet official atom creation. Do not silently convert an interpretation into a source fact.

## 8. Extract instructional knowledge evidence

From instructional content, identify evidence relevant to knowledge extraction, including where applicable:

- lexical items and senses;
- multiword expressions;
- idioms;
- phrasal verbs;
- collocations;
- grammar rules and patterns;
- word formation;
- usage and register;
- examples and contextual evidence;
- contrasts and boundaries explicitly supported by the source.

Preserve the source span and Segment provenance for every candidate finding.

The detailed schema and field semantics for knowledge atoms are defined in `docs/knowledge/atom-structure.md`; this SOP does not redefine that schema.

## 9. Extract assessment evidence separately

Extract exercises, tests, reviews, and answer material as source-derived assessment evidence.

Preserve, where available:

- Segment ID/type;
- exercise or test identifier;
- question number;
- original task type;
- prompt;
- options;
- answer/key when legitimately available;
- source location;
- provenance;
- the instructional or knowledge target supported by the source.

Do not transform source questions into generated questions during source extraction.

Assessment evidence can support atom discovery and validation, but a question does not automatically prove that every word or concept appearing in it is a tested knowledge target.

## 10. Preserve question ↔ evidence / atom relationships

When source-derived questions are linked to knowledge findings, preserve the relationship explicitly.

Use evidence such as:

- answer structure;
- instructional explanation;
- exercise instructions;
- lexical or grammatical target;
- source context;
- explicit source references.

Do not infer a relationship merely because a word or construction appears somewhere in the same Segment.

Question-to-knowledge relationships must remain traceable back to the source evidence that justified the relationship.

## 11. Create Candidate Atoms

Validated evidence may be synthesized into complete Candidate Atoms.

Candidate creation is an interpretation step. Each Candidate must retain its supporting evidence and provenance so that another reviewer or later process can reconstruct why it exists.

At this stage:

- the Candidate is not Official;
- create the canonical semantic ID immediately; do not create a separate `candidate_id` or temporary ID;
- use the canonical atom structure, with `review_status: pending`;
- do not invent unsupported meanings, constraints, or examples;
- do not silently merge distinct concepts merely because they are related;
- do not put learner mastery or attempt history into the atom;
- do not populate fields beyond what the evidence supports.

The canonical atom structure, taxonomy, and semantic-ID rules are defined separately in `docs/knowledge/`.

## 12. Run validation and promotion gates

Before a candidate atom becomes official, verify at minimum:

- source identity and provenance are recorded;
- Segment identity and source location are recoverable;
- supporting evidence is actually present in the source;
- segment boundaries are valid;
- the interpretation does not exceed the evidence;
- source-derived and generated content are distinguishable;
- assessment relationships are justified;
- unresolved extraction or interpretation problems are explicitly marked;
- no unsupported content was invented to repair gaps;
- the candidate conforms to the canonical atom taxonomy and structure.

Promotion is a controlled state transition, not an automatic consequence of successful text extraction or candidate generation.

## 13. Officialize Approved Candidates

Only Candidates with `review_status: approved` may be officialized.

The conceptual transition is:

```text
validated Segment evidence
        ↓
Candidate Store
        ↓
validation / human review
        ↓
approved Candidate
        ↓
officialize
        ↓
Official Store
```

Officialization writes the Official Atom with the same semantic ID, preserves source provenance, and then deletes the Candidate from the Candidate Store.

Learner mastery, attempts, and other learner-specific information belong to the learner-state layer, not to the knowledge atom. Review status belongs only to Candidates.

## 14. Source-specific adaptation

This SOP is the default operational procedure, not a rigid parser implementation.

For EPUB, HTML, scanned PDF/OCR, DOCX, or other formats:

- adapt acquisition and extraction mechanics;
- preserve the original source of truth;
- produce an explicit structural segmentation appropriate to the source;
- preserve Segment-level provenance where the source supports it;
- validate boundaries before mass evidence discovery;
- keep derived text downstream of the structural source representation;
- document source-specific deviations;
- do not reintroduce obsolete whole-source text or parallel structural layers merely because a tool prefers them.

For OCR sources in particular, extraction quality must be validated before evidence discovery because OCR errors can change lexical, grammatical, and assessment evidence.

## 15. Reproducibility and idempotence

A source-extraction pipeline should be safe to rerun.

Given the same source PDF, segmentation manifest, extraction configuration, and tool versions, it should produce the same structural outputs except for explicitly nondeterministic metadata.

Scripts should:

- fail loudly on unexpected input;
- avoid silent overwrites;
- make output paths explicit;
- record tool/configuration versions where useful;
- make segment-boundary validation testable;
- preserve stable IDs and ordering;
- make it possible to trace derived files back to their source inputs.

A change to segmentation boundaries is a source-structure change and should be reviewed as such; it must not silently alter downstream evidence or official knowledge.

## 16. Relationship to the canonical rulebook

`docs/learning-material/principles/` defines **what the learning system must preserve and why**.

This SOP defines **how source material is operationally segmented, extracted, validated, and moved into the knowledge system**.

The Segment architecture defined by `docs/learning-material/principles/06-source-unit-boundary.md` is the canonical source boundary. If a future implementation detail conflicts with that architecture or another canonical learning-material principle, preserve the principle and adapt the implementation.
