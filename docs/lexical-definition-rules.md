# PTNK Lexical Definition & Pronunciation Rules

> Status: Active project rule
> Scope: Lexicon / curated / official lexical data
> Applies to: `meaning_en`, `meaning_vi`, `pronunciation`, and any source-backed lexical metadata

## 1. No invented definitions

The assistant must **not invent or fabricate a lexical definition** from the context in which a word appears.

A word appearing in a PTNK passage or question does not, by itself, authorize the assistant to create a new definition from contextual inference.

The definition must come from a **reliable lexical source**.

## 2. No invented pronunciation / transcription

The assistant must **not invent, guess, or reconstruct a pronunciation transcription** merely from spelling, context, phonological intuition, or a generated pronunciation attempt.

`pronunciation` must be grounded in a **reliable pronunciation source**.

In particular, do not:

- guess IPA from the written spelling
- infer pronunciation from a similar-looking word
- copy an unverified pronunciation from an AI-generated source
- silently choose a pronunciation variant without evidence when the lexical item has multiple established readings
- present a generated phonetic respelling as if it were source-verified transcription

If the project specifies US IPA, the US IPA must still be **source-backed**; the formatting convention does not authorize guessing.

## 3. Context determines the intended sense, not the definition source

Context may be used to determine **which sense of an independently sourced definition is relevant**.

Correct workflow:

1. Identify the lexical item and intended sense from the PTNK context.
2. Find a reliable source that documents that sense.
3. Use or carefully paraphrase that source's definition without changing its meaning.
4. Record the definition source in provenance.

Incorrect workflow:

1. Read the PTNK sentence.
2. Infer what the word seems to mean.
3. Write a new definition and present it as authoritative.

## 4. Pronunciation workflow

Correct workflow:

1. Identify the exact lexical item and, where relevant, the intended pronunciation variant.
2. Find a reliable source documenting the pronunciation.
3. Record the pronunciation exactly or normalize it only according to the project's declared transcription convention without changing the underlying pronunciation.
4. Record the pronunciation source in provenance.

Incorrect workflow:

1. Read the spelling.
2. Guess how it sounds.
3. Generate IPA/phonetic spelling from intuition.
4. Present it as verified data.

If no reliable pronunciation source is available, leave the pronunciation **unverified / pending** rather than fabricating it.

## 5. Acceptable definition sources

Preferred sources include, where appropriate:

- reputable learner dictionaries
- major general dictionaries
- Cambridge / Oxford / Merriam-Webster and comparable authoritative lexical resources
- English Profile / English Vocabulary Profile where applicable
- specialized dictionaries for specialized terminology
- reliable corpus-backed lexical resources when they provide documented sense information

The source must be appropriate for the lexical item and intended sense.

## 6. Acceptable pronunciation sources

Preferred pronunciation sources include, where appropriate:

- reputable learner dictionaries that provide IPA/audio or documented pronunciation
- major general dictionaries with pronunciation entries
- authoritative specialized dictionaries when pronunciation is documented
- reliable lexical resources with documented pronunciation variants
- a directly verified pronunciation source appropriate to the target accent/dialect

A source should support the **actual lexical item and reading**, not merely a related word or spelling pattern.

## 7. Source traceability

For curated and official entries, the project should preserve enough provenance to answer:

> Where did this definition come from?
>
> Where did this pronunciation come from?

Definition source and pronunciation source are distinct from:

- the PTNK exam source
- the raw transcription source
- the source used to verify CEFR
- the source used to verify other metadata

Therefore `cefr_source` must never be treated as the general definition or pronunciation source.

## 8. Paraphrasing is allowed; semantic invention is not

Definitions may be shortened or rewritten into learner-friendly language **only when the resulting wording preserves the source meaning accurately**.

Do not:

- add a meaning that the source does not support
- remove a restriction that changes the sense
- merge unrelated senses
- infer a specialized meaning solely from the passage
- turn a contextual implication into a dictionary definition

For pronunciation, normalization is allowed only when it preserves the source-supported pronunciation and follows the project's declared transcription standard. Normalization must not become an excuse to guess missing phonetic information.

## 9. Vietnamese meanings

`meaning_vi` must also be grounded in a reliable lexical source and the verified intended sense.

The Vietnamese meaning may be concise and learner-friendly, but it must not introduce an unsupported meaning.

A literal translation is not automatically correct. When necessary, use a reliable bilingual dictionary or derive the Vietnamese wording from a verified English sense while preserving the documented meaning.

## 10. Missing source = do not fabricate

If a reliable source cannot be found for the intended sense or pronunciation:

- do not invent the definition
- do not invent the pronunciation/transcription
- do not mark the field as verified
- preserve the lexical item as raw evidence if appropriate
- leave the curated/official field pending until a suitable source is found

## 11. Evidence hierarchy

For lexical meaning, prefer:

1. authoritative dictionary / lexical resource documenting the exact sense
2. reliable specialized dictionary for technical vocabulary
3. established corpus-backed lexical resource with documented sense information
4. PTNK context as evidence for the **intended sense**, but not as the sole authority for defining the word

For pronunciation, prefer:

1. authoritative dictionary / lexical resource documenting the exact pronunciation
2. reliable specialized lexical resource documenting the relevant pronunciation
3. directly verified pronunciation evidence appropriate to the target accent/dialect
4. PTNK context only as evidence for which lexical item/variant is intended, **never as the sole basis for constructing a pronunciation**

## 12. Examples and patterns are separate

Examples and patterns may be derived or constructed for learning purposes, but they must not be used as a substitute for a reliable lexical definition or pronunciation source.

A natural example demonstrates usage; it does not establish the authoritative meaning or pronunciation of the word.
