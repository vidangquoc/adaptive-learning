# Challenge Extraction Design Decisions

This document records the design decisions established for the Challenge Extraction Pipeline.

## Q1. What assessment evidence should be discovered from a Source Segment?

Evidence discovery should identify concrete assessment occurrences together with the source material needed for later contextual analysis.

An assessment occurrence is evidence of a task that a learner is expected to perform and that produces a response or outcome that can be evaluated.

Evidence discovery should preserve the location and relevant source material rather than prematurely creating a Challenge or Knowledge Atom.

## Q2. How should an assessment occurrence be analyzed in context?

Assessment occurrences must be analyzed together with the surrounding source context needed to understand the task faithfully.

Challenge analysis and Knowledge Atom analysis are performed during the same contextual analysis. The analysis determines both what knowledge is being represented and what assessment task tests that knowledge.

Contextual analysis may therefore identify a Knowledge Atom from explanatory material, assessment material, or both.

## Q3. How should an assessment occurrence become a Challenge Candidate?

A Challenge Candidate is created from one independent assessment task.

Its boundary is determined by task independence, not by numbering, blanks, options, or other source formatting.

The Challenge Candidate must also identify the Knowledge Atom being assessed. The target may be an existing Knowledge Atom Candidate, an existing Official Knowledge Atom, or a Knowledge Atom identified during the same contextual analysis.

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
- exact source provenance;
- extraction evidence and relevant limitations or uncertainties.

The learner-facing task and answer information remain conceptually distinct.

## Q5. How should a Challenge Candidate be validated?

Validation checks whether the Candidate faithfully represents a concrete assessment occurrence and correctly identifies the knowledge being assessed.

At minimum, validation checks:

- assessment occurrence;
- assessment boundary;
- completeness;
- target Knowledge Atom;
- absence of invented source content;
- preservation of assessment structure;
- answer information when available;
- provenance;
- extraction scope;
- consistency between the Challenge and target Atom.

Validation is separate from Candidate review and approval.

## Q6. What should happen when a Challenge Candidate cannot be safely extracted?

Do not invent missing source content or force an unreliable interpretation.

Skip and report an occurrence when it is:

- outside current Atom-level extraction scope;
- dependent on substantial shared context;
- cross-segment and cannot be completely reconstructed from one Segment;
- missing essential information;
- too ambiguous to reconstruct reliably.

A skipped/incomplete extraction report should preserve enough evidence to explain the occurrence and the reason it could not be emitted as a normal Candidate.

If a task can be faithfully reconstructed despite incomplete or noisy source representation, it may still be extracted.
