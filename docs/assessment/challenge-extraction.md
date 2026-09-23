# Questions About Challenge Extraction

This document collects unresolved design questions about Challenge Extraction.

## Current assumptions

- Source-derived Challenges are extracted from assessment tasks already present in the source.
- The main source of Challenges is exercises and their individual items.
- Challenge Extraction is separate from Knowledge Atom Extraction.
- Knowledge Atoms are not required as input to Challenge Extraction.
- Challenge Extraction produces Challenge Candidates rather than approved Challenges.
- A later process may link a Challenge Candidate to a Knowledge Atom.
- Source provenance should be preserved for extracted Challenges.
- An Atom-level Challenge is a short assessment task focused on assessing one Knowledge Atom.
- Long integrated or composite exercises, such as long Cloze passages used to assess multiple pieces of knowledge together, are not used to extract Atom-level Challenges.

## Questions

### Q1. What exactly is the extraction unit?

Should one Challenge Candidate correspond to:
- one numbered exercise item;
- one learner action;
- one answerable blank;
- one complete subtask;
- or some other unit?

How should the boundary be determined when an exercise item contains multiple actions or blanks?

**Decision**

A Challenge Candidate represents one **independent assessment task** that a learner performs to produce a response that can be evaluated.

The extraction unit is therefore not defined by a particular source formatting unit such as a numbered item or a blank.

A numbered exercise item will normally produce one Challenge Candidate when it represents one independent assessment task. If an item contains multiple actions or blanks, the extraction boundary is determined by whether those parts together constitute one assessment task or represent separate independent tasks.

### Q2. Which parts of a source exercise belong to a Challenge?

How should we distinguish:
- exercise-level instructions;
- item-level instructions;
- prompt/context;
- answer options;
- examples;
- hints;
- answer keys;
- explanations;
- surrounding text?

Which of these should be preserved in the Challenge Candidate?

**Decision**

An Atom-level Challenge should be a **short assessment task focused on assessing one Knowledge Atom**.

The extracted Challenge should preserve the parts of the source task that are necessary for the learner to understand and perform that short task, such as:
- the relevant instruction;
- the prompt;
- necessary context;
- answer options or other response elements.

The extraction should not include unrelated surrounding material merely because it belongs to the same exercise.

Answer information may be preserved as assessment data, but it is distinct from the learner-facing task.

Long integrated exercises, especially long Cloze passages used to assess multiple pieces of knowledge together, should **not** be split into Atom-level Challenges. Such an exercise may instead be retained separately as an integrated or composite Challenge when the system needs that kind of assessment.

### Q3. How should different exercise forms be recognized?

How should extraction identify forms such as:
- multiple choice;
- fill in the blank;
- matching;
- sentence completion;
- transformation;
- error correction;
- reordering;
- word formation;
- translation;
- cloze;
- other exercise forms?

Should Challenge Extraction use a fixed set of Challenge forms, or should forms be discovered from the source?

**Decision**

Challenge Extraction should classify extracted tasks using a **defined set of Challenge forms**.

The extractor should attempt to classify a source task into an existing form rather than creating a new form for every variation encountered in source material.

The form taxonomy itself may evolve as new kinds of assessment tasks are encountered. A source task that cannot yet be classified is handled by Q14 rather than being silently forced into an unsuitable form.

### Q4. How should compound exercises be handled?

What should happen when one exercise item contains several interdependent tasks?

For example, should a task with several blanks become:
- one Challenge Candidate;
- several Challenge Candidates;
- or a compound Challenge Candidate?

**Decision**

Challenge Extraction should focus on **short Atom-level Challenges**.

A source exercise item should be extracted as an Atom-level Challenge only when it represents a short task focused on assessing one Knowledge Atom.

A task containing multiple blanks or multiple interdependent parts should not be split into separate Atom-level Challenges merely because there are multiple answer spaces.

In particular, long Cloze passages or similar integrated exercises that assess multiple pieces of knowledge together should not be decomposed into Atom-level Challenges.

