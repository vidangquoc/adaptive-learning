# Questions About Questions

This document collects unresolved design questions about Questions in the Adaptive Learning framework.

## Current invariants

- A Question is a concrete question item used to assess a Knowledge Atom.
- Each Question tests exactly one Knowledge Atom.
- A Knowledge Atom may have many Questions.
- If a Question appears to test knowledge involving multiple independent knowledge points, the tested knowledge must be represented by a single Knowledge Atom.
- If the Question tests knowledge about a relationship between independent Atoms, that relationship must itself be represented as a `relation` Atom, and the Question tests that relation Atom.
- There is no separate Test entity between a Knowledge Atom and a Question.
- Question data should be distinguished from learner performance data.

## Questions

### Q1. What exactly is a Question?

What constitutes a Question in the Adaptive Learning system, and what distinguishes it from a Knowledge Atom?

### Q2. What information must a Question contain?

Which fields are intrinsic to a Question, and which information belongs elsewhere?

### Q3. What makes a Question valid for a Knowledge Atom?

What criteria determine whether a Question genuinely tests its target Atom rather than merely mentioning or using it?

### Q4. Can one Knowledge Atom have different kinds of Questions?

For example, can the same Atom be tested through recognition, recall, production, error correction, completion, or other forms?

### Q5. What makes two Questions different?

Should Questions be considered distinct when they use different wording, different examples, different contexts, or different assessment mechanisms?

### Q6. How should Question difficulty be represented?

Is difficulty an intrinsic property of a Question, something derived from its content, or something learned from learner performance?

### Q7. How should Questions be generated from source Segments?

What assessment-like information can be extracted from a Segment, and how should that information become Question Candidates?

### Q8. What is a Question Candidate?

What is produced during candidate generation, and what must be reviewed before a Question becomes usable by the learning system?

### Q9. What is the lifecycle of a Question?

How should Question Candidates be reviewed, approved, rejected, corrected, replaced, or retired?

### Q10. How should Questions and source evidence be linked?

What source information should be preserved to explain why a Question was generated and what knowledge it is intended to test?

### Q11. How should Questions be stored?

Should Questions live in a central Question Store, alongside source-specific data, or in another structure?

### Q12. How should one Question reference its target Knowledge Atom?

Should the Question contain the Atom ID directly, and what validation rules should apply to that reference?

### Q13. Can a Question be reused across different learning materials?

If the same Question is applicable to an Atom taught by multiple sources, should it be shared or duplicated?

### Q14. Can multiple Questions test the same Atom in substantially different ways?

If so, what distinguishes these Questions without introducing a separate Test abstraction?

### Q15. How should answer data be represented?

What information is needed to determine whether a learner's response to a Question is correct?

### Q16. How should learner performance be recorded?

Which performance information belongs to the Question, and which belongs in learner-specific review data?

### Q17. Should Question statistics be stored?

For example, response counts, accuracy, discrimination, or other item-level statistics. If so, are these properties of the Question or derived operational data?

### Q18. How should Questions be selected for adaptive review?

How should the system choose among multiple Questions targeting the same Knowledge Atom?

### Q19. What makes a generated Question safe and appropriate?

What validation is needed to prevent ambiguity, accidental testing of another Atom, unsupported assumptions, or answers that cannot be reliably evaluated?

### Q20. What is the relationship between a Question and a Question Template?

Is a reusable generation pattern useful as a separate concept, or can Question generation be handled without introducing another ontology object?

### Q21. What happens when a Segment contains useful assessment information but does not provide enough information to generate a valid Question?

Should the information be retained as candidate-generation evidence, ignored, or handled through another structure?

### Q22. What is the identity of a Question?

What makes two Question Candidates the same Question versus two distinct Questions targeting the same Atom?

### Q23. Should Questions be source-specific or source-independent?

If a Question originates from a particular Segment, which parts should remain tied to that source and which parts should be reusable?

### Q24. What assessment information should explicitly remain outside the Question model?

Which concepts—such as learner attempts, review scheduling, learner ability, historical performance, or aggregate item statistics—should not be stored as intrinsic Question data?
