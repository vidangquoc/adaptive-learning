# Adaptive Learning — Project Context

> Canonical high-level context for continuing the project. The repository is the source of truth; inspect current files before relying on remembered conversation details.

## 1. Project identity

The canonical project is **Adaptive Learning** (`vidangquoc/adaptive-learning`).

**PTNK was the predecessor project from which Adaptive Learning was split.** PTNK remains an important domain-specific evidence source and validation target, but it is not the identity or scope of the whole repository.

This is not merely a vocabulary collection project and not merely a PTNK paper-analysis project. Vocabulary, grammar, knowledge atoms, challenges, assessments, learner state, and review logic are subsystems of a broader adaptive learning system.

## 2. Core objective

Build an evidence-based system that maximizes learning value under finite time and other real-world constraints by continuously deciding:

> **What should the learner do next, and why?**

Optimize learning value, not hours, pages, word counts, or syllabus completion.

## 3. Core adaptive loop

```text
Goal
  ↓
Competency model
  ↓
Knowledge sources
  ↓
Diagnostic / Challenge
  ↓
Learner state
  ↓
Learning frontier
  ↓
Next-best activity
  ↓
Assessment
  ↓
Updated learner state
  ↺
```

The curriculum must not punish mastery with repetition.

- If the learner already knows something, skip or compress it.
- If the learner learns quickly, accelerate.
- If one dimension is weak, target that dimension.
- If the competency is mastered, stop, maintain, or extend.

## 4. Challenge-first principle

When prior knowledge is plausible, challenging tasks should normally come before routine instruction.

```text
Knowledge / competency
        ↓
Challenge
   ↙         ↘
correct     wrong / uncertain
  ↓               ↓
skip/extend   trace exact gap
                  ↓
             targeted learning
                  ↓
                retest
```

Instruction is evidence-driven rather than page-driven.

## 5. Curriculum backbone

**Destination C1 & C2** is the initial curriculum/knowledge backbone. It is a source of competencies and knowledge, not a mandatory textbook sequence.

Additional books and sources are expansion layers. Open them when evidence shows a concrete breadth, depth, precision, or transfer benefit.

PTNK papers are primarily **calibration and validation evidence**. They help characterize competency coverage, task formats, difficulty/discrimination, and transfer requirements. They do not define the entire curriculum and past appearance does not make an individual vocabulary item intrinsically important.

Current working characterization of PTNK specialized English remains C1-centered, with a C1+ competitive/discrimination zone and a smaller C2 tail. Do not treat the whole exam as C2 without evidence.

## 6. Knowledge architecture

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

Knowledge atoms are **flat and independently diagnosable**. One lexical sense is one atom by default. Independently useful grammar uses/constructions/contrasts are separate atoms when supported by source evidence.

Do not create mandatory parent/child ancestry trees. Relationships are explicit typed links. Learner mastery belongs in learner-state data, not static knowledge.

## 7. Evidence and provenance rules

- Evidence > intuition.
- Accuracy > completeness.
- Preserve provenance and uncertainty.
- Never fabricate definitions, pronunciation, examples, patterns, relationships, CEFR, domain, or source evidence.
- Raw source material is distinct from curated knowledge.
- Generated practice/challenges are not evidence that an item is required.
- Structural extraction and provenance validation should fail closed on errors.

## 8. PTNK inheritance boundary

PTNK-specific artifacts may retain PTNK naming because they represent historical/domain-specific evidence. Examples include:

- `docs/ptnk-2026-pipeline-report.md`
- `sources/ptnk-2026/`
- `data/evidence/ptnk-2026-*`
- PTNK-specific lexical datasets

These names should **not** be renamed merely for cosmetic consistency. They describe the origin or target domain of the data.

Project-level documentation, however, must identify the repository as **Adaptive Learning** and describe PTNK as its predecessor/domain source.

## 9. Learning state

Learning state is separate from static knowledge.

Important dimensions include:

- recognition
- recall
- usage
- collocation
- discrimination
- transfer
- retention

Working progression:

```text
UNSEEN → KNOWN → RECALLABLE → USABLE → MASTERED → MAINTENANCE
                                      ↘ EXTENDED
```

These are working concepts/heuristics, not immutable constants.

## 10. Current implementation direction

The next major implementation phase is to make the adaptive loop executable:

1. concrete learner-state schema;
2. attempt-history schema;
3. competency-state schema;
4. review-queue schema;
5. deterministic state-update rules;
6. deterministic review-priority rules;
7. small end-to-end adaptive pilot;
8. only then expand knowledge coverage where the pilot demonstrates a need.

Do not revert to a vocabulary-only workflow.

## 11. Recovery protocol

When recovering context:

1. Read `PROJECT-CONTEXT.md`.
2. Read `PROJECT-STATUS.md`.
3. Read `docs/learning-state-specification.md`.
4. Read `docs/knowledge-atom-pipeline.md` and the relevant learning-material principles.
5. Read the relevant source/data rules.
6. Inspect current Git state and current data before changing anything.
7. Treat this repository as authoritative over stale conversation memory.

## 12. Maintenance rule

When a major architectural, ontology, data-layer, or governance decision is settled, update the canonical project documentation and recovery prompts.

When a decision is superseded, remove obsolete instructions so future sessions do not revive them.
