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

## Questions

### Q1. What exactly is the extraction unit?

Should one Challenge Candidate correspond to:
- one numbered exercise item;
- one learner action;
- one answerable blank;
- one complete subtask;
- or some other unit?

How should the boundary be determined when an exercise item contains multiple actions or blanks?

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

### Q4. How should compound exercises be handled?

What should happen when one exercise item contains several interdependent tasks?

For example, should a task with several blanks become:
- one Challenge Candidate;
- several Challenge Candidates;
- or a compound Challenge Candidate?

### Q5. How much should extraction normalize the source?

Should the extracted Challenge Candidate preserve the source wording and structure exactly, or should extraction normalize things such as numbering, whitespace, option labels, or formatting?

Where should the boundary be between extraction and later normalization?

### Q6. What information is required for a Challenge Candidate?

What is the minimum information that must be extracted so that the original assessment task can be understood and later turned into a Challenge?

### Q7. How should answers be extracted?

When an answer key exists in the source:
- should the answer be extracted together with the Challenge Candidate;
- should answer extraction be a separate process;
- how should multiple acceptable answers be represented;
- what should happen when the source does not provide an answer?

### Q8. How should exercise context be preserved?

When an individual item depends on instructions, examples, a word bank, a passage, an image, or other shared context, how should that dependency be represented?

### Q9. What counts as an extractable Challenge?

How should we distinguish a genuine assessment task from:
- an example;
- a demonstration;
- a practice instruction without an answerable task;
- explanatory text;
- a heading;
- an answer key;
- teacher notes?

### Q10. How should provenance identify the extracted task?

What source location is necessary to identify exactly where a Challenge Candidate came from?

Is source + segment sufficient, or do we need exercise/item identifiers, page/paragraph coordinates, or other location information?

### Q11. How should duplicated or repeated tasks be handled?

If the same assessment task appears multiple times in the source, should extraction create:
- separate Candidates for each occurrence;
- one Candidate with multiple provenance records;
- or another representation?

### Q12. How should extraction handle incomplete or ambiguous source material?

What should happen when:
- an item is partially missing;
- OCR/text extraction is damaged;
- an answer option is missing;
- an image contains essential task information;
- the task depends on material that was not extracted?

### Q13. When should extraction reject a task?

What minimum conditions must be satisfied before an assessment task is emitted as a Challenge Candidate?

### Q14. What should Challenge Extraction produce when a source contains a new exercise type?

Should the extractor:
- preserve the task as an unclassified Candidate;
- assign a generic form;
- infer a new form;
- or reject it until the form is defined?

### Q15. How should extraction interact with source Segments?

What should happen when an exercise spans multiple Segments, or when a Segment contains only part of an exercise?

Should Challenge Extraction operate on individual Segments or on larger source structures when necessary?

### Q16. What should remain source-specific?

Which information should remain as source provenance or extraction evidence rather than becoming intrinsic Challenge data?

### Q17. How should extraction quality be validated?

What checks can determine that the extracted Challenge Candidate faithfully represents the assessment task in the source?

### Q18. What should be preserved as extraction evidence?

When a Candidate is reviewed later, what evidence should be retained so that a reviewer can determine why and how the Candidate was extracted from the source?
