# PTNK 2026 source record

## Scope

This folder records the source and extraction notes for the first pilot dataset. The goal is to test the data model and priority rules on one exam before expanding to 2025, 2024, and earlier papers.

## Exam

- School: Trường Phổ thông Năng khiếu, ĐHQG-HCM
- Year: 2026
- Subject: English (Specialized)
- Date: 24/05/2026
- Duration: 150 minutes
- Questions: 130
- Sections: Language Use, Reading, Writing

The school's official page confirms the 2026 official entrance-exam release and lists Specialized English among the specialized subjects.

## Extraction source

The lexical entries were extracted from a public transcription/key of the 2026 paper and cross-checked against the published exam structure. The transcription includes question numbers, answer options, explanations, reading passages, word formation, error correction, and sentence transformation.

Because the transcription is not the school's canonical PDF, entries are treated as **source-transcribed**, not as independently CEFR-verified data.

## Dataset v0.1

- `data/vocabulary/ptnk-2026-v0.1.csv`: 50 pilot lexical entries
- `data/idioms/ptnk-2026-v0.1.csv`: 55 expressions/phrasal verbs/fixed phrases
- `data/word_formation/ptnk-2026-v0.1.csv`: 10 word-formation families observed in Q106-115

## Rules used in v0.1

1. Provenance is mandatory: year + section + question/passage.
2. CEFR is **not** assigned unless independently verified; current entries use `not_verified`.
3. P1 means high-value for PTNK preparation, not necessarily C1/C2.
4. Topic-specific vocabulary is marked P3 unless it has broader transfer value.
5. Distractors can be included when they represent useful lexical contrasts, but they should not automatically become study priorities.
6. This is a pilot dataset, not yet the final PTNK vocabulary list.

## Review questions for v0.2

- Are P1/P2/P3 boundaries useful for study planning?
- Should distractor words remain in the core dataset or move to a separate `options` table?
- Should collocations be separated from idioms?
- Should reading-only specialist vocabulary be stored separately from the learn-first core?
- Which fields are necessary for generating adaptive tests and flashcards?
