# Source Extraction SOP

## Purpose

This document defines the operational procedure for extracting instructional books and similar structured learning sources into the PTNK knowledge pipeline.

It is an implementation SOP, not a competing learning-material policy. The canonical learning-material principles remain in `docs/learning-material-principles.md`.

## Core rule

> Preserve evidence first; postpone interpretation rather than guessing.

The extraction pipeline must keep the original source recoverable and must separate extraction from cleaning, normalization, curation, and learning design.

## Standard pipeline

```text
SOURCE FILE
    ↓
source registration
    ↓
immutable source / provenance record
    ↓
text extraction
    ↓
RAW EVIDENCE
    ↓
extraction-quality inspection
    ↓
structure detection
    ↓
boundary validation
    ↓
structural evidence files
    ↓
knowledge extraction + exercise extraction
    ↓
CLEAN / NORMALIZED
    ↓
CURATED KNOWLEDGE
    ↓
KNOWLEDGE ATOMS
    ↓
QUESTION BANK
    ↓
COMPETENCY MAPPING
```

## 1. Register the source

Before extraction:

1. assign a stable `source_id`;
2. record title and edition/year when known;
3. record source type and acquisition method;
4. preserve canonical URL/reference when available;
5. record retrieval/acquisition timestamp;
6. compute and record a checksum for the acquired file;
7. record license and usage restrictions;
8. record the extraction method intended for the source.

Do not begin curation before source registration.

## 2. Preserve the original source

The acquired source is the recovery point.

```text
SOURCE FILE
    ↓
immutable source archive/reference
    ↓
raw extraction
```

Never overwrite the original source to repair extraction problems.

If redistribution is restricted, preserve the source only where legally and operationally permitted, while retaining enough provenance and metadata to reproduce the extraction.

## 3. Extract to an immutable raw evidence layer

For a text-based PDF, a typical deterministic workflow is:

```text
PDF
 ↓
pdftotext -layout
 ↓
RAW TXT
```

Record when practical:

- extraction tool;
- tool/version;
- command or configuration;
- extraction timestamp;
- input checksum;
- output checksum.

The raw text is evidence, not learner-facing content.

## 4. Inspect extraction quality before mass parsing

Inspect representative pages or sections before running a full parser.

Check for:

- missing text;
- broken character encoding;
- duplicated headers/footers;
- incorrect reading order;
- columns merged incorrectly;
- tables damaged;
- page numbers mixed into content;
- symbols or diacritics corrupted;
- answer choices reordered;
- exercise boundaries damaged.

If extraction is materially unreliable, stop and change the extraction strategy. Do not silently rewrite raw evidence to compensate.

## 5. Detect document structure

Identify structural anchors such as:

```text
Book
 ├─ Unit / Chapter
 │   ├─ Section
 │   ├─ Instructional content
 │   ├─ Examples
 │   ├─ Exercises
 │   │   └─ Questions
 │   └─ Review / Test
 └─ Answer key / Reference material
```

Use multiple structural signals where possible.

Do not assume every occurrence of a heading is a real boundary: PDFs commonly repeat running headers, page titles, and other navigation text.

## 6. Validate boundaries on a small sample

Before full-book extraction:

1. identify candidate boundaries;
2. select a representative unit or section;
3. extract a small test range;
4. inspect its beginning and end;
5. verify that the content belongs to the intended section;
6. verify that the next section has not leaked into the output;
7. only then run mass extraction.

A boundary parser that has not passed sample validation is not ready for full-book extraction.

## 7. Split structural evidence deterministically

Once boundaries are validated, create stable structural evidence files where useful.

Example:

```text
raw/
  Source.txt

units/
  unit-01.txt
  unit-02.txt
  ...
```

Rules:

- deterministic output names;
- stable ordering;
- no silent overwriting;
- explicit failure when an expected output already exists;
- preserve source line/location relationships where practical.

## 8. Parse instructional knowledge separately

Do not treat exercise answers as the entire knowledge universe.

Extract from instructional content:

- lexical items and senses;
- multiword expressions;
- idioms;
- phrasal verbs;
- collocations;
- grammar rules and patterns;
- word formation;
- usage and register;
- examples and contextual evidence.

Every extracted record should retain source location and provenance.

## 9. Parse exercises and questions separately

Extract exercises into source-derived question records.

Preserve, where available:

- exercise identifier;
- question number;
- original task type;
- prompt;
- options;
- answer/key when legitimately available;
- source location;
- provenance.

Do not transform source questions into generated questions during this stage.

## 10. Preserve question ↔ knowledge relationships

Map source-derived questions to the knowledge atoms they actually test.

Use evidence from:

- answer structure;
- instructional explanation;
- exercise instructions;
- lexical or grammatical target;
- source context.

Do not infer a relationship merely because a word appears somewhere in the same unit.

## 11. Normalize only downstream

After raw structural extraction is validated:

```text
RAW
 ↓
CLEAN
 ↓
NORMALIZED
 ↓
CURATED
```

Typical downstream operations include:

- encoding cleanup;
- whitespace normalization;
- structural canonicalization;
- controlled deduplication;
- normalization of labels and identifiers;
- conversion to machine-readable schemas.

Never make these edits directly to raw evidence.

## 12. Run quality gates

Before promoting extracted material, verify:

- source checksum and provenance are recorded;
- extraction is reproducible;
- expected units/sections are present;
- boundaries are validated;
- unexpected cross-boundary leakage is absent or flagged;
- question counts are plausible;
- source-derived and generated content are distinguishable;
- knowledge/question provenance is retained;
- unresolved extraction problems are explicitly marked;
- no unsupported content was invented to repair extraction gaps.

## 13. Promote to the knowledge system

Only after evidence and structural validation:

```text
RAW / EVIDENCE
      ↓
CLEAN / NORMALIZED
      ↓
CURATED KNOWLEDGE
      ↓
KNOWLEDGE ATOMS
      ↓
QUESTION BANK
      ↓
COMPETENCY MAPPING
```

Promotion is a controlled state transition, not an automatic consequence of successful text extraction.

## 14. Source-specific adaptation

This SOP is the default procedure, not a rigid parser implementation.

For EPUB, HTML, scanned PDF/OCR, DOCX, or other formats:

- adapt acquisition and extraction mechanics;
- preserve the raw/evidence boundary;
- preserve provenance;
- validate structure before mass parsing;
- keep cleaning downstream;
- preserve recoverability;
- document source-specific deviations.

## 15. Reproducibility and idempotence

A source-extraction pipeline should be safe to rerun.

Given the same source and extraction configuration, it should produce the same structural outputs except for explicitly nondeterministic metadata.

Scripts should:

- fail loudly on unexpected input;
- avoid silent overwrites;
- make output paths explicit;
- record tool/configuration versions where useful;
- make structural validation testable.

## 16. Relationship to the canonical rulebook

`docs/learning-material-principles.md` defines **what the learning system must preserve and why**.

This SOP defines **how source material is operationally extracted and moved into that system**.

If a future implementation detail conflicts with a canonical learning-material principle, preserve the principle and adapt the implementation.
