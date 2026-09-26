# Extraction Principles

This document defines the principles shared by extraction processes that derive Knowledge Atom Candidates and Challenge Candidates from learning-material sources.

Extraction-specific models and rules remain in their respective Knowledge and Assessment documentation.

## 1. Validated Source Input

Extraction operates only on source material whose structure and provenance have been sufficiently validated for the extraction task.

Before extraction begins:

- source and Segment boundaries must be established;
- source evidence must be preserved;
- provenance must be sufficient to identify and review the source occurrence.

Extraction must not silently repair invalid source structure or replace missing source evidence with invented information.

## 2. Extraction Segment

An extraction session operates on a canonical Source Segment.

The **Extraction Segment** is the Segment currently being analyzed. It remains the primary source boundary of the extraction occurrence.

Supporting context does not change the ownership or source boundary of an extracted Knowledge Atom or Challenge.

## 3. Extraction Context

Extraction context is broader than the Extraction Segment.

The AI must receive the source context required to understand the Extraction Segment and perform reliable semantic extraction. Depending on the source, the context may contain:

- the Extraction Segment;
- Global Supporting Segments;
- Specific Supporting Segments;
- Supporting Knowledge Atoms derived from the relevant Supporting Segments.

The exact mapping of these context inputs is source-specific and is defined separately from the canonical Segment structure.

## 4. Global Supporting Segments

A **Global Supporting Segment** is a Segment designated as supporting context for every extraction session within a Learning Material Source.

All Global Supporting Segments MUST be included in every extraction context for that source.

A Global Supporting Segment is included in its entirety. The extraction process does not select only a local portion of the Global Supporting Segment for inclusion.

Typical examples may include source-wide Answer Keys, glossaries, or vocabulary resources, but the global role is determined by the source's extraction-context configuration rather than by the Segment's source type or location alone.

## 5. Specific Supporting Segments

A **Specific Supporting Segment** is a Segment designated as supporting context for a particular Extraction Segment.

An Extraction Segment may have multiple Specific Supporting Segments.

Specific Supporting Segments are included in the extraction context in addition to the Global Supporting Segments.

A Specific Supporting Segment may itself require contextual information to be interpreted correctly. The extraction context must therefore include the context necessary to understand that supporting material.

## 6. Supporting Knowledge Atoms

Extraction context includes **Supporting Knowledge Atoms** derived from the Supporting Segments available in that context.

Supporting Knowledge Atoms are all Knowledge Atoms associated with the relevant Supporting Segments. They are derived context and are **not declared separately** in the Extraction Context Map.

Supporting Knowledge Atoms are not source text and must not be treated as new source evidence merely because the Atoms are available to the analysis.

They provide the knowledge state needed to interpret assessment evidence and, in particular, to identify which Knowledge Atom a Challenge assesses.

For example, a review Segment covering Units 1 and 2 may use all Knowledge Atoms associated with Units 1 and 2 as Supporting Knowledge Atoms when identifying the target Atom of its Challenges.

The Extraction Segment may also reveal a new knowledge point during the same analysis. Existing Supporting Knowledge Atoms must not force a new finding to match an existing Atom when the source evidence supports a genuinely new Atom.

## 7. Evidence Discovery

Evidence discovery locates source material that may be relevant to extraction.

Depending on the extraction task, discovery may locate knowledge evidence, exercises, assessment items, examples, explanations, patterns, or other source structures.

Discovery output is **evidence location**, not the extracted result itself.

Evidence discovery must not by itself create a canonical Knowledge Atom or Challenge. The located evidence must be interpreted through contextual semantic analysis before an extraction result is produced.

## 8. Contextual Semantic Analysis

Extraction requires semantic and contextual analysis of the discovered evidence together with the relevant Extraction Context.

The analysis determines what the source evidence means and whether it supports an extracted object under the applicable model.

Extraction is therefore not a mechanical conversion of parser output into Knowledge Atoms or Challenges. Automated discovery tools may locate evidence, but they do not by themselves determine the semantic extraction result.

The same contextual analysis may produce different kinds of findings, including Knowledge findings and Assessment findings, while each resulting Candidate remains governed by its own model.

## 9. Extraction Boundaries

Source evidence boundaries and extracted-object boundaries are related but are not inherently identical.

A single source occurrence may support:

- multiple extracted Knowledge Atoms;
- a single extracted Knowledge Atom;
- no Knowledge Atom;

and an identifiable assessment item may likewise be determined, after contextual analysis, to be:

- one Challenge;
- not an independent Challenge;
- or outside the current extraction scope.

Extraction must therefore determine the appropriate semantic boundary rather than assume that every source span or source structure maps one-to-one to one extracted object.

The detailed boundary rules for Knowledge Atoms and Challenges remain in their respective documents.

## 10. Evidence, Context, and Provenance

Information supplied as extraction context helps the AI interpret the Extraction Segment. Its presence in context does not automatically make it provenance or source evidence for the extracted result.

In particular:

- a Supporting Segment does not become the source location of a Challenge merely because it was supplied as context;
- an existing Knowledge Atom supplied as Knowledge Context does not become provenance of a newly created Atom merely because it informed the analysis;
- source provenance must identify the actual source occurrence and evidence supporting the extracted object.

Context and provenance therefore serve different purposes:

```
Context    → information available for interpretation
Provenance → evidence supporting the extracted result
```

