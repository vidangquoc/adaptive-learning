# PTNK Project — Context Recovery

> Recovery guide for the PTNK Adaptive Preparation System. The repository is the source of truth; inspect current files before trusting remembered conversation details.

## 1. Master recovery prompt

```text
Continue work on GitHub project `vidangquoc/PTNK`.

Project: PTNK Adaptive Preparation System for the Trường Phổ thông Năng khiếu (PTNK), ĐHQG-HCM specialized English entrance exam.

Core philosophy:
- This is a knowledge system + adaptive learning system, not a vocabulary list.
- Destination C1 & C2 are the foundational knowledge backbone.
- Challenge-first: challenge → diagnose gap → learn exactly what is needed → retest → update learner state.
- Destination exercises are canonical seed questions for the question bank.
- PTNK past papers are calibration/validation evidence, not the primary curriculum.
- No intrinsic priority for individual vocabulary items.
- Optimize learning value, not hours/pages/word counts.
- 700 hours is a ceiling/available budget, not a quota.

Source/data principles:
- Preserve raw source evidence separately from curated/normalized knowledge.
- Raw source data is immutable.
- Every promoted knowledge item retains provenance.
- Never invent definitions, meanings, pronunciation, examples, relationships, CEFR, or provenance.
- Accuracy beats completeness; preserve uncertainty instead of guessing.
- Structural extraction and provenance validation fail closed.

Destination source-boundary decision:
- The canonical structural source boundary is the **Unit**.
- Use `sources/destination-c1-c2/units/unit-XX.txt` as the authoritative Unit input.
- Do not use, require, or reconstruct `sources/destination-c1-c2/sections/`.
- Do not create a section manifest as an intermediate source-of-truth layer.
- Headings, topic labels, grammar labels, exercise labels, and other internal Unit structure may be retained as descriptive evidence/context, but they are not separate source-boundary files.
- Validate Unit boundaries before evidence discovery. If a Unit boundary is wrong, stop the pipeline and repair the source extraction before creating candidates.
- Provenance points to the Unit plus a precise location/span inside that Unit.

Knowledge-atom core decision:
- Knowledge atoms are FLAT and independent.
- One lexical sense = one atom by default.
- The same flat-atom rule applies to grammar: each independently useful grammar use, construction, rule, or contrast is its own atom when the source supports that distinction.
- Do not create word → sense → pattern → expression ancestry trees.
- Do not create parent grammar atoms with child uses merely because the source uses a shared heading.
- Related items may be separate atoms connected by explicit typed relationships when those relationships add real learning/query value.
- Learner mastery belongs in learner-state data, not in static knowledge.

Candidate-specific model:
- Candidate and official representations are separate.
- A candidate is a complete reviewable proposal, not a minimal parser row.
- Candidate fields include:
  atom_type
  canonical_form
  part_of_speech
  sense
  definition
  mother_says
  patterns
  usage_note
  source_status
  source_location
  evidence
  source_example
  context_status
  review_status
- Preserve ALL candidate fields even when values are blank/null/[] as appropriate.
- `definition` preserves a source-provided definition verbatim when available.
- `mother_says` is learner-facing Vietnamese interpretation, not source evidence.
- `patterns` and `usage_note` are populated only when supported by source evidence/context; otherwise remain empty/pending.
- `source_status`, `context_status`, and `review_status` are separate.
- Generated examples never replace source evidence.
- Officialization must not silently add new semantic interpretation.

Candidate → official flow:

SOURCE UNIT EVIDENCE
      ↓
CONTEXT-GROUNDED ANALYSIS
      ↓
COMPLETE CANDIDATE ATOM
      ↓
HUMAN REVIEW
      ↓
APPROVE / REJECT / HOLD
      ↓
COPY / PROMOTE
      ↓
OFFICIAL KNOWLEDGE

Officialization:
- current candidate status `APPROVED` and not yet officialized → promote/copy;
- already officialized → skip;
- any other status → do nothing;
- preserve candidate records intact;
- preserve provenance through `candidate_ref` or the current official lineage mechanism;
- do not invent new semantic meaning, patterns, usage notes, or evidence during promotion.

## 2. Discovery / extraction recovery prompt

```text
Resume Destination C1/C2 knowledge discovery.

Input:
- `sources/destination-c1-c2/units/unit-XX.txt`

Before discovery:
1. validate that Unit boundaries are correct;
2. confirm each Unit is complete and does not contain material from another Unit;
3. preserve the Unit source unchanged;
4. only then perform evidence discovery.

Discovery must work directly against Unit content.

Useful evidence signals include:
- explicit lexical/POS rows;
- word boxes and lexical tables;
- definitions and explanations;
- grammar headings and rule statements;
- examples and contrast blocks;
- collocation/pattern rows;
- idiom/phrasal-verb entries;
- word-formation rows;
- exercise/question material as assessment evidence.

Discovery output is evidence location, not canonical knowledge.
Do not automatically promote option pairs, fill-in answers, generic exercise markers, or other assessment artifacts into knowledge atoms.

