# Unit 1 — Test Knowledge Atoms

> **Working extraction, not canonical schema.**
>
> This file is a fresh test extraction of **Destination C1 & C2 — Unit 1: Grammar — Present time**. The previous version was wrong: it contained the vocabulary material *Thinking and learning*, which is canonical Unit 2.

## Extraction rules

- Scope: knowledge taught in Unit 1: Present simple, Present continuous, Present perfect simple, Present perfect continuous, and stative/non-stative verb behaviour.
- One atom = one independently diagnosable grammar rule, use, construction, or contrast.
- Every atom has exactly the same fields.
- Every atom has `is_tested`.
- `is_tested: true` means direct evidence exists in a Unit 1 exercise; appearance in the presentation alone is not enough.
- `is_tested: false` means no direct exercise evidence has been confirmed yet.
- This is deliberately a **test extraction**, not the final repository schema.

## Common fields

`id`, `type`, `name`, `form`, `meaning_or_function`, `conditions`, `contrast_or_boundary`, `examples`, `source_section`, `is_tested`, `test_evidence`, `notes`

---

# 1. Present simple

## 1.1 General truths
```yaml
id: unit1.grammar.present-simple.general-truths
type: grammar_usage
name: Present simple for general truths
form: present simple
meaning_or_function: State facts or principles regarded as generally true.
conditions: The statement is general rather than a temporary event happening now.
contrast_or_boundary: Present continuous normally describes an activity in progress or a temporary situation.
examples: [Water boils at 100°C.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, item 5
notes: Tested through tense selection.
```

## 1.2 Current habits and repeated actions
```yaml
id: unit1.grammar.present-simple.current-habits
type: grammar_usage
name: Present simple for current habits and repeated actions
form: present simple
meaning_or_function: Describe habits or actions that happen regularly in the present.
conditions: The event is habitual/repeated rather than a single temporary event.
contrast_or_boundary: Present continuous can describe a temporary/current activity.
examples: [I often order things online.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, items 10 and 12; Exercise B
notes: Frequency expressions commonly accompany this use.
```

## 1.3 Permanent situations and states
```yaml
id: unit1.grammar.present-simple.permanent-states
type: grammar_usage
name: Present simple for permanent situations and states
form: present simple
meaning_or_function: Describe relatively permanent situations, states, jobs, relationships, or characteristics.
conditions: The situation is viewed as stable rather than temporary.
contrast_or_boundary: Temporary situations favour present continuous.
examples: [Angie teaches French at a local centre.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, items 1 and 16; Exercise C
notes: Permanent is a viewpoint, not necessarily literally forever.
```

## 1.4 Informal storytelling
```yaml
id: unit1.grammar.present-simple.informal-storytelling
type: grammar_usage
name: Present simple for jokes and informal stories
form: present simple
meaning_or_function: Narrate events in a vivid immediate style when telling jokes or informal stories.
conditions: Past-like narrative events are presented as if happening now.
contrast_or_boundary: This is a narrative convention, not ordinary description of a current event.
examples: [A man goes into a bar and asks for a drink.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, item 8
notes: Interacts with the present-continuous background-story atom.
```

## 1.5 Live sports commentary
```yaml
id: unit1.grammar.present-simple.live-commentary
type: grammar_usage
name: Present simple for live sports commentary
form: present simple
meaning_or_function: Report rapid events in live sports commentary.
conditions: Events are presented as they happen in a conventional commentary style.
contrast_or_boundary: This is a special discourse convention; ordinary actions happening now commonly use present continuous.
examples: [Beckham passes and scores.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, item 11
notes: Distinct discourse use.
```

## 1.6 Newspaper headlines
```yaml
id: unit1.grammar.present-simple.headlines
type: grammar_usage
name: Present simple in newspaper headlines
form: present simple
meaning_or_function: Present recent events in compressed headline style.
conditions: The language functions as a headline.
contrast_or_boundary: Headline grammar differs from ordinary full-sentence narrative.
examples: [WOMAN WINS MAJOR LOTTERY PRIZE]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, item 12
notes: Treat as a discourse-specific atom.
```

