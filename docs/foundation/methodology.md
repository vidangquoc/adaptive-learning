# Methodology

## 1. Purpose

**Adaptive Learning** is an evidence-based adaptive learning system. It represents trustworthy knowledge, diagnoses what a learner needs, and selects useful next activities under finite learning time.

The project is a learning system rather than a vocabulary list, textbook summary, or mechanically sequenced curriculum.

## 2. Core Method

The system follows this general loop:

```text
Goal / target
     ↓
Knowledge + competency model
     ↓
Diagnostic / challenge
     ↓
Learner evidence
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

The system should test plausible prior knowledge before routine instruction, trace failures to the smallest useful gap, teach that gap, and verify it in a different context.

## 3. Evidence Principle

Learning-material decisions are evidence-based. Source evidence, reliable external evidence, learner evidence, and AI-generated practice have different roles.

AI-generated practice may support challenge generation and assessment, but its existence does not prove that a knowledge item belongs in the learning scope.

Accuracy and validity take precedence over extraction volume, row counts, or apparent completeness.

## 4. Separation of Concerns

The project keeps these concerns distinct:

```text
source evidence
      ↓
curated / normalized knowledge
      ↓
assessment and learning design
      ↓
learner evidence
      ↓
learner state
      ↓
adaptive decisions
```

The detailed rules for each concern belong to the specialized documents under `docs/` rather than being duplicated here.

## 5. Knowledge Representation

Knowledge is represented as independently useful, source-grounded knowledge atoms. The atom ontology, taxonomy, common structure, and discovery/promotion pipeline are defined in the `docs/knowledge/` documents.

Static knowledge must remain independent of learner-specific mastery.

## 6. Learning State

Learner state is an interpretation of the learner's current review evidence. It belongs to the learner layer and is used to determine review needs and next activities. The current project does not define a persisted or formal mastery model; any future mastery model must be specified separately from the current five-field review-state representation.

The detailed state model belongs to `docs/learner/learning-state.md`.

## 7. Learning-Material Workflow

Learning-material acquisition follows this high-level flow:

```text
Source
  ↓
Evidence capture
  ↓
Knowledge / assessment construction
  ↓
Validation and review
  ↓
Official learning material
  ↓
Adaptive learning
```

Source-specific extraction rules, provenance requirements, and source boundaries are defined under `docs/source/`.

## 8. Versioning

Authoritative rules must be versioned through repository history. When a rule changes, update the document that owns that rule and remove obsolete recovery instructions so future sessions do not revive superseded decisions.
