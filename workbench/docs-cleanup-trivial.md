# Documentation Consistency / Secondary Issues

> This workbench file tracks the remaining documentation consistency issues found during the full audit.
>
> These are secondary to the five critical architecture issues. Each should still be resolved so the documentation, terminology, and ownership model remain internally coherent.
>
> Resolved decisions belong in the appropriate canonical documentation.

## 1. Clarify the Criterion for When a Knowledge Point Becomes an Atom

Different learning-material documents currently imply two slightly different admission triggers:

- knowledge that is explicitly taught, explained, modeled, or exemplified may belong in the knowledge universe;
- for many distinctions, direct source-level testing or practice is described as the trigger for separate Atom representation.

### What must be clarified

Define one consistent rule for when a knowledge point becomes a separate Knowledge Atom, especially for source knowledge that is explicitly taught but never directly tested.

The rule should distinguish:

- source knowledge that should be captured in the knowledge universe;
- independently useful Atom boundaries;
- assessment evidence that strengthens or confirms an Atom;
- examples or explanations that are evidence but do not themselves create Atoms.

---

### Status

**Resolved.** `docs/knowledge/overall.md` now defines the admission criterion: an independently useful knowledge point directly taught or assessed by the source can become an Atom; direct testing is not required. Examples and incidental mentions do not create Atoms by themselves.

## 2. Clarify Taxonomy Coverage for Register, Restrictions, and Pragmatic/Discourse Knowledge

The interpretation principles explicitly ask the extraction process to consider:

- register;
- usage restrictions;
- discourse/pragmatic function;
- semantic contrasts;
- other constraints.

The current taxonomy does not provide an obvious type for every such independently learnable distinction.

### What must be clarified

For each class of knowledge not directly covered by the current vocabulary/grammar types, decide whether it should:

- remain a property of an existing Atom;
- be represented using an existing type;
- become a new canonical type; or
- remain outside the current taxonomy until source-grounded examples demonstrate a need.

The decision should prevent the taxonomy from silently promising support for knowledge categories that have no clear representation.

---

### Status

**Resolved.** `docs/knowledge/atom-types.md` now explicitly covers register, restrictions, pragmatic/discourse knowledge, and semantic contrasts: keep them as properties unless independently taught/assessed and representable by an existing type; do not add a new type without source-grounded modeling evidence.

## 3. Standardize Page-Number Semantics Across Source and Challenge/Atom Provenance

The source segmentation manifest currently defines page numbering as PDF-viewer-based 1-based numbering, while Challenge provenance defines `page_number` as the original/printed source page number. Atom provenance does not specify the convention precisely enough.

### What must be clarified

Define canonical page semantics for:

- source segmentation boundaries;
- Challenge provenance;
- Atom provenance;
- references to segment text.

At minimum, the documentation should make it impossible to confuse:

- PDF viewer page index;
- printed/book page number;
- segment-relative page number.

---

### Status

**Resolved.** Page provenance is now standardized to global PDF-viewer 1-based page numbering across source segmentation, Atom provenance, and Challenge provenance. Printed/book and segment-relative page numbers are not canonical coordinates.

## 4. Align the Source Extraction SOP With Simultaneous Knowledge + Challenge Analysis

The Challenge extraction pipeline explicitly defines Knowledge and Challenge extraction as simultaneous outputs of one shared contextual analysis.

The Source Extraction SOP still presents a high-level pipeline that appears Atom-oriented and later describes assessment extraction separately.

### What must be clarified

Update the operational description so it clearly distinguishes:

- shared contextual analysis;
- Knowledge findings;
- assessment findings;
- Candidate creation for each output.

The goal is not to merge ownership of Knowledge and Challenge objects, but to represent their shared analytical boundary consistently across docs.

---

### Status

**Resolved.** `docs/source/extraction.md` now models shared contextual analysis as producing Knowledge findings and Assessment findings simultaneously, with separate Candidate branches and lifecycles.

## 5. Define the Physical Representation of Skipped / Incomplete Extraction Reports

Challenge extraction requires skipped/incomplete occurrences to be explicitly reported, including a reason.

The current docs do not define a canonical physical representation for these reports.

### What must be clarified

Define, at minimum:

- where such reports are stored;
- whether they are source-level or Challenge-pipeline artifacts;
- their required fields;
- how the source occurrence is identified;
- how reasons/categories are represented;
- whether a schema is required.

If the project intentionally keeps these reports as process artifacts outside canonical data, that decision should be explicit.

---

### Status

**Resolved.** Extraction reports are persisted as `extraction_reports.md` alongside the Candidate Store. Knowledge reports use `data/knowledge/<source-id>/<segment-id>/<domain>/extraction_reports.md`; Challenge reports use `data/assessment/<source-id>/<segment-id>/extraction_reports.md`. Reports are process artifacts for skipped/incomplete/unresolved/non-emitted occurrences and are separate from Candidate review status.

## 6. Define Provenance for Answers Located Outside the Challenge Segment

A Challenge must belong entirely to one Source Segment, but answer information may come from a separate source segment such as an answer-key Segment.

The current provenance model identifies the Challenge occurrence but does not explicitly represent provenance for a separately located answer source.

### What must be clarified

Decide whether answer provenance needs its own structured reference, or whether the existing Challenge provenance plus extraction evidence is sufficient.

The decision should cover cases where:

- task text is in one Segment;
- answer/key is in another Segment;
- multiple source locations contribute to establishing the expected answer.

---

### Status

**Open.** The provenance representation for an expected answer located in a different Segment still requires an explicit design decision.

## 7. Repair Ownership Wording in `lexical-definition-rules.md`

The lexical-definition reference currently says that the canonical rules for extraction, normalization, provenance, proficiency metadata, Challenge linkage, challenge construction, copyright boundaries, and quality gates are all defined under:

```text
docs/learning-material/principles/
```

That is too broad for the current architecture.

Current ownership is distributed across at least:

- `docs/source/` for source structure and extraction;
- `docs/assessment/` for Challenge model and extraction;
- `docs/knowledge/` for Atom ontology/structure/pipeline;
- `docs/learning-material/principles/` for learning-material governance.

### What must be clarified

Narrow the ownership statement and replace the stale umbrella reference with precise cross-references to the current canonical owners.

---

### Status

**Blocked / stale path.** The file path named by this issue, `docs/learning-material/principles/lexical-definition-rules.md`, is not present in the current repository, and repository search did not locate it. No ownership wording was changed by assumption.

## 8. Clarify the Current Meaning of "Mastery" in Methodology

`docs/foundation/methodology.md` says learner state is used to determine mastery, while the current learner-state model defines only latest review state with a remembered/not-remembered review outcome and five persisted fields.

This is not necessarily a contradiction, but it can imply that a formal mastery model already exists.

### What must be clarified

Either:

- define what "mastery" means at the current conceptual level without implying an existing persisted mastery model; or
- defer the term until a formal mastery model exists.

The wording should remain compatible with the current learner-state scope.

### Status

**Resolved.** `docs/foundation/methodology.md` now describes learner state in terms of current review evidence and review needs, and explicitly states that no persisted/formal mastery model is currently defined.
