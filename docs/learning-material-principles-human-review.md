# Human Review and Promotion Principles

> This document is an extension of `docs/learning-material-principles.md` for the human-review gate used when constructing the official learning-material knowledge base.

## 1. Automated analysis is advisory, not authoritative

Automated analysis may discover candidates, collect evidence, infer attributes, identify curricular signals, detect back-matter support, calculate confidence, flag warnings, and produce recommendations.

None of these automated outputs may, by themselves, promote a candidate to an official knowledge atom.

> **Machine proposes. Human decides.**

## 2. Candidate and official atom are different states

A candidate is an evidence-backed hypothesis about a possible knowledge atom. An official atom is a candidate that has passed the human promotion gate.

```text
SOURCE EVIDENCE
      ↓
CANDIDATE
      ↓
AUTOMATED EVIDENCE ANALYSIS
      ↓
HUMAN REVIEW
      ↓
┌───────────────┬───────────────┬───────────────┐
│ APPROVE       │ REJECT        │ HOLD          │
↓               ↓               ↓
OFFICIAL ATOM   NOT PROMOTED    REVIEW LATER
```

## 3. Human review is the final promotion gate

Only an explicit human approval may promote a candidate into the official learning-material knowledge base.

Automated validation may establish that a candidate is structurally valid, well-supported, or highly plausible. It must not be treated as equivalent to human approval.

A candidate may be rejected even when automated confidence is high, and a candidate may be held when the evidence is insufficient for a reliable decision.

## 4. Curricular evidence is input to human review

The pipeline should provide evidence that helps the reviewer judge whether an atom belongs in the official learning material.

Relevant signals include:

- explicit instructional evidence in the source;
- linguistic and semantic evidence;
- source context supporting the intended sense or usage;
- presence in author-curated back matter;
- CEFR evidence when independently verified;
- source classification such as word list, phrasal-verb database, collocation database, or idiom database;
- exercise evidence and the knowledge tested by the exercise;
- warnings, ambiguity, or competing interpretations.

These are **inputs to judgment**, not automatic promotion rules.

## 5. Back matter is strong author-curated evidence

Back matter may provide particularly strong evidence that the book's authors consider an item part of the intended level and learning scope.

Relevant back matter may include:

- Word Lists;
- Topic Vocabulary databases;
- Phrasal Verbs databases;
- Phrases, Patterns and Collocations databases;
- Idioms databases;
- other explicitly author-curated lexical inventories.

Presence in back matter should therefore be surfaced prominently during human review.

However, back-matter presence does not by itself determine atomization. The reviewer and reasoning layer must still determine whether the occurrence represents one atom, multiple atoms, or a relationship among distinct atoms.

Likewise, absence from back matter does **not** automatically invalidate a candidate that is explicitly taught elsewhere in the source.

## 6. No learner-state criteria at material-construction time

The official learning-material corpus is constructed independently of an individual learner's current mastery, diagnostic results, review history, or scheduling state.

Learner state is a downstream concern. It must not be used as a criterion for deciding whether a candidate belongs to the source-grounded knowledge base.

## 7. Human decisions must be recorded

Each reviewed candidate should retain at least:

- review status: `approved`, `rejected`, or `hold`;
- reviewer identity or reviewer role;
- decision timestamp;
- decision rationale;
- relevant evidence references;
- any unresolved issue or follow-up note.

The review decision must be traceable back to the candidate and its source evidence.

## 8. Rejection does not destroy evidence

Rejecting a candidate must not delete its source evidence.

The candidate, evidence, automated analysis, and human decision should remain traceable so that the decision can be reconsidered if the ontology, source interpretation, or project scope changes.

## 9. Promotion rule

> **A candidate becomes an official knowledge atom only after explicit human approval. Automated evidence analysis supports the decision but never substitutes for it.**

This rule is the final gate between the evidence/discovery layer and the official learning-material knowledge base.
