# PTNK Data Pipeline

This document explains how PTNK lexical data moves from external evidence to the official learning dataset.

## 1. Pipeline

```text
External sources
    │
    ▼
RAW / EVIDENCE
    │  preserve original wording + provenance
    ▼
CURATED / NORMALIZED
    │  normalize + enrich + review
    ▼
OFFICIAL LEXICON
    │
    ├── P1
    ├── P2
    ├── P3
    └── P4
```

## 2. Raw / Evidence

Raw records represent what was obtained from a source with minimal transformation.

Examples:

- PTNK exam document
- verified transcription
- answer key
- dictionary evidence
- corpus evidence
- English Profile / EVP evidence

Raw data should preserve:

- `source_id`
- source type
- source reference/location
- original text where applicable
- year/section/question when applicable
- role/context
- source quality
- uncertainty

Raw records should not be rewritten merely to fit the final Lexicon schema.

## 3. Curated / Normalized

Curated records are derived from raw evidence.

Typical work:

- canonical lexical form
- word type
- intended sense
- US IPA
- English/Vietnamese meanings
- examples
- genuine patterns
- domain
- PTNK priority
- word-formation relationship

Every curated record must point back to its source evidence.

## 4. Official Lexicon

`official` means the project has reviewed and approved the record for learner-facing use.

It does **not** mean every field came from an official PTNK document.

For example:

```text
Source:
  PTNK 2026 transcription
  source_quality = transcription

Curated Lexicon item:
  official_status = official
```

This is valid because the provenance remains explicit.

## 5. CEFR Is Independent

CEFR evidence is a separate provenance dimension.

```text
lexical source → source_id/source_type/source_quality
PTNK relevance → ptnk_evidence
CEFR evidence  → cefr_status/cefr_source
```

`cefr_source` must never replace `source_id` or `ptnk_evidence`.

If CEFR is not independently verified:

```text
cefr_status = not_verified
cefr_source =
```

## 6. Official Promotion Checklist

Before promotion to `official`, confirm:

- provenance exists;
- lexical form and sense are reviewed;
- meanings are accurate;
- pronunciation is verified or left unverified;
- examples are natural;
- patterns are genuine;
- domain is justified;
- priority reflects PTNK learning value;
- source quality is honest;
- CEFR is not guessed;
- the record is curated rather than a raw transcription copy.

## 7. Migration

Older data directories may remain for historical/source purposes:

```text
data/vocabulary/
data/idioms/
data/phrasal_verbs/
data/collocations/
data/word_formation/
```

Migration should preserve those files and map their content into the unified Lexicon only after provenance and lifecycle status are clear.

Do not silently delete or overwrite historical evidence during migration.
