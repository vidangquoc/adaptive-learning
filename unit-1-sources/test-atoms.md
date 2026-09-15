# Unit 1 — Test Knowledge Atoms

> **Working extraction, not canonical data.** This file is an experiment for testing atom granularity.
>
> In the current project conversation, “Unit 1” refers to **Thinking and Learning**. In the book's canonical table of contents/source segmentation, **Present time is Unit 1 (Grammar)** and **Thinking and learning is Unit 2 (Vocabulary)**. This file follows the latter because that is the unit currently being extracted as “Unit 1” in our discussion.
>
> Source evidence comes from the repository's extracted Destination C1-C2 source plus corroborating copies of the book. The repository's source map identifies the original PDF as the source of truth. fileciteturn94file0L2-L6

## Conventions used in this experiment

- Every atom has `is_tested`.
- `is_tested: true` means the book explicitly tests/practises the knowledge in a Unit 1 question or exercise (not merely that the item appears in an example or answer key).
- `test_evidence` identifies the exercise where possible.
- `is_tested: false` means no Unit 1 exercise has yet been confirmed for that atom. It does **not** mean the atom is unimportant.
- These are deliberately human-readable and not yet the final repository schema.
- Items that are relationships rather than standalone knowledge are kept as atom-level notes only where the book explicitly teaches the distinction.

---

# 1. Topic vocabulary — Thinking

**Fields for every atom in this section:** `id`, `type`, `term`, `part_of_speech`, `meaning`, `usage_notes`, `source_section`, `is_tested`, `test_evidence`

### 1.1 assess

```yaml
id: unit1.lex.thinking.assess
 type: lexical_sense
term: assess
part_of_speech: verb
meaning: evaluate or estimate the quality, value, suitability, nature, or importance of something
usage_notes: Commonly used for judging something after considering relevant information.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 7
```

### 1.2 assume

```yaml
id: unit1.lex.thinking.assume
 type: lexical_sense
term: assume
part_of_speech: verb
meaning: believe that something is true without proof or sufficient evidence
usage_notes: The assumption may be wrong; the word does not itself imply that evidence exists.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 7; Review 1, item 13; word formation exercises
```

### 1.3 baffle

```yaml
id: unit1.lex.thinking.baffle
 type: lexical_sense
term: baffle
part_of_speech: verb
meaning: confuse someone completely so that they cannot understand or solve something
usage_notes: Typically takes a person as object: something baffles someone.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 6
```

### 1.4 biased

```yaml
id: unit1.lex.thinking.biased
 type: lexical_sense
term: biased
part_of_speech: adjective
meaning: unfairly preferring one person, group, side, or idea over another
usage_notes: Often used for opinions, reports, media, decisions, or people.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 2
```

### 1.5 concentrate

```yaml
id: unit1.lex.thinking.concentrate
 type: lexical_sense
term: concentrate
part_of_speech: verb
meaning: give all one's attention to something
usage_notes: Often occurs with on: concentrate on something.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 4
```

### 1.6 consider

```yaml
id: unit1.lex.thinking.consider
 type: lexical_sense
term: consider
part_of_speech: verb
meaning: think carefully about something before making a decision or forming an opinion
usage_notes: Also has a sense meaning to regard someone/something as being a particular way.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 5/8/9; Phrasal-verb exercise F, item 1; grammar section uses consider as a stative/action contrast
```

### 1.7 contemplate

```yaml
id: unit1.lex.thinking.contemplate
 type: lexical_sense
term: contemplate
part_of_speech: verb
meaning: think very carefully and deeply about something; consider a possible future action
usage_notes: The source examples support direct-object use and contemplation of an action or idea.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 5/8/9
```

### 1.8 cynical

```yaml
id: unit1.lex.thinking.cynical
 type: lexical_sense
term: cynical
part_of_speech: adjective
meaning: believing that people are mainly selfish or insincere, or expecting things not to succeed
usage_notes: Often describes an attitude, view, or person.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 3
```

### 1.9 deduce

```yaml
id: unit1.lex.thinking.deduce
 type: lexical_sense
term: deduce
part_of_speech: verb
meaning: reach a conclusion from information or evidence
usage_notes: Strongly associated with reasoning from available evidence.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 9; Review 1, item 40
```

### 1.10 deliberate

```yaml
id: unit1.lex.thinking.deliberate
 type: lexical_sense
term: deliberate
part_of_speech: verb
meaning: think about or discuss something very carefully, especially before an important decision
usage_notes: As a verb, stress is on the second syllable; this atom represents the thinking/action sense.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 2
```

### 1.11 dilemma

```yaml
id: unit1.lex.thinking.dilemma
 type: lexical_sense
term: dilemma
part_of_speech: noun
meaning: a situation in which a difficult choice or decision has to be made
usage_notes: Typically involves competing alternatives or undesirable outcomes.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 1; Review 1, item 35
```

### 1.12 discriminate

```yaml
id: unit1.lex.thinking.discriminate
 type: lexical_sense
term: discriminate
part_of_speech: verb
meaning: recognise or distinguish differences; also, treat someone unfairly because of a personal characteristic
usage_notes: The book teaches more than one sense; the senses should be separated if independently assessed.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 6
```

### 1.13 dubious

```yaml
id: unit1.lex.thinking.dubious
 type: lexical_sense
term: dubious
part_of_speech: adjective
meaning: not completely trustworthy, safe, or certain; uncertain about the truth or quality of something
usage_notes: Can describe either something questionable or a person's uncertainty.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 3
```

### 1.14 estimate

```yaml
id: unit1.lex.thinking.estimate
 type: lexical_sense
term: estimate
part_of_speech: verb/noun
meaning: calculate or judge an approximate amount, value, cost, or size
usage_notes: The book lists both verb and noun uses.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 9
```

### 1.15 faith

```yaml
id: unit1.lex.thinking.faith
 type: lexical_sense
term: faith
part_of_speech: noun
meaning: strong belief or trust in someone, something, or an idea
usage_notes: The unit contrasts this with guesswork, intuition, and related thinking concepts.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 7
```

