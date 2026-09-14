# Unit 01 — Context-aware knowledge-atom prototype

Status: REVIEW REQUIRED

This is a small source-order prototype. It is not a bulk promotion and does not treat parser output as canonical knowledge.

## Representation decisions validated by this prototype

- **One lexical sense = one atom.** If the source explicitly documents two senses, create two independent atoms so a reviewer can approve, reject, or hold them separately.
- **Source examples belong to the relevant sense atom.** Prefer the book's own example sentence over an invented example during extraction.
- **Evidence is first-class.** Every proposal records where the claim comes from, what source text supports it, and whether the claim is source-stated or inferred.
- **Cross-reference resolution is done by directly reading the relevant source sections.** No intermediate reference parser is required for this prototype.

## Source-order scope

The first lexical entries in the Unit 01 topic-vocabulary section are resolved against the Topic Vocabulary Database because the section explicitly points to page 224 for definitions. The topic-vocabulary section provides the lexical item and POS; the database provides sense-level definitions and examples. The topic-vocabulary table itself does not provide independent sentence context for these entries.

Source evidence:

- Unit 01 topic vocabulary: `sources/destination-c1-c2/sections/unit-01-s02-topic-vocabulary-thinking-see-page-224-for-definitions.txt`
- Topic Vocabulary Database: `sources/destination-c1-c2/appendix/appendix-01-topic-vocabulary-database.txt`, pp. 224–225

## Proposed atoms

### KA-U01-001 — assess — sense 1
- atom_type: word
- canonical_form: assess
- part_of_speech: verb
- sense: carefully consider a situation, person, or problem in order to make a judgment
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `assess (v) to carefully consider a situation, person or problem in order to make a judgment: We tried to assess his suitability for the job.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `We tried to assess his suitability for the job.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-002 — assess — sense 2
- atom_type: word
- canonical_form: assess
- part_of_speech: verb
- sense: calculate what something costs or is worth
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `assess (v) to calculate what something costs or is worth: Our agent will assess the value of your property.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `Our agent will assess the value of your property.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-003 — assume
- atom_type: word
- canonical_form: assume
- part_of_speech: verb
- sense: believe something is true even though no one has told you or you have no proof
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `assume (v) to believe that something is true, even though no one has told you or even though you have no proof: Everyone accepted she was telling the truth, although in fact this was quite a lot to assume.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `Everyone accepted she was telling the truth, although in fact this was quite a lot to assume.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-004 — baffle
- atom_type: word
- canonical_form: baffle
- part_of_speech: verb
- sense: make someone unable to understand or solve a problem or situation
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `baffle (v) if a problem, someone's behaviour, etc baffles you, you cannot understand it or solve it: Detectives remain baffled by these murders.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `Detectives remain baffled by these murders.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-005 — biased
- atom_type: word
- canonical_form: biased
- part_of_speech: adjective
- sense: preferring one person, thing, or idea to another in a way that is unfair
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `biased (adj) preferring one person, thing or idea to another in a way that is unfair: It was a biased report.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `It was a biased report.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-006 — concentrate
- atom_type: word
- canonical_form: concentrate
- part_of_speech: verb
- sense: give all your attention to the thing you are doing
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `concentrate (v) to give all your attention to the thing you are doing: I was sleeping badly and finding it hard to concentrate.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I was sleeping badly and finding it hard to concentrate.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: REJECTED

### KA-U01-007 — consider — sense 1
- atom_type: word
- canonical_form: consider
- part_of_speech: verb
- sense: think about something carefully before making a decision or developing an opinion
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `consider (v) to think about something carefully before making a decision or developing an opinion: She paused and considered for a moment.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `She paused and considered for a moment.`
- context_status: no independent Unit 1 sentence context in the topic-vocabulary table
- review_status: REJECTED

### KA-U01-008 — consider — sense 2
- atom_type: word
- canonical_form: consider
- part_of_speech: verb
- sense: have a particular opinion about someone or something
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `consider (v) to have a particular opinion about someone or something: They consider it inevitable that some jobs will be lost.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `They consider it inevitable that some jobs will be lost.`
- context_status: no independent Unit 1 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-009 — contemplate — sense 1
- atom_type: word
- canonical_form: contemplate
- part_of_speech: verb
- sense: consider doing something in the future
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `contemplate (v) to consider doing something in the future: I'm contemplating retirement next year.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I'm contemplating retirement next year.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-010 — contemplate — sense 2
- atom_type: word
- canonical_form: contemplate
- part_of_speech: verb
- sense: think very carefully about something for a long time
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `contemplate (v) to think very carefully about something for a long time: I haven't got time to sit around contemplating the meaning of life.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I haven't got time to sit around contemplating the meaning of life.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-011 — cynical
- atom_type: word
- canonical_form: cynical
- part_of_speech: adjective
- sense: believing that people care only about themselves and are not sincere or honest, or expecting things not to be successful or useful
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `cynical (adj) someone who is cynical believes that people care only about themselves and are not sincere or honest, or expects things not to be successful or useful: I know that some of you are very cynical about the proposals.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I know that some of you are very cynical about the proposals.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-012 — deduce
- atom_type: word
- canonical_form: deduce
- part_of_speech: verb
- sense: know something as a result of considering the information or evidence available
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `deduce (v) to know something as a result of considering the information or evidence that you have: Finding fossils far inland, he deduced that the area had once been covered by water.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `Finding fossils far inland, he deduced that the area had once been covered by water.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

### KA-U01-013 — deliberate
- atom_type: word
- canonical_form: deliberate
- part_of_speech: verb
- sense: think about or discuss something very carefully, especially before making an important decision
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `deliberate (v) to think about or discuss something very carefully, especially before you make an important decision: The judges deliberated for an hour before choosing the winner.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `The judges deliberated for an hour before choosing the winner.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: APPROVED

## What this prototype demonstrates

1. A single spelling can produce multiple independent atoms when the source documents distinct senses.
2. Each sense atom carries its own evidence and therefore its own human-review outcome.
3. When the source provides an example sentence, preserve it with the specific sense atom it supports.
4. Evidence is not just a source location: preserve the relevant source text/definition/example so a reviewer can verify the proposal without reconstructing the reasoning from scratch.
5. POS is taken from explicit source evidence; it is not inferred when already stated.
6. Meaning summaries are derived from source evidence; they are not invented from a word list alone.
7. Absence of sentence-level context in the Unit 01 topic-vocabulary table is recorded rather than filled by guesswork.
8. These proposals remain pending until human review.

## Next expansion gate

If this representation is accepted, continue in source order with the remaining Thinking entries, then the Learning entries, then phrases/patterns/collocations, idioms, and word formation. Do not bulk-generate the entire book before validating this representation.
