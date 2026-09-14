# PTNK Project — Context Recovery

> Purpose: restore the working context of the PTNK Adaptive Preparation System if the original conversation is unavailable, interrupted, or blocked.
>
> This file is a recovery prompt pack, not a replacement for the repository documentation. When in doubt, inspect the repository and treat the current repository state as authoritative over remembered conversation details.

---

## 1. Master recovery prompt

Paste this first:

```text
You are continuing work on my GitHub project `vidangquoc/PTNK`.

The project is the PTNK Adaptive Preparation System for preparing a learner for the Trường Phổ thông Năng khiếu (PTNK), ĐHQG-HCM specialized English entrance exam.

IMPORTANT PROJECT PHILOSOPHY
- This is a knowledge system + adaptive learning system, not a vocabulary list.
- Destination C1 & C2 are the foundational knowledge backbone.
- The learner prefers challenging tests/problems over reading textbooks sequentially.
- Use a challenge-first loop: challenge → diagnose gap → learn exactly what is needed → retest → update learning state.
- Destination exercises are canonical seed questions for the question bank.
- PTNK past papers are secondary calibration/validation evidence, not the primary vocabulary curriculum.
- Do not assign intrinsic priority to individual vocabulary items. A C1/C2 item in the source books remains potentially relevant regardless of past-paper frequency.
- Learning/task urgency may exist in learner state or review scheduling, but it is NOT lexical intrinsic priority.
- Optimize learning value, not hours/pages/word counts.
- 700 hours is a ceiling/available learning budget, not a quota.

SOURCE / DATA PRINCIPLES
- Preserve raw source evidence separately from normalized/curated knowledge.
- Raw source data is immutable.
- Every promoted knowledge item must retain provenance to source evidence.
- Never invent definitions, meanings, pronunciation, examples, CEFR, relationships, or provenance.
- Accuracy beats completeness.
- Preserve uncertainty instead of guessing.
- Structural extraction must fail closed.
- Do not promote extraction candidates directly into canonical knowledge without validation.

CURRENT DESTINATION EXTRACTION STATE
- Source: Destination C1-C2 PDF.
- Raw extraction: `sources/destination-c1-c2/raw/Destination_C1-C2.txt`
- 26 units were structurally validated.
- 177 structural section files were successfully extracted and validated.
- `sources/destination-c1-c2/sections/MANIFEST.tsv` is the section inventory.
- Evidence-specific knowledge-atom discovery v3 currently passes its promotion gate.
- Latest confirmed discovery result: 1,410 candidate lexical records, with 0 candidate errors and 285 warnings.
- The 1,410 records are DISCOVERY CANDIDATES, not yet canonical knowledge atoms.
- Evidence types currently include explicit POS rows, explicit word boxes, and lexical table heads.
- Exercise markers, option pairs, and fill-in-the-blank evidence are exercise/question evidence and must not automatically become knowledge atoms.

KNOWLEDGE ATOM DESIGN — CURRENT WORKING DECISION
The ontology is intentionally being kept simple.

A knowledge atom is a stable, source-grounded, independently assessable unit of knowledge.

CRITICAL DECISION:
- Knowledge atoms are FLAT and independent.
- Do NOT build word → sense → pattern → expression parent/child/grandparent hierarchies merely to model lexical relationships.
- If a lexical item has multiple meaningful variants/senses/usages that can be learned or assessed independently, represent those variants as separate knowledge atoms.
- Do not create an ancestry tree of atoms.
- Relationships may be represented explicitly when they have real learning/query value, but a relationship is not an ownership hierarchy.
- Example: `take` sense A, `take` sense B, `take responsibility`, and `take something for granted` may all be independent atoms.
- This flat model is intended to keep adaptive learning, mastery tracking, querying, and question linkage simple.
- Learner mastery belongs in LearningState, not inside the static KnowledgeAtom.

KEY DISTINCTIONS
Knowledge Atom ≠ word necessarily.
Knowledge Atom ≠ question.
Knowledge Atom ≠ competency.
Knowledge Atom ≠ learner state.
Knowledge Atom ≠ intrinsic priority.

Question ↔ atom is many-to-many.
Competency ↔ atom is many-to-many.
LearningState is learner-specific and separate from the atom.

CURRENT KNOWLEDGE-ATOM DESIGN FILE
Read `docs/knowledge-atom-design.md` before changing the ontology.
It is the working ontology discussion document. It is not automatically identical to the JSON schema.

CURRENT SCHEMA / PIPELINE FILES
- `schemas/knowledge-atom.schema.json`
- `docs/knowledge-atom-pipeline.md`
- `scripts/discover_validate_knowledge_atoms.py` (older/broader discovery)
- `scripts/discover_validate_knowledge_atoms_v2.py`
- `scripts/discover_validate_knowledge_atoms_v3.py` (current evidence-specific discovery)
- `scripts/profile_knowledge_atom_sources.py`

IMPORTANT ONTOLOGY RULE
Do NOT modify the final schema just because a convenient extraction structure suggests it.
First discuss and settle the ontology in `docs/knowledge-atom-design.md`, then update the schema and pipeline.

CURRENT NEXT DESIGN QUESTION
Before large-scale semantic enrichment, we need to determine exactly what information a flat knowledge atom contains, what belongs in relationships, what belongs in source evidence, and what belongs in learner state.

Continue from the repository's current state. Do not assume old conversation decisions that contradict the repository.
```