Such an exercise may be retained as an integrated or composite Challenge for holistic assessment, but it is outside the purpose of Atom-level Challenge extraction.

### Q5. How much should extraction normalize the source?

Should the extracted Challenge Candidate preserve the source wording and structure exactly, or should extraction normalize things such as numbering, whitespace, option labels, or formatting?

Where should the boundary be between extraction and later normalization?

**Decision**

Challenge Extraction should preserve the **source wording and assessment structure** rather than rewrite or reinterpret the task.

Normalization may remove purely presentational or technical noise that does not affect meaning or task structure, such as irrelevant whitespace or extraction artifacts.

Extraction should not silently:
- rewrite the wording;
- correct the source;
- change the intended task;
- invent missing information;
- or otherwise alter the assessment content.

Any more substantial normalization should be treated as a separate concern.

### Q6. What information is required for a Challenge Candidate?

What is the minimum information that must be extracted so that the original assessment task can be understood and later turned into a Challenge?

**Decision**

A Challenge Candidate must contain enough information to **reconstruct and understand the original assessment task** and to support later review and conversion into a Challenge.

At minimum, this includes:
- the task/prompt;
- information required to perform the task, such as options or other task elements;
- applicable instructions or context;
- answer information when available from the source;
- source provenance;
- the original Challenge form when it can be identified.

The exact schema is not defined by this decision.

### Q7. How should answers be extracted?

When an answer key exists in the source:
- should the answer be extracted together with the Challenge Candidate;
- should answer extraction be a separate process;
- how should multiple acceptable answers be represented;
- what should happen when the source does not provide an answer?

**Decision**

When the source provides answer information, that information should be **extracted together with the Challenge Candidate**.

Answer information is important for preserving the assessment task and for later evaluation, but it should remain conceptually distinct from the learner-facing task content.

If the source does not provide an answer, the Candidate may still be extracted; absence of an answer is not by itself a reason to discard the source task.

Questions about the detailed answer/evaluation model are outside this decision.

### Q8. How should exercise context be preserved?

When an individual item depends on instructions, examples, a word bank, a passage, an image, or other shared context, how should that dependency be represented?

**Decision**

For the current extraction scope, Challenges that depend on **substantial shared context** should be skipped rather than extracted.

Examples include exercises whose individual items depend on:
- a long shared passage;
- a substantial shared word bank;
- a shared image or other material that is essential to interpreting the task;
- extensive instructions or context that cannot be reduced to a short Atom-level Challenge without changing the assessment task.

This is a deliberate scope limitation, not a claim that such exercises are invalid assessments.

During extraction, skipped exercises of this kind must be **reported** so that the system records that an extractable-looking assessment task was encountered but intentionally not extracted.

The same reporting principle applies to **Cloze exercises** that are excluded from Atom-level Challenge extraction.

The detailed format and schema of the extraction report are handled separately.

### Q9. What counts as an extractable Challenge?

How should we distinguish a genuine assessment task from:
- an example;
- a demonstration;
- a practice instruction without an answerable task;
- explanatory text;
- a heading;
- an answer key;
- teacher notes?

**Decision**

A source element is extractable as a Challenge Candidate when it represents a **concrete assessment task that a learner is expected to perform and that produces a response or outcome that can be evaluated**.

Examples, demonstrations, explanations, headings, answer keys, and teacher notes are not Challenges merely because they are associated with an exercise.

An element that provides instructions for an actual assessment task is part of that task rather than a separate Challenge.

### Q10. How should provenance identify the extracted task?

What source location is necessary to identify exactly where a Challenge Candidate came from?

Is source + segment sufficient, or do we need exercise/item identifiers, page/paragraph coordinates, or other location information?

**Decision**

The provenance requirement is that an extracted Challenge Candidate **must be traceable to the exact assessment occurrence in the source**.

The Candidate must preserve enough provenance to identify the specific occurrence of the assessment task from which it was extracted.

The detailed structure of the source provenance and location data is **not decided here**. It will be designed later as part of the Challenge schema.

### Q11. How should duplicated or repeated tasks be handled?

