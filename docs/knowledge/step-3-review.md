# Step 3 Review — Knowledge Atom Taxonomy + Structure

> Working review document for Step 3. This file is intentionally separate from the canonical atom model documents. It records questions, objections, **initial proposals**, decisions, and unresolved points while Step 3 is being reviewed collaboratively.
>
> **Status: OPEN — Step 3 is not signed off.**
>
> Canonical references:
> - `docs/knowledge/overall.md` — conceptual model
> - `docs/knowledge/atom-structure.md` — common field structure and field semantics
> - `docs/knowledge/atom-types.md` — taxonomy
>
> This review document must not become a competing atom model. When a decision is finalized, the canonical documents above are updated; this file records the review history and unresolved questions.
>
> **Important:** The proposals in this document are the assistant's starting proposals for discussion. They are **not decisions** and must not be treated as accepted merely because they are written here.

---

## 1. Review objective

Review Step 3 slowly and explicitly before marking it complete.

The review should establish that:

1. the conceptual atom model is coherent;
2. the common field structure is sufficient and unambiguous;
3. the taxonomy does not duplicate properties or relations;
4. atom boundaries are practical for extraction and assessment;
5. semantic IDs remain stable and meaningful;
6. candidate/official lifecycle state does not get confused with atom ontology;
7. the model can later be expressed in JSON Schema without introducing a second model.

**Important:** No item in this file is considered accepted merely because it is written here. Unresolved items remain unresolved until explicitly agreed.

---

## 2. Review status

| Area | Status | Notes |
|---|---|---|
| Conceptual atom model | OPEN | Review `overall.md` against practical extraction cases. |
| Common field structure | OPEN | Review every field, including null/empty semantics. |
| `domain` | OPEN | Confirm current scope and future-extension rule. |
| `type` | OPEN | Confirm vocabulary/grammar classification boundaries. |
| `subtype` | OPEN | Especially grammar subtype boundaries. |
| Vocabulary taxonomy | OPEN | Review overlap among MWE, phrasal verb, idiom, collocation, etc. |
| Grammar taxonomy | OPEN | Review form/meaning/use/pattern/rule/constraint/exception. |
| Atom vs property | OPEN | Test against difficult examples. |
| Atom vs relation | OPEN | Test semantic and derivational relationships. |
| `name` / `meaning` / `mother_says` / `explanation` | OPEN | Review semantic responsibilities and redundancy. |
| `structure` / `usage` / `constraints` | OPEN | Review boundaries and possible overlap. |
| `examples` | OPEN | Review evidence/provenance representation. |
| `related_atoms` | OPEN | Review relation semantics and validation. |
| `extra` metadata | OPEN | Review provenance/testing/notes boundary. |
| Semantic IDs | OPEN | Test naming and identity stability. |
| Candidate vs official | OPEN | Keep lifecycle state separate from ontology. |

---

## 3. Review method

We will work **one issue at a time**.

For each issue:

```text
Question / objection
        ↓
Concrete examples
        ↓
Boundary analysis
        ↓
Initial proposal
        ↓
Discussion / objection
        ↓
Decision
        ↓
Update canonical document(s)
```

Do not batch unresolved questions into a single automatic conclusion.

---

## 4. Major questions and initial proposals

### 4.1. What exactly makes something an atom?

Current principle to examine:

> Create an atom when the knowledge itself is independently meaningful and useful to teach, assess, track, or retrieve.

Questions:

- Is "independently meaningful" sufficient?
- Must an atom always be independently assessable?
- Can something be an atom because it is useful to retrieve even if it is not normally assessed alone?
- How should very small grammar facts be handled?
- How should broad grammar concepts be prevented from becoming oversized atoms?
- When does splitting improve learning granularity versus creating atom inflation?

**Initial proposal — not accepted:**

Use **independent learnability/diagnosability** as the practical boundary rather than requiring every atom to be independently testable. An item should normally become an atom when it represents a distinct piece of knowledge that can be meaningfully taught, retrieved, explained, or diagnosed on its own. Assessment independence is strong evidence but not an absolute requirement.

