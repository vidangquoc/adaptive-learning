# Questions About Challenges

This document collects unresolved design questions about Challenges in the Adaptive Learning framework.

## Current invariants

- A Challenge is a concrete assessment task presented to a learner to assess a Knowledge Atom.
- Each Challenge assesses exactly one Knowledge Atom.
- A Knowledge Atom may have many Challenges.
- A Challenge is not necessarily a question in the linguistic sense. It may be a multiple-choice task, fill-in-the-blank task, sentence transformation, error correction, matching task, translation task, reordering task, or another exercise form commonly used in English-learning materials.
- If a Challenge appears to test knowledge involving multiple independent knowledge points, the tested knowledge must be represented by a single Knowledge Atom.
- If a Challenge tests knowledge about a relationship between independent Atoms, that relationship must itself be represented as a `relation` Atom, and the Challenge tests that relation Atom.
- There is no separate Test or Question entity between a Knowledge Atom and a Challenge.
- Challenge data should be distinguished from learner performance data.

## Questions

### Q1. What exactly is a Challenge?

What constitutes a Challenge in the Adaptive Learning system, and what distinguishes it from a Knowledge Atom?

### Q2. What information must a Challenge contain?

Which information is intrinsic to a Challenge, and which information belongs elsewhere?

### Q3. What makes a Challenge valid for a Knowledge Atom?

What criteria determine whether a Challenge genuinely assesses its target Atom rather than merely mentioning or using it?

### Q4. What kinds of Challenges should the system support?

Which exercise forms commonly used in English-learning materials should be represented, such as multiple choice, fill in the blank, sentence completion, matching, error correction, sentence transformation, reordering, translation, word formation, cloze, and other forms?

### Q5. What makes two Challenges different?

Should Challenges be considered distinct when they use different wording, examples, contexts, answer options, or assessment mechanisms?

### Q6. How should Challenge difficulty be represented?

Is difficulty an intrinsic property of a Challenge, something derived from its content, or something learned from learner performance?

### Q7. How should Challenges be generated from source Segments?

What assessment-relevant information can be extracted from a Segment, and how should that information become Challenge Candidates?

### Q8. What is a Challenge Candidate?

What is produced during candidate generation, and what must be reviewed before a Challenge becomes usable by the learning system?

### Q9. What is the lifecycle of a Challenge?

How should Challenge Candidates be reviewed, approved, rejected, corrected, replaced, or retired?

### Q10. How should Challenges and source evidence be linked?

What source information should be preserved to explain why a Challenge was generated and what knowledge it is intended to assess?

### Q11. How should Challenges be stored?

Should Challenges live in a central Challenge Store, alongside source-specific data, or in another structure?

### Q12. How should one Challenge reference its target Knowledge Atom?

Should the Challenge contain the Atom ID directly, and what validation rules should apply to that reference?

### Q13. Can a Challenge be reused across different learning materials?

If the same Challenge is applicable to an Atom taught by multiple sources, should it be shared or duplicated?

### Q14. Can multiple Challenges assess the same Atom in substantially different ways?

If so, what distinguishes these Challenges without introducing a separate Test or Question abstraction?

### Q15. How should answer and evaluation data be represented?

What information is needed to determine whether a learner's response to a Challenge satisfies the expected answer or evaluation criteria?

### Q16. How should learner performance be recorded?

Which performance information belongs to the Challenge, and which belongs in learner-specific review data?

### Q17. Should Challenge statistics be stored?

For example, response counts, accuracy, discrimination, or other item-level statistics. If so, are these properties of the Challenge or derived operational data?

### Q18. How should Challenges be selected for adaptive review?

How should the system choose among multiple Challenges targeting the same Knowledge Atom?

### Q19. What makes a generated Challenge safe and appropriate?

What validation is needed to prevent ambiguity, accidental testing of another Atom, unsupported assumptions, or responses that cannot be reliably evaluated?

### Q20. What is the relationship between a Challenge and a Challenge Template?

Is a reusable generation pattern useful as a separate concept, or can Challenge generation be handled without introducing another ontology object?

### Q21. What happens when a Segment contains useful assessment information but does not provide enough information to generate a valid Challenge?

Should the information be retained as candidate-generation evidence, ignored, or handled through another structure?

### Q22. What is the identity of a Challenge?

What makes two Challenge Candidates the same Challenge versus two distinct Challenges targeting the same Atom?

### Q23. Should Challenges be source-specific or source-independent?

If a Challenge originates from a particular Segment, which parts should remain tied to that source and which parts should be reusable?

### Q24. What assessment information should explicitly remain outside the Challenge model?

Which concepts—such as learner attempts, review scheduling, learner ability, historical performance, or aggregate item statistics—should not be stored as intrinsic Challenge data?
