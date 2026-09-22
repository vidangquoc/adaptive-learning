# Questions About Challenges

This document collects unresolved design questions about Challenges in the Adaptive Learning framework.

## Current invariants

- A Challenge is a concrete assessment task presented to a learner to assess a Knowledge Atom.
- Each Challenge assesses exactly one Knowledge Atom.
- A Knowledge Atom may have many Challenges.
- A Challenge is not necessarily a question in the linguistic sense.
- If a Challenge tests knowledge about a relationship between independent Atoms, that relationship must itself be represented as a `relation` Atom, and the Challenge tests that relation Atom.
- A Challenge is a concrete instance, not a reusable abstract template.
- A Challenge references its target Knowledge Atom by ID rather than copying the Atom's knowledge content.
- A Challenge may have source provenance when it is derived from learning material, but source is optional for source-independent or system-generated Challenges.
- Challenge data is distinct from learner performance data.
- The Challenge model does not define a `difficulty` concept.

## Questions

### Q1. What makes a Challenge valid for a Knowledge Atom?

What criteria determine whether a Challenge genuinely assesses its target Atom rather than merely mentioning or using it?

### Q2. How should Challenges be generated from source Segments?

What assessment-relevant information can be extracted from a Segment, and how should that information become Challenge Candidates?

### Q3. What is a Challenge Candidate?

What is produced during candidate generation, and what must be reviewed before a Challenge becomes usable by the learning system?

### Q4. What is the lifecycle of a Challenge?

How should Challenge Candidates be reviewed, approved, rejected, corrected, replaced, or retired?

### Q5. How should Challenges be stored?

Should Challenges live in a central Challenge Store, alongside source-specific data, or in another structure?

### Q6. How should answer and evaluation data be represented?

What information is needed to determine whether a learner's response to a Challenge satisfies the expected answer or evaluation criteria?

### Q7. How should learner performance be recorded?

Which performance information belongs to learner-specific review data, and which information, if any, should be retained with the Challenge?

### Q8. Should Challenge statistics be stored?

For example, response counts, accuracy, discrimination, or other item-level statistics. If so, are these properties of the Challenge or derived operational data?

### Q9. How should Challenges be selected for adaptive review?

How should the system choose among multiple Challenges targeting the same Knowledge Atom?

### Q10. What makes a generated Challenge safe and appropriate?

What validation is needed to prevent ambiguity, accidental testing of another Atom, unsupported assumptions, or responses that cannot be reliably evaluated?

### Q11. What is the role of a Challenge Template or generator?

A Challenge is a concrete instance rather than a template. Should reusable generation patterns or generators be represented as a separate concept, or remain implementation mechanisms outside the Challenge model?

### Q12. What happens when a Segment contains useful assessment information but does not provide enough information to generate a valid Challenge?

Should the information be retained as candidate-generation evidence, ignored, or handled through another structure?

### Q13. What is the identity of a Challenge?

What makes two Challenge Candidates the same Challenge versus two distinct Challenges targeting the same Atom?

### Q14. How should source provenance interact with Challenge reuse?

When a Challenge is derived from a particular Segment but is also reusable independently of that source, which source information should remain attached to the Challenge?

### Q15. What belongs outside the Challenge model?

Beyond the already established separation of learner performance and difficulty, which concepts—such as attempts, review scheduling, learner ability, historical performance, or aggregate operational statistics—should remain outside the intrinsic Challenge data?