### 1.16 gather

```yaml
id: unit1.lex.thinking.gather
 type: lexical_sense
term: gather
part_of_speech: verb
meaning: collect or obtain information; reach a conclusion from information
usage_notes: In the unit's thinking context, information gathering can support a conclusion.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 3
```

### 1.17 genius

```yaml
id: unit1.lex.thinking.genius
 type: lexical_sense
term: genius
part_of_speech: noun
meaning: a person with exceptional intellectual ability or exceptional skill
usage_notes: The unit also uses the term in contrast with ordinary ability or ideas.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 10
```

### 1.18 grasp

```yaml
id: unit1.lex.thinking.grasp
 type: lexical_sense
term: grasp
part_of_speech: verb/noun
meaning: understand something; an understanding of something
usage_notes: In the thinking section, the relevant sense is intellectual understanding.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 1
```

### 1.19 guesswork

```yaml
id: unit1.lex.thinking.guesswork
 type: lexical_sense
term: guesswork
part_of_speech: noun
meaning: the use of guesses rather than reliable knowledge or evidence
usage_notes: Contrasts with evidence-based deduction or assessment.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 2
```

### 1.20 hunch

```yaml
id: unit1.lex.thinking.hunch
 type: lexical_sense
term: hunch
part_of_speech: noun
meaning: a feeling or suspicion that something is true without definite evidence
usage_notes: A hunch is an intuition rather than a demonstrated conclusion.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 1
```

### 1.21 ideology

```yaml
id: unit1.lex.thinking.ideology
 type: lexical_sense
term: ideology
part_of_speech: noun
meaning: a set of beliefs or ideas forming the basis of a political or social system
usage_notes: In the unit's exercise it is contrasted with a personal hunch or suspicion.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 5
```

### 1.22 ingenious

```yaml
id: unit1.lex.thinking.ingenious
 type: lexical_sense
term: ingenious
part_of_speech: adjective
meaning: cleverly designed or inventive, especially in solving a problem
usage_notes: Positive evaluation of an idea, method, or solution.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 5
```

### 1.23 inspiration

```yaml
id: unit1.lex.thinking.inspiration
 type: lexical_sense
term: inspiration
part_of_speech: noun
meaning: a sudden idea or feeling that encourages someone to create or act
usage_notes: The unit uses it as a source of an idea rather than as a suspicion.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 9
```

### 1.24 intuition

```yaml
id: unit1.lex.thinking.intuition
 type: lexical_sense
term: intuition
part_of_speech: noun
meaning: an immediate feeling that something is true without conscious reasoning
usage_notes: Contrasts with deliberate reasoning and explicit evidence.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 3
```

### 1.25 justify

```yaml
id: unit1.lex.thinking.justify
 type: lexical_sense
term: justify
part_of_speech: verb
meaning: give a good reason or explanation for something, especially to show that it is reasonable
usage_notes: Often followed by a noun or gerund when explaining the basis for an action.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 8
```

### 1.26 naive

```yaml
id: unit1.lex.thinking.naive
 type: lexical_sense
term: naive
part_of_speech: adjective
meaning: lacking experience or judgement and therefore too ready to believe something
usage_notes: The source contrasts naive assumptions with more cautious thinking.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 4
```

### 1.27 notion

```yaml
id: unit1.lex.thinking.notion
 type: lexical_sense
term: notion
part_of_speech: noun
meaning: an idea, belief, or understanding about something
usage_notes: Often refers to an idea that may be general or not fully developed.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 4
```

### 1.28 optimistic

```yaml
id: unit1.lex.thinking.optimistic
 type: lexical_sense
term: optimistic
part_of_speech: adjective
meaning: expecting good things to happen or expecting a positive outcome
usage_notes: Contrasts with pessimistic.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 1
```

### 1.29 paradox

```yaml
id: unit1.lex.thinking.paradox
 type: lexical_sense
term: paradox
part_of_speech: noun
meaning: a situation, statement, or idea that appears contradictory or strange because apparently incompatible features coexist
usage_notes: Not simply any difficult or surprising situation.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 8
```

### 1.30 pessimistic

```yaml
id: unit1.lex.thinking.pessimistic
 type: lexical_sense
term: pessimistic
part_of_speech: adjective
meaning: expecting bad things to happen or expecting a negative outcome
usage_notes: Contrasts with optimistic.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 1
```

### 1.31 plausible

```yaml
id: unit1.lex.thinking.plausible
 type: lexical_sense
term: plausible
part_of_speech: adjective
meaning: seeming likely to be true, reasonable, or suitable
usage_notes: Plausibility is not proof; it concerns whether an explanation appears credible.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 5
```

### 1.32 ponder

```yaml
id: unit1.lex.thinking.ponder
 type: lexical_sense
term: ponder
part_of_speech: verb
meaning: think carefully and deeply about something for some time
usage_notes: Similar to contemplate but with its own usage and lexical pattern.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 8
```

### 1.33 prejudiced

```yaml
id: unit1.lex.thinking.prejudiced
 type: lexical_sense
term: prejudiced
part_of_speech: adjective
meaning: having an unreasonable negative opinion or feeling about someone or something, especially a group
usage_notes: More specific than merely having a preference; unfairness or unreasonable judgement is central.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 2
```

### 1.34 presume

```yaml
id: unit1.lex.thinking.presume
 type: lexical_sense
term: presume
part_of_speech: verb
meaning: believe something is true because it is likely, although it is not certain
usage_notes: Similar to assume but carries a different degree/basis of expectation.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 10
```

### 1.35 query

```yaml
id: unit1.lex.thinking.query
 type: lexical_sense
term: query
part_of_speech: noun/verb
meaning: a question or request for information; ask about or question something
usage_notes: The noun and verb forms are both listed.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C, item 11
```

### 1.36 reckon

```yaml
id: unit1.lex.thinking.reckon
 type: lexical_sense
term: reckon
part_of_speech: verb
meaning: believe or think that something is true
usage_notes: Often used to express an opinion or estimate.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 6
```

### 1.37 reflect

