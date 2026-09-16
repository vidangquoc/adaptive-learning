# Knowledge Atom Discovery and Promotion Pipeline

> Implementation specification for converting validated source evidence into reviewable knowledge-atom proposals and then official knowledge. Conceptual ontology belongs to `model.md`; formal structure belongs to `atom-structure.md`; governance policy belongs to `docs/learning-material/principles/03-evidence-provenance-and-governance.md`.

## 1. Purpose

The pipeline locates source evidence, analyzes it in context, produces reviewable atom proposals, validates them, and promotes approved proposals into official knowledge.

```text
validated source
      ↓
evidence discovery
      ↓
contextual analysis
      ↓
atom proposal
      ↓
validation
      ↓
human review
      ↓
official knowledge
```

The pipeline does not treat parser output as knowledge.

## 2. Inputs and Preconditions

The pipeline consumes validated source material and its provenance. Source-boundary validation is defined by the learning-material source-boundary document.

Before discovery begins:

- the source input must be structurally valid;
- source evidence must be preserved immutably;
- provenance must be sufficient for later review.

## 3. Evidence Discovery

Parsers, layout detectors, regular expressions, table detectors, or similar tools may locate likely evidence.

Discovery may identify lexical entries, phrases, patterns, collocations, idioms, phrasal verbs, word formation, grammar, contrasts, examples, explanations, and assessment evidence.

Discovery output is **evidence location**, not canonical knowledge.

## 4. Contextual Analysis

After evidence is located, analyze the relevant source context before proposing knowledge.

The analysis may determine or propose:

- atom type;
- canonical form;
- part of speech;
- intended sense;
- meaning;
- lexicalization or idiomaticity;
- syntactic or usage pattern;
- word-formation relationship;
- lexical or grammatical contrast;
- relationships to other independent atoms.

Use the evidence hierarchy:

```text
explicit source statement
        ↓
strong contextual inference
        ↓
weak / ambiguous inference
        ↓
null / pending / review-needed
```

When context is insufficient, preserve uncertainty rather than inventing missing information.

## 5. Atom Splitting, Merging, and Deduplication

One source span does not necessarily equal one atom:

```text
one evidence span → multiple atoms
multiple evidence spans → one atom
one evidence span → no atom
```

Split when independently useful knowledge distinctions are supported by evidence. Merge evidence only when it supports the same underlying knowledge item and sense/use.

Do not merge merely because forms are similar, meanings overlap, items share a word family, or one expression contains another.

False deduplication is more damaging than controlled redundancy.

## 6. Proposal Output

A reviewable proposal should preserve, where applicable:

- stable proposal ID;
- source identity and boundary;
- precise source location;
- exact source span;
- relevant context/evidence references;
- proposed atom type;
- proposed knowledge fields;
- source-stated versus inferred attributes;
- confidence;
- warnings/anomalies;
- supported relationships;
- validation status.

No field should be populated solely because the schema permits it.

## 7. Validation

Automated validation should check, as applicable:

1. source structure and boundary validity;
2. exact source-span correspondence;
3. provenance completeness;
4. supported atom type and canonical form;
5. source-grounded meaning and part of speech;
6. unsupported definitions, pronunciation, examples, patterns, proficiency, or domain claims;
7. evidence for splitting/merging decisions;
8. duplicate or near-duplicate proposals;
9. relationship references;
10. ambiguous or competing interpretations;
11. schema validity.

Validation is a gate, not a replacement for human approval.

## 8. Human Review and Promotion

After validation, proposals enter human review. Promotion follows the governance policy in `03-evidence-provenance-and-governance.md`.

```text
APPROVE → eligible for promotion
REJECT  → do not promote
HOLD    → do not promote
```

The implementation must preserve the review decision and provenance and must not destroy the proposal record when creating official knowledge.

## 9. Fail-Closed Behavior

```text
PASS → continue
WARN → continue only when explicitly acceptable
FAIL → stop / preserve evidence / require review
```

If source structure, provenance, context, semantics, or atom identity cannot be established sufficiently, do not promote.

## 10. Reproducibility and Preservation

Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting raw evidence.

Transformations should be reproducible and idempotent where practical. Repairs must be explicit rather than silently altering source evidence.