## 1.7 Reviews and summaries
```yaml
id: unit1.grammar.present-simple.reviews-summaries
type: grammar_usage
name: Present simple for reviews and summaries
form: present simple
meaning_or_function: Describe the plot, content, or progression of a work.
conditions: The speaker summarises content rather than narrating a current event.
contrast_or_boundary: The work may be completed, but present tense is conventional for summaries.
examples: [The film ends with the characters leaving the city.]
source_section: Unit 1 Grammar — Present simple
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Explicitly presented but not isolated in a confirmed exercise.
```

## 1.8 Instructions and directions
```yaml
id: unit1.grammar.present-simple.instructions-directions
type: grammar_usage
name: Present simple for instructions and directions
form: present simple
meaning_or_function: Give procedural instructions or describe a route.
conditions: The listener is told what to do or what happens at each step.
contrast_or_boundary: Procedural use differs from a habitual-action interpretation.
examples: [You turn left at the end of the road.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, item 4
notes: Exercise A uses a direction context.
```

## 1.9 Proverbs and sayings
```yaml
id: unit1.grammar.present-simple.proverbs-sayings
type: grammar_usage
name: Present simple in proverbs and sayings
form: present simple
meaning_or_function: State general principles in conventional sayings.
conditions: The sentence expresses a generalised principle.
contrast_or_boundary: Related to general truths but has a conventional proverb/saying discourse function.
examples: [Too many cooks spoil the broth.]
source_section: Unit 1 Grammar — Present simple
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Explicitly presented as a separate use.
```

## 1.10 Fixed future events
```yaml
id: unit1.grammar.present-simple.fixed-future
type: grammar_usage
name: Present simple for fixed future events
form: present simple
meaning_or_function: Refer to future events fixed by a timetable, schedule, or official programme.
conditions: The future event is externally fixed.
contrast_or_boundary: Distinguish from personal future arrangements expressed with present continuous.
examples: [The term ends on 21 December.]
source_section: Unit 1 Grammar — Present simple
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Unit 1 points to Unit 5 for fuller future treatment.
```

## 1.11 Future time clauses
```yaml
id: unit1.grammar.present-simple.future-time-clause
type: grammar_usage
name: Present simple in future time clauses
form: present simple in a subordinate time clause
meaning_or_function: Refer to a future event in a time clause while the main clause expresses the future.
conditions: Common after when, until, before, after, once, as soon as, and similar time conjunctions.
contrast_or_boundary: Do not normally use will merely because the event is future.
examples: [I’ll relax when I finish this crossword.]
source_section: Unit 1 Grammar — Present simple
is_tested: true
test_evidence: Exercise A, item 4; Exercise B, item 13
notes: Further future-time treatment is in Unit 5.
```

## 1.12 Emphatic do/does for contrast
```yaml
id: unit1.grammar.present-simple.emphatic-contrast
type: grammar_usage
name: Emphatic do/does for contrast
form: do/does + base verb
meaning_or_function: Emphasise a present-simple statement to correct or contrast information.
conditions: The speaker wants corrective or contrastive emphasis.
contrast_or_boundary: The auxiliary is emphatic rather than required for ordinary affirmative present simple.
examples: [He does know quite a lot about psychology.]
source_section: Unit 1 Grammar — Present simple
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Explicitly presented in the grammar table.
```

## 1.13 Emphatic do/does for strong feeling
```yaml
id: unit1.grammar.present-simple.emphatic-feeling
type: grammar_usage
name: Emphatic do/does for strong feeling
form: do/does + base verb
meaning_or_function: Strongly emphasise a genuine feeling, preference, or action.
conditions: The speaker wants emotional or corrective emphasis.
contrast_or_boundary: Ordinary affirmative present simple does not require do/does.
examples: [I do like playing word games!]
source_section: Unit 1 Grammar — Present simple
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Explicitly presented in the grammar table.
```

---

# 2. Present continuous

## 2.1 Happening now
```yaml
id: unit1.grammar.present-continuous.now
type: grammar_usage
name: Present continuous for an action happening now
form: am/is/are + -ing
meaning_or_function: Describe an action in progress at the moment of speaking.
conditions: The event is currently unfolding.
contrast_or_boundary: Present simple normally describes habits, general truths, or states.
examples: [The boys are doing their homework right now.]
source_section: Unit 1 Grammar — Present continuous
is_tested: true
test_evidence: Exercise A, items 2, 6 and 9; Exercise C
notes: Heavily tested in present-simple vs continuous exercises.
```

