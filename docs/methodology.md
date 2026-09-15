# Methodology

## Goal

Build a PTNK-specific advanced English lexical system rather than a generic C2 word list.

## Evidence hierarchy

1. Actual PTNK specialized English exams and official materials.
2. Cambridge English / English Profile / CEFR evidence.
3. Reliable learner/corpus evidence.
4. AI-generated practice material — useful for testing, but not evidence that a word is PTNK-required.

## Dataset design principles

The dataset separates the lexical item itself from the form actually tested. For example, `sound` is stored with the tested form `sound judgement`, rather than treating every sense of `sound` as equally relevant.

Each item should preserve provenance: year, section, question, role in the item, source quality, and source note. CEFR levels are not assigned unless independently verified.

## Knowledge atoms

Each independent knowledge unit is represented as a flat atom. An atom is a unit that can be independently diagnosed, taught, and assessed, while its boundary must be supported by source evidence rather than invented by AI.

Lexical and grammar knowledge follow the same flat-atom principle. Relationships between atoms are represented explicitly as typed relationships rather than by forcing a parent/child knowledge tree.

### Grammar knowledge atoms

A grammar atom is an independent grammar knowledge unit that a learner may need to diagnose, learn, and assess separately. The unit may be a distinct grammatical use, form, contrast, or other source-supported grammar knowledge unit.

A grammar point with multiple independently teachable uses should normally be split into separate atoms. For example, if a source explicitly teaches Present Simple for general truths, current habits, and permanent situations/states, these are separate atoms rather than one `present simple` atom containing all uses.

Different grammatical forms may also be separate atoms when the source teaches them as independent knowledge units. Contrastive knowledge may likewise be its own atom when the source explicitly teaches the distinction, such as Present Perfect versus Past Simple.

A grammar example alone is not sufficient evidence for creating a grammar atom. The system may use examples to understand context and interpret source material, but it must not infer an unstated grammar rule from an example alone. If the source does not provide sufficient evidence for an independent grammar unit, the corresponding field remains empty/null rather than being authored by AI.

Grammar patterns, usage notes, and relationships must follow the same provenance rule. A pattern is recorded only when supported by the source; it must not be reverse-engineered from an isolated example and presented as source fact.

An exercise may test multiple grammar atoms simultaneously. Atoms remain separate for knowledge storage and learner-state diagnosis even when a single challenge activates several atoms.

## Roles

- `correct_answer`: the keyed answer.
- `distractor`: an option that appeared in the question but was not the keyed answer.
- `reading_only`: vocabulary retained because it occurs in a reading/writing passage rather than as a direct lexical target.
- `transformation_target`: a form required by a transformation task.

## Study modes

- `learn`: high-value item worth active study.
- `recognize`: useful to recognize in context, but not necessarily a first-tier memorization target.
- `defer`: retain for provenance/reference, but postpone active study until the item is independently validated or recurs.

## Priority

- `P1`: core PTNK/general-English value; active study recommended.
- `P2`: useful secondary item; study after P1 or when weak.
- `P3`: mainly recognition or topic-specific vocabulary; do not let it crowd out core items.

Priority is a study decision, not a CEFR claim.

## Learning states

- `unknown`: learner does not know the item.
- `recognition_gap`: knows the meaning in isolation but misses it in context.
- `usage_gap`: knows the item but uses it incorrectly.
- `context_inferable`: can infer from context; do not automatically promote to core.
- `mastered`: confidently recognized and used.

## Specialized vocabulary

Topic-specific words appearing in reading passages are retained with domain metadata, but are normally lower priority unless they recur or have broader academic value.

## Versioning

`v0.1` is the initial extraction. `v0.2` adds tested form/context, role, study mode, source quality, and CEFR-source placeholders without inventing CEFR levels. New exam years should use the v0.2 schema only after this pilot is reviewed.
