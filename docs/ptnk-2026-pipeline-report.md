# PTNK 2026 Specialized English — End-to-End Pipeline Report

## Scope

This is the first complete pilot pass of the PTNK lexical pipeline using the 2026 specialized-English entrance exam.

**Important:** this is a high-confidence pilot, not a claim of exhaustive extraction of every lexical item in the 15-page paper.

## 1. RAW source

The official PTNK publication confirms the 2026 specialized-English exam and links the official Drive folder. The exam was held on 24/05/2026, lasted 150 minutes, and contained 130 questions.

Source record: `sources/ptnk-2026/english-specialized.md`

## 2. Lexical evidence extraction

Selected lexical candidates were extracted with:

- year
- section
- question number
- role (`correct_answer`, `distractor`, `reading_only`, or contextual pattern)
- raw lexical item
- context note

Evidence file: `data/evidence/ptnk-2026-specialized-english.csv`

## 3. Normalization

The selected evidence was normalized into canonical lexical forms. Multiword items remain in the same Lexicon as single words.

Examples:

- `errands` → `errand`
- `run errands` → expression
- `cottoned on to` → `cotton on to`
- `cut his losses` → `cut your losses`

## 4. Dictionary verification

Verification used reliable Cambridge Dictionary pages for the selected meanings, pronunciations, patterns, examples, and CEFR where available.

Rules applied:

- no invented IPA
- no context-invented definitions
- CEFR recorded only when independently verified
- missing verification is left as `not_verified`

## 5. PTNK relevance / priority

Priority was assigned for PTNK learning value, not raw difficulty.

- P1: 8 items
- P2: 5 items
- P3: 0 items
- P4: 0 items

The P2 set deliberately retains useful distractors because distractor status does not automatically make an item unimportant.

## 6. CEFR verification

Independently verified in this pilot:

- `derivative` — B1
- `run errands` — C1
- `stick to your guns` — C1
- `cotton on` — C1
- `out on a limb` — C1
- `in the face of` — C2

Other items remain `not_verified`.

## 7. Official promotion

Only the selected records that passed the current pilot QC were promoted into:

`data/lexicon/ptnk-2026-official-v0.1.csv`

An initially captured `raw data` contextual item was removed from the Official Lexicon because its lexical verification had not been completed. This is intentional and demonstrates the project's **accuracy over completeness** rule.

## 8. Learning views

Generated views:

- `data/lexicon/ptnk-2026-p1.csv`
- `data/lexicon/ptnk-2026-p2.csv`
- `data/lexicon/ptnk-2026-p3.csv`
- `data/lexicon/ptnk-2026-p4.csv`

P3/P4 are empty in this pilot because no selected candidate met those thresholds with enough confidence to justify placement there.

## 9. QC

Checks performed:

- provenance present for every official item
- PTNK question/role present
- canonical form normalized
- word type uses project taxonomy
- pronunciation supplied only when verified
- definitions grounded in reliable lexical sources
- examples are natural and sense-compatible
- patterns are usage patterns, not synonym lists
- CEFR is not inferred from difficulty
- priority is PTNK value, not difficulty
- no quota-driven examples
- no unsupported `raw data` item promoted

## 10. Repository state

The pilot is committed to GitHub in sequential commits. The latest commit in this pass is the official-lexicon correction:

`f2c46230259c786b37bde20277cee7d0dc775a39`

## Final assessment

The pipeline works as intended on a small, high-confidence slice of PTNK 2026:

`official source → raw evidence → normalized candidates → dictionary verification → PTNK priority → official lexicon → learning views → QC`

The main limitation is coverage, not data integrity. The next iteration should expand extraction across the remaining 2026 questions while keeping the same verification gates.