## 2.2 Around now
```yaml
id: unit1.grammar.present-continuous.around-now
type: grammar_usage
name: Present continuous for situations around now
form: am/is/are + -ing
meaning_or_function: Describe an activity or situation occurring during the current period, not necessarily this exact second.
conditions: The situation is temporary/current in the broader present period.
contrast_or_boundary: It need not be happening at the instant of speaking.
examples: [What book are you doing in English at the moment?]
source_section: Unit 1 Grammar — Present continuous
is_tested: true
test_evidence: Exercise C
notes: Current-period interpretation is central to Exercise C.
```

## 2.3 Temporary situations and series of actions
```yaml
id: unit1.grammar.present-continuous.temporary-series
type: grammar_usage
name: Present continuous for temporary situations and series of actions
form: am/is/are + -ing
meaning_or_function: Describe temporary circumstances or a series of activities during a limited period.
conditions: The situation is temporary rather than a stable characteristic.
contrast_or_boundary: Present simple is preferred when the situation is viewed as permanent or habitual.
examples: [We aren’t having exams while the lecturers are on strike.]
source_section: Unit 1 Grammar — Present continuous
is_tested: true
test_evidence: Exercise A, item 1; Exercise C
notes: Temporary is contextual, not simply synonymous with short.
```

## 2.4 Changing and developing situations
```yaml
id: unit1.grammar.present-continuous.change-development
type: grammar_usage
name: Present continuous for changing or developing situations
form: am/is/are + -ing
meaning_or_function: Describe a situation that is currently changing, increasing, decreasing, or developing.
conditions: The situation is viewed as being in transition.
contrast_or_boundary: Present simple presents the state as stable or general.
examples: [More people are recognising the advantages of learning languages.]
source_section: Unit 1 Grammar — Present continuous
is_tested: true
test_evidence: Exercise A, item 6
notes: Explicitly represented in the source presentation.
```

## 2.5 Annoying or amusing habits
```yaml
id: unit1.grammar.present-continuous.repeated-habits
type: grammar_usage
name: Present continuous with always for annoying or amusing habits
form: am/is/are + always + -ing
meaning_or_function: Emphasise repeated behaviour with an attitude such as annoyance, criticism, or amusement.
conditions: The repetition is emotionally evaluated by the speaker.
contrast_or_boundary: Neutral habitual repetition normally uses present simple.
examples: [Dan is always coming up with crazy ideas.]
source_section: Unit 1 Grammar — Present continuous
is_tested: true
test_evidence: Exercise A, item 14
notes: The attitude is part of the knowledge atom.
```

## 2.6 Background action in informal stories
```yaml
id: unit1.grammar.present-continuous.story-background
type: grammar_usage
name: Present continuous for background information in informal stories
form: am/is/are + -ing
meaning_or_function: Provide an ongoing background action while the main story is narrated in present forms.
conditions: The action forms the background/context for another event.
contrast_or_boundary: Present simple may carry the main narrative sequence while continuous supplies background activity.
examples: [A man goes to see his psychiatrist. He is carrying a bag.]
source_section: Unit 1 Grammar — Present continuous
is_tested: true
test_evidence: Exercise A, item 8
notes: Interacts with present-simple informal storytelling.
```

## 2.7 Future arrangements
```yaml
id: unit1.grammar.present-continuous.future-arrangements
type: grammar_usage
name: Present continuous for future arrangements
form: am/is/are + -ing
meaning_or_function: Refer to a planned future event understood as an arrangement.
conditions: The event has been arranged rather than being merely a prediction.
contrast_or_boundary: Distinguish from fixed timetable events expressed with present simple.
examples: [I’m taking my driving test next week.]
source_section: Unit 1 Grammar — Present continuous
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Unit 1 refers to Unit 5 for fuller future treatment.
```

