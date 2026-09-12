# Methodology

## Goal

Build a PTNK-specific advanced English lexical system rather than a generic C2 word list.

## Evidence hierarchy

1. Actual PTNK specialized English exams and official materials.
2. Cambridge English / English Profile / CEFR evidence.
3. Reliable learner/corpus evidence.
4. AI-generated practice material — useful for testing, but not evidence that a word is PTNK-required.

## Learning states

- `unknown`: learner does not know the item.
- `recognition_gap`: knows the meaning in isolation but misses it in context.
- `usage_gap`: knows the item but uses it incorrectly.
- `context_inferable`: can infer from context; do not automatically promote to core.
- `mastered`: confidently recognized and used.

## Core rule

Difficulty alone is not enough to promote an item into PTNK Core. Prefer items supported by exam occurrence, recurring lexical pattern, CEFR/Cambridge evidence, or strong general-English value.

## Specialized vocabulary

Topic-specific words appearing in reading passages are retained with domain metadata, but are normally lower priority unless they recur or have broader academic value.
