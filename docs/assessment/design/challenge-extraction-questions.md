# Questions About Challenge Extraction

This document collects unresolved design questions about the Challenge Extraction Pipeline.

## Questions

### Q1. What assessment evidence should be discovered from a source segment?

What should count as evidence of a concrete assessment occurrence, and what information should evidence discovery preserve for later analysis?

### Q2. How should an assessment occurrence be analyzed in context?

How should the extraction process use the surrounding source context to understand the assessment task, its expected learner action, and any information needed to reconstruct it faithfully?

### Q3. How should an assessment occurrence become a Challenge Candidate?

How should the process determine the Challenge boundary and create one Candidate from the source occurrence while preserving the assessment task and its relevant structure?

### Q4. What information must a Challenge Candidate preserve from the source?

What task content, instructions, response elements, answer information, provenance, and extraction evidence must be preserved so that the Candidate can be understood, reviewed, and later converted into a Challenge?

### Q5. How should a Challenge Candidate be validated?

What checks are needed to ensure that a Candidate faithfully represents a concrete assessment occurrence, is complete enough for review, contains no invented source content, and complies with the extraction scope?

### Q6. What should happen when a Challenge Candidate cannot be safely extracted?

How should the extraction process handle assessment occurrences that are out of scope, incomplete, ambiguous, cross-segment, or otherwise insufficient to form a reliable Candidate?
