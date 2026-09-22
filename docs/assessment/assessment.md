# Assessment

Assessment is the process of obtaining evidence about a learner's knowledge or ability by presenting a Challenge and evaluating the learner's response.

Assessment is concerned with determining what a learner knows or can do. It does not define the knowledge itself, the concrete task used to assess it, or the learner's long-term review state.

## Core concepts

The assessment model distinguishes four concepts:

- **Knowledge Atom** — the knowledge that is being assessed.
- **Assessment** — the process of obtaining and interpreting evidence about the learner's knowledge or ability.
- **Challenge** — a concrete task presented to the learner to obtain assessment evidence for one Knowledge Atom.
- **Learner Response** — the learner's response to a Challenge, which provides evidence for assessment.

An assessment may therefore be understood as:

```
Knowledge Atom
      │
      │ what is assessed
      ▼
  Assessment
      │
      │ uses
      ▼
  Challenge
      │
      │ produces
      ▼
Learner Response
      │
      │ provides evidence
      ▼
Assessment Result
```

## What Assessment is for

Assessment provides evidence that can be used to determine whether a learner has demonstrated a Knowledge Atom.

Within Adaptive Learning, assessment evidence is used to update the learner's state and help select subsequent learning or review activities.

Assessment should therefore be separated from:

- the definition of the Knowledge Atom;
- the content and structure of an individual Challenge;
- the learner's persistent review state;
- aggregate operational statistics about Challenges.

## Assessment and Knowledge Atoms

A Knowledge Atom defines **what knowledge exists** in the learning model.

Assessment determines **whether the learner demonstrates that knowledge**.

Each Challenge used for assessment targets exactly one Knowledge Atom.

If the knowledge being assessed is a relationship between independent Knowledge Atoms, that relationship must itself be represented as a `relation` Atom. The Challenge then assesses that relation Atom rather than directly targeting multiple independent Atoms.

## Assessment and Challenges

A Challenge is the concrete mechanism through which an Assessment obtains evidence.

Examples of Challenges include:

- multiple choice;
- fill in the blank;
- sentence completion;
- matching;
- error correction;
- sentence transformation;
- sentence reordering;
- translation;
- word formation;
- cloze tasks.

Different Challenges may assess the same Knowledge Atom while using different contexts, wording, answer mechanisms, or task forms.

Challenge design is specified separately in [Questions About Challenges](questions-about-challenge.md).

## Assessment evidence and learner state

A learner's response to a Challenge is evidence used by Assessment.

The resulting assessment information may be used to update learner-specific review data, such as review counts and scheduling information. Such learner state is not intrinsic to the Knowledge Atom or the Challenge.

The current review-data model is defined separately from Assessment.

## Assessment in Adaptive Learning

Assessment participates in the adaptive loop:

```
Select Knowledge Atom
        ↓
Select suitable Challenge
        ↓
Learner performs Challenge
        ↓
Evaluate Learner Response
        ↓
Obtain Assessment Result
        ↓
Update learner state
        ↓
Select next learning or review activity
```

The adaptive system may use assessment results to decide what the learner should encounter next.

## Scope

This document defines the conceptual boundary of Assessment.

It intentionally does not yet define:

- a Challenge schema;
- Challenge types or templates;
- answer and evaluation schemas;
- learner attempt storage;
- assessment algorithms;
- difficulty models;
- adaptive selection algorithms.

Those details should be designed after the Assessment concept and its boundaries are established.