A useful anti-fragmentation test would be:

```text
If removing this piece would leave the parent atom's meaning intact,
and the piece has no useful independent learning identity,
keep it as a property.

If the piece has its own meaning/function, can be independently
recognized or diagnosed, and matters as a learning target,
consider making it an atom.
```

This should be tested against both tiny grammar facts and large grammar topics before acceptance.

Status: **OPEN**

---

### 4.2. Atom vs property

Test difficult cases such as:

- register;
- connotation;
- transitivity;
- separability;
- complementation;
- preposition patterns;
- lexical restrictions;
- fixedness;
- exceptions;
- semantic nuances.

Key question:

> When does a characteristic become independently meaningful knowledge rather than remaining a property of another atom?

**Initial proposal — not accepted:**

Treat a characteristic as a **property** by default when its meaning depends on an existing atom and its primary function is to describe how that atom behaves.

Promote it to an **atom** only when the characteristic itself becomes an independently meaningful and diagnosable learning target.

Examples for discussion:

```text
"assume is transitive"
→ normally a property of lex.assume

"assume + object + complement pattern"
→ normally structure/usage of lex.assume

"formal register"
→ normally a property of the lexical/grammatical atom

A separately taught contrast such as
"stative verbs behave differently from dynamic verbs"
→ potentially an independent grammar atom, depending on the
actual knowledge being represented.
```

The key distinction is **dependency on the parent atom**, not simply whether the information is important.

Status: **OPEN**

---

### 4.3. Grammar `rule` vs `constraint` vs `use`

Current taxonomy permits grammar subtypes:

```text
form
meaning
use
pattern
rule
constraint
exception
```

At the same time, the common structure contains:

```yaml
usage:
constraints:
```

Questions:

- When is a grammar rule an independent atom?
- When is a grammar constraint merely a property?
- Is `constraint` as a grammar subtype necessary?
- Can the same knowledge legitimately appear as both an atom and a property, and if so, under what conditions?
- Is `exception` an atom only when the exception itself is independently learnable?

**Initial proposal — not accepted:**

Keep `usage` and `constraints` as **properties by default**. A grammar `rule` or `constraint` subtype should represent a rule-like piece of knowledge only when the rule itself is an independent learning target.

For example:

```text
"Use the present continuous for an action happening now."
→ could be an independent grammar atom if treated as the actual
  learning target.

"The present continuous normally uses be + V-ing."
→ could be a form/pattern atom, depending on the chosen atom boundary.

"This construction cannot normally occur with X."
→ normally a constraint property of the construction.

"There is a special exception for X."
→ normally an exception property unless the exception itself is
  important enough to teach and diagnose independently.
```

**Potential simplification to investigate:** remove `constraint` from grammar subtypes if it cannot be cleanly distinguished from the common `constraints` property. Likewise, verify whether `rule` is genuinely needed as a type or whether rule knowledge can be represented through `meaning`, `structure`, `usage`, and `constraints` of a grammar atom.

This is a major review point and should not be silently resolved.

Status: **OPEN**

---

### 4.4. `multiword_expression` vs specific vocabulary types

Current vocabulary types include:

```text
lexical_sense
multiword_expression
phrasal_verb
idiom
collocation
word_formation
morphological_form
```

Questions:

- Is `multiword_expression` a fallback type rather than a parent type?
- Must each atom have exactly one vocabulary `type`?
- What happens when an expression appears to qualify as both a collocation and an idiom?
- What evidence determines the most specific applicable type?
- Is the current taxonomy too broad or too narrow for real source material?

**Initial proposal — not accepted:**

Treat `multiword_expression` as a **fallback type**, not as a parent type. Each atom should have one primary `type` for classification.

A proposed decision sequence:

```text
Is it a phrasal verb?
  yes → phrasal_verb

Else, is the expression idiomatic in the relevant sense?
  yes → idiom

Else, is it a conventional collocation?
  yes → collocation

Else, if it is an independently meaningful multiword lexical unit:
  → multiword_expression
```

However, some expressions may genuinely have multiple linguistic properties. Those properties should not force multiple competing `type` values into one atom. If necessary, secondary characteristics should be represented through relations/properties rather than by making the taxonomy multi-valued.

The exact precedence between categories still needs testing against real examples.

Status: **OPEN**

---

### 4.5. `word_formation`

Current model distinguishes formation knowledge from the lexical forms involved.

Example under review:

```text
assume
assumption
formation relationship
```

Questions:

- Should formation knowledge itself be an atom?
- When is the relationship sufficient without a separate formation atom?
- How should productive formation patterns differ from one-off derivational relationships?
- What belongs in the formation atom versus `related_atoms`?

**Initial proposal — not accepted:**

Distinguish **formation knowledge** from a mere relationship between two lexical atoms.

```text
assume ↔ assumption
→ related_atoms can express the derivational relationship.

"-tion forms nouns from certain verbs"
→ potentially an independent word-formation atom because the
  formation pattern itself is learnable and reusable.
```

Therefore:

- a one-off relationship may need only `related_atoms`;
- a reusable/productive formation pattern may justify a `word_formation` atom;
- the existence of a derivational relationship alone should not automatically create a formation atom.

This prevents every pair such as `decide → decision` from creating unnecessary extra atoms.

Status: **OPEN**

---

### 4.6. `morphological_form`

Questions:

- When is an inflected/irregular form independently useful enough to become an atom?
- How do we prevent ordinary inflections from producing huge numbers of atoms?
- How should irregular forms relate to the lexical atom?
- Is `morphological_form` sufficiently distinct from `word_formation`?

**Initial proposal — not accepted:**

Do **not** create a separate atom for every ordinary inflected form.

Use `morphological_form` only when the form is independently useful because it is explicitly taught, irregular, lexically significant, or otherwise diagnostically important.

Examples:

```text
walk → walked
→ normally not a separate atom merely because it is an inflection.

be → was/were
→ may justify explicit morphological-form knowledge because the
  forms are irregular and independently important to learning.
```

`word_formation` should concern creation/derivation of lexical items or productive formation patterns; `morphological_form` should concern grammatical/morphological variants of an existing lexical item.

Status: **OPEN**

---

### 4.7. `meaning` vs `mother_says` vs `explanation`

Current fields are:

```yaml
meaning:
mother_says:
explanation:
```

Questions:

- Is `meaning` the source-grounded semantic core?
- Is `mother_says` strictly learner-facing Vietnamese?
- Can `mother_says` ever add information not present in `meaning`?
- When should `mother_says` be `null`?
- Does `explanation` risk becoming a catch-all field?
- How do we preserve source grounding while allowing useful explanation?

**Initial proposal — not accepted:**

Give the three fields clearly different jobs:

```text
meaning
→ concise semantic/function statement of the knowledge itself.

mother_says
→ Vietnamese learner-facing rendering/explanation; optimized for
  intuitive understanding rather than source wording.

explanation
→ additional structured explanation needed to understand the
  knowledge, especially boundaries, rationale, or interpretation.
```

Possible rule: `mother_says` may simplify or clarify `meaning`, but should not silently introduce a new independent knowledge claim. If it does introduce a new claim, that claim should either be supported or represented separately.

`explanation` should not become a dumping ground. If a statement has independent learning identity, it should be evaluated under the atom/property boundary rather than simply hidden inside `explanation`.

Status: **OPEN**

---

### 4.8. `structure` vs `usage` vs `constraints`

Questions:

- What belongs in each field?
- Where should syntactic patterns go?
- Where should register go?
- Where should restrictions on variation go?
- Where should contrasts go?
- Should some of these characteristics ever become separate atoms?

**Initial proposal — not accepted:**