```yaml
id: unit1.lex.thinking.reflect
 type: lexical_sense
term: reflect
part_of_speech: verb
meaning: think carefully and seriously about something
usage_notes: Often occurs with on/about when expressing the thinking sense.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 10
```

### 1.38 sceptical

```yaml
id: unit1.lex.thinking.sceptical
 type: lexical_sense
term: sceptical / skeptical
part_of_speech: adjective
meaning: having doubts about something that other people think is true or right
usage_notes: British spelling is sceptical; American spelling is skeptical.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 4
```

### 1.39 speculate

```yaml
id: unit1.lex.thinking.speculate
 type: lexical_sense
term: speculate
part_of_speech: verb
meaning: consider or discuss possible explanations or outcomes without complete information
usage_notes: Distinct from deduce because speculation does not require a sufficiently supported conclusion.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 8; Review 1, item 41
```

### 1.40 suppose

```yaml
id: unit1.lex.thinking.suppose
 type: lexical_sense
term: suppose
part_of_speech: verb
meaning: believe or think that something is probably true
usage_notes: Can express an assumption or tentative belief.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B, item 7
```

---

# 2. Topic vocabulary — Learning

**Fields for every atom in this section:** `id`, `type`, `term`, `part_of_speech`, `meaning`, `usage_notes`, `source_section`, `is_tested`, `test_evidence`

### 2.1 academic

```yaml
id: unit1.lex.learning.academic
 type: lexical_sense
term: academic
part_of_speech: noun/adjective
meaning: relating to education or study, especially at college or university level; a teacher or scholar at a university or college
usage_notes: The source lists both noun and adjective uses.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 5
```

### 2.2 conscientious

```yaml
id: unit1.lex.learning.conscientious
 type: lexical_sense
term: conscientious
part_of_speech: adjective
meaning: careful and thorough in doing work or fulfilling duties
usage_notes: Contrasts with inattentive in the learning context.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 2
```

### 2.3 cram

```yaml
id: unit1.lex.learning.cram
 type: lexical_sense
term: cram
part_of_speech: verb
meaning: study a large amount in a short time, especially before an examination
usage_notes: Strongly associated with last-minute study.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 3
```

### 2.4 curriculum

```yaml
id: unit1.lex.learning.curriculum
 type: lexical_sense
term: curriculum
part_of_speech: noun
meaning: the subjects and course of study taught by an educational institution
usage_notes: Refers to the planned educational content rather than a single class.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 6
```

### 2.5 distance learning

```yaml
id: unit1.lex.learning.distance-learning
 type: lexical_sense
term: distance learning
part_of_speech: noun phrase
meaning: education undertaken remotely rather than through regular attendance at a teaching location
usage_notes: A multi-word educational term.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 9 is a distractor; explicit testing of the distinction occurs in the exercise's option set
```

### 2.6 graduate

```yaml
id: unit1.lex.learning.graduate
 type: lexical_sense
term: graduate
part_of_speech: verb/noun
meaning: complete a degree course; a person who has completed a degree course
usage_notes: The source lists both verb and noun uses.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 10
```

### 2.7 ignorant

```yaml
id: unit1.lex.learning.ignorant
 type: lexical_sense
term: ignorant
part_of_speech: adjective
meaning: lacking knowledge or information about something
usage_notes: Does not necessarily mean unintelligent.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 2/5
```

### 2.8 inattentive

```yaml
id: unit1.lex.learning.inattentive
 type: lexical_sense
term: inattentive
part_of_speech: adjective
meaning: not paying sufficient attention
usage_notes: Contrasts with conscientious in the exercise context.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 2
```

### 2.9 intellectual

```yaml
id: unit1.lex.learning.intellectual
 type: lexical_sense
term: intellectual
part_of_speech: noun/adjective
meaning: relating to the ability to think and understand; a person engaged in intellectual work or thought
usage_notes: Distinct from intelligent: intellectual can concern a field or type of activity, not simply mental ability.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 5
```

### 2.10 intelligent

```yaml
id: unit1.lex.learning.intelligent
 type: lexical_sense
term: intelligent
part_of_speech: adjective
meaning: having or showing a good ability to learn, understand, and think
usage_notes: The exercise contrasts it with academic, intellectual, and knowledgeable.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 5
```

### 2.11 intensive

```yaml
id: unit1.lex.learning.intensive
 type: lexical_sense
term: intensive
part_of_speech: adjective
meaning: involving a great deal of activity, effort, or concentration in a short period
usage_notes: Can describe a course or period of study.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 2 is a distractor
```

### 2.12 knowledgeable

```yaml
id: unit1.lex.learning.knowledgeable
 type: lexical_sense
term: knowledgeable
part_of_speech: adjective
meaning: knowing a lot about a subject
usage_notes: Concerns amount/depth of knowledge rather than general intelligence.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 5
```

### 2.13 lecture

```yaml
id: unit1.lex.learning.lecture
 type: lexical_sense
term: lecture
part_of_speech: noun/verb
meaning: a formal educational talk; give such a talk
usage_notes: The noun and verb are both listed.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 3/6 options
```

### 2.14 mock exam

```yaml
id: unit1.lex.learning.mock-exam
 type: lexical_sense
term: mock exam
part_of_speech: noun phrase
meaning: a practice examination designed to resemble a real examination
usage_notes: Used for preparation rather than official certification.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 4
```

### 2.15 plagiarise

```yaml
id: unit1.lex.learning.plagiarise
 type: lexical_sense
term: plagiarise
part_of_speech: verb
meaning: use another person's work or ideas as one's own without proper acknowledgement
usage_notes: The learning context contrasts plagiarism with legitimate use of another person's ideas.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 8
```

### 2.16 self-study

```yaml
id: unit1.lex.learning.self-study
 type: lexical_sense
term: self-study
part_of_speech: noun
meaning: study carried out independently without regular direct instruction
usage_notes: The book treats this as an educational mode.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 9
```

### 2.17 seminar

```yaml
id: unit1.lex.learning.seminar
 type: lexical_sense
term: seminar
part_of_speech: noun
meaning: a class or meeting in which a small group discusses a subject
usage_notes: More discussion-oriented than a conventional lecture.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 6
```

