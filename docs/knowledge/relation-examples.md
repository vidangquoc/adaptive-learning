# Grammar Relation Atom Examples

## Purpose

This document contains design examples for the \`relation\` Knowledge Atom type.

A \`relation\` atom represents **knowledge about a relationship between two or more independent Knowledge Atoms when that relationship itself is an independently learnable or testable target**.

It does not represent:
- a raw graph edge between atoms;
- the structural relationship between components inside one grammar atom;
- a property of one atom;
- a grammar rule that explains how one construction is formed.

The examples therefore keep only relationships that can reasonably be understood as learning targets involving independently represented grammar atoms.

For a Candidate Atom, \`relation_type\` may initially be \`null\`. In these examples, however, the AI has been asked to make a provisional semantic decision, so each example contains a concrete \`relation_type\`.

The values below are **working semantic labels, not a finalized controlled vocabulary**.

---

## Example 1 — Contrast between present simple and present continuous

The two constructions are independently meaningful grammar atoms. Their contrast is itself useful knowledge because learners need to distinguish the situations each construction normally presents.

\`\`\`yaml
id: grammar.relation.present_simple.present_continuous_contrast
domain: grammar
type: relation
relation_type: contrast

name: present simple vs present continuous
part_of_speech: null
pronunciation: null

meaning: The present simple and present continuous contrast in how they normally present present-time situations, especially habitual or general situations versus situations occurring around the present time.
mother_says: null
explanation: This relation describes a contrast between two independently represented grammar constructions. Knowing the contrast helps a learner choose between the constructions when both are possible in the same general time frame.
structure: present simple ↔ present continuous

examples:
  - "She works in Ho Chi Minh City." ↔ "She is working from home today."
  - "I usually drink coffee in the morning." ↔ "I am drinking tea right now."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Provisional relation_type: contrast."
\`\`\`

---

## Example 2 — Contrast between present perfect and simple past

The two tense atoms are independently represented. The relation captures a learner-relevant distinction in how they locate a past event relative to the present and a finished past time.

\`\`\`yaml
id: grammar.relation.present_perfect.simple_past_contrast
domain: grammar
type: relation
relation_type: contrast

name: present perfect vs simple past
part_of_speech: null
pronunciation: null

meaning: The present perfect and simple past contrast in how a past event is related to the present and to completed past-time periods.
mother_says: null
explanation: The relation is not a rule for forming either tense. It is knowledge that distinguishes two independently represented tense constructions and guides the choice between them.
structure: present perfect ↔ simple past

examples:
  - "I have seen that film." ↔ "I saw that film last night."
  - "She has lived here for five years." ↔ "She lived there from 2018 to 2022."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Provisional relation_type: contrast."
\`\`\`

---

## Example 3 — Compatibility between present perfect and since

The participants can be independent atoms: the present perfect construction and the grammatical use of \`since\`. The relation concerns a meaningful combination of the two, rather than the internal structure of either atom.

\`\`\`yaml
id: grammar.relation.present_perfect.since_compatibility
domain: grammar
type: relation
relation_type: compatibility

name: present perfect with since
part_of_speech: null
pronunciation: null

meaning: The present perfect can combine with since to relate a situation continuing to the present to the point when it began.
mother_says: null
explanation: This relation describes compatibility between two independently represented grammar atoms. It is not merely the rule that forms the present perfect or the usage of since in isolation.
structure: present perfect + since

examples:
  - "I have lived here since 2020."
  - "She has worked there since January."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Provisional relation_type: compatibility."
\`\`\`

---

## Example 4 — Compatibility between present perfect and for

The present perfect construction and the duration-related use of \`for\` can each be represented independently. Their compatibility is a separate learner-relevant fact.

\`\`\`yaml
id: grammar.relation.present_perfect.for_compatibility
domain: grammar
type: relation
relation_type: compatibility

name: present perfect with for
part_of_speech: null
pronunciation: null

meaning: The present perfect can combine with for to express a duration extending from a point in the past toward the present.
mother_says: null
explanation: The relation connects two independently represented grammar atoms: the present perfect construction and the relevant duration use of for.
structure: present perfect + for + duration

examples:
  - "I have lived here for five years."
  - "They have worked together for a long time."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Provisional relation_type: compatibility."
\`\`\`

---

## Example 5 — Contrast between active and passive constructions

Active and passive constructions are independently meaningful grammar atoms. The relation captures the contrast in how the grammatical subject is associated with the event.

\`\`\`yaml
id: grammar.relation.active.passive_contrast
domain: grammar
type: relation
relation_type: contrast

name: active vs passive
part_of_speech: null
pronunciation: null

meaning: Active and passive constructions contrast in how the grammatical subject is related to the event, with the active construction typically presenting the doer as subject and the passive construction typically presenting the affected entity as subject.
mother_says: null
explanation: This is a contrast between two independently represented constructions. It is not a description of the internal formation rule of the passive construction.
structure: active ↔ passive

examples:
  - "The company built the bridge." ↔ "The bridge was built by the company."
  - "Someone stole my bike." ↔ "My bike was stolen."

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Provisional relation_type: contrast."
\`\`\`

---

## Example 6 — Compatibility between a grammar construction and a separately represented marker

A grammar relation can connect a construction with another independently represented grammar atom when the source teaches their combination as a reusable learning target.

\`\`\`yaml
id: grammar.relation.present_perfect.ever_compatibility
domain: grammar
type: relation
relation_type: compatibility

name: present perfect with ever
part_of_speech: null
pronunciation: null

meaning: The present perfect can combine with ever in questions about whether an experience has occurred at any time up to the present.
mother_says: null
explanation: The relation represents the combination of two independently learnable grammar atoms: the present perfect construction and the relevant interrogative use of ever.
structure: present perfect + ever

examples:
  - "Have you ever visited Japan?"
  - "Has she ever tried sushi?"

extra:
  source:
    origin: []
    atom_decision: []
  is_tested: false
  test_evidence: []
  notes: "Provisional relation_type: compatibility."
\`\`\`

---

## What is deliberately excluded

### Grammar components inside one construction

Examples such as:
- modal verb → bare infinitive;
- subject ↔ finite verb;
- auxiliary → subject;
- comparative form + than;
- constituent + and + constituent.

These describe how components participate in the structure or formation of a grammar construction. Under the current ontology, they belong in a \`rule\` atom rather than a \`relation\` atom.

### Properties of one atom

Information about when a particular tense is normally used belongs to that tense atom, typically as \`usage\`. It does not become a relation merely because the usage mentions another concept.

### Raw Atom-to-Atom edges

A statement such as:

\`\`\`text
present perfect → since
\`\`\`

is not persisted as graph metadata merely because the two atoms are related.

If the **knowledge that they are compatible in a particular way** is itself independently taught or tested, that knowledge can be represented as a \`relation\` atom, as in Example 3.

---

## Working relation_type vocabulary

The examples suggest two currently useful semantic categories:

- \`contrast\` — the learning target distinguishes two or more independent atoms by a meaningful difference;
- \`compatibility\` — the learning target states that two or more independent atoms can combine in a particular meaningful way.

This is intentionally a **minimal working vocabulary**, not a final enum.

A new \`relation_type\` should be introduced only when real source-grounded atom candidates require a semantic distinction that cannot be represented clearly by an existing value.

The AI may assign \`relation_type\` when creating a Candidate Atom, based on the actual knowledge represented by the candidate and its source evidence. Human review can later accept, refine, or reject that decision.

---

## Design rule

\`\`\`text
one independent learning target
        ↓
one ordinary atom type

knowledge about a relationship between
two or more independent atoms
        ↓
relation atom

structural relationship between components
inside one grammar construction
        ↓
rule atom
\`\`\`

The central test is:

> **Are the participants independently represented Knowledge Atoms, and is the relationship itself an independently learnable or testable target?**

If either condition is not satisfied, the knowledge should normally be represented by another atom type rather than \`relation\`.
