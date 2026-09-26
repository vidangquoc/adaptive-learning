# Challenge Extraction Pipeline

The Challenge Extraction Pipeline describes the processing flow for extracting Atom-level Challenge Candidates from Source Segments.

The pipeline applies the shared extraction principles defined in [`docs/extraction/principles.md`](../../extraction/principles.md) and the Challenge-specific extraction rules defined here.

## Scope

The process operates on individual Source Segments and performs a shared contextual analysis from which Knowledge findings and assessment findings are extracted simultaneously. The process may therefore create Knowledge Atom Candidates and Challenge Candidates during the same analysis session.

It does not approve Candidates, deduplicate Challenges, or handle integrated/composite Challenges.

## Pipeline

```
Extraction Segment
      ↓
Build Extraction Context
      ↓
Evidence Discovery
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
              │
              └── target Knowledge Atom
      ↓
Validation
      ↓
Candidates / Issues
```

Knowledge Atom and Challenge extraction are simultaneous outputs of the same contextual analysis. Whether the target Knowledge Atom already exists as an Official Atom, already exists as a Candidate, or must be created as a new Candidate during the same analysis session does not change this process.

The presence of an item within an exercise is the strongest evidence that the item is a Challenge. Therefore, exercise items should be considered Challenge candidates by default.

If an item is not emitted as a Challenge, the extraction process must record the reason.

An occurrence that cannot be extracted within the current scope follows the reporting path:

```
Exercise item
      ↓
Not a Challenge / out of scope / incomplete / ambiguous
      ↓
Skipped extraction report + reason
```

## Extraction Context

Before evidence discovery and contextual analysis, construct the Extraction Context according to the shared extraction principles.

The context includes:

- the Extraction Segment;
- all Global Supporting Segments for the source, included in their entirety;
- all Specific Supporting Segments mapped to the Extraction Segment; and
- existing Knowledge Atoms relevant to the supporting context.

The exact source-specific mapping of Global and Specific Supporting Segments is intentionally defined outside this Challenge pipeline.

## 1. Evidence Discovery

Inspect the Extraction Segment and its Extraction Context and locate evidence relevant to both:

- Knowledge Atom discovery; and
- exercises and their assessment items.

Evidence discovery should preserve the exercise and item boundaries when they are identifiable. These boundaries are strong evidence for later Challenge analysis.

Evidence discovery identifies where potentially relevant source material occurs. It does not by itself create canonical Knowledge Atoms or Challenge Candidates.

## 2. Contextual Analysis

Analyze the Extraction Segment together with its Extraction Context to determine:

- what Knowledge Atoms are represented or revealed by the source;
- what exercises and assessment items are present;
- what learner action each item requires;
- whether each item is an actual Challenge;
- the boundary of each Challenge;
- what specific expected answer is available;
- and which Knowledge Atom each Challenge assesses.

An exercise item is presumed to be a Challenge unless contextual analysis provides a reason not to emit it.

A Challenge target may be an existing Knowledge Atom Candidate, an existing Official Knowledge Atom, or a Knowledge Atom identified during the same analysis.

Assessment evidence may reveal a Knowledge Atom that is not otherwise explicit in the source.

If a Challenge assesses a relationship between independent Knowledge Atoms, identify or create the corresponding relation Knowledge Atom during this analysis and target it from the Challenge.

The extraction process must not invent an expected answer. If the source does not provide enough evidence to establish the specific expected answer, the occurrence must be treated as incomplete or unresolved rather than silently assigned a new answer.

## 3. Create Candidates

Create the relevant Knowledge Atom Candidates and Challenge Candidates from the results of the shared contextual analysis.

For each exercise item:

1. Treat the item as a Challenge candidate by default.
2. Determine whether it is an independent, evaluable learner task and within the current extraction scope.
3. If yes, create the Challenge Candidate, identify its target Knowledge Atom, and preserve the specific expected answer when supported by the source.
4. If no, do not silently discard it; create a skipped extraction report stating the reason.

The Challenge boundary normally follows the exercise item boundary. Multiple blanks, actions, or response spaces within one item remain part of the same Challenge unless contextual analysis establishes that the source actually contains multiple independent items.

## 4. Validate Candidates

Validate the extracted Candidates and their relationship.

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

## 5. Emit Candidates or Issues

If extraction and validation succeed, emit the relevant Knowledge Atom Candidates and Challenge Candidates.

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
