# Knowledge Atom Discovery and Validation Pipeline

> Implementation specification for converting validated Destination section evidence into conservative knowledge-atom candidates. The canonical learning-material rules remain in `docs/learning-material-principles.md`.

## 1. Purpose

A **knowledge atom** is the smallest useful, independently referenceable piece of source-grounded knowledge that can later be linked to questions, competencies, and learner state.

This pipeline deliberately separates:

```text
validated sections
      ↓
source-span discovery
      ↓
candidate atoms
      ↓
validation / quality gates
      ↓
curation
      ↓
canonical knowledge atoms
```

Discovery does **not** mean automatic approval.

The first implementation is conservative: when structure or meaning is uncertain, it creates a pending candidate or reports an anomaly instead of guessing.

## 2. Inputs

Canonical structural evidence:

```text
sources/destination-c1-c2/sections/
  MANIFEST.tsv
  unit-*.txt
```

The section extractor has already validated that these files exactly match the planned source slices. The knowledge-atom pipeline must not modify them.

## 3. Candidate output

Discovery writes only a proposal layer:

```text
sources/destination-c1-c2/knowledge-atoms/
  discovery.jsonl
  discovery-report.json
```

No canonical `knowledge-atoms.jsonl` is written by discovery.

Every candidate starts with:

```text
content_status = source_candidate
confidence = pending | low | medium | high
```

A candidate may be promoted only after the validation gates pass.

## 4. Discovery strategy

Discovery is section-aware but evidence-first.

### Lexical sections

For vocabulary, topic vocabulary, phrasal verbs, phrases/patterns/collocations, idioms, and word formation, discover likely entry spans from source layout such as:

- table-like lexical entries;
- lexical form + part-of-speech markers;
- lexical form + definition/usage text;
- phrasal-verb + explanation pairs;
- collocation/pattern rows;
- word-formation rows or explicit derivational statements.

The detector must preserve the original source span. It must not invent a cleaner definition or silently normalize a damaged extraction.

### Grammar sections

Discover candidate blocks from explicit grammar headings, numbered explanations, rule statements, examples, tables, and contrast blocks.

A grammar candidate may initially have `atom_type = grammar_rule`, `grammar_pattern`, `lexical_contrast`, or `unknown`. Classification can remain pending.

### Assessment sections

Assessment sections are primarily question evidence, not the preferred source for creating standalone knowledge atoms. Discovery may record references/anomalies but must not turn answer choices into knowledge atoms merely because they appear in an exercise.

## 5. Internal-boundary anomaly detection

A section file may be structurally valid while still containing evidence of another section because PDF extraction can damage headings.

Discovery therefore scans each section for suspicious internal markers, including recognizable headings such as:

```text
Grammar
Vocabulary
Phrasal verbs
Phrases, patterns and collocations
Idioms
Word formation
Review
Progress Test
Topic vocabulary
```

If an internal heading is detected, the section is marked `needs_review` and candidate promotion is blocked until the boundary issue is resolved.

This is intentionally stricter than the section extractor's structural validation.

## 6. Provenance contract

Every candidate must preserve:

- `source_id`;
- `source_type`;
- Unit;
- section file;
- section index when available;
- source line start/end;
- original source span;
- section type/name;
- evidence status.

A candidate without sufficient provenance cannot become canonical.

## 7. No intrinsic priority

The knowledge-atom schema deliberately contains no lexical `priority` field.

Task urgency and review priority belong to learner-state/task-selection layers, not to the knowledge atom itself.

## 8. Validation gates

Before promotion, validate:

1. ID is unique and stable.
2. Required fields exist.
3. Source section exists.
4. Source line range is valid.
5. Candidate text exactly matches the cited source span.
6. Provenance is complete enough for the intended use.
7. Atom type is supported or explicitly pending.
8. No intrinsic lexical priority is present.
9. Unsupported definitions, pronunciation, CEFR, examples, patterns, or domains are not fabricated.
10. Internal section-boundary anomalies are resolved or candidate remains pending.
11. Relationships reference known IDs when relationships are declared.
12. Duplicate candidates are flagged rather than silently collapsed.

## 9. Promotion rule

Discovery may produce many candidates, but only candidates that pass the validation contract should enter the canonical knowledge layer.

```text
source_candidate
      ↓
validated
      ↓
curated
      ↓
canonical knowledge atom
```

Validation is a gate, not a score.

## 10. Expected future extension

Later stages can add independently verified enrichment:

```text
candidate
  ├─ lexical-source definition
  ├─ pronunciation evidence
  ├─ examples
  ├─ patterns/collocations
  ├─ CEFR evidence
  └─ competency relationships
```

Each enrichment retains its own evidence. No enrichment should overwrite the original source span.
