# Source Registry

## Purpose

The Source Registry is the metadata layer for external evidence used by the PTNK Adaptive Preparation System.

It separates **source provenance** from **curated learning data** so that aggregation, filtering, prioritization, and curriculum strategy can change without having to rediscover or redownload the underlying sources.

Core principle:

> Source data should be as immutable and reproducible as practical; curriculum decisions remain mutable.

The registry is **not** the learner-facing lexicon and is **not** a priority list.

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

## Registry fields

| Field | Required | Meaning |
|---|---|---|
| `source_id` | yes | Stable internal identifier, e.g. `oxford-phrase-list` |
| `source_name` | yes | Human-readable source name |
| `source_type` | yes | `exam`, `lexicon`, `phrase_list`, `frequency`, `corpus`, `dictionary`, `grammar`, `research`, etc. |
| `publisher` | yes | Organization responsible for the source |
| `url` | yes | Canonical landing/resource URL |
| `version` | recommended | Version, edition, or release identifier when available |
| `published_at` | recommended | Publication/release date when known |
| `retrieved_at` | recommended | Date the project obtained/checked the source |
| `checksum` | recommended | SHA-256 of cached raw artifact when available |
| `license_usage` | yes | Copyright/license/usage constraints relevant to storage and redistribution |
| `cefr_coverage` | recommended | CEFR levels represented, e.g. `A1-C1`, `C1-C2` |
| `data_types` | yes | Words, phrases, idioms, phrasal verbs, exam questions, frequency, etc. |
| `frequency_available` | yes | `yes`, `no`, or `partial` |
| `acquisition_method` | yes | How the source is obtained: `manual`, `download`, `script`, `api`, etc. |
| `raw_cache_path` | recommended | Repository path for a permitted cached artifact or acquisition metadata |
| `status` | yes | `active`, `candidate`, `deprecated`, `blocked`, `superseded` |
| `notes` | recommended | Interpretation, limitations, and provenance notes |

## Status semantics

- **active** — approved for current evidence/candidate generation.
- **candidate** — potentially useful but not yet validated for production use.
- **deprecated** — retained for historical reproducibility but should not drive new extraction.
- **blocked** — known access, licensing, reliability, or methodological issue prevents current use.
- **superseded** — replaced by a newer/stronger source; retain metadata for traceability.

## Source vs. curriculum rules

A source may contribute evidence without becoming curriculum.

Examples:

- A C1 vocabulary list expands the candidate universe.
- Corpus frequency describes commonness.
- PTNK past papers provide exam evidence.
- Diagnostic results determine whether the learner needs an item.
- Coverage rules prevent the system from over-investing in one semantic neighborhood.

Therefore:

> **CEFR opens the map. Frequency describes commonness. PTNK evidence identifies exam relevance. Diagnostic identifies learner need. Coverage determines where to expand next.**

## Raw-data policy

When legally and technically appropriate, preserve the raw artifact so future aggregation strategies can be rerun without repeated external acquisition.

When redistribution of the raw artifact is restricted, preserve instead:

1. canonical source URL;
2. acquisition procedure/script;
3. retrieval timestamp;
4. checksum when the artifact was locally obtained;
5. license/usage notes;
6. transformation/extraction notes.

Do **not** treat a generated CSV as a substitute for provenance. Curated data must retain a `source_id` back to this registry.

## Initial registry scope

The first registry should cover:

1. PTNK official specialized-English papers, 2022–2026;
2. Oxford Phrase List;
3. Oxford 3000/5000;
4. Oxford Phrasal Verbs / related official lexical resources where usable;
5. OPAL (Oxford Phrases / Academic Lexicon resources as applicable);
6. Cambridge English Vocabulary Profile / English Profile resources where access and reuse permit;
7. EFLLex / CEFRLex frequency resources;
8. other validated C1 candidate lists used only as candidate-generation inputs.

## Evidence hierarchy

For PTNK-specific claims, prefer:

1. official PTNK documents;
2. primary publisher/research sources;
3. established corpus/lexical resources;
4. reputable secondary analysis;
5. third-party lists only for candidate discovery.

A third-party list must not override direct PTNK evidence or independently verified lexical information.

## Future extensions

The registry can later add:

- `source_relation` for source supersession/derivation;
- `access_date` and `etag` where reproducible retrieval needs it;
- `extraction_version` for parser/version tracking;
- `content_language`;
- `quality_score` as source-level metadata only;
- `evidence_scope` to distinguish lexical, grammatical, reading, writing, or exam-structure evidence.

These fields should be added only when they solve a real reproducibility or provenance problem.