Use a three-way boundary:

```text
structure
→ how the knowledge is formed or organized.
  Examples: grammatical form, word pattern, argument structure,
  required components, ordering.

usage
→ when/how/where the knowledge is normally used.
  Examples: context, communicative function, register, discourse use.

constraints
→ what limits, blocks, conditions, or restricts valid use/form.
  Examples: lexical restrictions, incompatibilities, required
  conditions, prohibited combinations.
```

A practical test:

```text
How is it built?      → structure
When/how is it used?  → usage
What limits it?       → constraints
```

But this boundary should be tested against difficult grammar cases where a statement could plausibly fit more than one field.

Status: **OPEN**

---

### 4.9. `examples`

Questions:

- What exactly is an example record?
- How is source-derived material distinguished from generated material?
- Is an example allowed to contain useful grammar/lexical knowledge beyond the current atom?
- How is example provenance represented?
- When does an example become an independent atom?

**Initial proposal — not accepted:**

An example should remain an **example/evidence object**, not an atom, unless the example contains a distinct piece of independently useful knowledge that needs its own identity.

Source-derived examples should preserve provenance. Generated examples should be explicitly distinguishable from source evidence.

A sentence may illustrate several atoms, but that does not make the sentence itself an atom.

If a supposedly "example" sentence introduces another learning target, that target should be extracted and evaluated separately rather than being buried inside the example.

Status: **OPEN**

---

### 4.10. `related_atoms`

Current conceptual form:

```yaml
related_atoms:
  - id: lex.assume
    relation: contrasts_with
```

Questions:

- Which relations are canonical?
- Which relations are directional?
- Which relations are symmetric?
- Must every relation have source support?
- Can a relation be justified by the knowledge model rather than explicit source text?
- Should relation metadata live only here or in a separate relations data layer later?

**Initial proposal — not accepted:**

Keep relationships separate from atom type and atom content.

Each relation should eventually have:

```text
source atom
relation type
target atom
provenance/evidence where applicable
```

Relations such as `contrasts_with`, `synonym_of`, `near_synonym_of`, `derived_from`, or `related_to` should be treated according to explicit directionality rules.

Likely distinction:

```text
symmetric relation
A ↔ B

asymmetric relation
A → B
```

For example, `derived_from` is directional, while `contrasts_with` is naturally symmetric.

Initial architectural proposal: keep `related_atoms` convenient in the atom representation, while allowing the underlying data architecture to normalize relations into `data/knowledge/relations/` later. The canonical semantics should be defined once and reused by both representations.

Status: **OPEN**

---

### 4.11. Semantic IDs

Current pattern:

```text
<namespace>.<concept>.<case>
```

Current namespaces:

```text
lex
gram
```

Questions:

- What exactly counts as the semantic concept name?
- When is a case necessary?
- How do we name multiple senses of the same lexical item?
- How do we prevent IDs from becoming too dependent on English wording?
- What constitutes an identity change versus a rename?

**Initial proposal — not accepted:**

IDs should identify the **knowledge concept**, not its source location, page, exercise, extraction event, or learner state.

Use:

```text
lex.<concept>
gram.<concept>
```

Add a final case component only when two independently meaningful atoms would otherwise collide.

Examples:

```text
lex.compelling
lex.assume

gram.present-perfect-continuous.duration
gram.present-perfect-continuous.continuing-activity
gram.present-perfect-continuous.recently-stopped-activity
```

Do not encode arbitrary sequence numbers, source IDs, page numbers, or exercise numbers into semantic identity.

Identity should remain stable when the atom is encountered in another source. A wording improvement or explanation change should not automatically create a new ID; a change in the underlying knowledge identity may require one.

Sense splitting remains an important open issue and should be tested with polysemous vocabulary.

Status: **OPEN**

---

### 4.12. Candidate vs official atoms

Pipeline currently distinguishes:

```text
Evidence
  ↓
Candidate
  ↓
Validation / review
  ↓
Official
```

