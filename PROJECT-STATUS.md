# PTNK Project Status

**Last updated:** 2026-09-13  
**Branch:** `main`  
**Project type:** Adaptive PTNK Specialized English Preparation System

---

## 1. Current project state

### Overall status

🟡 **Architecture established; implementation of the adaptive learning loop is the next major phase.**

The project has moved beyond vocabulary collection. The current objective is to build an evidence-based system that determines what the learner needs, measures mastery, allocates learning effort, and continuously updates the next-best learning activity.

### Current mental model

```text
PTNK admission goal
        ↓
Competency model
        ↓
Evidence-backed curriculum
        ↓
Diagnostic
        ↓
Learning State
        ↓
Learning Frontier
        ↓
Review Queue
        ↓
Next-best Activity
        ↓
Assessment
        └──────────────→ Learning State
```

---

## 2. Completed

### Evidence / lexical architecture

- [x] RAW / EVIDENCE / CURATED / OFFICIAL separation
- [x] Data collection rules
- [x] Lexical definition rules
- [x] Accuracy-over-completeness policy
- [x] PTNK specialized English evidence pipeline
- [x] Official Lexicon pilot
- [x] P1 / P2 / P3 / P4 learner-facing views
- [x] Pipeline report

### Strategic research

- [x] Reviewed PTNK specialized English exam evidence from 2022–2026
- [x] Established working characterization: **C1-centered + C1+ competitive/discrimination zone + smaller C2 tail**
- [x] Rejected the unsupported assumption that the entire exam should be treated as C2
- [x] Established that vocabulary alone is insufficient; preparation must cover grammar, cloze, reading, word formation, error identification, sentence transformation, collocations, idioms, and lexical precision

### Adaptive-learning architecture

- [x] Defined item → competency → module → PTNK skill hierarchy
- [x] Defined Learning State concept
- [x] Defined mastery dimensions
- [x] Defined mastery states
- [x] Defined diagnostic-first approach
- [x] Defined adaptive branching
- [x] Defined review queue concept
- [x] Defined PTNK transfer coverage
- [x] Defined 700h as a ceiling / learning budget rather than a quota

### Recovery / continuity

- [x] Added `PROJECT-CONTEXT.md`
- [x] Added `docs/learning-state-specification.md`

---

## 3. Current repository artifacts

Important files:

```text
PROJECT-CONTEXT.md
PROJECT-STATUS.md

docs/
├── data-collection-rules.md
├── data-pipeline.md
├── lexical-definition-rules.md
├── ptnk-2026-pipeline-report.md
└── learning-state-specification.md

sources/
└── ptnk-2026/
    └── english-specialized.md

data/
├── evidence/
│   └── ptnk-2026-specialized-english.csv
└── lexicon/
    ├── ptnk-2026-official-v0.1.csv
    ├── ptnk-2026-p1.csv
    ├── ptnk-2026-p2.csv
    ├── ptnk-2026-p3.csv
    └── ptnk-2026-p4.csv
```

The lexical pilot is intentionally **not exhaustive**.

---

## 4. Current lexical pilot

Current official pilot entries:

1. `errand`
2. `run errands`
3. `menial`
4. `derivative`
5. `discursive`
6. `malleable`
7. `stick to your guns`
8. `cotton on to`
9. `square up to`
10. `in the face of`
11. `clear the decks`
12. `out on a limb`
13. `cut your losses`

`raw data` was intentionally removed because lexical verification had not been completed.

---

## 5. Immediate next work

### Priority 1 — make Learning State executable

- [ ] Create concrete `learner-state.csv` schema
- [ ] Create `attempt-history.csv` schema
- [ ] Create `competency-state.csv` schema
- [ ] Create `review-queue.csv` schema
- [ ] Define deterministic state-update rules
- [ ] Define deterministic review-priority rules

### Priority 2 — build the first adaptive pilot

