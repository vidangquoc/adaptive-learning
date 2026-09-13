# Oxford Phrase List — Source Record

## Purpose

This source is a candidate-universe input for the PTNK Adaptive Preparation System. It is **source data, not curriculum**.

The Oxford Phrase List is an Oxford Learner's Dictionaries resource containing common phrases aligned to CEFR levels, including idioms, phrasal verbs, collocations, common prepositional phrases, complementation patterns, multi-word headwords, and other fixed phrases.

## Official source

- Landing page: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford-phrase-list
- List page: https://www.oxfordlearnersdictionaries.com/wordlists/oxford-phrase-list
- Official PDF: https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-phrase-list/Oxford%20Phrase%20List.pdf

## Source facts recorded

- Publisher: Oxford University Press / Oxford Learner's Dictionaries
- Resource: Oxford Phrase List
- Coverage: A1–C1
- Official PDF currently describes 750 common phrases.
- The online list exposes CEFR labels and supports filtering by level.

## Project usage rule

Do not treat the Oxford Phrase List as an automatically required study list.

Use it to build a broad **candidate universe**. Later filters determine whether an item is:

- active curriculum;
- maintenance;
- backlog;
- stretch;
- rejected.

The downstream selection process must combine source confidence, CEFR evidence, PTNK relevance, competency coverage, learner state, and marginal learning value.

## Raw-data policy

The original Oxford PDF is copyrighted source material. This repository records the authoritative source and retrieval procedure rather than committing a full verbatim reproduction of the copyrighted list.

When project tooling retrieves the source under permitted usage, place the locally cached source outside the canonical curated lexicon and record its checksum and retrieval date in the acquisition manifest.

## Acquisition

The repository includes an acquisition script/manifest so future processing can retrieve the same authoritative source instead of repeatedly designing ad-hoc scrapers or manually reconstructing the source.

## Important distinction

`source/` = evidence/provenance.

`data/lexicon/` = verified, normalized, learner-facing project data.

Never overwrite the source layer with filtered curriculum decisions.
