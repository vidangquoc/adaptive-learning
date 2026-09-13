# PTNK Project Context & Recovery Guide

> Canonical high-level context for continuing the project.

## 1. Project identity

This is **not merely a vocabulary collection project**.

Working concept:

> **PTNK Adaptive Preparation System** — an evidence-based, adaptive learning and strategy system whose objective is to maximize the learner's probability of success in the PTNK specialized English entrance exam, under finite time and school-load constraints.

Vocabulary/lexical research is one subsystem, not the final product.

## 2. Core optimization principle

Optimize **learning value**, not hours, pages, word counts, or syllabus completion.

Core loop:

```text
Goal → competency model → knowledge sources → diagnostic → learning state → learning frontier → next-best activity → assessment → updated learning state → review / extension
```

The curriculum must never punish mastery with repetition.

If the learner already knows something, skip it.
If the learner learns quickly, accelerate.
If one dimension is weak, target that dimension rather than reteaching everything.
If the target competency is mastered, stop or extend.

## 3. Curriculum backbone: Destination C1 & C2

**Destination C1 & C2 is the initial curriculum backbone.** It is the primary map from which the first competency/knowledge universe is constructed.

The system should first establish broad, durable mastery of the relevant competencies represented by Destination before systematically expanding into additional books.

Important: "master Destination" does **not** mean completing every page or exercise. It means demonstrating mastery of the competencies and knowledge items extracted from it.

Expansion principle:

```text
Destination C1 & C2
        ↓
Diagnostic
        ↓
Learn / skip / target weak dimensions
        ↓
Mastery + delayed retention
        ↓
Expansion gate
        ↓
Open additional sources only where they add meaningful breadth, depth, precision, or transfer
```

Additional sources are **expansion layers**, not parallel textbooks that must all be completed.

Suggested expansion roles:

- English Vocabulary in Use Advanced → vocabulary breadth/depth
- Advanced Grammar in Use → grammar depth and precision
- English Collocations in Use Advanced → collocation depth
- English Idioms in Use Advanced → idiom depth
- English Phrasal Verbs in Use Advanced → phrasal-verb depth
- Advanced Language Practice → integrated grammar/vocabulary practice
- Objective Advanced / Complete Advanced / Ready for Advanced / Expert Advanced → C1 competency and transfer practice
- C1 Advanced Trainer 2 / Cambridge authentic samples → assessment and transfer validation

A new source should normally be opened because the learner has reached an evidence-based frontier, not merely because the book exists.

## 4. Role of PTNK papers

PTNK papers are **calibration and validation evidence, not the primary vocabulary curriculum**.

Do not build a "PTNK vocabulary list" by treating past appearance as a prerequisite or by ranking words according to past frequency.

Working assumption:

> A C1/C2 item contained in the selected knowledge base is a legitimate candidate for future PTNK assessment, whether or not it appeared in the observed PTNK papers.

PTNK papers are used primarily to study:

- competency coverage;
- task formats;
- difficulty/discrimination;
- how advanced knowledge is operationalized in tasks;
- transfer requirements.

PTNK evidence may inform learning design and assessment, but **does not determine which individual vocabulary items are intrinsically more important**.

## 5. Current view of PTNK specialized English

Based on research of PTNK specialized English exams from 2022–2026:

- Do **not** assume the whole exam is C2.
- Best working characterization: **C1-centered, with a C1+ competitive/discrimination zone and a smaller C2 tail**.
- PTNK tests more than vocabulary: lexical precision, collocations, idioms, phrasal verbs, advanced grammar, cloze, reading inference, word formation, error identification, and sentence transformation.
- 2024–2026 especially place substantial weight on Language Use and Writing.
- Therefore preparation must be competency-based, not vocabulary-only.

## 6. Data architecture