Questions:

- Is candidate/official a lifecycle state rather than an atom type?
- Should candidate and official records use exactly the same knowledge fields?
- Which proposal-specific fields must remain outside the canonical atom structure?
- How should candidate identity relate to eventual official atom identity?
- How do we preserve rejected/held proposals without contaminating official knowledge?

**Initial proposal — not accepted:**

Treat `candidate`, `official`, `rejected`, `held`, etc. as **lifecycle/review states**, never as ontology types.

The canonical atom model should describe the knowledge itself. Proposal-specific information should remain in the extraction/validation layer, such as:

```text
proposal ID
source span
source evidence
extraction confidence
warnings
validation status
review notes
```

A candidate may point toward a future official atom ID, but candidate state should not alter the meaning of the atom itself.

Rejected proposals should remain traceable as historical extraction decisions without entering official knowledge.

Status: **OPEN**

---

## 5. Issues discovered during initial review

### Issue 1 — Grammar constraint/rule boundary

Observation:

The taxonomy permits `rule` and `constraint` as grammar subtypes, while the common atom structure also contains `constraints` as a property.

This is not automatically contradictory, but the distinction needs an explicit rule if both are retained.

**Initial proposal:** First test whether grammar `constraint` is genuinely needed as a subtype. If most constraint knowledge is adequately represented as the `constraints` property of another atom, removing the subtype may simplify the ontology. Likewise, test whether `rule` is a true atom category or simply a characteristic of a grammar atom.

**Status: OPEN**

---

### Issue 2 — `multiword_expression` classification boundary

Observation:

`multiword_expression` is described as the fallback when an expression does not fit the more specific `phrasal_verb`, `idiom`, or `collocation` types. The model therefore needs a clear single-type classification rule.

**Initial proposal:** Keep one primary type per atom and use `multiword_expression` as the fallback category, subject to testing against ambiguous real expressions.

**Status: OPEN**

---

### Issue 3 — Pipeline terminology drift

The current `atom-pipeline.md` still contains a stale reference to `model.md` even though Step 0 establishes `overall.md` as the canonical conceptual model.

This is a **Step 5 cleanup issue**, not a reason to alter the Step 3 model itself.

**Status: DEFERRED TO STEP 5**

---

## 6. Decision log

Use this section only after an issue is explicitly discussed and agreed.

| ID | Decision | Affected canonical file(s) | Status |
|---|---|---|---|
| — | No Step 3 decision has been formally signed off yet. | — | OPEN |

---

## 7. Proposed review order

To avoid trying to solve the entire ontology at once, the assistant proposes this discussion order:

1. **Atom boundary** — what qualifies as an atom at all?
2. **Atom vs property vs relation** — establish the three-way boundary before refining taxonomy.
3. **Grammar taxonomy** — especially `rule` / `constraint` / `use` / `pattern` / `exception`.
4. **Vocabulary taxonomy** — especially MWE / phrasal verb / idiom / collocation.
5. **Word formation vs morphological form**.
6. **Field semantics** — `meaning`, `mother_says`, `explanation`, `structure`, `usage`, `constraints`.
7. **Examples and provenance**.
8. **Relations and `related_atoms`**.
9. **Semantic IDs**.
10. **Candidate vs official lifecycle**.

This ordering is only a working proposal; it is not a decision.

---

## 8. Sign-off criteria

Step 3 should only be marked complete when we explicitly agree that:

- the atom boundary is sufficiently clear for extraction;
- the taxonomy has no unresolved category overlap that would make extraction inconsistent;
- the common structure has clear field semantics;
- atom/property/relation boundaries are operationally usable;
- semantic IDs have stable rules;
- candidate/official lifecycle does not create a second ontology;
- difficult examples have been tested against the model;
- any resulting canonical-document changes have been made;
- no major unresolved Step 3 objection remains.

Only then should `WORK-IN-PROGRESS.md` Step 3 be marked `[x]`.
