# Methodology

## 1. Project scope

**Adaptive Learning** is the broader project. It was split out from the earlier **PTNK** project, which remains a domain-specific predecessor, evidence source, and validation target.

The goal is not to build a generic C2 word list and not to reverse-engineer PTNK papers into a curriculum. The goal is to build an evidence-based adaptive learning system whose knowledge can support multiple learning targets while using PTNK as one important calibration domain.

Vocabulary/lexical research is one subsystem of the learning system.

## 2. Evidence hierarchy

1. Primary/source materials and official assessment evidence for the target domain.
2. Cambridge English / English Profile / CEFR evidence where relevant.
3. Reliable learner/corpus evidence.
4. AI-generated practice material — useful for testing and challenge generation, but not evidence that a knowledge item is required.

PTNK exam papers are primarily calibration and validation evidence. Their appearance does not by itself make an individual lexical item intrinsically important.

## 3. Dataset and knowledge design

Separate:

- raw source evidence;
- evidence/observations;
- curated/normalized knowledge;
- learner state;
- generated challenges and assessment history.

Every promoted knowledge item should preserve provenance. CEFR levels must not be assigned unless independently verified.

## 4. Data-layer boundary

All canonical learning data is organized under two explicit boundaries:

- `data/knowledge/` — static knowledge, source evidence, relationships, and assessment definitions: **what there is to learn**.
- `data/learner/` — learner profile, learner state, attempts, sessions, and review queue: **what this learner knows and what should happen next**.

Recommended structure:

```text
data/
├── knowledge/
│   ├── sources/
│   │   ├── books/
│   │   │   └── <book>/
│   │   │       ├── book.yaml
│   │   │       └── chapters/
│   │   │           ├── ch01.txt
│   │   │           └── ch02.txt
│   │   └── ...
│   ├── atoms/
│   │   ├── grammar/
│   │   └── lexicon/
│   ├── relations/
│   └── assessments/
└── learner/
    ├── profile.yaml
    ├── state/
    │   ├── atom-state.yaml
    │   └── competency-state.yaml
    ├── attempts/
    ├── sessions/
    └── review-queue.yaml
```

Knowledge atoms must not contain learner mastery. Learner state references atom IDs rather than copying the knowledge definition. Assessment definitions belong to the knowledge layer; actual responses and outcomes belong to the learner layer.

## 5. Knowledge atoms

Each independent knowledge unit is represented as a **flat atom**: a unit that can be independently diagnosed, taught, and assessed.

Lexical and grammar knowledge follow the same flat-atom principle. Relationships are represented explicitly as typed relationships rather than by forcing a parent/child knowledge tree.

One lexical sense is one atom by default. Independently useful grammar uses, constructions, rules, or contrasts are separate atoms when the source supports that distinction.

Do not infer ontology from parser structure, textbook headings, or isolated examples.

## 6. Grammar knowledge atoms

A grammar example alone is not sufficient evidence for creating a grammar atom. If the source does not provide sufficient evidence for an independent grammar unit, the corresponding field remains empty/null rather than being authored as source fact by AI.

Grammar patterns, usage notes, and relationships follow the same provenance rule: record them only when supported by source evidence.

An exercise may activate multiple atoms simultaneously. The atoms remain separate for knowledge storage and learner-state diagnosis.

## 7. Roles

- `correct_answer`: the keyed answer.
- `distractor`: an option that appeared in the question but was not the keyed answer.
- `reading_only`: knowledge retained because it occurs in a reading/writing passage rather than as a direct target.
- `transformation_target`: a form required by a transformation task.

## 8. Study modes

- `learn`: high-value knowledge worth active study.
- `recognize`: useful to recognize in context, but not necessarily a first-tier memorization target.
- `defer`: retain for provenance/reference, but postpone active study until independently validated or recurrent.

## 9. Priority

Priority is a **study decision**, not a CEFR claim.

For PTNK-specific datasets, historical P1/P2/P3/P4 labels may remain because they are part of that dataset's provenance and workflow. They must not be interpreted as the universal priority model of Adaptive Learning.

## 10. Learning states

Learning state belongs to the learner layer rather than static knowledge. The broader project uses dimensions such as recognition, recall, usage, discrimination, transfer, and retention to determine whether a competency is actually mastered.

Working states and thresholds are heuristics until validated by project data.

## 11. Challenge-first learning

When prior knowledge is plausible, challenge should precede routine instruction:

```text
Knowledge / competency
        ↓
Challenge
   ↙         ↘
correct     wrong / uncertain
  ↓               ↓
skip/extend   trace gap
                  ↓
             targeted learning
                  ↓
                retest
```

The system optimizes learning value rather than pages, hours, word counts, or syllabus completion. Mastery should reduce unnecessary repetition.

## 12. Book-to-learning workflow

When a learner supplies a book and requests a chapter, the intended flow is:

```text
Book / chapter
     ↓
Extract grammar + lexicon atoms
     ↓
Preserve provenance
     ↓
Identify exercises / assessment opportunities
     ↓
Map questions to atoms and competency dimensions
     ↓
Diagnostic / challenge
     ↓
Learner response
     ↓
Attempt history
     ↓
Update learner state
     ↓
Review queue
     ↓
Adaptive next question
```

One exercise may test multiple atoms, and one atom may be tested by multiple questions.

## 13. Source expansion

Destination C1 & C2 is the initial curriculum backbone. Additional books and sources are expansion layers opened when evidence shows they add meaningful breadth, depth, precision, or transfer value.

PTNK evidence is used to calibrate and validate the system, not to replace the broader competency model.

## 14. Versioning

Knowledge schemas, extraction rules, and learner-state schemas must be versioned explicitly. When a rule changes, update the authoritative documentation and remove obsolete recovery instructions so future sessions do not revive superseded decisions.