## 2.8 Present continuous in future time clauses
```yaml
id: unit1.grammar.present-continuous.future-time-clause
type: grammar_usage
name: Present continuous in future time clauses
form: am/is/are + -ing in a future time clause
meaning_or_function: Describe an action that will be in progress at a future reference point.
conditions: The subordinate clause refers to an ongoing future activity.
contrast_or_boundary: Continuous highlights ongoing activity; simple present can describe a future event as a fact/completion.
examples: [I’ll be nervous when I’m waiting outside the exam room.]
source_section: Unit 1 Grammar — Present continuous
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Further future-time treatment is deferred to Unit 5.
```

---

# 3. Present perfect simple

## 3.1 Past-to-present states and situations
```yaml
id: unit1.grammar.present-perfect-simple.past-to-present
type: grammar_usage
name: Present perfect simple for situations continuing from the past to now
form: have/has + past participle
meaning_or_function: Connect a past starting point with a situation or state still true now.
conditions: The state/situation began in the past and remains relevant or true.
contrast_or_boundary: Past simple normally places the situation in a completed past time frame.
examples: [I’ve been a member of the organisation for five years.]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise F, items 1, 3, 4 and 8; Exercise I, items 3, 8, 13 and 15
notes: Since and for are frequent signals, not the rule itself.
```

## 3.2 Series of actions continuing up to now
```yaml
id: unit1.grammar.present-perfect-simple.series-up-to-now
type: grammar_usage
name: Present perfect simple for a series of actions up to now
form: have/has + past participle
meaning_or_function: Describe completed actions within a period that continues to the present.
conditions: The period is still open and the completed events form a series or count.
contrast_or_boundary: Continuous can instead foreground the ongoing activity or duration.
examples: [She’s completed several qualifications so far.]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise G, item 1; Exercise H, item 1; Exercise I, items 5 and 6
notes: The presentation explicitly associates simple perfect with counts.
```

## 3.3 Completed action at an unspecified or irrelevant past time
```yaml
id: unit1.grammar.present-perfect-simple.unspecified-past-time
type: grammar_usage
name: Present perfect simple for completed past actions with no relevant specific time
form: have/has + past participle
meaning_or_function: Refer to a completed past action when its exact time is unspecified or unimportant to the current statement.
conditions: Present relevance matters more than a finished past-time frame.
contrast_or_boundary: A definite finished-time expression normally calls for past simple.
examples: [Have you ever read any books by that author?]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise G, items 2–4; Exercise H, item 2
notes: Ever, before, and first-time contexts are important evidence.
```

## 3.4 Present result of a completed action
```yaml
id: unit1.grammar.present-perfect-simple.present-result
type: grammar_usage
name: Present perfect simple for a completed action with a present result
form: have/has + past participle
meaning_or_function: Describe a completed event whose consequence is relevant now.
conditions: The current result matters more than the event's exact past time.
contrast_or_boundary: Past simple can narrate the event when the present result is not foregrounded.
examples: [She’s been awarded a scholarship and can now study abroad.]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise H, items 4–7; Exercise I, items 1, 7 and 14
notes: Just, already, and yet frequently occur in these contexts.
```

## 3.5 Recently completed actions
```yaml
id: unit1.grammar.present-perfect-simple.recent-actions
type: grammar_usage
name: Present perfect simple for recently completed actions
form: have/has + past participle
meaning_or_function: Refer to an action completed very recently with present relevance.
conditions: Completion is recent and the current consequence is salient.
contrast_or_boundary: Exact completed past time is not the focus.
examples: [I’ve just received my results.]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise H, item 4; Exercise I, items 1, 7 and 16
notes: Just is a common signal, not a mechanical requirement.
```

## 3.6 Present perfect simple in future time clauses
```yaml
id: unit1.grammar.present-perfect-simple.future-time-clause
type: grammar_usage
name: Present perfect simple in future time clauses
form: have/has + past participle in a time clause
meaning_or_function: Refer to an action that must be completed before a future event/reference point.
conditions: Completion precedes a future event introduced by a time conjunction.
contrast_or_boundary: Do not use will merely because the completion is future.
examples: [Tell me when you’ve finished the report.]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise I, items 4, 11 and 17; Exercise J
notes: Further future-time treatment is in Unit 5.
```

