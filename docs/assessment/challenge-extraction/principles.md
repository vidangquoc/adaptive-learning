# Challenge Extraction Principles

Challenge Extraction produces Challenge Candidates from assessment tasks found in source learning material.

This document defines the principles that govern Atom-level Challenge Extraction. It is derived from the design decisions recorded during the development of the extraction process.

## Scope

The current process extracts **Atom-level Challenges**.

An Atom-level Challenge is a short assessment task focused on assessing one Knowledge Atom.

Long integrated or composite exercises, including long Cloze exercises that assess multiple pieces of knowledge together, are outside the current scope. A separate extraction process may support integrated or composite Challenges in the future.

## Extraction Unit

A Challenge Candidate represents one **independent assessment task** that a learner performs to produce a response or outcome that can be evaluated.

The extraction unit is not defined by source formatting such as:

- a numbered item;
- a blank;
- an option;
- or another presentational unit.

A numbered item normally produces one Candidate when it represents one independent task. Multiple actions or blanks do not automatically create multiple Candidates; the boundary is determined by task independence.

## Assessment Task

Extract only a concrete assessment task that:

- is expected to be performed by the learner; and
- produces a response or outcome that can be evaluated.

Examples, demonstrations, explanations, headings, answer keys, and teacher notes are not Challenges.

Instructions required to perform an actual assessment task are part of that task.

## Task Content

Preserve the source information necessary to understand and perform the short assessment task, including where applicable:

- relevant instructions;
- the prompt;
- necessary context;
- answer options;
- other required response elements.

Do not include unrelated surrounding material merely because it belongs to the same source exercise.

## Source Preservation

Preserve the source wording and assessment structure.

Extraction may remove purely presentational or technical noise that does not affect meaning or task structure, such as irrelevant whitespace or extraction artifacts.

Extraction must not silently:

- rewrite wording;
- correct the source;
- change the intended task;
- invent missing information;
- or otherwise alter assessment content.

More substantial normalization is a separate concern.

## Challenge Form

Extracted tasks should be classified using the defined set of Challenge forms.

The extractor should prefer an existing form rather than creating a new form for every source variation.

If a task cannot yet be classified, preserve it as a Candidate with an unclassified or explicitly unresolved form. Do not force it into an unsuitable form.

The Challenge-form taxonomy may evolve as new task types are encountered.

## Answer Information

When the source provides answer information, extract it together with the Challenge Candidate.

Answer information is conceptually distinct from the learner-facing task content.

A Candidate may still be extracted when the source provides no answer information.

The detailed answer and evaluation model is outside this specification.

## Shared Context

Challenges that depend on substantial shared context are outside the current Atom-level extraction scope and should be skipped.

Examples include tasks depending on:

- a long shared passage;
- a substantial shared word bank;
- an essential shared image or other material;
- extensive instructions or context that cannot be reduced to a short Atom-level Challenge without changing the assessment task.

Skipped occurrences must be reported.

The same reporting principle applies to excluded Cloze or other integrated exercises.

## Source Segments

Challenge Extraction operates within individual Source Segments.

A Challenge Candidate must belong entirely to one Segment and must not span multiple Segments.

If an assessment task cannot be completely extracted from one Segment, it should not be emitted as a normal Candidate and should be reported as skipped or incomplete.

A Segment may contain zero, one, or multiple Challenge Candidates.

## Provenance

Every extracted Candidate must be traceable to the **exact assessment occurrence in the source**.

The Candidate must preserve enough provenance to identify the specific occurrence from which it was extracted.

Provenance describes origin, not Challenge semantics. It may include source identity, source location, original exercise/item identifiers, and other source-specific information.

The detailed provenance schema is defined separately.

## Repeated Occurrences

Each occurrence of an assessment task in the source is extracted as a separate Challenge Candidate.

Identical or nearly identical occurrences may later be candidates for reuse or deduplication, but extraction preserves occurrence identity.

Deduplication and Challenge reuse are separate concerns.

## Incomplete or Ambiguous Source

Do not silently invent or infer missing source content.

If the task can still be faithfully reconstructed from available source evidence, it may be extracted.

If essential information is missing or ambiguous such that the original assessment task cannot be reliably reconstructed, do not emit a normal valid Candidate. Preserve the problem in extraction evidence when appropriate.

Extraction should prefer explicit uncertainty or omission over invention.

## Candidate Completeness

A Candidate must contain enough information to reconstruct and understand the original assessment task and to support later review and conversion into a Challenge.

At minimum, extraction should preserve:

- the task or prompt;
- information required to perform the task;
- applicable instructions or context;
- answer information when available;
- source provenance;
- the Challenge form when identifiable.

The exact Candidate schema is defined separately.

## Extraction Evidence

Extraction evidence must preserve enough information for later review to determine:

- what was extracted;
- where it came from;
- what source material or context was used;
- and, where relevant, what limitations or uncertainties existed.

Evidence is source-specific and is not part of intrinsic Challenge semantics.

## Validation

Every extracted Candidate should be validated for faithful representation of a concrete assessment occurrence in the source.

Validation should check:

- assessment occurrence;
- assessment boundary;
- completeness;
- absence of invented source content;
- preservation of assessment structure;
- answer information when available;
- provenance;
- compliance with extraction scope.

Validation may include structural checks and source-faithfulness checks.

Validation does not replace the separate Candidate review and approval process.