### 2.18 special needs

```yaml
id: unit1.lex.learning.special-needs
 type: lexical_sense
term: special needs
part_of_speech: noun phrase
meaning: additional educational or support requirements arising from a learner's circumstances or disabilities
usage_notes: The book uses the phrase in the context of educational provision.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 1
```

### 2.19 tuition

```yaml
id: unit1.lex.learning.tuition
 type: lexical_sense
term: tuition
part_of_speech: noun
meaning: teaching or instruction; also, in educational contexts, payment for instruction
usage_notes: The exercise tests the educational-service sense in contrast with tutorial.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 7
```

### 2.20 tutorial

```yaml
id: unit1.lex.learning.tutorial
 type: lexical_sense
term: tutorial
part_of_speech: noun
meaning: a small teaching session, usually involving a tutor and a small group or individual learner
usage_notes: Distinct from tuition, which refers to teaching/instruction or fees for it.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 7
```

---

# 3. Phrasal verbs

**Fields for every atom in this section:** `id`, `type`, `expression`, `meaning`, `usage_pattern`, `source_section`, `is_tested`, `test_evidence`

### 3.1 brush up (on)

```yaml
id: unit1.pv.brush-up-on
 type: phrasal_verb
expression: brush up (on)
meaning: practise and improve existing skills or knowledge
usage_pattern: brush up on + subject/skill
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 4
```

### 3.2 come (a)round (to)

```yaml
id: unit1.pv.come-around-to
 type: phrasal_verb
expression: come (a)round (to)
meaning: change one's opinion or decision because someone has persuaded one
usage_pattern: come around to + idea/opinion
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 5; Review 1, item 31
```

### 3.3 come up with

```yaml
id: unit1.pv.come-up-with
 type: phrasal_verb
expression: come up with
meaning: think of an idea or plan
usage_pattern: come up with + idea/plan/excuse
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 2; Review 1, item 12
```

### 3.4 face up to

```yaml
id: unit1.pv.face-up-to
 type: phrasal_verb
expression: face up to
meaning: accept something difficult and try to deal with it
usage_pattern: face up to + fact/problem
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 3; Review 1, item 32
```

### 3.5 figure out

```yaml
id: unit1.pv.figure-out
 type: phrasal_verb
expression: figure out
meaning: understand something or solve a problem; understand a person's behaviour
usage_pattern: figure out + object / how, why, what clause
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 7; Review 1, item 33
```

### 3.6 hit upon

```yaml
id: unit1.pv.hit-upon
 type: phrasal_verb
expression: hit upon
meaning: suddenly have an idea or discover something by chance
usage_pattern: hit upon + idea/discovery
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise E, item 4
```

### 3.7 make out

```yaml
id: unit1.pv.make-out
 type: phrasal_verb
expression: make out
meaning: see, hear, or understand something with difficulty; suggest or imply
usage_pattern: make out + object / clause
source_section: Phrasal verbs
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed
```

### 3.8 mull over

```yaml
id: unit1.pv.mull-over
 type: phrasal_verb
expression: mull over
meaning: think carefully about something over a period of time
usage_pattern: mull over + problem/idea/decision
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise E, item 1; Exercise F, item 1; Review 1, item 30
```

### 3.9 piece together

```yaml
id: unit1.pv.piece-together
 type: phrasal_verb
expression: piece together
meaning: learn or reconstruct the truth by combining separate pieces of information
usage_pattern: piece together + information/story/truth
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise E, item 2; Review 1, item 27
```

### 3.10 puzzle out

```yaml
id: unit1.pv.puzzle-out
 type: phrasal_verb
expression: puzzle out
meaning: solve a confusing or complicated problem by thinking carefully
usage_pattern: puzzle out + problem/answer/solution
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 8
```

### 3.11 read up (on/about)

```yaml
id: unit1.pv.read-up-on
 type: phrasal_verb
expression: read up (on/about)
meaning: get information about a subject by reading extensively
usage_pattern: read up on/about + subject
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 9; Review 1, item 34
```

### 3.12 swot up (on)

```yaml
id: unit1.pv.swot-up-on
 type: phrasal_verb
expression: swot up (on)
meaning: study something very hard, especially for an examination
usage_pattern: swot up on + subject
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 6; Review 1, item 34
```

### 3.13 take in

```yaml
id: unit1.pv.take-in
 type: phrasal_verb
expression: take in
meaning: understand and remember information; accept something as real or true; trick someone into believing something false
usage_pattern: take in + information / person
source_section: Phrasal verbs
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed
```

### 3.14 think over

```yaml
id: unit1.pv.think-over
 type: phrasal_verb
expression: think over
meaning: consider a problem or decision carefully
usage_pattern: think over + problem/offer/decision
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise F, item 1; Review 1, item 30
```

### 3.15 think through

```yaml
id: unit1.pv.think-through
 type: phrasal_verb
expression: think through
meaning: consider the facts and consequences in an organised and thorough way
usage_pattern: think through + plan/problem/possibilities
source_section: Phrasal verbs
is_tested: true
test_evidence: Exercise E, item 7
```

### 3.16 think up

```yaml
id: unit1.pv.think-up
 type: phrasal_verb
expression: think up
meaning: invent or imagine something, especially an excuse or idea
usage_pattern: think up + idea/excuse/plan
source_section: Phrasal verbs
is_tested: true
test_evidence: Review 1, item 29
```

---

# 4. Phrases, patterns and collocations

For this first extraction experiment, a **headword cluster** is used as one provisional atom because the book presents these combinations as grouped lexical-pattern knowledge. This is intentionally provisional; a later extraction pass can split individual combinations into separate atoms if evidence shows they are independently useful.

**Fields for every atom in this section:** `id`, `type`, `headword`, `patterns`, `meaning_scope`, `source_section`, `is_tested`, `test_evidence`

### 4.1 account