- [ ] Define 5–10 representative competencies
- [ ] Map them to PTNK skills
- [ ] Create diagnostic questions
- [ ] Record attempt results
- [ ] Update state after each attempt
- [ ] Generate a review queue
- [ ] Verify that the queue explains *why* each item is recommended

### Priority 3 — expand curriculum coverage

Only after the adaptive loop works:

- [ ] Expand lexical coverage
- [ ] Expand grammar competencies
- [ ] Expand cloze competencies
- [ ] Expand reading competencies
- [ ] Expand word formation
- [ ] Expand error identification
- [ ] Expand sentence transformation

Do **not** reverse this order by collecting thousands of additional words before the learning-state loop is operational.

---

## 6. Current design rules

### Rule A — mastery beats exposure

Seeing an item in a lesson does not count as mastery.

### Rule B — no punishment for mastery

If diagnostic evidence shows the learner already knows something, skip or compress it.

### Rule C — diagnose dimensions, not just totals

Example:

```text
recall          98%
collocation     94%
usage           91%
transformation  58%
```

If transformation is required, the competency is not fully mastered.

### Rule D — target the bottleneck

Do not reteach an entire module when only one dimension is weak.

### Rule E — vocabulary is not the goal

Vocabulary is valuable only insofar as it contributes to actual PTNK competency and transfer.

### Rule F — 700h is not a quota

The learner may need much less than 700h. The system should allocate time according to demonstrated need and marginal learning value.

### Rule G — heuristics are provisional

Mastery thresholds and review intervals are starting rules. Do not present them as empirically validated until project data supports them.

### Rule H — preserve provenance

Every curriculum/evidence item should remain traceable to its source where applicable.

---

## 7. Current strategic hypothesis

The working strategic hypothesis is:

> The highest-value preparation is not maximizing the number of difficult English words learned. It is maximizing the learner's mastery of the competencies that discriminate performance on the PTNK specialized English exam, while minimizing wasted study time.

For a learner with strong vocabulary acquisition ability, the system should increasingly shift from breadth to:

- lexical precision;
- collocation;
- semantic discrimination;
- register;
- contextual usage;
- reading inference;
- advanced grammar;
- transformation;
- cloze reasoning;
- error detection;
- PTNK-style transfer.

---

## 8. 700-hour strategy

Current conceptual ceiling:

```text
CORE       ~300h
STRONG     ~200h
STRETCH    ~200h
TOTAL      ≤700h
```

This is elastic.

A learner who reaches the target early should stop, maintain, or optionally extend. A learner who has a specific bottleneck should spend more time there rather than following a fixed weekly quota.

---

## 9. Recovery protocol

If a new conversation is started, do this first:

### Read

1. `PROJECT-CONTEXT.md`
2. `PROJECT-STATUS.md`
3. `docs/learning-state-specification.md`
4. `docs/ptnk-2026-pipeline-report.md`
5. `docs/data-pipeline.md`
6. `docs/data-collection-rules.md`

### Then inspect

- current Git history;
- current `data/lexicon/` files;
- current `data/evidence/` files;
- current `sources/` files;
- any newer commits after this status file.

### Resume from

> **Priority 1: implement the concrete Learning State + Attempt History + Competency State + Review Queue schemas, then run a small end-to-end adaptive pilot.**

### Do not

- restart as a vocabulary-only project;
- assume C2 is the entire PTNK exam;
- treat the 700h framework as mandatory;
- collect huge lexical lists without a learning-state purpose;
- fabricate lexical or learner evidence;
- overwrite historical assessment evidence.

---

## 10. Definition of “done” for the next phase

The next phase is complete when the system can take a learner attempt such as:

```text
Learner answered a PTNK-style sentence-transformation item incorrectly.
```

and deterministically produce something like:

```text
Attempt recorded
      ↓
Competency identified
      ↓
Transfer dimension updated
      ↓
Competency remains below mastery gate
      ↓
Review queue entry created
      ↓
Reason: transfer weakness
      ↓
Recommended activity: targeted transformation drill
```

At that point the project has moved from **knowledge collection** to an actual **closed-loop learning system**.