```text
External sources
      ↓
RAW / EVIDENCE
      ↓
CURATED / NORMALIZED
      ↓
KNOWLEDGE BASE
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

Current learner-facing schema should **not require a vocabulary priority score**. Priority ranking of individual words is intentionally removed.

Core fields:

```text
id | word | word_type | pronunciation | meaning_en | meaning_vi | examples | patterns | usage_note | domain | word_formation | source_id | source_type | source_quality | official_status | cefr_status | cefr_source
```

Accuracy > completeness.
Never fabricate definitions, IPA, examples, patterns, CEFR, domain, or provenance.

## 7. Learning state

See `docs/learning-state-specification.md`.

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

## 8. Adaptive curriculum

Default module lifecycle:

```text
Diagnostic
→ Core
→ Usage
→ Application
→ Discrimination
→ Transfer
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

## 9. Expansion gate

The system should expand beyond Destination when all of the following are sufficiently satisfied:

1. the relevant Destination backbone competencies are broadly mastered;
2. delayed retention is stable enough;
3. important transfer weaknesses have been addressed;
4. the learner still has meaningful unused capacity/time;
5. an additional source offers a concrete breadth/depth/precision/transfer benefit.

Expansion should be **targeted**, not sequential book completion.

The default rule is:

> **Master → expand outward → deepen selectively when evidence shows depth has higher marginal value.**

Do not indefinitely deepen a semantic neighborhood merely because the learner is good at it.

## 10. 700-hour framework

The 700 hours are a **ceiling / available learning budget**, not a requirement.

Conceptual allocation:

```text
CORE       ~300h
STRONG     ~200h
STRETCH    ~200h
TOTAL      ≤700h
```

Actual time must be generated from learning state.

A module planned for 8h may take 2h if already mastered, or longer if a critical transfer weakness requires it.

Do not force the learner to consume all 700h.

## 11. Strategic priorities

Near-term objective:

> maximize probability of admission to PTNK specialized English while respecting school workload, health, sustainability, and opportunity cost.

The learner has strong demonstrated English ability and unusually good vocabulary learning capacity; therefore the system should aggressively avoid low-value repetition and use excess capacity for depth, discrimination, transfer, and advanced challenge.

Robotics is currently treated as a lower-priority activity during the fixed PTNK preparation window, with the understanding that this is a temporary allocation decision rather than abandonment of the longer-term STEM trajectory. Do not make absolute claims that Robotics has no relevance to future admissions.

## 12. Repository artifacts already established

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
- `docs/source-registry.md`
- `sources/source-registry.csv`
- `docs/books.md`

The current lexicon is an **end-to-end pilot**, not an exhaustive extraction of every lexical item from every exam.

## 13. Source-library policy

The current book library is considered **sufficient**. Do not continue expanding the bibliography merely to find more C1/C2 books.

The selected books have different roles, but Destination is the backbone. Other books are opened selectively as expansion layers.

Source discovery is therefore effectively frozen unless a genuinely new source demonstrates a clear missing capability that the existing library cannot cover.

Do not scrape or redistribute copyrighted books wholesale. Preserve provenance, acquisition procedure, checksums, extraction notes, and licensing/usage constraints where applicable.

## 14. What to build next

The next implementation step is **not simply adding more vocabulary**.

Priority order:

1. Formalize Destination C1 & C2 as the backbone knowledge/competency source.
2. Create concrete learning-state CSV schemas.
3. Create attempt-history structure.
4. Create competency/module definitions.
5. Create review-queue generation rules.
6. Map competencies to PTNK skills and task formats.
7. Create a small end-to-end pilot with real learner attempts.
8. Add expansion-source mappings only where the pilot reveals a concrete need.

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

## 15. Recovery instructions

If this conversation is lost, start by reading:

1. `PROJECT-CONTEXT.md`
2. `docs/learning-state-specification.md`
3. `docs/books.md`
4. `docs/ptnk-2026-pipeline-report.md`
5. `docs/data-pipeline.md`
6. `docs/data-collection-rules.md`
7. current files under `data/lexicon/`

Then inspect current Git history and repository state before making changes.

Do **not** restart the project as a vocabulary-list project or a PTNK-paper reverse-engineering project.

The correct mental model is:

> **Destination-backed adaptive PTNK preparation system; the broader C1/C2 library is an expansion layer, and PTNK papers are calibration/validation evidence.**
