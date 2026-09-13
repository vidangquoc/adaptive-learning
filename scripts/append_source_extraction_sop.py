from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "docs" / "learning-material-principles.md"

MARKER = "## 33. Canonical data shapes"

SOP = r'''## 33. Standard Source-Extraction Procedure (SOP)

This procedure is the default operational method for converting a source book or other structured instructional document into auditable evidence and downstream learning material.

The procedure is source-first: **acquire → preserve → extract → validate → segment → parse → curate**. Never begin by designing learner-facing records directly from the visual source.

### 33.1 Source registration

Before extraction, create or verify a source record containing, where applicable:

```text
source_id
source_title
author / publisher
edition / year
source_type
canonical_reference
retrieval_timestamp
checksum
license / usage_status
acquisition_method
notes
```

Do not begin downstream curation until the source identity is stable enough to be audited.

### 33.2 Preserve the original source

Keep the original acquired source unchanged whenever legally and operationally appropriate.

For a PDF book, preserve the original PDF as the source artifact. Never use a cleaned or manually edited derivative as the primary evidence file.

### 33.3 Extract raw text before interpretation

Use an appropriate deterministic extraction tool for the source format. For PDFs, a layout-preserving text extraction such as `pdftotext -layout` is the default starting point when suitable.

```text
Original PDF
    ↓
Raw text extraction
    ↓
RAW / EVIDENCE text
```

The raw output must be treated as immutable. Encoding artifacts, broken line wraps, repeated headers, and other extraction noise are expected evidence-layer problems; do not manually repair them in place.

### 33.4 Validate extraction before parsing

Before writing large-scale parsers, inspect representative portions of the raw extraction and verify:

- text is present and readable enough for the intended parser;
- major headings are detectable;
- page headers/footers can be distinguished from real content;
- unit/section boundaries are recoverable;
- exercises and answer sections remain identifiable;
- obvious encoding problems are recorded rather than silently corrected;
- the extracted text is sufficiently faithful to support downstream use.

If structural fidelity is inadequate, stop and improve extraction before building downstream parsers.

### 33.5 Discover structure before extracting records

First identify the document's structural grammar, for example:

```text
Book
 ├─ Unit
 │   ├─ Section
 │   │   ├─ Teaching / explanation
 │   │   ├─ Examples
 │   │   ├─ Exercises
 │   │   └─ Review / answer material
 │   └─ ...
 └─ ...
```

Do not assume that every occurrence of a heading is a new section. Repeated page headers, contents pages, running headers, and answer-key repetitions must be distinguished from actual structural boundaries.

### 33.6 Build and test boundary rules on a small sample

Before parsing the entire book:

1. identify candidate structural markers;
2. inspect their occurrences and false positives;
3. select deterministic boundary rules;
4. test them on one or a few units;
5. verify both the start and end of each extracted segment;
6. only then run the parser across the full source.

A parser should fail loudly when expected structure is missing or ambiguous. It must never silently produce plausible-looking but incorrect files.

### 33.7 Split into immutable structural evidence units

After boundary validation, split the raw evidence into recoverable structural chunks such as:

```text
unit-01.txt
unit-02.txt
...
```

The exact chunking depends on the source, but every chunk must retain enough source identity and location to reconstruct where it came from.

Do not treat these chunks as curated learning material yet. They remain evidence-layer artifacts.

### 33.8 Parse knowledge and questions as separate but linked streams

From the validated structural chunks, perform two related extraction passes:

```text
Structural evidence
       ├──────────────→ Knowledge extraction
       │
       └──────────────→ Exercise / question extraction
                              ↓
                     knowledge ↔ question links
```

Knowledge extraction must cover the whole taught knowledge universe, not merely exercise answers.

Question extraction must preserve the original task structure and provenance.

### 33.9 Normalize only downstream of raw evidence

Perform encoding cleanup, whitespace normalization, canonicalization, structural normalization, and controlled deduplication only in the clean/normalized layer.

Never overwrite raw evidence with normalized text.

If normalization changes a representation materially, retain enough provenance to trace the normalized record back to the original source location.

### 33.10 Curate only after extraction is auditable

Only after source extraction and structural parsing have passed validation should the project resolve:

- knowledge-atom identity;
- lexical/grammatical type;
- sense;
- patterns and collocations;
- examples;
- pronunciation;
- CEFR or other external metadata;
- competency mapping;
- question-to-knowledge relationships.

These are learning-system interpretations and must not be silently mixed into raw extraction.

### 33.11 Required validation gates

A source-extraction run is not complete until it passes, where applicable:

1. source identity/checksum is recorded;
2. original source remains recoverable;
3. raw extraction exists and is immutable;
4. expected structural markers are found;
5. structural boundaries have been manually spot-checked;
6. parser output count matches expectations or an explained source-specific rule;
7. first and last records of representative chunks are correct;
8. no downstream step silently overwrote raw evidence;
9. provenance survives every transformation;
10. extraction failures and uncertainty are visible rather than silently repaired.

### 33.12 Reproducibility and idempotence

Extraction scripts should be deterministic and safe to rerun.

Prefer this behavior:

```text
same source + same extraction code + same parameters
                         ↓
                 same raw/structural output
```

Parsers should refuse to overwrite existing outputs unless an explicit, deliberate replacement operation is being performed. When possible, record the script/version and extraction parameters used.

### 33.13 Source-specific adaptations

The SOP is the default procedure, not a claim that every source has identical structure.

A source-specific parser may adapt to:

- PDF layout;
- EPUB/HTML structure;
- scanned/OCR sources;
- tables;
- answer keys;
- appendices;
- teacher resources;
- exam papers.

Adaptation is allowed when necessary, but the source-first principles, raw/evidence immutability, provenance, validation, and separation of extraction from learning design remain mandatory.

### 33.14 Reference implementation pattern for books

For a textbook such as Destination C1 & C2, the preferred implementation pattern is:

```text
Destination PDF
      ↓
source registration + checksum
      ↓
pdftotext -layout
      ↓
sources/.../raw/Destination_C1-C2.txt
      ↓
inspect headings / encoding / repeated headers
      ↓
test Unit 1 boundary
      ↓
validate parser assumptions
      ↓
split all units
      ↓
exercise/question extraction
      ↓
knowledge extraction
      ↓
clean / normalized layer
      ↓
knowledge atoms + canonical seed questions
      ↓
question ↔ knowledge linkage
      ↓
competency mapping
      ↓
adaptive learning system
```

The critical rule is: **never skip directly from PDF to learner-facing data while bypassing the raw/evidence and validation stages.**

---

'''

text = TARGET.read_text(encoding="utf-8")

if "## 33. Standard Source-Extraction Procedure (SOP)" in text:
    raise SystemExit("SOP already present; refusing to modify file.")

if MARKER not in text:
    raise SystemExit(f"Insertion marker not found: {MARKER}")

text = text.replace(MARKER, SOP + MARKER, 1)
TARGET.write_text(text, encoding="utf-8", newline="\n")
print(f"Updated: {TARGET}")
