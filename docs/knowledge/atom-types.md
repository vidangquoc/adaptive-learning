# Knowledge Atom Types for Destination C1-C2

## Purpose

This document defines the knowledge types to be extracted from **Destination C1-C2**. It is intentionally limited to knowledge contained in the book itself.

It does **not** define learner skills, learner state, assessment types, mastery, review state, learning strategies, or other learner-side concepts.

The goal is to provide a controlled taxonomy for extracting book evidence into the Adaptive Learning knowledge base without turning every observable feature into a separate atom.

---

## 1. Lexical Knowledge

### 1.1. Lexical sense

A specific meaning of a lexical item.

Examples:

- `assess` → evaluate or estimate something
- `assume` → accept something as true without sufficient evidence
- `infer` → reach a conclusion from evidence

One independently meaningful sense should normally be one atom.

If the book teaches distinct senses of the same word, they should be represented separately rather than merged into one atom.

### 1.2. Multi-word expression

A multi-word lexical unit taught as a unit.

Examples:

- `by and large`
- `in the long run`

### 1.3. Phrasal verb

A verb plus particle/preposition functioning as a lexical unit.

Examples:

- `carry out`
- `come across`
- `put off`

This may technically overlap with multi-word expressions, but it is retained as a distinct subtype because it is a recurring and pedagogically meaningful category in the book.

### 1.4. Idiom

A fixed or semi-fixed expression whose meaning is not straightforwardly compositional.

Examples:

- `spill the beans`
- `hit the nail on the head`

### 1.5. Collocation

A conventional combination of words that the book explicitly teaches or exemplifies as a lexical usage pattern.

Examples:

- `assess the risk`
- `strong evidence`
- `draw a conclusion`

A collocation should be treated as knowledge in its own right when knowing the individual words is insufficient to reproduce the taught combination naturally.

### 1.6. Word formation

Knowledge about morphological relationships among lexical forms.

Examples:

- `assume` → `assumption`
- `infer` → `inference`
- `accurate` → `accuracy`

The derived lexical forms remain lexical items; the word-formation relationship is represented separately when useful.

### 1.7. Morphological form

A grammatical or inflectional form of a lexical item, especially where the book explicitly teaches an irregular or otherwise important form.

Examples:

- `think` → `thought`
- `write` → `written`

---

## 2. Grammatical Knowledge

### 2.1. Grammatical form

The formal structure used to construct a grammatical expression.

Example:

- present perfect → `have/has + past participle`

### 2.2. Grammatical meaning

The meaning conveyed by a grammatical form or construction.

Example:

- present perfect can connect a past event with present relevance

Form and meaning should remain separable when the source provides distinct evidence for them.

### 2.3. Grammatical use / function

Knowledge about when or why a grammatical form is used.

Examples:

- present continuous for a temporary activity
- present simple for habitual or general situations

### 2.4. Grammatical pattern / construction

A recurring syntactic construction taught by the book.

Examples:

- `suggest + V-ing`
- `suggest + that-clause`
- `consider + noun`
- `consider + V-ing`

### 2.5. Grammatical rule

An explicit rule governing grammatical form or use.

Example:

- stative verbs are not normally used in continuous forms

### 2.6. Grammatical constraint

A restriction on where or how a grammatical structure can be used.

Example:

- a normally stative verb does not normally occur in a continuous form

### 2.7. Grammatical exception

An explicitly documented exception to a general grammatical rule or constraint.

Exceptions must be supported by source evidence; they must not be invented from generated examples.

---

## 3. Usage Knowledge

Usage knowledge covers lexical or grammatical behavior that is more specific than a general definition or rule.

### 3.1. Complementation

The complement structure associated with a lexical item or construction.

Examples:

- `avoid + V-ing`
- `want + to-infinitive`

### 3.2. Preposition pattern

A lexical or grammatical pattern involving a particular preposition.

Examples:

- `depend on`
- `interested in`
- `responsible for`

### 3.3. Argument structure

The syntactic structure in which a lexical item takes its arguments.

Example:

- `contemplate + noun`

This category is particularly useful for preventing unsupported constructions such as `contemplate on` when the source supports only a direct object.

### 3.4. Lexical restriction

A restriction on which lexical combinations are acceptable or conventional when explicitly supported by the source.

Example:

- `make a decision` rather than `do a decision`

### 3.5. Register

The explicitly taught level or variety of formality associated with an expression.

Examples:

- formal
- informal
- colloquial
- academic

Register is normally better represented as a property of a lexical or usage atom rather than as an independent atom.

### 3.6. Connotation