## 11. Uncertainty and Fail-Closed Behavior

Extraction must preserve uncertainty when the available evidence or context is insufficient.

If required evidence or context cannot establish the extracted object's essential information with sufficient support, the result must remain unresolved, incomplete, skipped, or otherwise subject to review according to the applicable extraction rules.

The extractor must not invent missing source information merely to produce a complete Candidate.

A failed extraction must not be silently converted into a valid-looking result.

## 12. Shared Analysis and Multiple Extraction Outputs

Knowledge Atom extraction and Challenge extraction are simultaneous outputs of the same shared contextual analysis.

The common flow is:

```
Extraction Segment
      +
Extraction Context
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
        Challenge Candidates
```

The two outputs are related but do not have shared ownership. Knowledge Atoms remain governed by the Knowledge Atom ontology and lifecycle; Challenges remain governed by the Challenge model and extraction rules.

A Challenge may target an existing Knowledge Atom or a Knowledge Atom identified during the same analysis session. The existence of one output does not make the other output authoritative over its own model.

## 13. Extraction Reports

Extraction produces Candidates or explicit extraction reports; it does not silently discard source occurrences that were considered but could not be emitted as valid Candidates.

An extraction report is a process artifact recording a skipped, incomplete, unresolved, or otherwise non-emitted occurrence. It is separate from Candidate data and from downstream review status.

Each extraction pipeline defines the physical location of its reports alongside its Candidate Store. For Knowledge Atom extraction, reports are stored in `data/knowledge/<source-id>/<segment-id>/<domain>/extraction_reports.md`. For Challenge extraction, reports are stored in `data/assessment/<source-id>/<segment-id>/extraction_reports.md`.

The report identifies the source occurrence and records the reason the occurrence was not emitted as a normal Candidate. A rejected Candidate is not an extraction report; rejection belongs to the Candidate review lifecycle.

## 14. Extraction Output and Lifecycle Boundary

Extraction produces Candidates or explicit extraction issues; it does not by itself constitute approval, officialization, deduplication, or other downstream governance decisions.

After extraction:

- Knowledge Atom Candidates follow the Knowledge Atom validation, review, and officialization rules;
- Challenge Candidates follow the Challenge validation and lifecycle rules;
- skipped, incomplete, ambiguous, or unresolved occurrences remain explicitly represented according to the applicable pipeline.

Extraction and downstream governance are therefore separate stages.

## 14. Source-Specific Context Configuration

The set of Global and Specific Supporting Segments is specific to each Learning Material Source.

The source may therefore define different extraction-context relationships without changing the canonical Source Segment model.

Each source defines these relationships in an **Extraction Context Map** located alongside `source-segments.yaml` in the source-specific directory:

```
sources/<source-id>/
├── source-segments.yaml
├── extraction-context-map.yaml
├── segments/
└── segment-text/
```

The map uses Segment IDs defined by `source-segments.yaml`; Segment filenames do not define the identity referenced by the map.

The map has the following structure:

```yaml
source_id: destination-c1-c2

global_supporting_segments:
  - appendix-answer-key
  - appendix-vocabulary

extraction_contexts:
  unit-1:
    supporting_segments:
      - appendix-unit-1-review

  unit-2:
    supporting_segments:
      - appendix-unit-2-review

  unit-3:
    supporting_segments:
      - unit-1
      - unit-2
```

Its semantics are:

- `source_id` identifies the Learning Material Source to which the map applies.
- `global_supporting_segments` lists Segments included in the Extraction Context of every Extraction Segment for that source, in their entirety.
- `extraction_contexts` defines context specific to individual Extraction Segments.
- Each key under `extraction_contexts` is an Extraction Segment ID.
- `supporting_segments` lists one or more Specific Supporting Segments for that Extraction Segment.
- The distinction between Global and Specific Supporting Segments is defined by their location in the map; no per-entry `type` field is required.
- Supporting Knowledge Atoms are derived automatically from the Knowledge Atoms associated with the relevant Supporting Segments and are not declared in the map.

The map defines contextual relationships only. It does not change canonical Segment boundaries, and Supporting Segments do not become the provenance location of extracted objects merely because they are supplied as context.

The exact recursive-resolution rules for Supporting Segments, including whether Supporting Segments themselves inherit additional mapped context, remain open until explicitly decided.

## 15. Context Boundary

Supporting context may cross ordinary Segment boundaries when the source configuration establishes that the additional Segment is relevant.

However, the Extraction Segment itself remains the canonical boundary of the extraction occurrence.

Extraction context must not be used to silently merge independent source occurrences into one occurrence or to move the ownership of extracted objects from the Extraction Segment to a Supporting Segment.

## 16. Relationship to Extraction Pipelines

The shared principles in this document apply to both:

- Knowledge Atom extraction; and
- Challenge extraction.

The detailed Knowledge Atom pipeline defines the Knowledge-specific interpretation, Candidate structure, validation, review, and officialization rules.

The detailed Challenge extraction pipeline defines the Challenge-specific interpretation, Candidate structure, validation, and extraction-scope rules.

Neither pipeline should redefine the shared meaning of Extraction Segment, Extraction Context, Global Supporting Segment, Specific Supporting Segment, Supporting Knowledge Atoms, evidence discovery, contextual analysis, or fail-closed extraction behavior.
