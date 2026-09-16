# Knowledge Atom Discovery, Contextual Analysis, and Promotion Pipeline

> Implementation specification for converting validated Destination source evidence into context-grounded knowledge-atom proposals. The canonical learning-material rules remain in `docs/learning-material-principles.md` and its conceptually grouped child documents.

## 1. Purpose

A **knowledge atom** is the smallest useful, independently referenceable piece of source-grounded knowledge that can later be linked to questions, competencies, and learner state.

The pipeline must not treat parser output as knowledge. Extraction tools are used to locate and preserve evidence; interpretation and validation must operate on the source content and its relevant context.

The canonical flow is:

```text
validated Unit source
        ↓
source-order extraction / evidence discovery
        ↓
context-aware linguistic / semantic analysis
        ↓
knowledge-atom proposal
        ↓
human review
        ↓
verified knowledge atom
        ↓
enrichment / knowledge base
```

There is intentionally no requirement that a permanent intermediate `candidate` dataset exist between extraction and analysis. A tool may create temporary candidates internally when useful, but the reviewable output must be a context-grounded proposal rather than an unvalidated parser row.

## 2. Inputs

Canonical structural evidence is the **Unit source itself**:

```text
sources/destination-c1-c2/units/
  unit-01.txt
  unit-02.txt
  ...
```

A Unit is the canonical source boundary. The knowledge-atom pipeline must not depend on, require, or reconstruct a pre-cut `sections/` directory or section manifest.

Before discovery begins, validate the Unit boundaries and preserve the Unit source immutably. If Unit boundaries are invalid, stop the pipeline and repair the extraction layer before producing candidates.

## 3. Source-Order and Context Requirements

Analysis must preserve the instructional order of the Unit.

For each potential knowledge item, collect enough surrounding material to interpret it, including where available:

- headings and subheadings within the Unit;
- source lines around the item;
- lexical table row or word box;
- definitions or explanations supplied by the source;
- example sentences;
- usage notes and patterns;
- contrast sets;
- nearby instructions or task framing;
- relevant references elsewhere in the same Unit.

Do not reduce an item to an isolated token before analysis when surrounding context may determine its part of speech, sense, usage, or atom type.

When context is insufficient, preserve the uncertainty rather than inventing missing information.

## 4. Evidence Discovery

A parser, layout detector, regex, table detector, or other extraction method may be used to locate likely lexical or grammatical evidence.

For vocabulary, topic vocabulary, phrasal verbs, phrases/patterns/collocations, idioms, and word formation, useful evidence signals include:

- table-like lexical entries;
- lexical form + part-of-speech markers;
- lexical form + definition/usage text;
- phrasal-verb + explanation pairs;
- collocation/pattern rows;
- word-formation rows or explicit derivational statements.

For grammar, useful evidence signals include:

- explicit grammar headings within a Unit;
- numbered explanations;
- rule statements;
- examples;
- tables;
- contrast blocks;
- usage restrictions.

For assessment material, question content is primarily assessment evidence. Answer choices must not be promoted into knowledge atoms merely because they appear in an exercise.

Discovery output is **evidence location**, not canonical knowledge.

## 5. Context-Aware Analysis

After evidence is located, analyze the source content before proposing the atom.

The analysis may determine or propose:

- canonical form;
- atom type;
- part of speech;
- intended sense;
- meaning;
- lexicalization / idiomaticity;
- syntactic or usage pattern;
- word-formation relationship;
- lexical or grammatical contrast;
- orthographic variants;
- relationships to other independently useful atoms.

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

A field must remain null or pending when the available context does not support a reliable inference.

Context may identify an intended sense, but context alone must not be treated as authority for inventing a dictionary definition.

All inferred attributes must be distinguishable from source-stated attributes and retain appropriate evidence/provenance and confidence.

## 6. Atom Splitting, Merging, and Deduplication

One source span does not necessarily equal one knowledge atom.

The analysis may propose:

```text
one evidence span → multiple independent atoms
multiple evidence spans → one atom with multiple evidence links
one evidence span → no atom
```

Split when distinctions are independently useful for learning, assessment, querying, or learner-state tracking. For example, a source entry marked `(v,n)` may support separate verb and noun atoms if the evidence supports both readings.

For grammar, the same principle applies: if a Unit supports separate uses or contrasts that can be independently learned or assessed, split them into flat independent atoms. Do not create a parent grammar atom with child uses merely because they share a textbook heading.

Do not merge merely because forms are similar, meanings overlap, items share a word family, or one expression contains another.

False deduplication is more damaging than controlled redundancy.

## 7. Proposal Output

The pipeline should produce a reviewable **atom proposal** containing, where supported:

- stable proposal ID;
- source ID/type;
- source Unit;
- precise source location within the Unit;
- exact original source span;
- surrounding context/evidence references;
- proposed atom type;
- proposed canonical form;
- source-stated attributes;
- inferred attributes;
- confidence;
- warnings/anomalies;
- relationships, if supported;
- analysis notes;
- validation status.

No proposal field should be populated solely because the schema permits it.

## 8. Provenance Contract

Every proposal must preserve enough provenance to answer:

> **Where did this come from, and what evidence supports this interpretation?**

At minimum preserve:

- `source_id`;
- `source_type`;
- Unit;
- precise source location within the Unit;
- exact original source span;
- relevant surrounding Unit context;
- evidence status;
- inference status where applicable.

A proposal without sufficient provenance cannot become canonical.

The Unit is the source-boundary identifier. A textbook heading, topic label, exercise label, or exam section may be recorded as descriptive context when useful, but none is a required extracted source layer.

## 9. Automated Validation and Quality Gates

Automated analysis is advisory but must perform substantive validation before human review.

Validate, as applicable:

1. Unit exists and is structurally valid.
2. Source span exactly matches the cited evidence.
3. Provenance is complete enough for review.
4. Proposed atom type is supported or explicitly pending.
5. Canonical form is grounded in the source.
6. Part of speech is source-stated or context-supported.
7. Meaning/sense is source-stated or sufficiently supported by context.
8. Unsupported definitions, pronunciation, CEFR, examples, patterns, or domains are not fabricated.
9. Atom splitting/merging decisions have evidence.
10. Duplicate or near-duplicate proposals are flagged rather than silently collapsed.
11. Relationships reference known or explicitly pending entities.
12. Unit-boundary anomalies are resolved or the proposal remains blocked.
13. No intrinsic lexical priority is introduced.
14. Ambiguous or competing interpretations are explicitly flagged.
15. Insufficient evidence results in `null`, `pending`, or `review-needed`, not a guessed value.

Validation is a gate, not a score. A high confidence value does not replace human approval.

## 10. Human Promotion Gate

After automated contextual analysis and validation, the proposal enters human review.

The reviewer may:

```text
APPROVE
REJECT
HOLD
```

Only `APPROVE` may promote a proposal to an official knowledge atom.

The human decision and rationale must be preserved with provenance.

> **Machine proposes. Human decides.**

## 11. Fail-Closed Behavior

```text
PASS → continue
WARN → continue only when explicitly acceptable
FAIL → stop / preserve evidence / require review
```

If structure, provenance, context, semantics, or atom identity cannot be established with sufficient confidence, do not promote.

Preserve the evidence and mark the proposal for review instead.

## 12. Reproducibility and Source Preservation

Raw Unit source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting the raw evidence layer.

Transformations should be reproducible and idempotent where practical. Do not silently repair source evidence; record repairs or downstream normalization explicitly.

Keep these concerns separable:

```text
source Unit evidence
contextual interpretation
validation
human decision
enrichment
learning design
learner state
```
