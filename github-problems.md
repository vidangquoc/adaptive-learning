# GitHub Problems & Recovery Notes

## Problem: confusing parser output with knowledge-atom discovery

### Observed failure

The first knowledge-atom discovery approach treated parser-detected lexical structures as if they were already knowledge atoms. This is unsafe.

A parser can reliably find evidence such as:

- POS rows;
- word boxes;
- lexical tables;
- expression-like strings;
- phrasal-verb-looking patterns;
- headings;
- exercise boundaries.

But a pattern match does not prove what the underlying learning unit is.

The same problem was exposed more clearly by the grammar prototype: a grammar heading or rule fragment cannot automatically become a grammar atom because the final atom requires interpretation of form, meaning, function, constraints, context, and contrasts.

The same principle applies to lexical material. A parser cannot by itself reliably decide whether a string is:

- one word with one sense;
- one word with multiple independently useful senses;
- a lexicalized multiword expression;
- a literal compositional phrase;
- an idiom;
- a phrasal verb with one or several senses/patterns;
- a genuine collocation;
- a word-formation relationship;
- multiple distinct knowledge items that happen to share surface text.

### Root cause

The pipeline implicitly collapsed two different tasks:

```text
Evidence discovery
        ≠
Knowledge interpretation
```

Regex/parser logic is appropriate for finding evidence candidates, but semantic/linguistic interpretation is required before promotion to canonical knowledge.

### Correct architecture

Use a fail-closed layered pipeline:

```text
SOURCE
  ↓
RAW / STRUCTURAL EVIDENCE
  ↓
EVIDENCE CANDIDATES
  ↓
LINGUISTIC / SEMANTIC ANALYSIS
  ↓
KNOWLEDGE-ATOM CANDIDATES
  ↓
VALIDATION / QUALITY GATES
  ↓
VERIFIED KNOWLEDGE ATOMS
```

Core rule:

> **Parser discovers evidence. Reasoning interprets evidence. Validation decides whether the interpretation is safe enough to become knowledge.**

### Required handling when this problem recurs

1. **Do not improve the regex first merely because atom quality is poor.**
2. Determine whether the failure is actually an evidence-discovery problem or an interpretation problem.
3. If the parser is finding the relevant source evidence but atomization is wrong, keep the parser and add/fix the linguistic-analysis layer.
4. Preserve the original evidence and provenance; do not overwrite raw material with inferred interpretations.
5. Allow one evidence span to produce multiple atom candidates.
6. Allow multiple evidence spans to support one atom candidate.
7. Allow an evidence span to produce no atom and be marked `review-needed` when evidence is insufficient.
8. Never equate candidate count with verified-atom count.
9. Never promote a candidate merely because a regex matched.
10. Apply the same principle to lexical and grammatical material.
11. Fail closed when competing interpretations cannot be resolved safely.

### Example: lexical material

Evidence:

```text
look up
```

The parser may correctly identify the string. It must not decide by itself that there is exactly one atom. Linguistic analysis may determine that multiple independently useful senses/patterns exist and should be represented as separate flat atoms.

Likewise:

```text
spill the beans
```

requires distinguishing the idiomatic use from a literal occurrence.

### Example: grammar material

Evidence:

```text
Past time
Past perfect
```

These are structural headings, not automatically knowledge atoms. The analyzer must derive a useful construction/rule with form, meaning/function, constraints, and assessment implications.

### Related validation rule

For grammar questions, grammaticality is not enough. The system must check:

```text
grammaticality
contextual appropriateness
intended meaning
```

If two candidates are grammatical and contextually compatible, reject or rewrite the question even if a source answer key selects one.

### Permanent project rule

This problem resulted in an update to the canonical learning-material principles. The canonical rule is now that **parser output is evidence discovery, not canonical knowledge**, and that **lexical as well as grammatical atomization requires linguistic/semantic reasoning before promotion**.

When implementing future extraction/discovery work, consult `docs/learning-material-principles.md` first and preserve this separation of responsibilities.