## 3.7 Present perfect simple with since/for
```yaml
id: unit1.grammar.present-perfect-simple.since-for
type: grammar_usage
name: Present perfect simple with since/for for a continuing state or situation
form: have/has + past participle + since/for phrase
meaning_or_function: Express how long a continuing state or situation has lasted.
conditions: The state/situation extends from a past point or period up to now.
contrast_or_boundary: With dynamic actions, continuous may better foreground duration/process.
examples: [We’ve lived here for five years.]
source_section: Unit 1 Grammar — Present perfect simple
is_tested: true
test_evidence: Exercise F, items 1 and 8; Exercise I, items 3, 8, 13 and 15
notes: Since identifies a starting point; for identifies a duration.
```

## 3.8 Present perfect simple for count
```yaml
id: unit1.grammar.present-perfect-simple.count
type: grammar_usage
name: Present perfect simple for a particular number of times or things
form: have/has + past participle
meaning_or_function: Specify how many times an event has occurred or how many things have been completed in an open period.
conditions: Quantity/count is the information focus.
contrast_or_boundary: Continuous does not normally foreground a discrete count of completed events.
examples: [I’ve written two essays this week.]
source_section: Unit 1 Grammar — Present perfect simple vs continuous
is_tested: true
test_evidence: Exercise G, item 1; Exercise H, item 1
notes: Explicit rule in the presentation.
```

---

# 4. Present perfect continuous

## 4.1 Continuing action up to now
```yaml
id: unit1.grammar.present-perfect-continuous.continuing-action
type: grammar_usage
name: Present perfect continuous for an action continuing up to now
form: have/has been + -ing
meaning_or_function: Describe an activity that began before now and has continued to the present.
conditions: The activity/process itself is the focus.
contrast_or_boundary: Simple perfect more readily foregrounds completed result, count, or state.
examples: [We’ve been waiting for two hours.]
source_section: Unit 1 Grammar — Present perfect continuous
is_tested: true
test_evidence: Exercise G, items 2 and 5–8; Exercise H, items 3, 5–7
notes: Duration/process is central.
```

## 4.2 Recent ongoing activity with present relevance
```yaml
id: unit1.grammar.present-perfect-continuous.recent-activity
type: grammar_usage
name: Present perfect continuous for activity continuing until just before now
form: have/has been + -ing
meaning_or_function: Highlight recent activity whose process or evidence is relevant now.
conditions: The activity may have just stopped but has present relevance.
contrast_or_boundary: Simple perfect may foreground the completed result.
examples: [I’ve been working all morning, so I’m tired.]
source_section: Unit 1 Grammar — Present perfect continuous
is_tested: true
test_evidence: Exercise G, items 6 and 7; Exercise H
notes: The presentation explicitly includes activity continuing “or just before” the present.
```

## 4.3 Present perfect continuous in future time clauses
```yaml
id: unit1.grammar.present-perfect-continuous.future-time-clause
type: grammar_usage
name: Present perfect continuous in future time clauses
form: have/has been + -ing in a time clause
meaning_or_function: Describe an activity that will have been continuing for a period before a future event.
conditions: A future reference point is preceded by an ongoing activity whose duration matters.
contrast_or_boundary: Simple perfect foregrounds completion; continuous foregrounds duration/process.
examples: [I won’t take the test until I’ve been having lessons for two months.]
source_section: Unit 1 Grammar — Present perfect continuous
is_tested: false
test_evidence: No direct Unit 1 exercise item confirmed.
notes: Explicitly presented; fuller future treatment is in Unit 5.
```

## 4.4 Duration emphasis
```yaml
id: unit1.grammar.present-perfect-continuous.duration
type: grammar_usage
name: Present perfect continuous to emphasise duration
form: have/has been + -ing + since/for
meaning_or_function: Emphasise how long an action or situation has been continuing.
conditions: Duration/process is more salient than completed result or count.
contrast_or_boundary: Simple perfect can state the same duration more neutrally, especially with stative verbs.
examples: [I’ve been working here for five years.]
source_section: Unit 1 Grammar — Present perfect simple vs continuous
is_tested: true
test_evidence: Exercise G, items 5–8; Exercise H, items 3, 5–7
notes: Explicitly contrasted with simple perfect in the presentation.
```

