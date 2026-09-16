# Source Registry

## Purpose

The Source Registry is the metadata layer for external evidence used by the PTNK Adaptive Preparation System.

It separates **source provenance** from **curated learning data** so that extraction, filtering, prioritization, and curriculum strategy can change without having to rediscover the underlying sources.

Core principle:

> Source data should be as immutable and reproducible as practical; curriculum decisions remain mutable.

The registry is **not** the learner-facing lexicon and is **not** a study checklist.

## Architecture

```text
EXTERNAL SOURCE
      ↓
SOURCE REGISTRY
      ↓
RAW / EVIDENCE CACHE
      ↓
NORMALIZATION / EXTRACTION
      ↓
CANDIDATE POOL
      ↓
PTNK RELEVANCE + LEARNER STATE + COVERAGE FILTERS
      ↓
OFFICIAL LEARNING DATA
```

## Source roles

`source_role` is mandatory because CEFR level alone does not determine how a source should be used.

| Role | Meaning |
|---|---|
| `ptnk_evidence` | Direct evidence from PTNK exams and official materials. Highest priority for PTNK claims. |
| `c1_candidate_lexicon` | Candidate-generation source for C1/C1-C2 lexical material. Never automatically becomes curriculum. |
| `grammar_reference` | Grammar reference/practice source used to model competencies. |
| `competency_practice` | Practice source used to extract or reinforce testable competencies. |
| `exam_coursebook` | C1 exam-preparation coursebook covering multiple skills. |
| `assessment` | Diagnostic, transfer, and mock-test evidence. Not a curriculum source. |

## Registry fields

| Field | Required | Meaning |
|---|---|---|
| `source_id` | yes | Stable internal identifier |
| `source_name` | yes | Human-readable source name |
| `source_type` | yes | `exam`, `book`, `lexicon`, `phrase_list`, `frequency`, etc. |
| `source_role` | yes | Operational role in the PTNK evidence pipeline |
| `publisher` | yes | Organization responsible for the source |
| `url` | yes | Canonical landing/resource URL |
| `version` | recommended | Edition, release, or version when known |
| `cefr_coverage` | recommended | Actual CEFR scope represented by the source |
| `data_types` | yes | Words, collocations, idioms, grammar, exam tasks, etc. |
| `frequency_available` | yes | `yes`, `no`, or `partial` |
| `acquisition_method` | yes | How the source is obtained |
| `raw_cache_path` | recommended | Repository path for permitted raw material or acquisition metadata |
| `status` | yes | `active`, `candidate`, `deprecated`, `blocked`, or `superseded` |
| `notes` | recommended | Interpretation, limitations, and provenance notes |

## What was removed from the initial registry

The following broad resources were removed from the active registry because they are useful evidence sources in general but do **not** belong in the focused C1 book/source library:

- Oxford 3000/5000 — broad A1-C1 resource, not a C1-specific source.
- OPAL — academic vocabulary/phrases resource, not a C1-specific general candidate list.
- Cambridge English Vocabulary Profile / English Profile — broad A1-C2 research resource, not a C1-only syllabus.
- EFLLex / CEFRLex — broad A1-C2 frequency/CEFR resource; frequency metadata should be a separate future layer rather than being mistaken for a C1 curriculum source.
- Oxford Phrase List — useful A1-C1 multiword source, but not sufficiently C1-specific for the current focused bibliography. It can be reintroduced later as a supplementary multiword evidence source if needed.

These removals do **not** mean the resources are bad. They mean their role is different from a focused C1 candidate bibliography.

## Current source-selection rule

The current bibliography is deliberately centered on sources that can contribute to one of four things:

1. C1/C1-C2 lexical candidate generation;
2. advanced grammar and competency modeling;
3. C1 exam-skill practice;
4. diagnostic and transfer assessment.

A book being labeled C1 does **not** make every item inside it mandatory.

The pipeline remains:

```text
C1/C1-C2 source
      ↓
candidate universe
      ↓
PTNK evidence
      ↓
learner diagnostic
      ↓
coverage / marginal-value gate
      ↓
official learning data
```

## Evidence hierarchy

For PTNK-specific claims, prefer:

1. official PTNK documents;
2. primary publisher/research sources;
3. established corpus/lexical resources;
4. reputable secondary analysis;
5. third-party lists only for candidate discovery.

A C1 book is therefore a **candidate source**, not evidence that PTNK requires every item in that book.

## Raw-data policy

When legally and technically appropriate, preserve the raw artifact so future aggregation strategies can be rerun without repeated external acquisition.

When redistribution is restricted, preserve instead:

1. canonical source URL;
2. acquisition procedure/script;
3. retrieval timestamp;
4. checksum when the artifact was locally obtained;
5. license/usage notes;
6. transformation/extraction notes.

Do not treat a generated CSV as a substitute for provenance.

## Current registry scope

The registry currently covers:

- PTNK specialized-English entrance papers, 2022-2026;
- C1/C1-C2 vocabulary;
- C1/C1-C2 collocations;
- C1/C1-C2 idioms;
- C1/C1-C2 phrasal verbs;
- advanced grammar;
- advanced grammar/vocabulary practice;
- C1 exam-preparation coursebooks;
- C1 Advanced mock/assessment sources.

The registry intentionally does **not** attempt to be an exhaustive catalogue of every C1 book.

## Future extensions

Potential future source roles include:

- `frequency_metadata` — only when a frequency layer is actually needed;
- `academic_enrichment` — if academic vocabulary becomes a deliberate subsystem;
- `reading_corpus` — for reading-level and discourse evidence;
- `writing_corpus` — for writing-language evidence;
- `source_relation` — supersession/derivation tracking;
- `extraction_version` — parser/version tracking.

Add these only when they solve a concrete reproducibility or modeling problem.
