# PTNK Project Context & Recovery Guide

> This file is the canonical high-level context for continuing the project in a new conversation.

## 1. Project identity

This is **not merely a vocabulary collection project**.

Working concept:

> **PTNK Adaptive Preparation System** — an evidence-based, adaptive learning and strategy system whose objective is to maximize the learner's probability of success in the PTNK specialized English entrance exam, under finite time and school-load constraints.

Vocabulary/lexical research is one subsystem, not the final product.

Ultimate strategic context: PTNK admission is a near-term objective and potentially a useful environment for the learner's longer-term academic/STEM trajectory. Do not treat PTNK itself as the ultimate life goal.

---

## 2. Core optimization principle

The system should optimize **learning value**, not hours, pages, word counts, or syllabus completion.

Core loop:

```text
Goal
→ competency model
→ evidence / curriculum
→ diagnostic
→ learning state
→ learning frontier
→ next-best activity
→ assessment
→ updated learning state
→ review / extension
```

The curriculum must never punish mastery with repetition.

If the learner already knows something, skip it.
If the learner learns quickly, accelerate.
If one dimension is weak, target that dimension rather than reteaching everything.
If the target competency is mastered, stop or extend.

---

## 3. Current view of PTNK specialized English

Based on research of PTNK specialized English exams from 2022–2026:

- Do **not** assume the whole exam is C2.
- Best working characterization: **C1-centered, with a C1+ competitive/discrimination zone and a smaller C2 tail**.
- PTNK tests more than vocabulary: lexical precision, collocations, idioms, phrasal verbs, advanced grammar, cloze, reading inference, word formation, error identification, and sentence transformation.
- 2024–2026 especially place substantial weight on Language Use and Writing.
- Therefore preparation must be competency-based, not vocabulary-only.

Evidence and source details live under `sources/`, `data/evidence/`, and `docs/`.

---

## 4. Data architecture

```text
External sources
      ↓
RAW / EVIDENCE
      ↓
CURATED / NORMALIZED
      ↓
OFFICIAL LEXICON
      ↓
COMPETENCY / MODULE MODEL
      ↓
LEARNING STATE
      ↓
REVIEW QUEUE
      ↓
NEXT-BEST ACTIVITY
```

### Vocabulary

The Lexicon contains single words, idioms, phrasal verbs, collocations, fixed expressions, and selected word-formation results.

Current learner-facing schema:

```text
id | word | word_type | pronunciation | meaning_en | meaning_vi | examples | patterns | usage_note | domain | priority | word_formation | ptnk_evidence | source_id | source_type | source_quality | official_status | cefr_status | cefr_source
```

Accuracy > completeness.
Never fabricate definitions, IPA, examples, patterns, CEFR, domain, priority, or provenance.

### Learning state

See:

`docs/learning-state-specification.md`

Main levels:

```text
item → competency → module → PTNK skill
```

Core states:

```text
UNSEEN → KNOWN → RECALLABLE → USABLE → MASTERED → MAINTENANCE
                                             ↘ EXTENDED
```

Important mastery dimensions:

- recognition
- recall
- usage
- collocation
- discrimination
- transfer
- retention

A single high score is not enough to declare mastery if a required dimension is weak.

---

## 5. Adaptive curriculum

Default module lifecycle:

```text
Diagnostic
→ Core
→ Usage
→ Application
→ Discrimination
→ PTNK Transfer
→ Mastery Gate
→ Maintenance / Extension
```

A module is a single testable competency, not a chapter or a fixed number of words.

Diagnostic-first rule:

- ≥90–95% and no critical weak dimension → skip/compress core;
- 80–89% → targeted practice;
- 65–79% → developing/remediation;
- <65% → weak/remediate.

These thresholds are starting heuristics, not sacred constants.

---

## 6. 700-hour framework

The 700 hours are a **ceiling / available learning budget**, not a requirement.

Conceptual allocation:

```text
CORE       ~300h
STRONG     ~200h
STRETCH    ~200h
TOTAL      ≤700h
```

Actual time must be generated from learning state.

A module planned for 8h may take 2h if already mastered, or 10h if a critical transfer weakness requires it.

Do not force the learner to consume all 700h.

---

## 7. Strategic priorities

Near-term objective:

> maximize probability of admission to PTNK specialized English while respecting school workload, health, sustainability, and opportunity cost.

The learner has strong demonstrated English ability and unusually good vocabulary learning capacity; therefore the system should aggressively avoid low-value repetition and use excess capacity for depth, discrimination, transfer, and advanced challenge.

Robotics is currently treated as a lower-priority activity during the fixed PTNK preparation window, with the understanding that this is a temporary allocation decision rather than abandonment of the longer-term STEM trajectory. Do not make absolute claims that Robotics has no relevance to future admissions.

---

## 8. Repository artifacts already established

Important files:

- `docs/data-collection-rules.md`
- `docs/data-pipeline.md`
- `docs/lexical-definition-rules.md`
- `docs/ptnk-2026-pipeline-report.md`
- `docs/learning-state-specification.md`
- `sources/ptnk-2026/english-specialized.md`
- `data/evidence/ptnk-2026-specialized-english.csv`
- `data/lexicon/ptnk-2026-official-v0.1.csv`
- `data/lexicon/ptnk-2026-p1.csv`
- `data/lexicon/ptnk-2026-p2.csv`
- `data/lexicon/ptnk-2026-p3.csv`
- `data/lexicon/ptnk-2026-p4.csv`

The current lexicon is an **end-to-end pilot**, not an exhaustive extraction of every lexical item from every exam.

---

## 9. Important current lexical pilot

The 13 current official pilot entries are:

- errand
- run errands
- menial
- derivative
- discursive
- malleable
- stick to your guns
- cotton on to
- square up to
- in the face of
- clear the decks
- out on a limb
- cut your losses

`raw data` was deliberately removed because lexical verification had not been completed.

---

## 10. What to build next

The next implementation step is **not simply adding more vocabulary**.

Priority order:

1. Create concrete learning-state CSV schemas.
2. Create attempt-history structure.
3. Create competency/module definitions.
4. Create review-queue generation rules.
5. Map competencies to PTNK skills.
6. Create a small end-to-end pilot with real learner attempts.
7. Only then scale lexical coverage and curriculum breadth.

Desired eventual system:

```text
Question / exercise result
        ↓
Attempt history
        ↓
Learning-state update
        ↓
Weakness / retention detection
        ↓
Review queue
        ↓
Next-best activity
```

---

## 11. Recovery instructions for a new conversation

If this conversation is lost, start by reading:

1. `PROJECT-CONTEXT.md`
2. `docs/learning-state-specification.md`
3. `docs/ptnk-2026-pipeline-report.md`
4. `docs/data-pipeline.md`
5. `docs/data-collection-rules.md`
6. current files under `data/lexicon/`

Then inspect the current Git history and repository state before making changes.

Do **not** restart the project as a vocabulary-list project.

The correct mental model is:

> **adaptive PTNK preparation system; vocabulary is one evidence-backed subsystem.**

Before adding substantial new data, preserve the separation between evidence, curated knowledge, curriculum, and learner state.
