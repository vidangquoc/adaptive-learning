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