For each proposal preserve:
- source Unit;
- precise location/span within Unit;
- exact source evidence;
- relevant surrounding Unit context;
- evidence type/status;
- inferred-vs-source-stated attributes.

Fail closed on:
- Unit-boundary errors;
- missing or contradictory provenance;
- unsupported semantic inference;
- malformed source spans;
- ambiguous atom identity.
```

## 3. Knowledge-model recovery prompt

```text
Resume the PTNK knowledge-atom model.

Read:
1. `schemas/knowledge-atom-candidate.schema.json`
2. `schemas/official-knowledge-atom.schema.json`
3. `docs/learning-material-principles/02-knowledge-model-and-interpretation.md`
4. `docs/knowledge-atom-pipeline.md`

Core ontology:
- flat independent atoms;
- one lexical sense = one atom by default;
- independently useful grammar uses/constructions/contrasts are separate atoms when supported;
- relationships are explicit typed links, not ancestry or inherited mastery;
- learner state is separate.

Do not infer ontology from parser structure or textbook headings.
```

## 4. Officialization recovery prompt

```text
Resume the candidate → official knowledge promotion workflow.

Promotion:
- if candidate `review_status` is `APPROVED` and not already officialized: copy/promote it;
- if already officialized: skip it;
- if status is anything else: do nothing;
- preserve candidate records intact;
- preserve candidate/source provenance;
- do not silently invent new meaning, patterns, usage notes, or other semantic interpretation during promotion;
- generated examples remain distinguishable from source examples/evidence.
```

## 5. Adaptive-learning recovery prompt

```text
Core adaptive loop:
Goal → competency model → knowledge base → diagnostic → learner state → learning frontier → next-best activity → assessment → updated learner state → review/extension.

Challenge-first:
Destination knowledge → challenge → correct: compress/skip → wrong/uncertain: identify exact gap → learn only what is needed → retest → update state.

Learning state is separate from static knowledge.
Potential mastery dimensions:
recognition, recall, usage, collocation, discrimination, transfer, retention.

Working progression:
UNSEEN → KNOWN → RECALLABLE → USABLE → MASTERED → MAINTENANCE
                                      ↘ EXTENDED

These are heuristics, not immutable constants.
Knowing one related atom never automatically implies knowing another atom.
```

## 6. Important stable decisions

- Destination C1/C2 = foundation; other sources are expansion layers.
- Challenge-first rather than sequential textbook completion.
- Destination exercises = canonical seed questions.
- PTNK specialized English is C1-centered with a C1+ competitive zone and a smaller C2 tail; do not label the whole exam C2 without official evidence.
- Individual vocabulary has no intrinsic priority.
- Raw/evidence/curated/learner-state layers remain separate.
- Source and official learning data are distinct: a raw source can support an official item without itself being the official learning record.
- `cefr_source` records where CEFR was independently verified; it is not the lexical source/provenance field.
- Fail closed on structural/provenance errors.
- Flat independent knowledge atoms; no mandatory lexical or grammar ancestry hierarchy.
- One lexical sense = one atom by default.
- Candidate-specific schema is distinct from official schema.
- Candidate is a complete reviewable proposal.
- `mother_says`, `patterns`, and `usage_note` belong in candidacy, not only officialization.
- Human review is the final promotion gate.
- Officialization is copy/promote, not hidden semantic authoring.

## 7. Repository navigation prompt

```text
Before substantive work, inspect current repository state and identify authoritative files.

At minimum inspect:
- `PROJECT-CONTEXT.md`
- `docs/learning-material-principles/`
- `docs/knowledge-atom-pipeline.md`
- candidate and official schemas
- relevant `data/candidates/` and `data/knowledge/` files
- relevant `scripts/`
- `sources/destination-c1-c2/units/`

Do not use an extracted `sections/` directory as a source-of-truth layer.
Use Git history to understand previous decisions, but do not revive superseded section-based extraction rules.
```

## 8. Recovery checklist

1. Identify repo `vidangquoc/PTNK`.
2. Read `PROJECT-CONTEXT.md`.
3. Read `docs/learning-material-principles/`.
4. Read candidate and official knowledge schemas.
5. Read `docs/knowledge-atom-pipeline.md`.
6. Inspect current Git state before assuming an old version is current.
7. Validate the Unit source boundaries.
8. Confirm the Unit files are complete before discovery.
9. Preserve flat-atom and candidate/official separation.
10. Make changes incrementally and verify consequential writes.

## 9. Maintenance rule

Update this file whenever a major architectural, ontology, data-layer, or governance decision is settled.

Do not record temporary hypotheses. Record only stable decisions needed to reconstruct the project accurately.

When a decision is superseded:
1. update the current rule;
2. preserve historical reasoning in the appropriate design document/Git history when useful;
3. remove obsolete instructions from recovery prompts so future sessions do not revive them.

The former section-based Destination extraction is superseded. Do not revive the old `177 sections`, `MANIFEST.tsv`, or `1,410 discovery candidates` as current repository state.
