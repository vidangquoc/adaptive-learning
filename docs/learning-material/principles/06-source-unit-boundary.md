# Source Segmentation and Segment Boundary

## Canonical Rule

For Destination C1 & C2, **Segment is the canonical structural source boundary**.

A Unit is one kind of Segment. It is not a separate repository layer and must not have a parallel `units/` directory.

The source pipeline is:

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
      ↓
Candidate atoms
      ↓
Validation
      ↓
Official atoms
```

The canonical source structure is:

```text
sources/destination-c1-c2/
├── segments/
├── segment-text/
└── source-segments.yaml
```

The original source PDF lives at `sources/Destination_C1-C2.pdf` and remains the source of truth.

## Source Segmentation Specification

`source-segments.yaml` is the segmentation specification and manifest for the source PDF.

It defines the structural boundaries and metadata of the source segments, including Units and other source sections such as reviews, progress tests, databases, revision tests, answer keys, header, and footer where applicable.

A segment has a stable segment ID and a segment type. For example:

```yaml
id: unit-01
type: unit
number: 1
start_page: 7
```

Therefore:

```text
Segment
├── Unit
├── Review
├── Progress Test
├── Database
├── Revision Test
├── Answer Key
└── other explicitly defined source segment types
```

The manifest is the authority for segmentation boundaries. Directory names and filenames alone do not define source boundaries.

## Segment PDF Layer

`segments/` contains the PDF representation of each segment defined by `source-segments.yaml`.

For example:

```text
segments/
├── unit-01.pdf
├── unit-02.pdf
├── review-01.pdf
├── progress-test-01.pdf
├── database-idioms.pdf
└── ...
```

These PDFs are produced by splitting the original source PDF according to the segmentation specification.

`segments/` is the **structural source layer**. It establishes the physical source artifact corresponding to each segment boundary.

It is not the knowledge-atom layer.

## Segment Text Layer

`segment-text/` contains the text representation of the corresponding segment PDFs.

For example:

```text
segment-text/
├── unit-01.txt
├── unit-02.txt
├── review-01.txt
├── progress-test-01.txt
├── database-idioms.txt
└── ...
```

Segment text is derived from the corresponding segment PDF. It is the **machine-readable textual input used for evidence discovery**, because the current GitHub workflow cannot reliably inspect all source PDF content directly.

`segment-text/` is therefore not an independent source structure. Every segment text file must remain traceable to its segment PDF and, through that segment, to the original source PDF.

The intended relationship is:

```text
Original source PDF
      ↓
Segment ID in source-segments.yaml
      ↓
segments/<segment-id>.pdf
      ↓
segment-text/<segment-id>.txt
```

## Segment Validation Gate

Before downstream evidence discovery begins, validate the segmentation and its text representation.

At minimum:

1. Every canonical segment has a defined boundary in `source-segments.yaml`.
2. Segment order is preserved.
3. Segment PDF boundaries match the manifest.
4. Segment text corresponds to the correct segment PDF.
5. No source content is silently omitted from a segment.
6. No content from an adjacent segment is silently included.
7. Segment text is sufficiently complete for downstream evidence discovery.

If a required condition fails:

```text
FAIL → stop extraction → repair segmentation/text → revalidate
```

Do not continue evidence discovery against known-invalid segment input.

## Unit Boundary

A Unit boundary is validated through the same Segment boundary rules.

For a Unit segment, validate:

1. Unit start is correct.
2. Unit end is correct.
3. No content is missing.
4. No content from an adjacent Unit is included.
5. Unit order is preserved.
6. The Unit can be read as complete source context for downstream analysis.

A Unit may contain multiple knowledge domains and evidence types. Grammar, vocabulary, exercises, explanations, examples, and assessment material can coexist inside the same Unit segment.

Do not create artificial repository subdivisions merely to make extraction easier.

## Provenance

Source provenance should preserve the full trace from source artifact to evidence:

```text
source PDF
  ↓
segment ID / segment type
  ↓
segment PDF
  ↓
segment text
  ↓
precise location/span
  ↓
source evidence
  ↓
candidate atom
  ↓
official atom
```

A textbook heading, topic label, grammar label, exercise label, or similar internal marker may be recorded as descriptive context, but it does not replace segment provenance or become a separate source layer.

## Downstream Discovery

Evidence discovery operates on `segment-text/`, using the segment identity and provenance defined by `source-segments.yaml`.

Discovery may identify vocabulary, phrases, patterns, collocations, idioms, phrasal verbs, word formation, grammar, contrasts, examples, explanations, and assessment evidence.

Discovery output is evidence location and interpretation input, not canonical knowledge. Knowledge interpretation and atomization are defined elsewhere.

Exercises and Challenges inside a segment are source evidence for assessment. Answer choices, fill-in rows, generic exercise markers, and similar structural artifacts must not automatically become knowledge atoms.


