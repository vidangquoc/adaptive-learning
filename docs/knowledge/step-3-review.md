# Step 3 Review — Knowledge Atom Taxonomy + Structure

> Working review document for Step 3. This file is intentionally separate from the canonical atom model documents. It records questions, objections, decisions, and unresolved points while Step 3 is being reviewed collaboratively.
>
> **Status: OPEN — Step 3 is not signed off.**
>
> Canonical references:
> - `docs/knowledge/overall.md` — conceptual model
> - `docs/knowledge/atom-structure.md` — common field structure and field semantics
> - `docs/knowledge/atom-types.md` — taxonomy
>
> This review document must not become a competing atom model. When a decision is finalized, the canonical documents above are updated; this file records the review history and unresolved questions.

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
Proposed rule (if needed)
        ↓
Decision
        ↓
Update canonical document(s)
```

Do not batch unresolved questions into a single automatic conclusion.

---

## 4. Major questions to examine

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

Status: **OPEN**

---

### 4.6. `morphological_form`

Questions:

- When is an inflected/irregular form independently useful enough to become an atom?
- How do we prevent ordinary inflections from producing huge numbers of atoms?
- How should irregular forms relate to the lexical atom?
- Is `morphological_form` sufficiently distinct from `word_formation`?

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

Status: **OPEN**

---

### 4.9. `examples`

Questions:

- What exactly is an example record?
- How is source-derived material distinguished from generated material?
- Is an example allowed to contain useful grammar/lexical knowledge beyond the current atom?
- How is example provenance represented?
- When does an example become an independent atom?

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

Status: **OPEN**

---

## 5. Issues discovered during initial review

### Issue 1 — Grammar constraint/rule boundary

Observation:

The taxonomy permits `rule` and `constraint` as grammar subtypes, while the common atom structure also contains `constraints` as a property.

This is not automatically contradictory, but the distinction needs an explicit rule if both are retained.

**Status: OPEN**

---

### Issue 2 — `multiword_expression` classification boundary

Observation:

`multiword_expression` is described as the fallback when an expression does not fit the more specific `phrasal_verb`, `idiom`, or `collocation` types. The model therefore needs a clear single-type classification rule.

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

## 7. Sign-off criteria

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
