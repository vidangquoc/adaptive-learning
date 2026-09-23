# Challenge Forms

This document defines the common forms of Challenges used to assess Knowledge Atoms.

Its purpose is to establish the Challenge Form taxonomy before finalizing the canonical Challenge structure. Form-specific analysis will determine what information a Challenge must contain in its task and answer fields.

A Challenge Form describes how the learner performs an assessment task. It does not identify the Knowledge Atom being assessed.

## 1. Principles

### 1.1 Form is about the assessment task

A form answers:

> What kind of task is the learner performing?

It does not answer what knowledge is being tested. That is identified by target_atom_id.

The same Knowledge Atom may be assessed through different forms, such as multiple choice and fill in the blank.

### 1.2 Form does not determine the target Atom

A form is independent of the knowledge domain.

For example:
- multiple choice may assess vocabulary or grammar;
- fill in the blank may assess vocabulary or grammar;
- matching may assess a vocabulary relation or a grammar distinction.

### 1.3 One Challenge may contain multiple response elements

A form may involve multiple blanks, matches, corrections, or other response elements while still constituting one Challenge.

The number of response elements does not by itself determine the number of Challenges.

## 2. Initial Form Taxonomy

The following forms are common in English-learning materials and are suitable candidates for the initial taxonomy.

Challenge Form
├── selected_response
│   ├── multiple_choice
│   ├── true_false
│   └── matching
│
├── constructed_response
│   ├── fill_in_blank
│   ├── sentence_completion
│   ├── short_answer
│   ├── error_correction
│   ├── sentence_transformation
│   ├── sentence_reordering
│   ├── word_formation
│   └── translation
│
└── cloze
    └── cloze

This is an initial working taxonomy. The grouping is conceptual; canonical stored form values may later use a flatter representation.

## 3. Multiple Choice

The learner selects one answer from a finite set of explicitly provided options.

Example:

Choose the correct answer.

Darren ___ home at eight yesterday.

A. gets
B. got
C. has got

Expected outcome: B.

Characteristics:
- finite explicit options;
- learner selects rather than constructs the answer;
- distractors are part of the task.

Whether the selected option should be identified by stable option ID, position, or value is a separate structural decision.

## 4. True / False

The learner classifies a statement into one of two explicitly defined alternatives, normally True or False.

Example:

Darren got home at eight yesterday. True / False

Expected outcome: True.

This is structurally similar to multiple choice. Whether it should remain a separate canonical form or be represented as a constrained multiple-choice form remains open.

## 5. Matching

The learner associates items from one set with corresponding items from another set.

Example:

Match the words with their meanings.

1. acquire
2. obtain

a. get
b. learn or gain

Expected outcome:

1 → b
2 → a

Matching usually contains multiple response elements, and its answer is inherently structured as a set of pairings.

## 6. Fill in the Blank

The learner supplies missing material in an incomplete expression, sentence, or other bounded context.

Example:

Darren ___ home at eight yesterday.

Expected answer: got.

A single Challenge may contain multiple blanks when they form one independent assessment task.

A blank is a response element, not necessarily a Challenge.

## 7. Sentence Completion

The learner completes a sentence or sentence frame so that it satisfies the task requirements.

Example:

If I had known about the problem, I __________.

Expected answer: would have helped.

This overlaps with fill in the blank. The distinction should remain pragmatic rather than being based only on typography. It may eventually be unnecessary if both forms use the same structural model.

## 8. Short Answer

The learner produces a short, bounded response without being given a finite list of options.

Example:

What is the past tense of "go"?

Expected answer: went.

The response is constructed, but the expected answer remains sufficiently specific for evaluation.

Open-ended essay, speaking, or free-form composition is outside the current Challenge model when a specific expected answer cannot be established.

## 9. Error Correction

The learner identifies and/or corrects an error in provided language.

Example:

Correct the sentence:

Darren go home at eight yesterday.

Expected answer:

Darren went home at eight yesterday.

Some exercises ask the learner to identify the erroneous part, while others ask for the corrected sentence. These may require different answer structures or may later become distinct forms.

## 10. Sentence Transformation

The learner transforms a given sentence according to a specified instruction while preserving the required meaning or satisfying a grammatical transformation.

Example:

Rewrite using "used to":

