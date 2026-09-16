# Source Registry

## Purpose

The Source Registry is the metadata layer for external evidence used by Adaptive Learning.

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
LEARNER STATE + COVERAGE FILTERS
      ↓
OFFICIAL LEARNING DATA
```

## Source roles

`source_role` is mandatory because proficiency level alone does not determine how a source should be used.

| Role | Meaning |
|---|---|
| `candidate_lexicon` | Candidate-generation source for lexical material. Never automatically becomes curriculum. |
| `grammar_reference` | Grammar reference/practice source used to model competencies. |
| `competency_practice` | Practice source used to extract or reinforce testable competencies. |
| `coursebook` | Integrated coursebook covering multiple skills. |
| `assessment` | Diagnostic, transfer, and mock-test evidence. Not automatically a curriculum source. |
| `reference` | Reference source used to verify meanings, pronunciation, usage, or other knowledge properties. |

## Registry fields

| Field | Required | Meaning |
|---|---|---|
| `source_id` | yes | Stable internal identifier |
| `source_name` | yes | Human-readable source name |
| `source_type` | yes | `book`, `exam`, `lexicon`, `phrase_list`, `frequency`, etc. |
| `source_role` | yes | Operational role in the learning-material pipeline |
| `publisher` | yes | Organization responsible for the source |
| `url` | yes | Canonical landing/resource URL |
| `version` | recommended | Edition, release, or version when known |
| `proficiency_coverage` | recommended | Actual proficiency scope represented by the source |
| `data_types` | yes | Words, collocations, idioms, grammar, tasks, etc. |
| `frequency_available` | yes | `yes`, `no`, or `partial` |
| `acquisition_method` | yes | How the source is obtained |
| `raw_cache_path` | recommended | Repository path for permitted raw material or acquisition metadata |
| `status` | yes | `active`, `candidate`, `deprecated`, `blocked`, or `superseded` |
| `notes` | recommended | Interpretation, limitations, and provenance notes |

## Source-selection rule

The source library should be centered on sources that contribute to one or more of:

1. lexical candidate generation;
2. advanced grammar and competency modeling;
3. skill and competency practice;
4. diagnostic, transfer, and assessment evidence;
5. reliable lexical or grammatical reference.

A book being labeled C1 or C2 does **not** make every item inside it mandatory.

The general pipeline is:

```text
learning source
      ↓
candidate universe
      ↓
source evidence
      ↓
learner diagnostic
      ↓
coverage / marginal-value gate
      ↓
official learning data
```

## Evidence hierarchy

For source-specific claims, prefer:

1. official or primary source material;
2. authoritative publisher/reference sources;
3. established corpus/lexical resources;
4. reputable secondary analysis;
5. third-party lists only for candidate discovery.

A learning book is therefore a **candidate or reference source** according to its registered role, not automatic evidence that every item must be learned.

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

The registry covers selected C1/C2 and advanced learning sources, including:

- vocabulary;
- collocations;
- idioms;
- phrasal verbs;
- advanced grammar;
- grammar/vocabulary practice;
- integrated advanced coursebooks;
- assessment sources;
- lexical and grammatical reference sources.

The registry intentionally does **not** attempt to be an exhaustive catalogue of every advanced learning source.

## Future extensions

Potential future source roles include:

- `frequency_metadata` — only when a frequency layer is actually needed;
- `academic_enrichment` — if academic vocabulary becomes a deliberate subsystem;
- `reading_corpus` — for reading-level and discourse evidence;
- `writing_corpus` — for writing-language evidence;
- `source_relation` — supersession/derivation tracking;
- `extraction_version` — parser/version tracking.

Add these only when they solve a concrete reproducibility or modeling problem.