An explicitly taught evaluative or affective association of a lexical item.

Examples:

- a word with positive, negative, or neutral connotation

Connotation is normally better represented as a property unless the source makes the distinction independently important.

---

## 4. Semantic Knowledge

### 4.1. Synonymy

A semantic relationship between lexical items with equivalent or closely equivalent meanings.

Example:

- `begin` ↔ `start`

Usually represented as a relation rather than as a separate atom.

### 4.2. Near-synonymy

A relationship between words with similar meanings but important differences in use, meaning, register, or context.

Examples:

- `assess` ↔ `evaluate`
- `consider` ↔ `contemplate`

This is especially important at C1-C2 level.

### 4.3. Antonymy

A semantic opposition between lexical items.

Example:

- `increase` ↔ `decrease`

Usually represented as a relation.

### 4.4. Semantic distinction

An explicitly taught distinction between items that learners could reasonably confuse.

Examples:

- `assume` vs `infer`
- `vague` vs `ambiguous`
- `imply` vs `infer`

This is a high-value knowledge relation for Destination C1-C2 and should be preserved when supported by the source.

### 4.5. Hypernym / hyponym

A category–subcategory relationship.

Example:

- `vehicle` → `car`, `train`, `bicycle`

### 4.6. Part–whole relationship

A semantic relationship between a component and the entity containing it.

Example:

- `engine` → `car`

---

## 5. Discourse Knowledge

### 5.1. Discourse marker / discourse function

Knowledge about expressions that organize relationships between ideas.

Examples:

- `however` → contrast
- `therefore` → consequence
- `moreover` → addition

### 5.2. Cohesive reference

Knowledge about expressions used to refer back to or connect with information in discourse.

Examples:

- `this`
- `that`
- `such`
- `former`
- `latter`

Only extract this when the book explicitly teaches or exemplifies the relevant reference behavior.

### 5.3. Discourse relation

An explicitly taught relationship between parts of discourse.

Examples:

- cause → effect
- contrast
- concession
- addition

### 5.4. Information structure

Knowledge about how sentence structure organizes focus, emphasis, or information.

Examples:

- cleft constructions such as `It was John who...`
- pseudo-cleft constructions such as `What I need is...`

---

## 6. Pragmatic / Functional Knowledge

These types apply when Destination C1-C2 explicitly teaches communicative functions or pragmatic meaning.

### 6.1. Language function

A communicative purpose expressed through language.

Examples:

- expressing doubt
- making suggestions
- disagreeing
- hedging

### 6.2. Speech act

A communicative act performed through an utterance.

Examples:

- request
- apology
- refusal
- complaint

### 6.3. Pragmatic meaning

A meaning or communicative implication that depends on context and goes beyond literal lexical/grammatical meaning.

Example:

- `Could you possibly...?` → polite request

---

# Representation Rules

The taxonomy above describes **knowledge that can be extracted from the book**, but not every category should automatically become a standalone atom.

The extractor should distinguish at least four kinds of knowledge objects:

```text
Knowledge Atom
Property
Relation
Category / Metadata
```

For example:

```text
assess
→ lexical-sense atom

formal
→ usually a property of a lexical/usage atom

assess ≈ evaluate
→ near-synonym relation

assess vs assume
→ semantic-distinction relation

Thinking and Learning
→ category / metadata
```

The guiding principle is:

> **Create an atom when the knowledge itself is independently meaningful and independently diagnosable; use properties and relations when they describe an existing atom rather than constituting a separate learning unit.**

---

# Extraction Constraints

1. **Source evidence comes first.** Do not invent definitions, patterns, collocations, restrictions, distinctions, or exceptions from intuition.
2. **One lexical sense = one atom by default.** Split distinct senses when the source supports them.
3. **Do not turn every example sentence into an atom.** An example is evidence for an atom unless it teaches an independently reusable pattern.
4. **Do not turn every semantic relationship into an atom.** Synonymy, antonymy, near-synonymy, and distinctions are normally relations between atoms.
5. **Do not infer unsupported grammar.** A generated question or model intuition is not evidence for a grammatical pattern.
6. **Preserve provenance.** Every curated atom should be traceable to the relevant source/unit/section/item evidence.
7. **Preserve uncertainty.** Candidate knowledge that has not been validated must not silently become canonical knowledge.
8. **Avoid atom inflation.** The purpose of this taxonomy is to represent the book's knowledge at useful granularity, not to maximize the number of records.
9. **Keep learner data out.** Mastery, attempts, confidence, retention, review status, and learning progress belong to the learner layer, not this taxonomy.