```yaml
id: unit1.collocation.account
 type: collocation_cluster
headword: account
patterns:
  - account for
  - give an account of
  - take into account
  - take account of
  - on account of
  - by all accounts
  - on someone's account
meaning_scope: explanation/cause; report; consideration; because of; according to reports; for someone's sake
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 14; Exercise K, item 3; Review 1, item 11
```

### 4.2 associate

```yaml
id: unit1.collocation.associate
 type: collocation_cluster
headword: associate
patterns:
  - associate something with something
meaning_scope: connect one thing mentally or conceptually with another
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 6
```

### 4.3 balance

```yaml
id: unit1.collocation.balance
 type: collocation_cluster
headword: balance
patterns:
  - hang in the balance
  - strike a balance
  - upset/alter/redress the balance
  - balance between/of
  - on balance
  - off balance
meaning_scope: state of uncertainty; achieve equilibrium; change/correct equilibrium; overall judgement; lack of physical or figurative stability
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 13; Exercise K, item 5
```

### 4.4 basis

```yaml
id: unit1.collocation.basis
 type: collocation_cluster
headword: basis
patterns:
  - basis for
  - on a daily/temporary/etc basis
  - on the basis of
  - on the basis that
meaning_scope: foundation/reason; regular or specified frequency; grounds for a decision or claim
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 12
```

### 4.5 belief

```yaml
id: unit1.collocation.belief
 type: collocation_cluster
headword: belief
patterns:
  - express belief(s)
  - belief in
  - belief that
  - contrary to popular belief
  - beyond belief
  - in the belief that
  - popular/widely held/widespread/firm/strong/growing belief
meaning_scope: ways of expressing or qualifying belief
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 8; Exercise J, items 2-3; Review 1, item 15
```

### 4.6 brain

```yaml
id: unit1.collocation.brain
 type: collocation_cluster
headword: brain
patterns:
  - pick someone's brains
  - rack your brains
  - the brains behind
  - brainless
  - brainchild of
  - brainstorm
  - brainwash
  - brainwave
meaning_scope: asking for ideas/knowledge; thinking hard; person responsible for an idea; related derived expressions
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 4
```

### 4.7 conclusion

```yaml
id: unit1.collocation.conclusion
 type: collocation_cluster
headword: conclusion
patterns:
  - bring something to a conclusion
  - come to a conclusion
  - arrive at a conclusion
  - reach a conclusion
  - jump/leap to conclusions
  - in conclusion
  - conclusion of
  - logical conclusion
  - foregone conclusion
meaning_scope: ending; reaching a judgement; drawing a conclusion too quickly; concluding discourse
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise K, item 2; Review 1, item 16
```

### 4.8 consideration

```yaml
id: unit1.collocation.consideration
 type: collocation_cluster
headword: consideration
patterns:
  - take into consideration
  - give consideration to
  - show consideration for
  - under consideration
  - for someone's consideration
  - out of consideration for
meaning_scope: considering something; giving something attention; being considerate
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 7; Exercise K, item 6
```

### 4.9 doubt

```yaml
id: unit1.collocation.doubt
 type: collocation_cluster
headword: doubt
patterns:
  - doubt that
  - have your doubts about
  - cast doubt on
  - raise doubts
  - in doubt
  - doubt as to/about
  - beyond any doubt
  - reasonable doubt
  - without a doubt
  - open to doubt
meaning_scope: uncertainty and expressions for questioning certainty
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 2; Exercise J, item 3; Review 1, item 15
```

### 4.10 dream

```yaml
id: unit1.collocation.dream
 type: collocation_cluster
headword: dream
patterns:
  - dream of/about/that
  - have a dream
  - a dream to
  - beyond your wildest dreams
  - a dream come true
  - in your dreams
  - like a dream
meaning_scope: common combinations for dreams, aspirations, imagined outcomes, and comparisons
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 6
```

### 4.11 focus

```yaml
id: unit1.collocation.focus
 type: collocation_cluster
headword: focus
patterns:
  - focus on
  - the focus of/for
  - in focus
  - out of focus
  - focus group
  - main/primary/major focus
meaning_scope: concentration/central attention; photographic clarity; group research context
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 3
```

### 4.12 impression

```yaml
id: unit1.collocation.impression
 type: collocation_cluster
headword: impression
patterns:
  - have/give the impression that
  - do an impression of
  - create/make an impression on someone
  - under the impression that
  - first impressions
meaning_scope: belief or appearance created by something; imitation; effect on someone
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 3; Review 1, item 13
```

### 4.13 mental

```yaml
id: unit1.collocation.mental
 type: collocation_cluster
headword: mental
patterns:
  - make a mental note of/about
  - mental arithmetic
  - mental illness
  - mental age
  - mental health
meaning_scope: combinations relating to thought, calculation, illness, developmental age, and health
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 2
```

### 4.14 mind

```yaml
id: unit1.collocation.mind
 type: collocation_cluster
headword: mind
patterns:
  - make up your mind
  - cross/slip your mind
  - have/bear in mind
  - have a one-track mind
  - take your mind off
  - bring to mind
  - in two minds about
  - on your mind
  - state of mind
  - narrow/broad/open/absent-minded
meaning_scope: deciding; forgetting; remembering/considering; mental preoccupation; attitudes or mental states
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 7; Exercise J, item 6; Review 1, item 14
```

### 4.15 misapprehension

```yaml
id: unit1.collocation.misapprehension
 type: collocation_cluster
headword: misapprehension
patterns:
  - under the misapprehension that
meaning_scope: incorrect understanding or belief
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 1; Review 1, item 18
```

### 4.16 perspective

```yaml
id: unit1.collocation.perspective
 type: collocation_cluster
headword: perspective
patterns:
  - put into perspective
  - from another/different/someone's perspective
  - from the perspective of
  - in perspective
  - out of perspective
  - a sense of perspective
meaning_scope: viewpoint; contextualising relative importance; correct visual or figurative proportion
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 10
```

### 4.17 principle

