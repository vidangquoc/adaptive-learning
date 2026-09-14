# Unit 01 — Context-aware knowledge-atom prototype

Status: REVIEW REQUIRED

This is a small source-order prototype. It is not a bulk promotion and does not treat parser output as canonical knowledge.

## Representation decisions validated by this prototype

- **One lexical sense = one atom.** If the source explicitly documents two senses, create two independent atoms so a reviewer can approve, reject, or hold them separately.
- **Use the source's own definition whenever one is provided.** Do not rewrite or paraphrase a source-provided definition as the atom's primary sense description. Preserve the source wording and provenance. Add a translated meaning or an inferred interpretation only as a separate, explicitly labelled field when needed.
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

## Next source-order batch

The next ten lexical entries are `dilemma`, `discriminate` (two senses), `dubious` (two senses), `estimate` (three senses), `faith`, and `gather`. The Topic Vocabulary Database provides source definitions and examples for all of them, so the primary meaning field below preserves the source definition verbatim rather than paraphrasing it.

### KA-U01-014 — dilemma
- atom_type: word
- canonical_form: dilemma
- part_of_speech: noun
- definition: `a situation in which you have to make a difficult decision`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `dilemma (n) a situation in which you have to make a difficult decision: I'm in a dilemma over whether to tell him or not.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I'm in a dilemma over whether to tell him or not.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-015 — discriminate — sense 1
- atom_type: word
- canonical_form: discriminate
- part_of_speech: verb
- definition: `to treat someone unfairly because of their religion, race or other personal features`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `discriminate (v) to treat someone unfairly because of their religion, race or other personal features: Employers are not allowed to discriminate on the basis of gender.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `Employers are not allowed to discriminate on the basis of gender.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-016 — discriminate — sense 2
- atom_type: word
- canonical_form: discriminate
- part_of_speech: verb
- definition: `to recognise the difference between things`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `discriminate (v) to recognise the difference between things: Long-range missile attacks simply cannot discriminate between military and civilian targets.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `Long-range missile attacks simply cannot discriminate between military and civilian targets.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-017 — dubious — sense 1
- atom_type: word
- canonical_form: dubious
- part_of_speech: adjective
- definition: `not completely good, safe or honest`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `dubious (adj) not completely good, safe or honest: The story seemed a bit dubious to me.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `The story seemed a bit dubious to me.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-018 — dubious — sense 2
- atom_type: word
- canonical_form: dubious
- part_of_speech: adjective
- definition: `not sure about the truth or quality of something, or whether you should do something`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `dubious (adj) not sure about the truth or quality of something, or whether you should do something: I'm very dubious about his ability to do the job.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I'm very dubious about his ability to do the job.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-019 — estimate — sense 1
- atom_type: word
- canonical_form: estimate
- part_of_speech: noun
- definition: `an amount that you guess or calculate using the information available`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `estimate (n) an amount that you guess or calculate using the information available: According to official estimates, over 25% of carbon emissions come from the United States.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `According to official estimates, over 25% of carbon emissions come from the United States.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-020 — estimate — sense 2
- atom_type: word
- canonical_form: estimate
- part_of_speech: noun
- definition: `a statement telling a customer how much money you will charge if they employ you to do a particular piece of work`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `estimate (n) a statement telling a customer how much money you will charge if they employ you to do a particular piece of work: The committee are currently getting estimates for repairs to the stonework.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `The committee are currently getting estimates for repairs to the stonework.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-021 — estimate — sense 3
- atom_type: word
- canonical_form: estimate
- part_of_speech: verb
- definition: `to say what you think an amount or value will be, either by guessing or by using available information to calculate it`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `estimate (v) to say what you think an amount or value will be, either by guessing or by using available information to calculate it: It's difficult to estimate the cost of making your house safe.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `It's difficult to estimate the cost of making your house safe.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-022 — faith
- atom_type: word
- canonical_form: faith
- part_of_speech: noun
- definition: `strong belief in or trust of someone or something`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `faith (n) strong belief in or trust of someone or something: I'm delighted to know you have such faith in me.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `I'm delighted to know you have such faith in me.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

### KA-U01-023 — gather
- atom_type: word
- canonical_form: gather
- part_of_speech: verb
- definition: `to believe that something is true, although no one has directly told you about it`
- source_status: source-stated
- source_location: Unit 01 Topic Vocabulary: Thinking; Topic Vocabulary Database, p.224
- evidence:
  - source_text: `gather (v) to believe that something is true, although no one has directly told you about it: You're new here, I gather.`
  - evidence_type: definition_and_source_example
  - claim_status: source-stated
- source_example: `You're new here, I gather.`
- context_status: no independent Unit 01 sentence context in the topic-vocabulary table
- review_status: PENDING

## What this prototype demonstrates

1. A single spelling can produce multiple independent atoms when the source documents distinct senses.
2. Each sense atom carries its own evidence and therefore its own human-review outcome.
3. When the source provides an example sentence, preserve it with the specific sense atom it supports.
4. Evidence is not just a source location: preserve the relevant source text/definition/example so a reviewer can verify the proposal without reconstructing the reasoning from scratch.
5. POS is taken from explicit source evidence; it is not inferred when already stated.
6. When a source provides a definition, preserve the source definition verbatim rather than rewriting it as a model-generated sense summary.
7. Meaning summaries or translations may be added separately when useful, but they must not silently replace source wording.
8. Absence of sentence-level context in the Unit 01 topic-vocabulary table is recorded rather than filled by guesswork.
9. These proposals remain pending until human review.

## Next expansion gate

If this representation is accepted, continue in source order with the remaining Thinking entries, then the Learning entries, then phrases/patterns/collocations, idioms, and word formation. Do not bulk-generate the entire book before validating this representation.
