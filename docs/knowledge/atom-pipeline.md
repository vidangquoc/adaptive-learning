# Knowledge Atom Discovery and Promotion Pipeline

> Implementation specification for converting validated source evidence into Candidates and then Official Atoms. Conceptual ontology belongs to `overall.md`; formal structure belongs to `atom-structure.md`; taxonomy belongs to `atom-types.md`; governance policy belongs to `docs/learning-material/principles/03-evidence-provenance-and-governance.md`.

## 1. Purpose

The pipeline locates source evidence, analyzes it in context, creates complete Candidate Atoms, validates and reviews them, and officializes approved Candidates into the separate Official Store.

```text
validated source
      ↓
evidence discovery
      ↓
contextual analysis
      ↓
Candidate Store
      ↓
validation
      ↓
human review
      ↓
approved Candidate
      ↓
officialize
      ↓
Official Store
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

## 6. Candidate Output

A Candidate is a complete Knowledge Atom, not a partial proposal schema.

Candidate output uses the canonical atom structure defined in `atom-structure.md`, with the additional lifecycle field:

```yaml
review_status: pending
```

### Candidate physical representation

Candidates are persisted in `knowledge_atom_candidates.md` as a Markdown collection of fenced YAML blocks. Each fenced YAML block is one complete Candidate Atom and must independently validate against `schemas/candidate-atom.schema.json`.

There is no collection-level YAML wrapper such as `candidates:` and no second presentation-specific atom format. `review_status` remains a top-level lifecycle field in each Candidate and is not part of `extra`.

Markdown headings may be used to make human review easier, but headings are organizational presentation and are not part of the Candidate Atom data.

The Candidate must preserve, where applicable:

- semantic ID;
- source identity and boundary;
- precise source location;
- exact source evidence;
- relevant context/evidence references;
- atom type and canonical knowledge fields;
- source-stated versus inferred attributes;
- confidence or warnings when supported by the implementation.

A Candidate does not use a separate `candidate_id`, temporary ID, or tracking ID. Its semantic ID is created correctly when the Candidate is created.

No field should be populated solely because the schema permits it.

## 7. Physical Store Layout

Candidate and Official Atoms are stored under the same source/segment/domain hierarchy, while lifecycle is represented by the file name:

```text
data/
└── knowledge/
    └── <source-id>/
        └── <segment-id>/
            └── <domain>/
                ├── knowledge_atoms.md
                └── knowledge_atom_candidates.md
```

The stores are:

- Official Store: `data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atoms.md`
- Candidate Store: `data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atom_candidates.md`

Path semantics:

- `<source-id>` is the canonical `source_id` from the Source Registry.
- `<segment-id>` is the canonical `segment_id` from source segmentation.
- `<domain>` is the Knowledge Atom domain.
- The storage path is an organizational location, not the semantic identity of an atom.
- Atom semantic IDs remain independent of their storage path.

There is no additional `official/` or `candidates/` directory layer.

## 8. Validation

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

## 9. Human Review and Officialization

After validation, Candidates enter human review. Review status has exactly three values:

```text
pending
approved
rejected
```

- A newly created Candidate starts as `pending`.
- The reviewer may leave it `pending`, change it to `approved`, or change it to `rejected`.
- A rejected Candidate remains in the Candidate Store and may be reviewed again.
- `approved` means eligible for officialization; it is not yet Official.

Officialization is a storage transition:

1. select Candidates with `review_status: approved`;
2. write each Official Atom to the separate Official Store with the same semantic ID;
3. delete the corresponding Candidate from the Candidate Store.

There is no `officialized` review status. Pending and rejected Candidates are not affected by officialization. An Official Atom does not return to the Candidate/rejected lifecycle.

## 10. Official Atom Correction

An Official Atom may be corrected or refined while retaining the same semantic ID when the knowledge identity remains unchanged. A change that creates a genuinely different knowledge identity must be handled as a semantic-identity change rather than as ordinary correction.

## 11. Fail-Closed Behavior

```text
PASS → continue
WARN → continue only when explicitly acceptable
FAIL → stop / preserve evidence / require review
```

If source structure, provenance, context, semantics, or atom identity cannot be established sufficiently, do not promote.

## 12. Reproducibility and Preservation

Raw source evidence is immutable once captured. Later stages may add interpretation, validation, enrichment, competency mappings, questions, or learner-state data without rewriting raw evidence.

Transformations should be reproducible and idempotent where practical. Repairs must be explicit rather than silently altering source evidence.