```yaml
id: unit1.collocation.principle
 type: collocation_cluster
headword: principle
patterns:
  - have principles
  - stand by/stick to your principles
  - principle of
  - principle that
  - in principle
  - a matter/an issue of principle
  - against someone's principles
  - set of principles
meaning_scope: moral/ethical rules, general rules, and theoretical acceptance
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 5; Exercise J, item 1
```

### 4.18 question

```yaml
id: unit1.collocation.question
 type: collocation_cluster
headword: question
patterns:
  - beg the question
  - raise the question of
  - a/no question of
  - in question
  - out of the question
  - without question
  - beyond question
  - some question over/as to/about
  - awkward question
meaning_scope: questioning, possibility/impossibility, certainty, and disputed matters
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise J, item 4; Review 1, item 16
```

### 4.19 sense

```yaml
id: unit1.collocation.sense
 type: collocation_cluster
headword: sense
patterns:
  - sense that
  - see sense
  - make sense of
  - have the sense to
  - come to your senses
  - a sense of
  - in a/one sense
  - common sense
meaning_scope: perception, understanding, practical judgement, and ways of describing meaning
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 5; Review 1, item 17
```

### 4.20 side

```yaml
id: unit1.collocation.side
 type: collocation_cluster
headword: side
patterns:
  - side with someone
  - take sides
  - see both sides of an argument
  - look on the bright side
  - on the plus/minus side
  - by someone's side
  - on someone's side
  - on either side of
meaning_scope: supporting a person/position, considering alternatives, and describing positions
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 4
```

### 4.21 straight

```yaml
id: unit1.collocation.straight
 type: collocation_cluster
headword: straight
patterns:
  - set/put someone straight about
  - set/put the record straight
  - get/come straight to the point
  - get something straight
  - think/see straight
  - straight talking
  - straight answer
meaning_scope: correcting information, speaking directly, understanding clearly, and being direct
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise I, item 1
```

### 4.22 view

```yaml
id: unit1.collocation.view
 type: collocation_cluster
headword: view
patterns:
  - view something as
  - take the view that
  - take a dim/poor view of
  - come into view
  - in view of
  - with a view to
  - view on/about/that
  - in someone's view
  - viewpoint
  - point of view
meaning_scope: opinion, evaluation, visual appearance, purpose/intention, and perspective
source_section: Phrases, patterns and collocations
is_tested: true
test_evidence: Exercise H, item 11; Review 1, item 14
```

---

# 5. Idioms

**Fields for every atom in this section:** `id`, `type`, `expression`, `meaning`, `usage_notes`, `source_section`, `is_tested`, `test_evidence`

### 5.1 go to your head

```yaml
id: unit1.idiom.go-to-your-head
 type: idiom
expression: go to your head
meaning: make someone think they are more important or successful than they really are
usage_notes: Commonly used about praise, fame, or success.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 5; Review 1, item 22
```

### 5.2 have your wits about you

```yaml
id: unit1.idiom.have-your-wits-about-you
 type: idiom
expression: have/keep your wits about you
meaning: be able to think quickly and make sensible decisions
usage_notes: Usually describes alertness in a difficult or unexpected situation.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 4; Review 1, item 19
```

### 5.3 in the dark (about)

```yaml
id: unit1.idiom.in-the-dark
 type: idiom
expression: in the dark (about)
meaning: not know important information because it has been kept secret or not provided
usage_notes: Usually followed by about + topic.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 9; Review 1, item 23
```

### 5.4 know what's what

```yaml
id: unit1.idiom.know-whats-what
 type: idiom
expression: know what's what
meaning: know the important facts about a situation and understand how things work
usage_notes: Often implies experience or practical understanding.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 3
```

### 5.5 not have a leg to stand on

```yaml
id: unit1.idiom.not-have-a-leg-to-stand-on
 type: idiom
expression: not have a leg to stand on
meaning: have no convincing basis or evidence for claiming that you are right
usage_notes: Common in arguments and legal contexts.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 12; Review 1, item 25
```

### 5.6 not see the wood for the trees

```yaml
id: unit1.idiom.not-see-the-wood-for-the-trees
 type: idiom
expression: not see the wood for the trees
meaning: fail to understand the overall situation because of excessive attention to details
usage_notes: British expression; equivalent idea is missing the big picture.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 10; Review 1, item 20
```

### 5.7 put two and two together

```yaml
id: unit1.idiom.put-two-and-two-together
 type: idiom
expression: put two and two together
meaning: infer what is happening or what something means from information you have seen or heard
usage_notes: Involves informal inference from clues rather than formal deduction.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 6
```

### 5.8 quick/slow on the uptake

```yaml
id: unit1.idiom.on-the-uptake
 type: idiom
expression: quick/slow on the uptake
meaning: quick/slow to understand or realise something
usage_notes: Describes speed of comprehension.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 11; Review 1, item 26
```

### 5.9 ring a bell

```yaml
id: unit1.idiom.ring-a-bell
 type: idiom
expression: ring a bell
meaning: sound familiar without enabling someone to remember the exact details
usage_notes: Often used when a name, fact, or expression seems familiar.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 1; Review 1, item 21
```

### 5.10 round the bend

```yaml
id: unit1.idiom.round-the-bend
 type: idiom
expression: round the bend
meaning: crazy or mentally confused
usage_notes: Informal expression.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 7; Review 1, item 24
```

### 5.11 split hairs

```yaml
id: unit1.idiom.split-hairs
 type: idiom
expression: split hairs
meaning: argue about or worry about very small and unimportant distinctions
usage_notes: Usually negative: the speaker considers the distinction unnecessarily fine.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 2
```

### 5.12 take stock (of)

```yaml
id: unit1.idiom.take-stock-of
 type: idiom
expression: take stock (of)
meaning: think carefully about a situation before deciding what to do next
usage_notes: Implies pausing to assess the current situation.
source_section: Idioms
is_tested: true
test_evidence: Idiom exercise L, item 8
```

---

# 6. Word formation knowledge

**Fields for every atom in this section:** `id`, `type`, `base_word`, `word_family`, `formation_notes`, `source_section`, `is_tested`, `test_evidence`

### 6.1 assume