---

## 2. Knowledge-atom ontology discussion prompt

Use this when the conversation specifically needs to resume the Knowledge Atom design:

```text
Resume the PTNK Knowledge Atom ontology discussion.

Read these first:
1. `docs/learning-material-principles.md`
2. `docs/knowledge-atom-design.md`
3. `schemas/knowledge-atom.schema.json`
4. `docs/knowledge-atom-pipeline.md`
5. the current knowledge-atom discovery scripts

Current core decision:

Knowledge atoms are FLAT, independent units.

For a lexical item, meaningful variants that can be independently learned, assessed, or tracked should be separate atoms. Do NOT create parent/child/grandparent/ancestor hierarchies such as:

word → sense → pattern → expression

Instead, represent each independently useful unit as an atom and use explicit typed relationships only when they provide genuine learning/query value.

For example, these can be separate atoms:
- a particular sense of `take`
- another sense of `take`
- `take responsibility`
- `take something for granted`

The fact that they are related does not mean one atom owns another.

Discuss the ontology from first principles. Focus on:
- minimum definition of an atom;
- atom boundaries;
- lexical variants;
- idioms, phrasal verbs, collocations, fixed expressions;
- grammar/pattern knowledge;
- word formation;
- what belongs directly in an atom;
- what belongs in typed relationships;
- provenance/evidence;
- derived metadata;
- what must remain outside the atom;
- how an atom can be independently assessed;
- how learner mastery can be tracked without embedding learner state;
- how atom ↔ question ↔ competency relationships work.

Do not rush into implementation. If the ontology is not settled, propose alternatives and test them with concrete Destination C1/C2 examples.
```

---

## 3. Schema-design prompt

Use only after the ontology discussion is sufficiently settled:

```text
We have agreed that PTNK Knowledge Atoms are flat independent units with no mandatory parent/child lexical hierarchy.

Now design the canonical `knowledge-atom.schema.json`.

Constraints:
- preserve provenance;
- preserve source evidence separately from normalized knowledge;
- no intrinsic lexical priority field;
- no learner-specific mastery fields inside the atom;
- do not silently invent fields just because an extraction script can produce them;
- distinguish source evidence, canonical knowledge, relationships, and derived metadata;
- allow explicit uncertainty/unknown status where appropriate;
- support lexical, grammatical, word-formation, and usage knowledge without forcing everything into one giant opaque text field;
- keep the model simple enough for adaptive querying and learner-state tracking.

Before writing the schema, explain the proposed fields and why each belongs in the atom.
Then validate the design against at least 10 concrete examples.
Only after that should the schema be changed.
```

---

## 4. Discovery / validation pipeline recovery prompt

```text
Resume the Destination C1/C2 knowledge-atom discovery pipeline.

Current state:
- 177 validated structural sections.
- v2 boundary validation passes with 0 blockers.
- v3 evidence-specific discovery passes with 1,410 candidates, 0 errors, 285 warnings.
- The candidate set is not canonical yet.

Current v3 evidence classes:
- explicit_pos_row
- explicit_word_box
- lexical_table_head

Do not automatically promote:
- option pairs;
- fill-in-the-blank rows;
- generic exercise markers.
Those are primarily question/exercise evidence.

Next recommended step is stratified validation of a reproducible sample of candidates before promotion.
Validate:
- canonical form;
- atom type;
- source location;
- lexical-vs-layout authenticity;
- expression completeness;
- exercise contamination;
- provenance fidelity;
- duplicate handling without prematurely destroying evidence.

Fail closed on validation errors.
Do not weaken validation merely to increase candidate counts.
Do not enrich semantics at scale before discovery quality is demonstrated.
```

---

## 5. Adaptive-learning architecture recovery prompt

