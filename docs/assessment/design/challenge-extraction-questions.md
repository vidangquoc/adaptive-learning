# Challenge Extraction Design Decisions

This document records the design decisions established for the Challenge Extraction Pipeline.

## Q1. What assessment evidence should be discovered from a Source Segment?

Evidence discovery should identify concrete assessment occurrences together with the source material needed for later contextual analysis.

The strongest evidence that an assessment occurrence is a Challenge is that it is an **item within an exercise**. When an exercise contains multiple smaller items, each item should be treated as a Challenge candidate by default.

Evidence discovery should preserve identifiable exercise and item boundaries, together with their location and relevant source material.

## Q2. How should an assessment occurrence be analyzed in context?

Assessment occurrences must be analyzed together with the surrounding source context needed to understand the task faithfully.

Challenge analysis and Knowledge Atom analysis are performed during the same contextual analysis. The analysis determines both what knowledge is being represented and what assessment task tests that knowledge.

An exercise item is presumed to be a Challenge unless contextual analysis determines that it is not an independent, evaluable learner task or is otherwise outside the current extraction scope.

Contextual analysis may therefore identify a Knowledge Atom from explanatory material, assessment material, or both.

## Q3. How should an assessment occurrence become a Challenge Candidate?

A Challenge Candidate is normally created from one exercise item.

The exercise item is the primary Challenge boundary. Multiple blanks, actions, or response spaces within one item do not automatically create multiple Challenges.

The Challenge Candidate must identify the Knowledge Atom being assessed. The target may be an existing Knowledge Atom Candidate, an existing Official Knowledge Atom, or a Knowledge Atom identified during the same contextual analysis.

If an exercise item is not a Challenge, it must not be silently discarded. The extraction process must report the item and the reason it was not emitted.

If the assessment tests a relationship between independent Knowledge Atoms, that relationship is represented as a relation Knowledge Atom and becomes the Challenge target.

## Q4. What information must a Challenge Candidate preserve from the source?

A Candidate must preserve enough information to reconstruct and understand the original assessment task and support review and later conversion into a Challenge.

This includes, where applicable:

- task/prompt;
- required instructions and context;
- answer options or other response elements;
- answer information when available;
- target Knowledge Atom;
- Challenge form when identifiable;
- exact source provenance, including exercise/item occurrence;
- extraction evidence and relevant limitations or uncertainties.

The learner-facing task and answer information remain conceptually distinct.

## Q5. How should a Challenge Candidate be validated?

Validation checks whether the Candidate faithfully represents a concrete assessment occurrence and correctly identifies the knowledge being assessed.

At minimum, validation checks:

- exercise/item occurrence;
- assessment boundary;
- completeness;
- target Knowledge Atom;
- absence of invented source content;
- preservation of assessment structure;
- answer information when available;
- provenance;
- extraction scope;
- consistency between the Challenge and target Atom.

Validation also checks that every identifiable exercise item has either been emitted as a Challenge Candidate or has an explicit skipped extraction report with a reason.

Validation is separate from Candidate review and approval.

## Q6. What should happen when a Challenge Candidate cannot be safely extracted?

Do not invent missing source content or force an unreliable interpretation.

Skip and report an exercise item when it is:

- not an independent, evaluable learner task;
- outside current Atom-level extraction scope;
- dependent on substantial shared context;
- cross-segment and cannot be completely reconstructed from one Segment;
- missing essential information;
- too ambiguous to reconstruct reliably.

The skipped/incomplete extraction report should identify the exercise item and preserve enough evidence to explain why it was not emitted as a Challenge.

If a task can be faithfully reconstructed despite incomplete or noisy source representation, it may still be extracted.