## 4.5 Simple vs continuous: count/result vs duration/process
```yaml
id: unit1.grammar.present-perfect.simple-vs-continuous
type: grammar_usage
name: Choosing simple or continuous perfect by information focus
form: have/has + past participle vs have/has been + -ing
meaning_or_function: Choose simple perfect when count/completion/result is foregrounded and continuous when duration/process is foregrounded.
conditions: Both forms may describe related situations but highlight different aspects.
contrast_or_boundary: This is a meaning/focus distinction, not merely a time-expression rule.
examples: [I’ve written three essays this week.; I’ve been writing essays all morning.]
source_section: Unit 1 Grammar — Present perfect simple vs continuous
is_tested: true
test_evidence: Exercise G, items 1–8; Exercise H, items 1–7
notes: High-value contrast atom.
```

---

# 5. Stative and non-stative verbs

## 5.1 General stative rule
```yaml
id: unit1.grammar.stative.general
type: grammar_usage
name: Stative verbs generally use simple forms
form: simple tense for state meaning
meaning_or_function: Describe states such as knowledge, belief, possession, emotion, perception, or relationships with simple forms.
conditions: The verb is used for a state rather than a dynamic activity.
contrast_or_boundary: Selected verbs can take continuous forms when their meaning becomes dynamic.
examples: [I understand the problem.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise D, items 1–15; Exercise E
notes: The source groups stative verbs by semantic category.
```

## 5.2 Think: believe vs consider
```yaml
id: unit1.grammar.stative.think
type: grammar_usage
name: Think as belief versus active consideration
form: think vs am/is/are thinking
meaning_or_function: Simple think expresses belief; continuous think expresses an active process of considering.
conditions: Tense follows the intended lexical meaning.
contrast_or_boundary: “I think” = believe/state; “I’m thinking about” = consider/process.
examples: [I think it is important.; I’m thinking about taking a course.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise C, item 14; Exercise E, items 2, 3, 9 and 10
notes: Major semantic tense contrast.
```

## 5.3 Have: possession vs activity
```yaml
id: unit1.grammar.stative.have
type: grammar_usage
name: Have as possession/state versus activity
form: have vs am/is/are having
meaning_or_function: Simple have describes possession/stable relations; continuous have can describe an activity or experience.
conditions: Meaning determines stative versus dynamic use.
contrast_or_boundary: Possessive have normally does not take continuous form.
examples: [Do the Deacons have a swimming pool?; We’re having a barbecue.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise E, item 4
notes: Explicit paired contrast.
```

## 5.4 See: perception vs dynamic activity
```yaml
id: unit1.grammar.stative.see
type: grammar_usage
name: See as perception/state versus dynamic activity
form: see vs am/is/are seeing
meaning_or_function: Simple see expresses perception/knowledge; continuous see can express a planned or ongoing meeting/activity.
conditions: The intended meaning is either involuntary perception/state or a dynamic event.
contrast_or_boundary: Not every use of see is stative.
examples: [I see what you mean.; I’m seeing a client this afternoon.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise E, item 10
notes: Dynamic sense depends on context.
```

## 5.5 Feel: state vs current condition
```yaml
id: unit1.grammar.stative.feel
type: grammar_usage
name: Feel as state versus current condition
form: feel vs am/is/are feeling
meaning_or_function: Choose simple or continuous according to whether feeling is a state or a current temporary experience.
conditions: Context determines the interpretation.
contrast_or_boundary: Continuous can foreground a temporary/current condition.
examples: [I feel fine.; I’m feeling better today.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise E, item 2
notes: Feel is explicitly listed as capable of both uses.
```

## 5.6 Look: appearance vs deliberate activity
```yaml
id: unit1.grammar.stative.look
type: grammar_usage
name: Look as appearance versus deliberate activity
form: look vs am/is/are looking
meaning_or_function: Simple look can describe appearance; continuous look can describe directing the eyes or searching.
conditions: Meaning determines tense choice.
contrast_or_boundary: Appearance/state differs from dynamic activity.
examples: [He looks tired.; I’m looking for a book.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise E, item 1
notes: Explicit paired contrast.
```