If the same assessment task appears multiple times in the source, should extraction create:
- separate Candidates for each occurrence;
- one Candidate with multiple provenance records;
- or another representation?

**Decision**

Each **occurrence of an assessment task in the source is extracted as a separate Challenge Candidate**.

Two occurrences may have identical or nearly identical content and may later be candidates for reuse or deduplication, but extraction should preserve the distinction between source occurrences.

Deduplication or Challenge reuse is a separate concern.

### Q12. How should extraction handle incomplete or ambiguous source material?

What should happen when:
- an item is partially missing;
- OCR/text extraction is damaged;
- an answer option is missing;
- an image contains essential task information;
- the task depends on material that was not extracted?

**Decision**

Challenge Extraction must not silently invent or infer missing source content in order to complete a Candidate.

If the task can still be faithfully reconstructed from the available source evidence, it may be extracted.

If essential information is missing or ambiguous such that the original assessment task cannot be reliably reconstructed, the task should not be emitted as a normal valid Challenge Candidate.

The extraction evidence should preserve the problem for later review where appropriate.

### Q13. When should extraction reject a task?

What minimum conditions must be satisfied before an assessment task is emitted as a Challenge Candidate?

**Decision**

A task should be emitted as a Challenge Candidate only when the source provides enough information to identify it as a concrete assessment task and to understand what the learner is expected to do.

Extraction should reject or withhold a task when essential information is missing, the task cannot be reliably reconstructed, or the extracted material is too ambiguous to establish the original assessment task.

The extractor must prefer omission or explicit uncertainty over silently inventing source information.

### Q14. What should Challenge Extraction produce when a source contains a new exercise type?

Should the extractor:
- preserve the task as an unclassified Candidate;
- assign a generic form;
- infer a new form;
- or reject it until the form is defined?

**Decision**

A new or not-yet-supported exercise type should **not be discarded merely because its Challenge form is not yet in the defined set**.

The assessment task should be preserved as a Challenge Candidate with an unclassified or otherwise explicitly unresolved form, so that it can be reviewed and the Challenge-form taxonomy can evolve.

The extractor must not force the task into an unsuitable existing form.

### Q15. How should extraction interact with source Segments?

What should happen when an exercise spans multiple Segments, or when a Segment contains only part of an exercise?

Should Challenge Extraction operate on individual Segments or on larger source structures when necessary?

**Decision**

Challenge Extraction operates within individual Source Segments.

A Challenge Candidate must belong entirely to **one Segment**. A Challenge must not span multiple Segments.

If an assessment task appears to span two or more Segments and therefore cannot be extracted as a complete Challenge from a single Segment:
- it should not be extracted as a Challenge Candidate;
- the occurrence should be reported as skipped/incomplete.

A Segment may contain zero, one, or multiple Challenge Candidates. Segment boundaries therefore do not determine the number of Challenges, but they do determine whether an individual Challenge can be extracted.

### Q16. What should remain source-specific?

Which information should remain as source provenance or extraction evidence rather than becoming intrinsic Challenge data?

**Decision**

Information that describes **where and how the Challenge Candidate was extracted from the source** should remain source-specific rather than becoming intrinsic assessment semantics.

This includes information such as:
- source identity;
- source location;
- original exercise/item identifiers;
- extraction-specific evidence;
- source formatting or representation details that are not part of the assessment task itself.

Challenge semantics should represent the assessment task, while provenance and extraction evidence explain its origin.

### Q17. How should extraction quality be validated?

What checks can determine that the extracted Challenge Candidate faithfully represents the assessment task in the source?

### Q18. What should be preserved as extraction evidence?

When a Candidate is reviewed later, what evidence should be retained so that a reviewer can determine why and how the Candidate was extracted from the source?

**Decision**

Extraction evidence should preserve enough information for a reviewer to **trace the Candidate back to the source and understand what source material was used to create it**.

The evidence should support review of:
- what was extracted;
- where it came from;
- what source context was used;
- and, where relevant, what limitations or uncertainties existed during extraction.

The exact evidence schema is not defined by this decision.