```text
Resume the PTNK Adaptive Preparation System architecture.

Core loop:

Goal
→ competency model
→ knowledge base
→ diagnostic
→ learner state
→ learning frontier
→ next-best activity
→ assessment
→ updated learner state
→ review / extension

Challenge-first interface:

Destination C1/C2 knowledge
→ challenge
→ correct: compress/skip
→ wrong/uncertain: identify exact knowledge gap
→ learn only what is needed
→ retest
→ update state

Learning state is separate from static knowledge.

Potential mastery dimensions:
- recognition
- recall
- usage
- collocation
- discrimination
- transfer
- retention

Possible state progression:
UNSEEN → KNOWN → RECALLABLE → USABLE → MASTERED → MAINTENANCE
                                      ↘ EXTENDED

Do not treat these as immutable constants; they are working heuristics.

The adaptive system should never assume that knowing one related atom means knowing another atom. This is especially important under the flat Knowledge Atom model.
```

---

## 6. Repository navigation prompt

```text
Before doing substantive work on PTNK, inspect the repository and identify the current authoritative files.

At minimum inspect:
- `PROJECT-CONTEXT.md`
- `docs/learning-material-principles.md`
- `docs/knowledge-atom-design.md`
- `docs/knowledge-atom-pipeline.md`
- `schemas/knowledge-atom.schema.json`
- relevant `scripts/` files
- `sources/destination-c1-c2/sections/MANIFEST.tsv`

Treat current repository state as authoritative. Git history is useful for understanding why a decision exists, but do not revive superseded decisions without explicit discussion.
```

---

## 7. Important historical decisions

### Destination C1/C2
Destination C1 & C2 are the foundational knowledge backbone. Other sources are expansion layers, not parallel textbooks.

### Challenge-first
The learner does not need to read Destination sequentially. Use its exercises and extracted knowledge as backend material for challenges.

### Question bank
Destination exercises are canonical seed questions. Each question should ultimately be linked to the knowledge it tests. Generated questions should add instructional value rather than merely increase volume.

### PTNK exam level
Working characterization: PTNK specialized English is C1-centered, with a C1+ competitive/discrimination zone and a smaller C2 tail. Do not describe the entire exam as C2 without official evidence.

### Vocabulary priority
Removed. Do not rank individual lexical items by intrinsic importance.

### Raw/evidence/curated separation
Do not mix extraction, normalization, semantic enrichment, question generation, and learner-state computation into one layer.

### Fail-closed extraction
If structural boundaries or provenance validation fail, stop rather than guessing or silently overwriting data.

### Knowledge Atom model
Current working decision: **flat independent atoms**. Avoid elaborate lexical ancestry trees. Use explicit relationships only when they add real value.

---

## 8. Recovery checklist

When restarting after context loss:

1. Identify the repository: `vidangquoc/PTNK`.
2. Read `PROJECT-CONTEXT.md`.
3. Read `docs/learning-material-principles.md`.
4. Read `docs/knowledge-atom-design.md`.
5. Read the current knowledge-atom schema and pipeline docs.
6. Inspect current Git state/commits before assuming an old version is current.
7. Confirm the 177-section structural extraction state.
8. Confirm the v3 discovery result rather than rerunning blindly.
9. Treat 1,410 as candidates, not canonical atoms.
10. Preserve the flat-atom decision unless explicitly reconsidered.
11. Discuss ontology before modifying the final schema.
12. Make changes incrementally and validate after each stage.

---

## 9. Short emergency prompt

If there is very little context window available, paste this:

```text
Continue my project `vidangquoc/PTNK` as the PTNK Adaptive Preparation System.

Read `PROJECT-CONTEXT.md`, `docs/learning-material-principles.md`, and `docs/knowledge-atom-design.md` first.

Critical current decisions:
- Destination C1/C2 = foundational knowledge backbone.
- Challenge-first adaptive learning.
- Destination exercises = canonical seed question bank.
- PTNK papers = calibration/validation, not primary curriculum.
- No intrinsic vocabulary priority.
- Raw source → evidence → candidate → verified knowledge → enrichment → KB.
- Fail closed on structural/provenance errors.
- Current Destination extraction: 177 validated sections.
- Current v3 discovery: 1,410 lexical candidates, 0 errors, 285 warnings; candidates are NOT yet canonical atoms.
- Knowledge atoms are FLAT independent units. Do NOT create word/sense/pattern parent-child ancestry trees. Related variants can simply be separate atoms connected by explicit relationships when useful.
- Learner mastery/state is separate from static knowledge atoms.

Do not modify the final schema until the ontology is agreed.
```

---

## 10. Maintenance rule for this file

Update this file whenever a major architectural or ontology decision is settled.

Do not turn every temporary hypothesis into a recovery rule. Only record decisions that are stable enough to reconstruct the project accurately.

When a decision is superseded:
1. update the current rule;
2. optionally preserve the old reasoning in the relevant design document or Git history;
3. remove obsolete instructions from the emergency recovery prompt so the next session does not revive them.