## 5.7 Smell: quality/state vs active perception
```yaml
id: unit1.grammar.stative.smell
type: grammar_usage
name: Smell as quality/state versus active perception
form: smell vs am/is/are smelling
meaning_or_function: Simple smell describes an inherent quality; continuous smell describes the active act of smelling.
conditions: The sentence describes either a property or a deliberate sensory action.
contrast_or_boundary: State and action meanings license different forms.
examples: [The chicken smells fresh.; Why are you smelling the chicken?]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise E, item 5
notes: Explicit paired contrast.
```

## 5.8 Depend: state vs dynamic use
```yaml
id: unit1.grammar.stative.depend
type: grammar_usage
name: Depend as stative relation versus dynamic use
form: depend vs am/is/are depending
meaning_or_function: The normal state meaning expresses a relation; dynamic use is possible when dependence is viewed as an unfolding/current process.
conditions: Tense follows the intended meaning/context.
contrast_or_boundary: The unit explicitly includes depend among verbs capable of state/action interpretations.
examples: [It depends on the weather.]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise E, item 7
notes: Keep as an atom because the unit explicitly tests the distinction.
```

## 5.9 Stative semantic categories
```yaml
id: unit1.grammar.stative.semantic-categories
type: grammar_usage
name: Semantic categories of stative verbs
form: simple tense preferred for state meaning
meaning_or_function: Recognise stative behaviour across communication, thinking, existence, emotion, perception, possession/relationships, and other states.
conditions: The verb is used with its stative meaning.
contrast_or_boundary: Selected verbs can become continuous when their meaning changes to an activity/process.
examples: [know, believe, own, belong, need, understand]
source_section: Unit 1 Grammar — Stative and non-stative uses
is_tested: true
test_evidence: Exercise D, items 1–15
notes: Category-level atom; specific high-value lexical contrasts are separate atoms.
```

---

# 6. Cross-form distinctions

## 6.1 Present simple vs present continuous
```yaml
id: unit1.grammar.contrast.simple-vs-continuous
type: grammar_usage
name: Present simple vs present continuous for stable/habitual versus temporary/current situations
form: present simple vs am/is/are + -ing
meaning_or_function: Choose according to whether the situation is general, habitual, or stable versus temporary, current, or in progress.
conditions: Interpret the speaker’s viewpoint and time span, not only an adverb.
contrast_or_boundary: Special discourse uses and stative meanings can override the basic contrast.
examples: [I usually work from home.; I’m working from home this week.]
source_section: Unit 1 Grammar — Present simple and Present continuous
is_tested: true
test_evidence: Exercises A–E
notes: High-level diagnostic atom linking many individual uses.
```

## 6.2 Time expressions as cues, not automatic rules
```yaml
id: unit1.grammar.time-expressions.contextual
type: grammar_usage
name: Time expressions must be interpreted with context
form: tense selected from meaning and context
meaning_or_function: Use expressions such as now, usually, since, for, already, yet, ever, and so far as contextual evidence rather than automatic tense commands.
conditions: The same expression can occur in different constructions depending on meaning.
contrast_or_boundary: Avoid one-adverb-equals-one-tense rules.
examples: [For five years can occur with simple or continuous perfect depending on focus.]
source_section: Unit 1 Grammar — Words and phrases used with present forms
is_tested: true
test_evidence: Exercise B; Exercise I
notes: Useful meta-grammar atom for diagnostics.
```

---

# 7. Coverage summary

The canonical Unit 1 order is **Present simple → Present continuous → Present perfect simple → Present perfect continuous → Stative and non-stative uses**, followed by exercises A–J.

Exercise coverage used for `is_tested`:

- **A–E:** present simple/continuous and stative/non-stative distinctions.
- **F:** present perfect simple construction.
- **G:** present perfect simple vs continuous choice.
- **H:** productive present-perfect formation.
- **I:** present-perfect time expressions.
- **J:** integrated present-time grammar.

The source presentation explicitly lists the individual present-simple and present-continuous uses, the present-perfect meanings, the simple-vs-continuous focus distinction, and stative/non-stative behaviour. citeturn1view0turn2view0

## Boundary

This file contains **only canonical Unit 1 grammar atoms**. *Thinking and learning* is canonical **Unit 2 Vocabulary** and must be extracted separately.
