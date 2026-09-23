# Challenge Forms

This document defines the current forms of Challenges used to assess Knowledge Atoms.

Its purpose is to establish the Challenge Form taxonomy before finalizing the canonical Challenge structure. Form-specific analysis will determine what information a Challenge must contain in its challenge content, options, and answer fields.

A Challenge Form describes how a learner performs a Challenge. It does not identify the Knowledge Atom being assessed.

## 1. Principles

### 1.1 Form is about the Challenge

A form answers:

> What kind of Challenge is presented to the learner?

It does not answer what knowledge is being tested. That is identified by target_atom_id.

The same Knowledge Atom may be assessed through different forms.

### 1.2 Form does not determine the target Atom

A form is independent of the knowledge domain.

For example:
- multiple choice may assess vocabulary or grammar;
- fill in the blank may assess vocabulary or grammar;
- word formation may assess morphological or lexical knowledge.

### 1.3 One Challenge may contain multiple response elements

A Challenge may involve multiple blanks, corrections, or other response elements while still constituting one Challenge.

The number of response elements does not by itself determine the number of Challenges.

## 2. Current Form Taxonomy

The current working set contains eight forms:

1. multiple_choice
2. fill_in_blank
3. sentence_completion
4. short_answer
5. error_correction
6. sentence_transformation
7. sentence_reordering
8. word_formation

The following forms have been explicitly excluded:

- true_false — represented as a special case of multiple_choice;
- matching — excluded from the current model;
- translation — excluded from the current model;
- cloze — excluded from the current model.

## 3. Multiple Choice

The Challenge presents a finite set of explicitly provided options, and the learner selects one option.

True/False is treated as a special case of Multiple Choice in which the available options are True and False. It is not a separate Challenge Form.

Example:

Choose the correct answer.

Darren ___ home at eight yesterday.

A. gets
B. got
C. has got

The canonical answer is the **content of the selected option**, not its presentation label.

Therefore:

- options = [gets, got, has got]
- answer = got

The labels A, B, C are presentation details and do not define the answer.

A True/False Challenge is therefore conceptually:

- options = [true, false]
- answer = true

The fundamental invariant is:

> The answer must identify an option by its semantic content, not by its display label or position.

Characteristics:
- finite explicit options;
- learner selects rather than constructs the answer;
- distractors are part of the Challenge;
- the answer is one of the option values.

## 4. Fill in the Blank

The Challenge presents an incomplete expression, sentence, or other bounded context containing one or more blanks. The learner supplies the missing material.

Example:

Darren ___ home at eight yesterday.

Expected answer: got.

A single Challenge may contain multiple blanks when they form one independent assessment task.

A blank is a response element, not necessarily a Challenge.

## 5. Sentence Completion

The Challenge presents a sentence or sentence frame that the learner must complete so that it satisfies the Challenge requirements.

Example:

If I had known about the problem, I __________.

Expected answer: would have helped.

This overlaps with Fill in the Blank. The distinction should remain pragmatic rather than being based only on typography. It may eventually be unnecessary if both forms use the same structural model.

## 6. Short Answer

The Challenge asks the learner to produce a short, bounded response without providing a finite list of options.

Example:

What is the past tense of "go"?

Expected answer: went.

The response is constructed, but the expected answer remains sufficiently specific for evaluation.

Open-ended essay, speaking, or free-form composition is outside the current Challenge model when a specific expected answer cannot be established.

## 7. Error Correction

The Challenge presents language containing an error and asks the learner to identify and/or correct it.

Example:

Correct the sentence:

Darren go home at eight yesterday.

Expected answer:

Darren went home at eight yesterday.

Some exercises ask the learner to identify the erroneous part, while others ask for the corrected sentence. These may require different answer structures or may later become distinct forms.

## 8. Sentence Transformation

The Challenge presents a sentence and an instruction requiring the learner to transform it while preserving the required meaning or satisfying a grammatical transformation.

Example:

Rewrite using "used to":

I lived in London when I was a child.

Expected answer:

I used to live in London when I was a child.

The original sentence and transformation instruction are part of the Challenge; the transformed sentence is the expected outcome.

## 9. Sentence Reordering

The Challenge provides words or chunks and requires the learner to arrange them in the required order.

Example:

Put the words in the correct order:

yesterday / home / went / I

Expected answer:

I went home yesterday.

The supplied tokens/chunks are part of the Challenge. The answer may eventually be represented as an ordered sequence rather than only as a string.

## 10. Word Formation

The Challenge provides a base word or lexical context and requires the learner to derive the required word form.

Example:

He made an important ______ to the project.
Base: contribute

Expected answer: contribution.

This Challenge Form must not be confused with the Knowledge Atom type word_formation. The Form describes the Challenge; the target Atom describes the knowledge being assessed.

## 11. Excluded Forms

### 11.1 True / False

True/False is not a separate form.

It is represented by multiple_choice with exactly two options:

- true
- false

The expected answer is the selected option content.

### 11.2 Matching

Matching is excluded from the current Challenge model.

It is therefore not part of the current canonical Form taxonomy.

### 11.3 Translation

Translation is excluded from the current Challenge model.

It is therefore not part of the current canonical Form taxonomy.

### 11.4 Cloze

Cloze is excluded from the current Challenge model.

Long integrated Cloze exercises are not decomposed into Challenges by the current extraction model.

## 12. Common High-Level Structure

The examples examined so far suggest that most current forms can be described using a common high-level structure:

Challenge
├── instruction
├── prompt
├── options?
└── answer

The optional options component is primarily associated with multiple_choice.

The major observation is that the current forms do not necessarily require a completely different top-level Challenge structure. Instead, the form may determine the internal structure or interpretation of the Challenge content, options, and answer.

For example:

multiple_choice
- instruction
- prompt
- options
- answer

fill_in_blank
- instruction
- prompt
- answer

sentence_transformation
- instruction
- prompt
- answer

sentence_reordering
- instruction
- prompt
- answer

word_formation
- instruction
- prompt
- answer

This observation is one of the reasons the Challenge structure should be designed only after the Challenge Form analysis is sufficiently stable.

## 13. Open Questions

The following questions remain for further analysis:

1. Should fill_in_blank and sentence_completion remain separate forms?
2. Should error_correction distinguish identifying an error from producing a correction?
3. Should short_answer remain a broad form or be split by response semantics?
4. Which forms require structured Challenge content rather than a simple value?
5. Which forms require structured answer values rather than a simple value?
6. Are some apparent forms actually variations of the same underlying Challenge?
7. Should the canonical form field use a flat taxonomy?
8. Which Challenge mechanics are structural enough to affect Form identity?

These questions should be resolved through comparison with real source exercises before the Challenge structure is frozen.

## 14. Relationship to Challenge Structure

The design order is intentional:

Challenge Forms
↓
form-specific Challenge content/answer structures
↓
canonical Challenge Structure
↓
Candidate / Official schemas

Therefore, this document is a prerequisite for finalizing challenge-structure.md.

The Challenge structure should not prematurely force every form into one generic content or answer shape.
