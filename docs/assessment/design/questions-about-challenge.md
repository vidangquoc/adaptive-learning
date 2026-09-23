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
- Source-derived Challenges are extracted from concrete assessment tasks in the source, such as exercise items, rather than generated from Knowledge Atoms.

## Questions

### Q4. What is the lifecycle of a Challenge?

How should Challenge Candidates be reviewed, approved, rejected, corrected, replaced, or retired?

### Q5. How should Challenges be stored?

Should Challenges live in a central Challenge Store, alongside source-specific data, or in another structure?

### Q6. How should answer and evaluation data be represented?

What information is needed to determine whether a learner's response to a Challenge satisfies the expected answer or evaluation criteria?

### Q7. How should learner performance be recorded?

Which performance information belongs in learner-specific review data, and which information, if any, should be retained with the Challenge?

### Q8. Should Challenge statistics be stored?

For example, response counts, accuracy, discrimination, or other item-level statistics. If so, are these properties of the Challenge or derived operational data?

### Q9. How should Challenges be selected for adaptive review?

How should the system choose among multiple Challenges targeting the same Knowledge Atom?

### Q11. What is the role of a Challenge Template or generator?

A Challenge is a concrete instance rather than a template. Should reusable generation patterns or generators be represented as a separate concept, or remain implementation mechanisms outside the Challenge model?

### Q13. What is the identity of a Challenge?

What makes two extracted Challenge Candidates the same Challenge versus two distinct Challenges targeting the same Atom?

### Q14. How should source provenance interact with Challenge reuse?

When a Challenge is extracted from a particular source exercise but is also reusable independently of that source, which source information should remain attached to the Challenge?

### Q15. What belongs outside the Challenge model?

Beyond the already established separation of learner performance and difficulty, which concepts—such as attempts, review scheduling, learner ability, historical performance, or aggregate operational statistics—should remain outside the intrinsic Challenge data?
