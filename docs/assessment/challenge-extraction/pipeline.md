# Challenge Extraction Pipeline

The Challenge Extraction Pipeline describes the processing flow for extracting Atom-level Challenge Candidates from Source Segments.

The pipeline applies the principles defined in [Challenge Extraction Principles](principles.md).

## Scope

The pipeline operates on individual Source Segments and produces Challenge Candidates or explicit skipped/incomplete extraction reports.

It does not approve Candidates, link Candidates to Knowledge Atoms, deduplicate Challenges, or handle integrated/composite Challenges.

## Pipeline

```
Source Segment
      ↓
Identify assessment occurrences
      ↓
Determine extraction scope
      ↓
Determine Challenge boundary
      ↓
Extract task content
      ↓
Classify Challenge form
      ↓
Extract answer information
      ↓
Attach provenance and evidence
      ↓
Validate Candidate
      ↓
Challenge Candidate
```

An occurrence that cannot be extracted within the current scope follows the reporting path:

```
Assessment occurrence
      ↓
Out of scope / incomplete / ambiguous
      ↓
Skipped extraction report
```

## 1. Identify Assessment Occurrences

Inspect the Source Segment and identify concrete assessment tasks that a learner is expected to perform and that produce a response or outcome that can be evaluated.

Do not treat examples, demonstrations, explanations, headings, answer keys, or teacher notes as assessment occurrences.

Instructions that belong to an actual task are part of that occurrence.

## 2. Determine Extraction Scope

Determine whether the occurrence is within the current Atom-level Challenge Extraction scope.

Extract only short tasks focused on one Knowledge Atom.

Skip and report occurrences that depend on substantial shared context or are long integrated/composite exercises, including long Cloze exercises that assess multiple pieces of knowledge together.

Also skip and report an occurrence when it cannot be completely extracted from one Source Segment.

## 3. Determine Challenge Boundary

Determine the smallest complete assessment task represented by the source occurrence.

Do not define the boundary merely by numbered items, blanks, or other formatting units.

If multiple actions or blanks form one independent task, keep them together.

Do not split a task merely because it contains multiple response spaces.

## 4. Extract Task Content

Preserve the source wording and assessment structure.

Extract the information needed for the learner to understand and perform the task, such as:

- relevant instructions;
- prompt;
- necessary context;
- options;
- required response elements.

Exclude unrelated surrounding material.

Remove only technical or presentational noise that does not affect meaning or task structure.

Do not rewrite, correct, reinterpret, or invent source content.

## 5. Classify Challenge Form

Attempt to classify the extracted task using the defined Challenge-form taxonomy.

If the task matches an existing form, record that form.

If it does not match a supported form, preserve the Candidate with an unclassified or explicitly unresolved form rather than forcing an unsuitable classification.

## 6. Extract Answer Information

When answer information is present in the source, extract it together with the Candidate.

Keep answer information distinct from learner-facing task content.

If no answer information is available, the Candidate may still be emitted when the task is otherwise sufficiently reconstructable.

Detailed answer and evaluation modeling is outside this pipeline.

## 7. Attach Provenance and Evidence

Attach enough provenance to trace the Candidate to the exact assessment occurrence in the source.

Preserve extraction evidence sufficient to determine:

- what source material was used;
- where the occurrence came from;
- what context was used;
- and any relevant limitations or uncertainties.

A Candidate must belong entirely to one Source Segment.

## 8. Validate the Candidate

Validate that the Candidate faithfully represents the concrete assessment occurrence.

At minimum, check:

- occurrence identity;
- assessment boundary;
- completeness;
- source-faithfulness;
- absence of invented content;
- preservation of assessment structure;
- answer information when available;
- provenance;
- scope compliance.

A Candidate that fails these checks should not be emitted as a normal valid Candidate. The extraction problem should instead be represented in the appropriate skipped/incomplete evidence.

## 9. Emit Candidate or Skip Report

If the Candidate passes extraction and validation requirements, emit the Challenge Candidate.

If the occurrence is intentionally excluded or cannot be reliably reconstructed, do not emit a normal Candidate. Emit a skipped/incomplete extraction report with sufficient evidence to explain the reason.

## Post-Extraction Concerns

The following are separate processes and are not part of this pipeline:

- linking a Candidate to a Knowledge Atom;
- Candidate review and approval;
- converting a Candidate into an approved Challenge;
- Challenge deduplication;
- Challenge reuse;
- integrated/composite Challenge extraction;
- detailed answer/evaluation modeling;
- adaptive Challenge selection.
