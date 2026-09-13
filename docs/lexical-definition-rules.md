# PTNK Lexical Definition Rules

> Status: Active project rule
> Scope: Lexicon / curated / official lexical data
> Applies to: `meaning_en`, `meaning_vi`, and any source-backed sense description

## 1. No invented definitions

The assistant must **not invent or fabricate a lexical definition** from the context in which a word appears.

A word appearing in a PTNK passage or question does not, by itself, authorize the assistant to create a new definition from contextual inference.

The definition must come from a **reliable lexical source**.

## 2. Context determines the intended sense, not the definition source

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

## 3. Acceptable definition sources

Preferred sources include, where appropriate:

- reputable learner dictionaries
- major general dictionaries
- Cambridge / Oxford / Merriam-Webster and comparable authoritative lexical resources
- English Profile / English Vocabulary Profile where applicable
- specialized dictionaries for specialized terminology
- reliable corpus-backed lexical resources when they provide documented sense information

The source must be appropriate for the lexical item and intended sense.

## 4. Source traceability

For curated and official entries, the project should preserve enough provenance to answer:

> Where did this definition come from?

A definition source is distinct from:

- the PTNK exam source
- the raw transcription source
- the source used to verify CEFR
- the source used to verify pronunciation

Therefore `cefr_source` must never be treated as the general definition source.

## 5. Paraphrasing is allowed; semantic invention is not

Definitions may be shortened or rewritten into learner-friendly language **only when the resulting wording preserves the source meaning accurately**.

Do not:

- add a meaning that the source does not support
- remove a restriction that changes the sense
- merge unrelated senses
- infer a specialized meaning solely from the passage
- turn a contextual implication into a dictionary definition

## 6. Vietnamese meanings

`meaning_vi` must also be grounded in a reliable lexical source and the verified intended sense.

The Vietnamese meaning may be concise and learner-friendly, but it must not introduce an unsupported meaning.

A literal translation is not automatically correct. When necessary, use a reliable bilingual dictionary or derive the Vietnamese wording from a verified English sense while preserving the documented meaning.

## 7. Missing source = do not fabricate

If a reliable source cannot be found for the intended sense:

- do not invent the definition
- do not mark the definition as verified
- preserve the lexical item as raw evidence if appropriate
- leave the curated/official definition pending until a suitable source is found

## 8. Evidence hierarchy

For lexical meaning, prefer:

1. authoritative dictionary / lexical resource documenting the exact sense
2. reliable specialized dictionary for technical vocabulary
3. established corpus-backed lexical resource with documented sense information
4. PTNK context as evidence for the **intended sense**, but not as the sole authority for defining the word

## 9. Examples and patterns are separate

Examples and patterns may be derived or constructed for learning purposes, but they must not be used as a substitute for a reliable lexical definition.

A natural example demonstrates usage; it does not establish the authoritative meaning of the word.
