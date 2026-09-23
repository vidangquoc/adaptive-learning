# Challenge Extraction Principles

Challenge Extraction produces Challenge Candidates from assessment tasks found in source learning material.

This document defines the principles that govern Atom-level Challenge Extraction. It is derived from the design decisions established during the development of the extraction process.

## Scope

The current process extracts **Atom-level Challenges**.

An Atom-level Challenge is a short assessment task focused on assessing one Knowledge Atom.

Long integrated or composite exercises, including long Cloze exercises that assess multiple pieces of knowledge together, are outside the current scope. A separate extraction process may support integrated or composite Challenges in the future.

## Assessment Item as Strong Evidence

The strongest source evidence that an assessment occurrence is a Challenge is that it is an **item within an exercise**.

When a source exercise is composed of multiple smaller items, each item should be treated as a Challenge candidate by default.

This rule takes precedence over superficial formatting such as blanks, answer spaces, or other presentational units. An item may contain multiple blanks, actions, or response elements and still constitute one Challenge.

An item should not be treated as a Challenge only when contextual analysis determines that it does not represent an independent, evaluable learner task or is otherwise outside the current extraction scope.

When an exercise item is not emitted as a Challenge, the extraction process must report the reason.

This makes omission explicit rather than silently losing source assessment evidence.

## Shared Contextual Analysis

Challenge Extraction and Knowledge Atom Extraction are not independent processes.

Both are derived from the same contextual analysis of a Source Segment. The analysis must identify the knowledge represented in the segment and the assessment tasks that provide evidence about that knowledge.

When a Challenge Candidate is created, the extraction process must also identify the **Knowledge Atom being assessed**.

The target Atom may be:

- an existing Knowledge Atom Candidate identified earlier;
- an existing Official Knowledge Atom; or
- a Knowledge Atom identified or created during the same contextual analysis.

A Challenge must not be emitted with an unresolved target Atom when the source provides enough evidence to identify the knowledge being assessed.

A Challenge may also provide evidence for discovering a Knowledge Atom. Assessment task wording, expected answers, or other assessment evidence may reveal a knowledge point that is not sufficiently explicit elsewhere in the source.

If a Challenge assesses a relationship between independent Knowledge Atoms, that relationship must itself be represented as a relation Knowledge Atom, and the Challenge targets that relation Atom.

Structural relationships among components inside one grammatical construction are not relation Atoms; they remain part of the relevant grammar rule or other Atom representation.

## Extraction Unit

A Challenge Candidate represents one **independent assessment task** that a learner performs to produce a response or outcome that can be evaluated.

The extraction unit is not defined by source formatting such as:

- a numbered item;
- a blank;
- an option;
- or another presentational unit.

In a multi-item exercise, the exercise item is the primary candidate boundary. Within an item, multiple actions or blanks do not automatically create multiple Candidates; the item remains one Challenge when those elements form one independent task.

If an exercise item cannot be treated as a Challenge, it must be explicitly reported with the reason.

## Assessment Task

Extract only a concrete assessment task that:

- is expected to be performed by the learner; and
- produces a response or outcome that can be evaluated against a specific expected answer.

Speaking and open-ended free-response tasks are outside the current Challenge model.

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

A supported Challenge has a specific expected answer.

When the source provides answer information, extract that answer together with the Challenge Candidate.

The answer is conceptually distinct from the learner-facing task content, but it is intrinsic to the supported Challenge model.

The answer may be structured according to the Challenge form rather than represented as a single string.

A Candidate may still be reported as incomplete or unresolved when the source does not provide enough information to establish its specific expected answer. The extractor must not invent an answer.

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

A Candidate must contain enough information to reconstruct and understand the original assessment task, identify the Knowledge Atom being assessed, and support later review and conversion into a Challenge.

At minimum, extraction should preserve:

- the task or prompt;
- information required to perform the task;
- applicable instructions or context;
- the target Knowledge Atom;
- the specific expected answer when it is available from the source;
- source provenance;
- the Challenge form when identifiable.

The exact Candidate schema is defined separately.

## Extraction Evidence

Extraction evidence must preserve enough information for later review to determine:

- what was extracted;
- where it came from;
- what source material or context was used;
- what Knowledge Atom was identified as the assessment target;
- what expected answer was identified, when available;
- and, where relevant, what limitations or uncertainties existed.

Evidence is source-specific and is not part of intrinsic Challenge semantics.

## Validation

Every extracted Candidate should be validated for faithful representation of a concrete assessment occurrence in the source and for correct identification of the Knowledge Atom being assessed.

Validation should check:

- assessment occurrence;
- assessment boundary;
- completeness;
- target Knowledge Atom;
- absence of invented source content;
- preservation of assessment structure;
- specific expected answer when available or required by the extraction result;
- provenance;
- compliance with extraction scope;
- and, when an exercise item is not emitted, the explicit reason for omission.

Validation may include structural checks, source-faithfulness checks, and consistency checks between the Challenge and its target Atom.

Validation does not replace the separate Candidate review and approval process.