```yaml
id: unit1.wf.assume
 type: word_formation
base_word: assume
word_family: assumption; assuming; unassuming; assumed
formation_notes: Noun, participial/adjectival, negative/personality-related and past-participial forms are listed.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 2; Review 1, item 3
```

### 6.2 believe

```yaml
id: unit1.wf.believe
 type: word_formation
base_word: believe
word_family: disbelieve; belief; disbelief; believer; unbeliever; believable; unbelievable; disbelieving; unbelievably
formation_notes: Includes negative verb, noun, person noun, adjective, and adverb forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 6; Review 1, item 15
```

### 6.3 brilliant

```yaml
id: unit1.wf.brilliant
 type: word_formation
base_word: brilliant
word_family: brilliance; brilliantly
formation_notes: Adjective → noun and adverb.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 3
```

### 6.4 conceive

```yaml
id: unit1.wf.conceive
 type: word_formation
base_word: conceive
word_family: conceptualise; concept; conception; conceptual; inconceivable; conceivably; inconceivably
formation_notes: The source presents a family spanning verb, noun, adjective, and adverb forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 1; Review 1, item 8
```

### 6.5 confuse

```yaml
id: unit1.wf.confuse
 type: word_formation
base_word: confuse
word_family: confusion; confused; confusing; confusingly
formation_notes: Verb → noun/adjectives/adverb.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 1; Review 1, item 7
```

### 6.6 convince

```yaml
id: unit1.wf.convince
 type: word_formation
base_word: convince
word_family: conviction; convinced; unconvinced; convincing; unconvincing; convincingly; unconvincingly
formation_notes: Verb, noun, adjective, and adverb forms including negative forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 6; Review 1, item 10
```

### 6.7 decide

```yaml
id: unit1.wf.decide
 type: word_formation
base_word: decide
word_family: decision; decider; decisiveness; deciding; decisive; indecisive; decisively; indecisively
formation_notes: Includes noun and adjective/adverb forms expressing decisiveness and its opposite.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 7
```

### 6.8 define

```yaml
id: unit1.wf.define
 type: word_formation
base_word: define
word_family: definition; defined; definitive; definitively; indefinite; indefinitely
formation_notes: Verb, noun, adjective, and adverb forms, including negative forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 4; Review 1, item 2
```

### 6.9 doubt

```yaml
id: unit1.wf.doubt
 type: word_formation
base_word: doubt
word_family: doubter; doubtful; undoubted; doubtless
formation_notes: Noun/person, adjective, negative adjective, and adverb forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 3; Review 1, item 9
```

### 6.10 explain

```yaml
id: unit1.wf.explain
 type: word_formation
base_word: explain
word_family: explanation; explanatory; unexplained; inexplicable; inexplicably
formation_notes: Verb → noun/adjective/adverb with negative and related forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 5; Review 1, item 1
```

### 6.11 imagine

```yaml
id: unit1.wf.imagine
 type: word_formation
base_word: imagine
word_family: imagination; imaginings; imaginary; imaginative; unimaginative
formation_notes: Verb, noun, adjective forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 8
```

### 6.12 judge

```yaml
id: unit1.wf.judge
 type: word_formation
base_word: judge
word_family: judgement; judiciary; judiciousness; judicious; judicial; judgemental; judiciously
formation_notes: The family includes several semantically related noun/adjective forms that should not be collapsed into one lexical sense.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 9
```

### 6.13 logic

```yaml
id: unit1.wf.logic
 type: word_formation
base_word: logic
word_family: illogical; logically
formation_notes: The source specifically highlights negative formation with il-.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 10; Exercise N
```

### 6.14 opinion

```yaml
id: unit1.wf.opinion
 type: word_formation
base_word: opinion
word_family: opinionated
formation_notes: Noun → adjective describing someone strongly or excessively opinionated.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 10
```

### 6.15 rational

```yaml
id: unit1.wf.rational
 type: word_formation
base_word: rational
word_family: rationalise; rationalisation; rationalist; rationalism; irrationality; irrational; rationally; irrationally
formation_notes: Adjective family spanning verbs, nouns, person nouns, and negative forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 2; Exercise N
```

### 6.16 reason

```yaml
id: unit1.wf.reason
 type: word_formation
base_word: reason
word_family: reasoning; reasonableness; unreasonable; reasoned; unreasonably; reasonable
formation_notes: Noun family expressing reasoning, reasonableness, and related adjectives/adverbs.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 8
```

### 6.17 sane

```yaml
id: unit1.wf.sane
 type: word_formation
base_word: sane
word_family: insanity; insane; sanely
formation_notes: Adjective → noun/adverb and negative state.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise M, item 9
```

### 6.18 sense

```yaml
id: unit1.wf.sense
 type: word_formation
base_word: sense
word_family: desensitise; nonsense; sensitivity; sensibility; senselessness; sensible; nonsensical; sensibly; sensitive
formation_notes: The family contains several semantically distinct derivations; each derived lexical item should be considered separately during canonical extraction.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 5; Exercise N; Review 1, item 10
```

### 6.19 think

```yaml
id: unit1.wf.think
 type: word_formation
base_word: think
word_family: thought; thinker; thinking; thoughtfulness; thoughtlessness; thinkable; unthinkable; thoughtful; thoughtless
formation_notes: Verb → noun/adjective family with positive and negative evaluative forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 4
```

### 6.20 wise

```yaml
id: unit1.wf.wise
 type: word_formation
base_word: wise
word_family: wisdom; unwise; wisely; unwisely
formation_notes: Adjective → noun/adverb and negative forms.
source_section: Word formation
is_tested: true
test_evidence: Word-formation exercise O, item 7
```

---

# 7. Cross-atom semantic distinctions explicitly useful for this unit

These are **relations, not additional lexical atoms**. They are included here because the extraction experiment needs to show which relationships are worth preserving.

**Fields for every relation:** `id`, `type`, `source_atom_ids`, `relation`, `distinction`, `source_section`, `is_tested`, `test_evidence`

### 7.1 assume vs presume

