# Questions About Tests

This document collects unresolved design questions about Tests in the Adaptive Learning framework.

## Current invariants

- A Test tests exactly one Knowledge Atom.
- An Atom may have multiple Tests.
- If a Test appears to test knowledge involving multiple independent knowledge points, that knowledge must be represented by a single Knowledge Atom.
- If the knowledge being tested is a relationship between independent Atoms, that relationship must itself be represented as a `relation` Atom, and the Test tests that relation Atom.
- Test is distinct from Question: a Test represents the assessment target/knowledge being tested; a Question is a concrete question instance or item used to assess that Test.
- A Test must not directly link to multiple Knowledge Atoms.

## Questions

### Q1. What exactly is a Test?

What knowledge or assessment object does a Test represent, and how is it different from a Question?

### Q2. What information must a Test contain?

Which properties are intrinsic to a Test, and which information belongs to Questions generated from the Test?

### Q3. What is the relationship between a Test and its source Segment?

Can a Test be extracted directly from a Segment? What source evidence should be preserved?

### Q4. What makes a Test valid for an Atom?

What criteria determine whether a proposed Test actually tests the target Atom rather than merely mentioning or using it?

### Q5. Can one Atom have different kinds of Tests?

For example, can the same Atom be tested through recognition, recall, production, error correction, or other forms of assessment?

### Q6. How should Test difficulty be represented?

Is difficulty an intrinsic property of a Test, something determined by its Question instances, or something learned from learner performance?

### Q7. Can Tests have dependencies on other Tests or Atoms?

If a Test requires prerequisite knowledge in order to answer it, should that prerequisite relationship be represented explicitly, or should it remain outside the Test model?

### Q8. What is a Test Candidate?

What is extracted from source material during the candidate-generation stage, and what must be reviewed before a Test becomes official?

### Q9. What is the lifecycle of a Test?

How should Test Candidates be reviewed, approved, rejected, officialized, corrected, or retired?

### Q10. How are Tests and Questions linked?

Does one Test generate many Questions? Can the same Question be associated with more than one Test, given the 1:1 Test → Atom rule?

### Q11. What makes a Question a valid realization of a Test?

What constraints must a generated Question satisfy so that it genuinely tests the Test's target Atom?

### Q12. How should Questions be generated from Tests?

What information must be available to generate varied questions without changing the underlying knowledge target?

### Q13. How should learner performance be recorded?

Should performance be attached to the Test, the Question, the Atom, or a separate learner-review structure?

### Q14. Can a Test be reused across different source Segments?

If the same Atom is taught by multiple sources, should identical or equivalent Tests be deduplicated into one Test, or can multiple source-specific Tests coexist?

### Q15. What constitutes the identity of a Test?

What makes two Test Candidates the same Test versus two different Tests for the same Atom?

### Q16. Can a Test target a relation Atom?

Yes, under the current framework: if the tested knowledge concerns a relationship between independent Atoms, that relationship must itself be a `relation` Atom. The Test then targets exactly that one relation Atom.

### Q17. What should happen when a Segment contains assessment-like content but no independently testable Atom?

Should such content be ignored, retained only as source evidence, or represented in another structure?

### Q18. Should Tests be source-independent or source-specific?

If a Test is extracted from a particular Segment, which parts of it should remain tied to that source and which parts should be reusable across the learning system?

### Q19. What is the boundary between a Test and a Question template?

Is a Test an abstract assessment specification while a Question Template defines a reusable question form, or should those concepts be unified?

### Q20. What assessment information belongs outside the Test model?

Which concepts—such as learner ability, attempt history, item statistics, scheduling, or generated-question history—should explicitly not be stored on a Test?
