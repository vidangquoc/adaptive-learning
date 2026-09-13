# PTNK Data Pipeline

> **Canonical learning-material construction principles:** `docs/learning-material-principles.md`
>
> This document describes the implementation layers of the data pipeline. It does not define a separate learning-material policy.

## 1. Pipeline

```text
External sources
    │
    ▼
RAW / EVIDENCE
    │  preserve original wording + provenance
    ▼
CLEAN / NORMALIZED
    │  normalize without destroying evidence
    ▼
CURATED KNOWLEDGE
    │  evidence-backed review
    ▼
KNOWLEDGE BASE
    │
    ├── knowledge atoms
    └── source exercises / questions
             │
             ▼
      Question ↔ Knowledge
             │
             ▼
      Competency / Challenge
```

## 2. Raw / Evidence

Raw records represent what was obtained from a source with minimal transformation.

Examples:

- instructional book material;
- PTNK exam document;
- verified transcription;
- answer key;
- dictionary evidence;
- corpus evidence;
- English Profile / EVP evidence.

Raw data should preserve source identity, location, original text where applicable, context, source quality, and uncertainty.

Raw records should not be rewritten merely to fit a final learner-facing schema.

## 3. Clean / Normalized

Cleaning and normalization are separate from raw evidence. Typical implementation work includes encoding cleanup, structural normalization, canonicalization, and controlled deduplication.

The raw layer remains the evidence baseline and must remain recoverable.

## 4. Curated Knowledge and Knowledge Base

Curated knowledge is derived from raw/evidence after the evidence requirements in `docs/learning-material-principles.md` have been satisfied.

The knowledge base may contain lexical, grammatical, word-formation, usage, and other knowledge atoms, together with provenance and relationships.

Destination exercises are retained as canonical seed questions and linked to the knowledge atoms they test.

## 5. Provenance dimensions

Keep provenance dimensions separate:

```text
lexical/source evidence → source_id / source_type / source_quality
PTNK relevance          → ptnk_evidence
CEFR evidence           → cefr_status / cefr_source
project lifecycle       → official_status
```

No one field should silently substitute for another.

## 6. Canonical rules

For all questions about how learning material should be constructed, classified, evidenced, normalized, linked, or promoted, use:

`docs/learning-material-principles.md`

That document is the single source of truth for:

- knowledge extraction;
- lexical and grammatical classification;
- meanings and pronunciation;
- examples and patterns;
- provenance;
- CEFR and external metadata;
- intrinsic-priority policy;
- question extraction;
- question-to-knowledge linkage;
- generated material;
- competency mapping;
- quality gates;
- copyright boundaries.

This file describes pipeline implementation only and must not introduce competing learning-material rules.
