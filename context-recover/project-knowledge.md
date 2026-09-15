# Adaptive Learning — Project Knowledge

## Purpose

This file is the compact knowledge baseline used to recover the meaning of the Adaptive Learning project before task-specific work begins.

It is a **map to authoritative project knowledge**, not a replacement for the detailed documentation in `docs/` or the actual data in the repository.

## 1. Project Identity

- Repository: `vidangquoc/adaptive-learning`
- Project: **Adaptive Learning**
- Adaptive Learning was split from the earlier **PTNK** project.
- PTNK remains a domain-specific predecessor, evidence source, and calibration/validation target; it is not the identity or scope of the whole project.

Authoritative overview and methodology:
- `docs/methodology.md`

## 2. Project Model

Adaptive Learning is an evidence-based adaptive learning system whose central decision is:

> **What should the learner do next, and why?**

The intended closed loop is:

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

Core methodological principles include challenge-first learning, evidence-driven instruction, mastery-sensitive progression, and explicit provenance.

See:
- `docs/methodology.md`
- relevant files under `docs/learning-material-principles/`

## 3. Learning Knowledge Model

The knowledge side represents **what there is to learn** and the evidence supporting it.

Primary concepts:

- source material / evidence;
- curated and normalized knowledge;
- flat knowledge atoms;
- typed relationships;
- competencies;
- assessment definitions;
- provenance and uncertainty.

A knowledge atom is independently diagnosable, teachable, and assessable. One lexical sense is one atom by default. Independently useful grammar uses, constructions, rules, or contrasts may be separate atoms when supported by evidence.

Knowledge atoms do not contain learner mastery.

Authoritative detailed references:
- `docs/methodology.md`
- `docs/knowledge-atom-pipeline.md`
- `docs/data-architecture.md`
- `docs/learning-state-specification.md`

## 4. Learning-Material Data

Canonical learning data is organized under `data/knowledge/`.

```text
data/knowledge/
├── sources/
├── atoms/
│   ├── grammar/
│   └── lexicon/
├── relations/
└── assessments/
```

The exact contents and current implementation state must always be read from the repository rather than inferred from this map.

Important boundary:

> Knowledge data describes what can be learned; it does not describe what a particular learner has mastered.

Source provenance must remain traceable. Generated practice is not evidence that an item is required.

## 5. Learner-Data Model

Learner data describes **what a learner has done, knows, needs to review, and how their state changes over time**.

Canonical boundary:

```text
data/learner/
├── profile.yaml
├── state/
│   ├── atom-state.yaml
│   └── competency-state.yaml
├── attempts/
├── sessions/
└── review-queue.yaml
```

The structure is a logical target architecture; current files must be verified in the repository.

Key distinctions:

- **Attempt history** = historical evidence from learner interactions.
- **Learner state** = current interpretation of accumulated evidence.
- **Session** = sequence of adaptive decisions and resulting evidence/state changes.
- **Review queue** = derived recommendation view, not the source of truth.
- **Assessment definition** = knowledge-side definition of what a question tests.
- **Learner response/outcome** = learner-side record of what happened.

Learner state references knowledge-atom IDs rather than duplicating knowledge definitions.

Detailed references:
- `docs/data-architecture.md`
- `docs/learning-state-specification.md`

## 6. Learning-State Concepts

The project uses learning-state dimensions such as:

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

These are working concepts/heuristics and must not be treated as immutable constants unless authoritative documentation establishes them as such.

## 7. Book-to-Learning Flow

The intended flow from learning material to adaptive learning is:

```text
Book / chapter
     ↓
Source evidence
     ↓
Knowledge atoms
     ↓
Assessment definitions
     ↓
Diagnostic / challenge
     ↓
Learner attempts
     ↓
Learner state
     ↓
Review queue
     ↓
Next-best activity
```

One exercise may test multiple atoms, and one atom may be tested by multiple questions.

## 8. Curriculum and PTNK Boundary

Destination C1 & C2 is the initial curriculum/knowledge backbone, not a mandatory textbook sequence.

Additional sources are expansion layers opened when evidence shows meaningful breadth, depth, precision, or transfer value.

PTNK materials are primarily calibration/validation evidence. PTNK-specific artifacts retain `ptnk-*` naming where that naming reflects actual provenance/domain scope.

Do not generalize PTNK-specific evidence into project-wide rules without supporting evidence.

## 9. Evidence and Change Rules

- Evidence > intuition.
- Accuracy > completeness.
- Preserve provenance and uncertainty.
- Do not fabricate definitions, pronunciation, examples, patterns, CEFR, relationships, or source evidence.
- Structural/provenance validation should fail closed on errors.
- Static knowledge and learner state must remain separate.
- Static knowledge changes must not silently rewrite historical learner attempts.
- Learner-state changes must not alter source evidence or canonical knowledge meaning.
- When current repository state conflicts with old conversation context, verify and prefer the repository.

## 10. Authoritative Documentation Map

Use the detailed documents below instead of expanding this file with their contents:

- `docs/methodology.md` — project methodology and core rules.
- `docs/data-architecture.md` — canonical knowledge/learner data boundaries and structures.
- `docs/learning-state-specification.md` — learning-state model.
- `docs/knowledge-atom-pipeline.md` — knowledge-atom extraction/promotion pipeline.
- `docs/learning-material-principles/` — learning-material principles.
- `data/knowledge/` — current knowledge data.
- `data/learner/` — current learner data.
- `sources/` — source/evidence material.
- Git history — historical decisions and changes when needed.

## 11. Recovery Boundary

This file answers:

> **What does an AI need to understand about Adaptive Learning and the meaning of its learning/learner data before working on a task?**

It does not answer:

> **What are we doing in the current conversation?**

That belongs to `context-recover.md`.
