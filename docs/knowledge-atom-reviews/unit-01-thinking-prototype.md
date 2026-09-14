# Unit 01 — Context-aware knowledge-atom prototype

Status: REVIEW REQUIRED

This is a small source-order prototype. It is not a bulk promotion and does not treat parser output as canonical knowledge.

## Source-order scope

The first lexical entries in the Unit 01 topic-vocabulary section are resolved against the Topic Vocabulary Database because the section explicitly points to page 224 for definitions. The database contains multiple senses for several entries, so senses are kept separate rather than flattened.

## Proposed atoms

### KA-U01-001 — assess
- atom_type: word
- canonical_form: assess
- part_of_speech: verb
- senses:
  1. carefully evaluate a person, situation, or problem in order to make a judgement
  2. calculate the cost or value of something
- source_status: source-stated in Topic Vocabulary Database
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- proposal_note: retain both senses; do not choose one without contextual evidence
- review_status: PENDING

### KA-U01-002 — assume
- atom_type: word
- canonical_form: assume
- part_of_speech: verb
- meaning_summary: believe something is true without being told or having proof
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- review_status: PENDING

### KA-U01-003 — baffle
- atom_type: word
- canonical_form: baffle
- part_of_speech: verb
- meaning_summary: make someone unable to understand or solve a problem or situation
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- review_status: PENDING

### KA-U01-004 — biased
- atom_type: word
- canonical_form: biased
- part_of_speech: adjective
- meaning_summary: unfairly preferring one person, thing, or idea over another
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- review_status: PENDING

### KA-U01-005 — concentrate
- atom_type: word
- canonical_form: concentrate
- part_of_speech: verb
- meaning_summary: give full attention to the activity or thing being considered or done
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- review_status: PENDING

### KA-U01-006 — consider
- atom_type: word
- canonical_form: consider
- part_of_speech: verb
- senses:
  1. think carefully about something before making a decision or forming an opinion
  2. have a particular opinion about a person or thing
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- proposal_note: preserve both senses because the source explicitly distinguishes them
- review_status: PENDING

### KA-U01-007 — contemplate
- atom_type: word
- canonical_form: contemplate
- part_of_speech: verb
- senses:
  1. consider doing something in the future
  2. think very carefully about something for a long time
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- proposal_note: preserve both senses; future-action complement and prolonged consideration are distinct usage information
- review_status: PENDING

### KA-U01-008 — cynical
- atom_type: word
- canonical_form: cynical
- part_of_speech: adjective
- meaning_summary: expecting people to be self-interested/insincere or expecting things not to succeed or be useful
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- review_status: PENDING

### KA-U01-009 — deduce
- atom_type: word
- canonical_form: deduce
- part_of_speech: verb
- meaning_summary: reach knowledge or a conclusion by considering available information or evidence
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- proposal_note: evidence-to-conclusion relation should be retained as part of the meaning
- review_status: PENDING

### KA-U01-010 — deliberate
- atom_type: word
- canonical_form: deliberate
- part_of_speech: verb
- meaning_summary: think about or discuss something very carefully, especially before an important decision
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- context_status: no independent sentence context in the table
- review_status: PENDING

## What this prototype demonstrates

1. Cross-reference resolution can be done by directly reading the relevant source sections.
2. A single lexical item can legitimately produce multiple independent atoms/senses when the source distinguishes them.
3. POS can be taken from explicit source evidence; it is not inferred when already stated.
4. Meaning summaries are derived from source evidence; they are not invented from a word list alone.
5. Absence of sentence-level context is recorded rather than filled by guesswork.
6. These proposals remain pending until human review.

## Next expansion gate

If this representation is accepted, continue in source order with the remaining Thinking entries, then the Learning entries, then phrases/patterns/collocations, idioms, and word formation. Do not bulk-generate the entire book before validating this representation.
