# Questions About Challenges

This document records the design questions that were raised while defining the Challenge model and their resolved decisions.

## Current invariants

- A Challenge is a concrete assessment task presented to a learner to assess a Knowledge Atom.
- Each Challenge assesses exactly one Knowledge Atom.
- A Knowledge Atom may have many Challenges.
- A Challenge is not necessarily a question in the linguistic sense.
- If a Challenge tests knowledge about a relationship between independent Atoms, that relationship must itself be represented as a `relation` Atom, and the Challenge tests that relation Atom.
- A Challenge is a concrete instance, not a reusable abstract template.
- A Challenge references its target Knowledge Atom by ID rather than copying the Atom's knowledge content.
- A Challenge may have source provenance when it is derived from learning material, but source is optional for source-independent or system-generated Challenges.
- Challenge data is distinct from learner performance data.
- The Challenge model does not define a `difficulty` concept.
- Source-derived Challenges are extracted from concrete assessment tasks in the source, such as exercise items, rather than generated from Knowledge Atoms.
- The current Challenge model supports Challenges with a specific expected answer. Speaking and open-ended free-response Challenges are outside the current model.

## Resolved Questions

### Q4. What is the lifecycle of a Challenge?

A Challenge follows a Candidate-to-Official lifecycle analogous to the Knowledge Atom lifecycle.

The lifecycle is:

```
Challenge Candidate
       ↓
   validation
       ↓
 human review
       ↓
 approved / rejected
       ↓
  officialize
       ↓
Official Challenge
       ↓
    retired
```

Candidate review status is `pending | approved | rejected`.

An approved Candidate is not yet an Official Challenge. Officialization is the storage transition that creates the Official Challenge and removes the Candidate.

An Official Challenge may be corrected or refined without changing its semantic identity. If a change makes it a semantically different assessment task, a new Challenge identity must be created.

An Official Challenge may be retired. Retired Challenges are not returned to the Candidate lifecycle.

### Q5. How should Challenges be stored?

Challenges are organized by source and Source Segment, following the organizational approach used for Knowledge Atoms:

```
data/
└── challenges/
    └── <source-id>/
        └── <segment-id>/
            ├── challenges.md
            └── challenge_candidates.md
```

- `challenges.md` stores Official Challenges.
- `challenge_candidates.md` stores Challenge Candidates.
- Candidate and Official storage are separate.
- No additional `official/` or `candidates/` directory layer is used.
- The storage path is an organizational location, not the semantic identity of a Challenge.

A Challenge may be reused independently of its source. Source information remains provenance metadata rather than becoming part of the Challenge's semantic identity.

### Q6. How should answer and evaluation data be represented?

The current model does not include an open-ended evaluation specification.

The supported Challenge model requires a **specific expected answer**. Speaking and free-response Challenges are outside the current scope.

Conceptually:

```
Challenge
├── task
├── form
├── target_atom_id
└── answer
```

- `task` describes what the learner must do.
- `form` identifies the Challenge form, such as multiple choice, fill in the blank, matching, sentence transformation, or reordering.
- `target_atom_id` identifies the one Knowledge Atom being assessed.
- `answer` represents the specific expected answer. Its representation may be structured according to the Challenge form; it is not necessarily a single string.

Examples include a selected option, a required word, a specific transformed sentence, or a specific matching arrangement.

Evaluation of a learner response is a runtime/assessment concern: the learner response is compared with the Challenge's expected answer according to the supported Challenge form. Evaluation results and learner performance are not intrinsic Challenge data.

During extraction, answer information is taken from the source when available. The extractor must not invent an answer that is not supported by the source.

### Q7. How should learner performance be recorded?

Learner performance is learner-specific operational data and is kept separate from the Challenge.

A Challenge does not store a learner's attempts, review history, correctness history, or learner state.

The learner's interaction follows:

```
Challenge
    ↓
Learner Response
    ↓
Assessment Result
    ↓
Learner State
```

The learner-specific review model records the information needed by the adaptive system rather than modifying the Challenge itself.

### Q8. Should Challenge statistics be stored?

Challenge statistics are derived operational data, not intrinsic properties of a Challenge.

Examples include:

- response counts;
- accuracy;
- other aggregate performance measures.

Such statistics may be computed or stored separately when needed by the system. They do not belong in the intrinsic Challenge representation.

### Q9. How should Challenges be selected for adaptive review?

Challenge selection is an adaptive-system concern, not part of the intrinsic Challenge model.

When multiple Challenges target the same Knowledge Atom, the adaptive system selects among them using learner state and the system's review/selection logic.

Challenge selection may consider factors such as prior learner performance, whether a Challenge has recently been used, and the need to avoid repeatedly presenting the same Challenge, but the specific selection algorithm is outside the Challenge model.

### Q11. What is the role of a Challenge Template or generator?

A Challenge is a concrete instance, not a reusable template.

Reusable templates, generation patterns, and generators are separate concepts or implementation mechanisms and are not part of the Challenge model.

They may be introduced later if the adaptive system needs them.

### Q13. What is the identity of a Challenge?

Challenge identity is based on the identity of the concrete assessment task, not merely on its target Knowledge Atom.

Two Challenges targeting the same Atom are not automatically the same Challenge.

A concrete task's semantic identity is determined by the assessment content and expected answer required by that task. Source occurrence is provenance and does not by itself define semantic identity.

During extraction, each source occurrence is preserved as a separate Challenge Candidate. Later deduplication or reuse may determine that multiple Candidates represent the same reusable Challenge, but that is a separate process from extraction.

### Q14. How should source provenance interact with Challenge reuse?

Source provenance remains attached as provenance metadata when a Challenge is reused independently of its original source.

The Challenge's semantic identity does not become source-specific merely because it was extracted from a source.

If the same Challenge is associated with multiple source occurrences, the system may retain the relevant provenance records rather than changing the Challenge's identity.

Source provenance records where the Challenge came from; they do not define what the Challenge means.

### Q15. What belongs outside the Challenge model?

The following remain outside intrinsic Challenge data:

- learner attempts and responses;
- assessment results;
- learner review state and history;
- review scheduling;
- learner ability or estimated mastery;
- aggregate Challenge statistics;
- adaptive Challenge selection logic;
- reusable Challenge templates and generators;
- other runtime or operational data.

The Challenge model contains the concrete assessment task, its form, its target Knowledge Atom, its specific expected answer, and relevant source provenance.