```yaml
id: unit1.rel.assume-presume
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.assume
  - unit1.lex.thinking.presume
relation: near_synonym_with_distinction
distinction: Both express accepting something as true without certainty; presume is associated with something considered likely, while assume can be a less evidence-based acceptance.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 7 and item 10
```

### 7.2 assume vs deduce

```yaml
id: unit1.rel.assume-deduce
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.assume
  - unit1.lex.thinking.deduce
relation: semantic_distinction
distinction: Assume accepts something as true without sufficient proof; deduce reaches a conclusion from information or evidence.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 7 and item 9; Review 1, item 40
```

### 7.3 assess vs estimate

```yaml
id: unit1.rel.assess-estimate
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.assess
  - unit1.lex.thinking.estimate
relation: near_synonym_with_distinction
distinction: Both involve evaluation; estimate focuses on an approximate amount/value, while assess is broader evaluation or judgement.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 7 and item 9
```

### 7.4 optimistic vs pessimistic

```yaml
id: unit1.rel.optimistic-pessimistic
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.optimistic
  - unit1.lex.thinking.pessimistic
relation: antonymy
distinction: Positive expectation versus negative expectation.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 1
```

### 7.5 biased vs prejudiced

```yaml
id: unit1.rel.biased-prejudiced
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.biased
  - unit1.lex.thinking.prejudiced
relation: near_synonym_with_distinction
distinction: Both involve unfair judgement; biased is broader preference for one side, while prejudiced emphasises an unreasonable negative opinion or feeling, especially toward a group.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 2
```

### 7.6 dubious vs cynical

```yaml
id: unit1.rel.dubious-cynical
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.dubious
  - unit1.lex.thinking.cynical
relation: semantic_distinction
distinction: Dubious concerns uncertainty or questionable quality/truth; cynical concerns distrust of people's motives or expectation of failure.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 3
```

### 7.7 plausible vs ingenious

```yaml
id: unit1.rel.plausible-ingenious
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.plausible
  - unit1.lex.thinking.ingenious
relation: semantic_distinction
distinction: Plausible describes an explanation that seems likely or reasonable; ingenious describes clever inventiveness.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise A, item 5
```

### 7.8 consider vs contemplate vs ponder

```yaml
id: unit1.rel.consider-contemplate-ponder
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.consider
  - unit1.lex.thinking.contemplate
  - unit1.lex.thinking.ponder
relation: semantic_distinction
distinction: All concern thinking about something; the source distinguishes ordinary careful consideration from deeper/longer contemplation and pondering.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise B
```

### 7.9 guesswork vs hunch vs intuition

```yaml
id: unit1.rel.guesswork-hunch-intuition
 type: semantic_relation
source_atom_ids:
  - unit1.lex.thinking.guesswork
  - unit1.lex.thinking.hunch
  - unit1.lex.thinking.intuition
relation: semantic_distinction
distinction: Guesswork relies on guesses rather than reliable evidence; a hunch is a feeling/suspicion; intuition is an immediate feeling of truth without conscious reasoning.
source_section: Topic vocabulary — Thinking
is_tested: true
test_evidence: Vocabulary exercise C
```

### 7.10 intelligent vs intellectual vs knowledgeable

```yaml
id: unit1.rel.intelligent-intellectual-knowledgeable
 type: semantic_relation
source_atom_ids:
  - unit1.lex.learning.intelligent
  - unit1.lex.learning.intellectual
  - unit1.lex.learning.knowledgeable
relation: semantic_distinction
distinction: Intelligent concerns ability to learn/understand; intellectual concerns thinking/academic or intellectual activity; knowledgeable concerns having substantial knowledge.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 5
```

### 7.11 tuition vs tutorial

```yaml
id: unit1.rel.tuition-tutorial
 type: semantic_relation
source_atom_ids:
  - unit1.lex.learning.tuition
  - unit1.lex.learning.tutorial
relation: semantic_distinction
distinction: Tuition refers to teaching/instruction or its cost; a tutorial is a small teaching session.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 7
```

### 7.12 mock exam vs actual exam

```yaml
id: unit1.rel.mock-exam-exam
 type: semantic_relation
source_atom_ids:
  - unit1.lex.learning.mock-exam
relation: semantic_distinction
distinction: A mock exam is a practice examination rather than the official examination.
source_section: Topic vocabulary — Learning
is_tested: true
test_evidence: Vocabulary exercise D, item 4
```

---

# 8. Extraction observations from this test file

1. **Topic vocabulary entries are not always one atom.** `discriminate`, for example, has more than one meaning listed in the source. A canonical extraction should probably split those senses.
2. **Word-formation entries are not necessarily lexical atoms themselves.** The word-family record is useful as source knowledge, but canonical data may eventually represent the individual derived forms as lexical atoms plus derivational relations.
3. **Phrases/patterns/collocations are the largest granularity problem.** The book groups many expressions under a headword. This test file temporarily uses `collocation_cluster` to avoid pretending that every combination has already been independently validated as an atom.
4. **`is_tested` is source coverage, not learner evidence.** `true` only means the book exercises test/practise that knowledge. It says nothing about whether the learner knows it.
5. **A distractor counts as tested here only when the exercise is explicitly designed to discriminate the item.** This is why some items in the learning vocabulary exercise are marked true even when they are distractors.
6. **Generated questions are not used as evidence of book coverage.** The Unit 1 exercise structure is the evidence for `is_tested`.
7. The grammar unit preceding this vocabulary unit is deliberately not included here because this file is the experimental extraction of **Thinking and Learning**.

## Source anchors

- The repository source map identifies `sources/Destination_C1-C2.pdf` as the canonical source and maps `unit-01` to the Present Time grammar section. fileciteturn94file0L2-L6
- The extracted source text contains the Thinking and Learning topic vocabulary, Learning vocabulary, phrasal verbs, phrases/patterns/collocations, idioms, and word-formation sections. fileciteturn7view0L663-L901
- The source text shows the vocabulary exercises and their tested items. fileciteturn7view0L908-L1036
- The source text shows the phrase/pattern, idiom, and word-formation exercises used to determine `is_tested`. fileciteturn7view0L1075-L1215
