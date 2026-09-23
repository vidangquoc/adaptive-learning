# Assessment

Assessment is the process of obtaining evidence about a learner's knowledge or ability.

In Adaptive Learning, Assessment provides a way to determine whether a learner has demonstrated a Knowledge Atom by using a Challenge and interpreting the learner's response.

## Relationship to Knowledge

A Knowledge Atom represents **what the learner is expected to know**.

Assessment concerns **whether the learner demonstrates that knowledge**.

The knowledge being assessed is always represented by a Knowledge Atom. If the knowledge concerns a relationship between independent Knowledge Atoms, that relationship is represented as a `relation` Atom and can therefore be assessed like any other Atom.

## Relationship to Challenge

A Challenge is the concrete task through which assessment evidence is obtained.

One Challenge assesses exactly one Knowledge Atom. Multiple Challenges may assess the same Knowledge Atom in different ways.

The conceptual Challenge model is described in [Challenge](challenge.md), and its canonical structure is defined in [Challenge Structure](challenge-extraction/challenge-structure.md).

## Assessment Evidence

Assessment is based on evidence produced when a learner responds to a Challenge.

At a conceptual level:

```text
Knowledge Atom
      │
      │ is assessed
      ▼
Assessment
      │
      │ uses
      ▼
Challenge
      │
      │ produces evidence
      ▼
Learner Response
      │
      ▼
Assessment Result
```

The details of Challenges, learner responses, evaluation, and assessment results are separate concerns and are not defined by this overview.

## Assessment in Adaptive Learning

Assessment is part of the adaptive learning loop:

```text
Knowledge
    ↓
Assessment
    ↓
Evidence
    ↓
Learner State
    ↓
Next Learning Activity
```

Assessment evidence can be used by the adaptive system to update learner state and determine what the learner should encounter next.

## Scope

This document provides an overall conceptual view of Assessment.

It does not define:

- learner performance storage;
- review scheduling;
- difficulty models;
- adaptive selection algorithms.
