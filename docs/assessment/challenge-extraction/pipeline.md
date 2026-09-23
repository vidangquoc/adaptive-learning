# Challenge Extraction Pipeline

The Challenge Extraction Pipeline describes the processing flow for extracting Atom-level Challenge Candidates from Source Segments.

The pipeline applies the principles defined in the Challenge Extraction Principles.

## Scope

The pipeline operates on individual Source Segments and produces Challenge Candidates or explicit skipped/incomplete extraction reports.

Challenge extraction and Knowledge Atom extraction share the same contextual analysis. The pipeline therefore identifies the Knowledge Atom being assessed while creating each Challenge Candidate.

It does not approve Candidates, deduplicate Challenges, or handle integrated/composite Challenges.

## Pipeline

```
Source Segment
      ↓
Evidence Discovery
      ↓
Contextual Analysis
      ├── Knowledge Atom Candidates
      └── Challenge Candidates
                 │
                 └── target Knowledge Atom
      ↓
Validation
      ↓
Candidates / Issues
```

Knowledge Atom and Challenge Candidates are sibling outputs of the same contextual analysis. The target Knowledge Atom of each Challenge must be identified during that analysis.

An occurrence that cannot be extracted within the current scope follows the reporting path:

```
Assessment occurrence
      ↓
Out of scope / incomplete / ambiguous
      ↓
Skipped extraction report
```

## 1. Evidence Discovery

Inspect the Source Segment and locate evidence relevant to both:

- Knowledge Atom discovery; and
- concrete assessment occurrences.

Evidence discovery identifies where potentially relevant source material occurs. It does not by itself create canonical Knowledge Atoms or Challenge Candidates.

## 2. Contextual Analysis

Analyze each relevant occurrence together with the surrounding source context needed to understand it.

The analysis determines:

- what Knowledge Atoms are represented or revealed by the source;
- what concrete assessment tasks are present;
- the boundary of each assessment task;
- what learner action is expected;
- what Challenge form applies;
- what answer information is available;
- and which Knowledge Atom each Challenge assesses.

A Challenge target may be an existing Knowledge Atom Candidate, an existing Official Knowledge Atom, or a Knowledge Atom identified during the same analysis.

Assessment evidence may reveal a Knowledge Atom that is not otherwise explicit in the source.

If a Challenge assesses a relationship between independent Knowledge Atoms, identify or create the corresponding relation Knowledge Atom during this analysis and target it from the Challenge.

## 3. Create Candidates

Create Knowledge Atom Candidates and Challenge Candidates from the results of contextual analysis.

A Challenge Candidate must preserve enough task information to reconstruct the source assessment occurrence and must identify its target Knowledge Atom.

The Challenge boundary is determined by task independence, not by numbered items, blanks, options, or other formatting units.

Multiple actions or response spaces remain together when they form one independent task.

## 4. Validate Candidates

Validate the extracted Candidates and their relationship.

For Challenge Candidates, check at minimum:

- concrete assessment occurrence;
- correct assessment boundary;
- sufficient task content;
- target Knowledge Atom;
- source-faithfulness;
- absence of invented content;
- preservation of assessment structure;
- answer information when available;
- provenance;
- scope compliance;
- consistency between the Challenge and its target Atom.

Knowledge Atom Candidates are validated according to the Atom Extraction process.

A Candidate that fails required checks should not be emitted as a normal valid Candidate. The issue should instead be represented in the appropriate extraction evidence or skipped/incomplete report.

## 5. Emit Candidates or Issues

If extraction and validation succeed, emit the relevant Knowledge Atom Candidates and Challenge Candidates.

If an assessment occurrence is intentionally excluded or cannot be reliably reconstructed, do not emit a normal Challenge Candidate. Emit a skipped/incomplete extraction report with sufficient evidence to explain the reason.

## Post-Extraction Concerns

The following remain separate processes:

- Candidate review and approval;
- converting Candidates into approved Challenges;
- Challenge deduplication;
- Challenge reuse;
- integrated/composite Challenge extraction;
- detailed answer/evaluation modeling;
- adaptive Challenge selection.
