# PTNK Project — Context Recovery

> Recovery prompt for the PTNK Adaptive Preparation System. The repository is the source of truth; inspect current files before trusting remembered conversation details.

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

Destination extraction state:
- 26 units structurally validated.
- 177 structural section files extracted and validated.
- Section inventory: `sources/destination-c1-c2/sections/MANIFEST.tsv`.
- v3 evidence-specific discovery: 1,410 lexical candidates, 0 errors, 285 warnings.
- These 1,410 records are discovery candidates, NOT canonical knowledge atoms.
- v3 evidence classes: explicit_pos_row, explicit_word_box, lexical_table_head.
- Exercise markers, option pairs, and fill-in-the-blank rows are primarily question/exercise evidence and must not automatically become knowledge atoms.

Knowledge-atom core decision:
- Knowledge atoms are FLAT and independent.
- One lexical sense = one atom by default.
- Do not create word → sense → pattern → expression ownership/ancestry trees.
- Related items may be separate atoms connected by explicit typed relationships when those relationships add real learning/query value.
- Learner mastery belongs in learner-state data, not in static atoms.

Current candidate-specific model is separate from the official atom model.
Read:
- `schemas/knowledge-atom-candidate.schema.json`
- `schemas/official-knowledge-atom.schema.json` (or the current official schema path in the repo)
- `docs/learning-material-principles/02-knowledge-model-and-interpretation.md`
- `docs/knowledge-atom-pipeline.md`
- relevant discovery/extraction scripts

Candidate atoms are complete reviewable proposals, not minimal placeholders.
Candidate fields currently include:
- atom_type
- canonical_form
- part_of_speech
- sense
- definition
- mother_says
- patterns
- usage_note
- source_status
- source_location
- evidence
- source_example
- context_status
- review_status

Important candidate rules:
- Preserve ALL candidate fields even when data is unavailable. Do not delete empty fields.
- `definition` preserves a source-provided definition verbatim when available; do not paraphrase it.
- `mother_says` is the learner-facing Vietnamese meaning. Explanatory wording beyond the concise equivalent goes in parentheses, e.g. `suy ngẫm (suy nghĩ rất kỹ về điều gì đó trong một thời gian dài)`.
- `mother_says` is learner-facing interpretation, not source evidence or a source quote.
- `patterns` contains only genuine usage patterns supported by source evidence or strong context. No arbitrary combinations, translations, or synonyms. If unsupported, use `[]`.
- `usage_note` contains verified or strongly context-supported restriction, register, nuance, contrast, or other important usage information. If unsupported, leave blank/null.
- `source_status`, `context_status`, and `review_status` are separate. Strong source/context status does not imply `APPROVED`.
- `mother_says`, `patterns`, and `usage_note` are visible during human review; they are NOT invented only during officialization.
- If evidence is insufficient, preserve uncertainty rather than guessing.
- Officialization must not silently add new semantic interpretation to an approved candidate. Promotion is primarily copy + transform according to the official schema, with separately authorized enrichment only.
- Generated examples must never replace or masquerade as source evidence.
- If core semantic identity changes, return to candidate/review rather than silently patching official knowledge.

Candidate → official flow:

SOURCE EVIDENCE
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

Human review is the final gate for promotion.
Officialization is intentionally simple:
- current candidate status `APPROVED` and not yet officialized → promote/copy;
- already officialized → skip;
- any other status → do nothing.
A candidate may be reviewed again later and changed to `APPROVED`; no candidate-versioning machinery is required for this workflow.

Do not collapse candidate and official schemas for convenience.
Do not modify the final official schema merely because an extraction structure suggests a field. Settle ontology first, then update schema/pipeline.
```

## 2. Candidate atom recovery prompt

```text
Resume the PTNK candidate knowledge-atom model.

Read:
1. `schemas/knowledge-atom-candidate.schema.json`
2. `docs/learning-material-principles/02-knowledge-model-and-interpretation.md`
3. `data/candidates/` relevant files

Current decision:
A candidate is a complete reviewable knowledge-atom proposal.

Keep all candidate fields. Empty data stays represented as blank/null/[]; fields are never deleted merely because data is unavailable.

Candidate fields:
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

`mother_says`, `patterns`, and `usage_note` must be decided before human review when evidence supports them. Do not defer semantic interpretation to officialization.

Rules:
- source definition is preserved verbatim;
- mother_says = Vietnamese learner-facing meaning, with explanatory clarification in parentheses; it is not source evidence;
- patterns = evidence-supported genuine usage patterns only;
- usage_note = evidence-supported restriction/register/nuance/contrast only;
- unsupported values remain empty/pending;
- source_status, context_status, and review_status are separate and must not be conflated;
- generated examples are enrichment, not source evidence;
- no guessing merely to fill schema fields.
```

## 3. Officialization recovery prompt

```text
Resume the candidate → official knowledge promotion workflow.

Candidate and official are distinct representations.

