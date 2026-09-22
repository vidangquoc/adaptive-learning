# Adaptive Learning

Evidence-based adaptive learning system for building knowledge, diagnosing learner state, selecting the next-best learning activity, and validating transfer.

## Project origin

**PTNK** was the predecessor project from which this repository was split. PTNK work remains an important domain-specific evidence source and validation target, but **Adaptive Learning is the broader project and the canonical repository identity**.

The system is not merely a vocabulary collection or a PTNK paper-analysis project. Vocabulary, grammar, challenges, assessments, learner state, and review logic are components of a larger adaptive learning system.

## Core architecture

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

## Current backbone

- **Destination C1 & C2** — initial knowledge and competency backbone.
- **Challenge-first learning** — challenge before routine instruction when prior knowledge is plausible.
- **PTNK** — an important calibration/validation domain, not the identity of the whole system.
- Additional books/sources — targeted expansion layers, not mandatory parallel curricula.

## Repository structure

- `data/` — curated knowledge and evidence datasets
- `data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atoms.md` — Official Knowledge Atom store
- `data/knowledge/<source-id>/<segment-id>/<domain>/knowledge_atom_candidates.md` — Candidate Knowledge Atom store
- `sources/` — source material and provenance
- `analysis/` — evidence and research analysis
- `flashcards/` — learner-facing exports and experiments
- `schemas/` — machine-readable data contracts
- `scripts/` — extraction, validation, and transformation tooling
- `docs/` — methodology, architecture, rules, and recovery documentation

## Data principles

- Evidence over intuition.
- Accuracy over completeness.
- Preserve provenance and uncertainty.
- Never fabricate definitions, pronunciation, examples, relationships, CEFR, or source evidence.
- Static knowledge and learner state are separate layers.
- Knowledge atoms are flat and independently diagnosable.
- Human review remains the promotion gate where required.

PTNK-specific files and paths retain their `ptnk-*` naming because they represent PTNK evidence, not because PTNK is the repository's project identity.
