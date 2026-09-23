# Challenge Form Examples

This document provides one concrete Challenge example for each currently recognized Challenge Form.

The examples are intentionally concrete. Their purpose is to expose the information that each form needs in its task and expected answer, so that the canonical Challenge structure can later be designed from actual cases.

Cloze is deliberately excluded from the Challenge Form model and does not appear in this document.

## 1. Multiple Choice

**Task**

Choose the correct answer.

> Darren ___ home at eight yesterday.

- A. gets
- B. got
- C. has got

**Expected answer**

B — got

**Target**

The Knowledge Atom representing the relevant grammatical knowledge.

---

## 2. True / False

**Task**

Read the statement and decide whether it is true or false.

> Darren got home at eight yesterday.

- True
- False

**Expected answer**

True

**Target**

The Knowledge Atom representing the relevant knowledge being assessed.

---

## 3. Matching

**Task**

Match each word with its meaning.

| Word | Meaning |
|---|---|
| 1. acquire | a. get |
| 2. obtain | b. learn or gain |

**Expected answer**

- 1 → b
- 2 → a

**Target**

The Knowledge Atom representing the vocabulary knowledge or relationship being assessed.

---

## 4. Fill in the Blank

**Task**

Complete the sentence with the correct word.

> Darren ___ home at eight yesterday.

**Expected answer**

got

**Target**

The Knowledge Atom representing the relevant grammatical or lexical knowledge.

---

## 5. Sentence Completion

**Task**

Complete the sentence using the appropriate grammatical form.

> If I had known about the problem, I __________.

**Expected answer**

would have helped

**Target**

The Knowledge Atom representing the relevant grammatical construction.

---

## 6. Short Answer

**Task**

Answer the question.

> What is the past tense of “go”?

**Expected answer**

went

**Target**

The Knowledge Atom representing the relevant lexical/morphological knowledge.

---

## 7. Error Correction

**Task**

Correct the sentence.

> Darren go home at eight yesterday.

**Expected answer**

Darren went home at eight yesterday.

**Target**

The Knowledge Atom representing the grammatical knowledge being assessed.

---

## 8. Sentence Transformation

**Task**

Rewrite the sentence using **used to** without changing the intended meaning.

> I lived in London when I was a child.

**Expected answer**

I used to live in London when I was a child.

**Target**

The Knowledge Atom representing the relevant grammatical construction.

---

## 9. Sentence Reordering

**Task**

Put the words in the correct order to make a sentence.

> yesterday / home / went / I

**Expected answer**

I went home yesterday.

**Target**

The Knowledge Atom representing the grammatical or syntactic knowledge being assessed.

---

## 10. Word Formation

**Task**

Complete the sentence using the correct form of the word in brackets.

> He made an important __________ to the project.  
> (CONTRIBUTE)

**Expected answer**

contribution

**Target**

The Knowledge Atom representing the relevant word-formation knowledge.

---

## 11. Translation

**Task**

Translate the sentence into English.

> Tôi đã về nhà lúc tám giờ hôm qua.

**Expected answer**

I went home at eight yesterday.

**Target**

The Knowledge Atom representing the knowledge being assessed.

---

## 12. Excluded Form: Cloze

Cloze is deliberately excluded.

The current Challenge model does not define Cloze as a Challenge Form. In particular, long passages containing multiple gaps are not treated as a collection of independent Challenge forms merely because each gap produces an answer.

Therefore:

- no `cloze` form is defined;
- no Cloze example is included among the canonical forms;
- long integrated Cloze exercises remain outside the current Challenge extraction model.

## 13. Why These Examples Matter

These examples demonstrate that different Challenge Forms require different task and answer structures.

For example:

- **multiple choice** requires options and a selected option;
- **matching** requires two sets of items and a set of pairings;
- **fill in the blank** requires response elements and corresponding values;
- **sentence transformation** requires an original sentence, an instruction, and a transformed outcome;
- **sentence reordering** requires an ordered reconstruction;
- **word formation** requires a base word plus contextual information;
- **translation** requires a source expression and an expected target expression.

Therefore, the canonical Challenge structure should not be finalized until these form-specific differences have been examined.

## 14. Current Form Set

The current working set is:

1. `multiple_choice`
2. `true_false`
3. `matching`
4. `fill_in_blank`
5. `sentence_completion`
6. `short_answer`
7. `error_correction`
8. `sentence_transformation`
9. `sentence_reordering`
10. `word_formation`
11. `translation`

Cloze is not part of the set.
