# Extraction Principles

This document defines the principles shared by extraction processes that derive Knowledge Atom Candidates and Challenge Candidates from learning-material sources.

Extraction-specific models and rules remain in their respective Knowledge and Assessment documentation.

## 1. Extraction Segment

An extraction session operates on a canonical Source Segment.

The **Extraction Segment** is the Segment currently being analyzed. It remains the primary source boundary of the extraction occurrence.

Supporting context does not change the ownership or source boundary of an extracted Knowledge Atom or Challenge.

## 2. Extraction Context

Extraction context is broader than the Extraction Segment.

The AI must receive the source context required to understand the Extraction Segment and perform reliable semantic extraction. Depending on the source, the context may contain:

- the Extraction Segment;
- Global Supporting Segments;
- Specific Supporting Segments;
- existing Knowledge Atoms relevant to the supporting context.

The exact mapping of these context inputs is source-specific and is defined separately from the canonical Segment structure.

## 3. Global Supporting Segments

A **Global Supporting Segment** is a Segment designated as supporting context for every extraction session within a Learning Material Source.

All Global Supporting Segments MUST be included in every extraction context for that source.

A Global Supporting Segment is included in its entirety. The extraction process does not select only a local portion of the Global Supporting Segment for inclusion.

Typical examples may include source-wide Answer Keys, glossaries, or vocabulary resources, but the global role is determined by the source's extraction-context configuration rather than by the Segment's source type or location alone.

## 4. Specific Supporting Segments

A **Specific Supporting Segment** is a Segment designated as supporting context for a particular Extraction Segment.

An Extraction Segment may have multiple Specific Supporting Segments.

Specific Supporting Segments are included in the extraction context in addition to the Global Supporting Segments.

A Specific Supporting Segment may itself require contextual information to be interpreted correctly. The extraction context must therefore include the context necessary to understand that supporting material.

## 5. Knowledge Context

Extraction context may contain existing Knowledge Atoms associated with relevant supporting context.

Knowledge Context is not source text and must not be treated as new source evidence merely because the Atoms are available to the analysis.

Existing Knowledge Atoms can provide the knowledge state needed to interpret assessment evidence and, in particular, to identify which Knowledge Atom a Challenge assesses.

For example, a review Segment covering Units 1 and 2 may use the Knowledge Atoms established for Units 1 and 2 as Knowledge Context when identifying the target Atom of its Challenges.

The Extraction Segment may also reveal a new knowledge point during the same analysis. Existing Knowledge Context must not force a new finding to match an existing Atom when the source evidence supports a genuinely new Atom.

## 6. Shared Contextual Analysis

Knowledge Atom extraction and Challenge extraction are simultaneous outputs of the same shared contextual analysis.

The common flow is:

```
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
        Challenge Candidates
```

The two outputs are related but do not have shared ownership. Knowledge Atoms remain governed by the Knowledge Atom ontology and lifecycle; Challenges remain governed by the Challenge model and extraction rules.

## 7. Context Is for Interpretation, Not Automatic Provenance

Information supplied as extraction context helps the AI interpret the Extraction Segment. Its presence in context does not automatically make it provenance or source evidence for the extracted result.

In particular:

- a Supporting Segment does not become the source location of a Challenge merely because it was supplied as context;
- an existing Knowledge Atom supplied as Knowledge Context does not become provenance of a newly created Atom merely because it informed the analysis;
- source provenance must continue to identify the actual source occurrence and evidence supporting the extracted object.

Context and provenance therefore serve different purposes:

```
Context    → information available for interpretation
Provenance → evidence supporting the extracted result
```

## 8. Source-Specific Context Configuration

The set of Global and Specific Supporting Segments is specific to each Learning Material Source.

The source may therefore define different extraction-context relationships without changing the canonical Source Segment model.

A separate Extraction Context Map will define these relationships for each source. Its exact structure and resolution rules are intentionally outside this document.

## 9. Context Boundary

Supporting context may cross ordinary Segment boundaries when the source configuration establishes that the additional Segment is relevant.

However, the Extraction Segment itself remains the canonical boundary of the extraction occurrence.

Extraction context must not be used to silently merge independent source occurrences into one occurrence or to move the ownership of extracted objects from the Extraction Segment to a Supporting Segment.

## 10. Uncertainty and Fail-Closed Behavior

Extraction must preserve uncertainty when the available context is insufficient.

If the required context cannot establish the meaning, structure, target Atom, expected answer, or other essential information with sufficient confidence, the relevant extraction result must remain unresolved, incomplete, skipped, or otherwise subject to review according to the applicable extraction rules.

The extractor must not invent missing source information merely to produce a complete Candidate.

## 11. Relationship to Extraction Pipelines

The shared principles in this document apply to both:

- Knowledge Atom extraction; and
- Challenge extraction.

The detailed Knowledge Atom pipeline defines how Knowledge findings become Candidates and later Official Atoms.

The detailed Challenge extraction pipeline defines how assessment findings become Challenge Candidates.

Neither pipeline should redefine the shared meaning of Extraction Segment, Extraction Context, Global Supporting Segment, Specific Supporting Segment, or Knowledge Context.