I lived in London when I was a child.

Expected answer:

I used to live in London when I was a child.

The original sentence and transformation instruction are part of the task; the transformed sentence is the expected outcome.

## 11. Sentence Reordering

The learner rearranges supplied words or chunks into the required order.

Example:

Put the words in the correct order:

yesterday / home / went / I

Expected answer:

I went home yesterday.

The supplied tokens/chunks are part of the task. The answer may eventually be represented as an ordered sequence rather than only as a string.

## 12. Word Formation

The learner derives the required word form from a supplied base word or lexical context.

Example:

He made an important ______ to the project.
Base: contribute

Expected answer: contribution.

This Challenge Form must not be confused with the Knowledge Atom type word_formation. The Form describes the assessment task; the target Atom describes the knowledge being assessed.

## 13. Translation

The learner translates a supplied expression from one language into another.

Example:

Translate into English:

Tôi đã về nhà lúc tám giờ hôm qua.

Expected answer:

I went home at eight yesterday.

Translation can become open-ended very quickly. Under the current Challenge model, a translation Challenge is supported only when a sufficiently specific expected answer can be established.

A task with many equally acceptable translations may require a richer evaluation model and is therefore not automatically a valid supported Challenge.

## 14. Cloze

The learner supplies missing words or forms in a continuous passage or larger connected text.

Example:

When I arrived home, Darren ___ already ___ dinner.

The answer is generally a set or sequence of missing values.

Long integrated Cloze exercises are currently outside the main Challenge extraction scope. Therefore, cloze remains a recognized Form, but long multi-item Cloze exercises should not automatically be decomposed into Challenges by the current extraction pipeline.

## 15. Possible Later Forms

The initial taxonomy may later need forms such as:

- listening discrimination;
- listening comprehension;
- reading comprehension;
- pronunciation production;
- dictation;
- substitution;
- gap-fill with word bank;
- selection from a word bank;
- information-gap tasks;
- dialogue completion;
- categorization;
- sequencing;
- identifying an error;
- identifying a correct form;
- odd-one-out;
- paraphrasing.

They should be added when the Challenge model can represent their task, expected outcome, and evaluation semantics clearly.

## 16. Form versus Task Mechanics

Some distinctions are merely mechanics inside a form rather than distinct forms.

For example:
- one blank versus three blanks;
- four options versus five options;
- vertical versus horizontal option layout;
- source exercise numbering;
- number of lines provided for writing.

These should not automatically become separate Challenge Forms.

A Form should represent a meaningful difference in the nature of the learner's assessment task.

## 17. Form-Specific Structure

Each form can impose different requirements on the eventual Challenge structure.

Conceptually:

form
↓
determines
- task structure
- response structure
- answer structure

Illustrative examples:

multiple_choice
- task: instruction, prompt, options
- answer: selected option

fill_in_blank
- task: prompt, response elements
- answer: values

matching
- task: left items, right items
- answer: pairings

sentence_transformation
- task: instruction, original sentence
- answer: transformed sentence

These are not schemas. They expose structural differences that the canonical Challenge structure must accommodate.

## 18. Open Questions

Before finalizing the Challenge structure and schemas, resolve:

1. Should true_false be a separate Form or a constrained multiple_choice?
2. Should fill_in_blank and sentence_completion remain separate Forms?
3. Should error_correction distinguish identifying an error from producing a correction?
4. Should short_answer remain broad or be split by response semantics?
5. Should translation support only exact translations or a set of acceptable answers?
6. Should cloze remain a Form even though long Cloze extraction is currently out of scope?
7. Which forms require structured answers rather than strings?
8. Which task mechanics are structural enough to affect Form identity?
9. Should the canonical form field use a flat taxonomy or hierarchical categories?
10. Are some apparent Forms actually reusable task mechanics shared by several Forms?

These questions should be resolved through comparison with real source exercises before the Challenge structure is frozen.

## 19. Relationship to Challenge Structure

The design order is intentional:

Challenge Forms
↓
form-specific task/response/answer structures
↓
canonical Challenge Structure
↓
Candidate / Official schemas

Therefore, this document is a prerequisite for finalizing challenge-structure.md.

The Challenge structure should not prematurely force every form into one generic task or answer shape.
