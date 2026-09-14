# Destination C1–C2 Reference Layer

The reference layer is a searchable evidence layer used to resolve cross-references and validate source interpretation before knowledge-atom proposals are created.

## Purpose

Reference data is **not** canonical knowledge atoms. It is supporting source evidence.

The layer currently covers:

- Topic vocabulary database — including the glossary entries referenced by Unit sections such as `see page 224 for definitions` and `see page 225 for definitions`.
- Phrasal verbs database.
- Phrases, patterns and collocations database.
- Idioms database.
- Answer key.

## Role in the pipeline

```text
Unit evidence
    ↓
Reference lookup
    ↓
Context-aware linguistic / semantic analysis
    ↓
Knowledge-atom proposal
    ↓
Human review
```

A reference entry may supply a definition, sense, pattern, answer, or other evidence, but it must not automatically become a verified knowledge atom.

## Provenance requirements

Every reference record must retain:

- `reference_id`
- `source_id`
- `source_path`
- `source_type`
- `source_location`
- `source_text`
- `parsed_fields`
- `parser_version`

The original extracted source files remain immutable evidence. Normalized reference records are derived data and may be regenerated.

## Current source inventory

| Source | Role |
|---|---|
| `appendix-01-topic-vocabulary-database.txt` | glossary / topic-vocabulary definitions |
| `appendix-02-phrasal-verbs-database.txt` | phrasal-verb definitions |
| `appendix-03-phrases-patterns-collocations-database.txt` | phrase/pattern/collocation reference |
| `appendix-04-idioms-database.txt` | idiom definitions |
| `back-matter/section-01-answer-key.txt` | exercise-answer evidence |

## Design rule

**Reference extraction must preserve uncertainty and source wording.** If a record cannot be parsed confidently, keep the raw evidence and mark the structured fields as unresolved rather than guessing.
