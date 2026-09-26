# Challenge Extraction Pipeline

The Challenge Extraction Pipeline describes the processing flow for extracting Atom-level Challenge Candidates from Source Segments.

The pipeline follows the shared extraction principles defined in [`docs/extraction/principles.md`](../../extraction/principles.md) and defines only Challenge-specific extraction rules.

## Scope

The process operates on individual Source Segments and performs shared contextual analysis from which Knowledge findings and assessment findings are extracted simultaneously. The Challenge-specific branch then analyzes assessment findings and produces Challenge Candidates.

It does not approve Candidates, deduplicate Challenges, or handle integrated/composite Challenges.

## Pipeline

~~~
Extraction Segment
      +
Extraction Context
      ↓
Shared Contextual Analysis
      ├── Knowledge findings
      │       ↓
      │   Knowledge Atom Candidates
      │
      └── Assessment findings
              ↓
        Item-level analysis
              ↓
       Challenge Candidates
              ↓
          Validation
              ↓
      Candidates / Issues
~~~

The shared stages are defined by the extraction principles. This pipeline begins its Challenge-specific processing from the assessment findings produced by that shared analysis.

Whether the target Knowledge Atom already exists as an Official Atom, already exists as a Candidate, or must be created as a new Candidate during the same analysis session does not change the Challenge extraction process.

The presence of an item within an exercise is the strongest evidence that the item is a Challenge. Therefore, exercise items should be considered Challenge candidates by default.

If an item is not emitted as a Challenge, the extraction process must record the reason.

An occurrence that cannot be extracted within the current scope follows the reporting path:

~~~
Exercise item
      ↓
Not a Challenge / out of scope / incomplete / ambiguous
      ↓
Skipped extraction report + reason
~~~

## 1. Item-Level Analysis

For each assessment item identified during shared contextual analysis, determine:

- what learner action the item requires;
- whether the item is an actual Challenge;
- the boundary of the Challenge;
- what specific expected answer is available;
- which Knowledge Atom the Challenge assesses.

An exercise item is presumed to be a Challenge unless Challenge-specific analysis provides a reason not to emit it.

A Challenge target may be an existing Knowledge Atom Candidate, an existing Official Knowledge Atom, or a Knowledge Atom identified during the same shared analysis.

Assessment evidence may reveal a Knowledge Atom that is not otherwise explicit in the source.

If a Challenge assesses a relationship between independent Knowledge Atoms, identify or create the corresponding relation Knowledge Atom during the shared analysis and target it from the Challenge.

The extraction process must not invent an expected answer. If the source does not provide enough evidence to establish the specific expected answer, the occurrence must be treated as incomplete or unresolved rather than silently assigned a new answer.

## 2. Create Candidates

Create Challenge Candidates from the assessment findings after item-level analysis.

For each exercise item:

1. Treat the item as a Challenge candidate by default.
2. Determine whether it is an independent, evaluable learner task and within the current extraction scope.
3. If yes, create the Challenge Candidate, identify its target Knowledge Atom, and preserve the specific expected answer when supported by the source.
4. If no, do not silently discard it; create a skipped extraction report stating the reason.

The Challenge boundary normally follows the exercise item boundary. Multiple blanks, actions, or response spaces within one item remain part of the same Challenge unless contextual analysis establishes that the source actually contains multiple independent items.

## 3. Validate Candidates

Validate Challenge Candidates and their relationship to their target Knowledge Atoms.

For Challenge Candidates, check at minimum:

- concrete assessment occurrence;
- exercise/item provenance;
- correct assessment boundary;
- sufficient task content;
- target Knowledge Atom;
- source-faithfulness;
- absence of invented content;
- preservation of assessment structure;
- specific expected answer when available or required;
- provenance;
- scope compliance;
- consistency between the Challenge and its target Atom.

Also validate that every identifiable exercise item has either:

- produced a Challenge Candidate; or
- produced an explicit skipped extraction report with a reason.

Knowledge Atom Candidates follow the canonical Knowledge Atom ontology, structure, identity, provenance, and review rules defined by the Knowledge documentation.

A Candidate that fails required checks should not be emitted as a normal valid Candidate. The issue should instead be represented in the appropriate extraction evidence or skipped/incomplete report.

## 4. Emit Candidates or Issues

If Challenge extraction and validation succeed, emit the Challenge Candidates.

If an exercise item is not a Challenge or cannot be reliably reconstructed, do not silently omit it. Emit a skipped/incomplete extraction report with sufficient evidence to identify the item and explain the reason.

## Post-Extraction Concerns

The following remain separate processes:

- Candidate review and approval;
- converting Candidates into approved Challenges;
- Challenge deduplication;
- Challenge reuse;
- integrated/composite Challenge extraction;
- learner-response evaluation;
- learner performance recording;
- adaptive Challenge selection.