Promotion:
- if candidate `review_status` is `APPROVED` and the candidate has not already been officialized: copy/promote it;
- if already officialized: skip it;
- if status is anything other than `APPROVED`: do nothing;
- preserve candidate records intact;
- preserve candidate/source provenance through `candidate_ref` or the current official lineage mechanism;
- do not silently invent new meaning, patterns, usage notes, or other semantic interpretation during promotion;
- apply only explicit official-schema normalization/transformation and separately authorized enrichment;
- generated examples must remain distinguishable from source examples/evidence.

No candidate-versioning machinery is required for this workflow.
```

## 4. Adaptive-learning recovery prompt

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

## 5. Discovery / extraction recovery prompt

```text
Resume Destination C1/C2 knowledge discovery.

Current validated structure:
- 26 units
- 177 sections
- MANIFEST.tsv is the structural inventory

v3 discovery:
- 1,410 lexical candidates
- 0 errors
- 285 warnings
- evidence classes: explicit_pos_row, explicit_word_box, lexical_table_head

Treat discovery output as evidence candidates, not canonical atoms.
Do not automatically promote option pairs, fill blanks, or generic exercise markers.
Validate canonical form, atom type, source location, lexical/layout authenticity, expression completeness, exercise contamination, provenance fidelity, and duplicate handling.
Fail closed on validation errors.
Do not weaken validation to increase counts.
```

## 6. Repository navigation prompt

```text
Before substantive work, inspect current repository state and identify authoritative files.

At minimum inspect:
- `PROJECT-CONTEXT.md`
- `docs/learning-material-principles/`
- `docs/knowledge-atom-pipeline.md`
- candidate and official schemas
- relevant `data/candidates/` and `data/knowledge/` files
- relevant `scripts/`
- `sources/destination-c1-c2/sections/MANIFEST.tsv`

Treat the current repository as authoritative. Use Git history to understand decisions, but do not revive superseded decisions without discussion.
```

## 7. Important historical decisions

- Destination C1/C2 = foundation; other sources are expansion layers.
- Challenge-first rather than sequential textbook completion.
- Destination exercises = canonical seed questions.
- PTNK specialized English is best treated as C1-centered with a C1+ competitive zone and smaller C2 tail; do not label the whole exam C2 without official evidence.
- Individual vocabulary has no intrinsic priority.
- Raw/evidence/curated/learner-state layers remain separate.
- Fail closed on structural/provenance errors.
- Flat independent knowledge atoms; no mandatory lexical ancestry hierarchy.
- One lexical sense = one atom by default.
- Candidate-specific schema is distinct from official schema.
- Candidate is a complete reviewable proposal.
- `mother_says`, `patterns`, and `usage_note` belong in candidacy, not only officialization.
- `mother_says` is learner-facing interpretation, not source evidence.
- Source examples remain source evidence; generated examples are separate enrichment.
- `source_status`, `context_status`, and `review_status` are distinct.
- Temporary parser candidates may exist internally; candidates entering human review must be persisted under `data/candidates/`.
- Officialization is intentionally simple and idempotent: current `APPROVED` + not yet officialized → copy/promote; already officialized → skip; any other status → do nothing.
- Officialization does not require candidate-versioning machinery.
- Officialization is copy/promote, not a hidden semantic-authoring step.
- Human review is the final promotion gate.

## 8. Recovery checklist

1. Identify repo `vidangquoc/PTNK`.
2. Read `PROJECT-CONTEXT.md`.
3. Read `docs/learning-material-principles/`.
4. Read candidate and official knowledge schemas.
5. Read `docs/knowledge-atom-pipeline.md`.
6. Inspect current Git state before assuming an old version is current.
7. Confirm 177-section extraction state.
8. Confirm v3 discovery state; do not rerun blindly.
9. Treat 1,410 as candidates, not canonical atoms.
10. Preserve flat-atom and candidate/official separation.
11. Make changes incrementally and verify consequential writes.

## 9. Maintenance rule

Update this file whenever a major architectural, ontology, data-layer, or governance decision is settled.

Do not record every temporary hypothesis. Record only stable decisions needed to reconstruct the project accurately.

When a decision is superseded:
1. update the current rule;
2. preserve historical reasoning in the appropriate design document/Git history when useful;
3. remove obsolete instructions from recovery prompts so future sessions do not revive them.

## 10. Current repository state snapshot

Latest candidate schema update:
- commit: `fb6e21c7b1401eff227aba3d8e6d402381b6e857`
- content SHA: `f7301c3e3c280e69ab7da803f26f041bc5637dd1`

Latest knowledge-model interpretation update:
- commit: `9f9c535858ed9b867b974e7842cfb3c8552a5c4f`
- content SHA: `db4399d233fe87870b5c4386c3c63e093715db0b0`

Latest evidence/provenance/governance update:
- commit: `f165096f7a27fb623c17822b343ec376d8436cd1`
- content SHA: `6a14aa910b40baf0bfd24e0f3ee5b94343f424a0`

These hashes are navigation aids, not substitutes for inspecting current repository state.
