# Adaptive Learning — Context Recovery

> Mục đích: khôi phục nhanh ngữ cảnh làm việc của repository `vidangquoc/adaptive-learning` khi cuộc hội thoại bị mất hoặc chuyển sang cuộc hội thoại mới.

## 1. Master recovery prompt

```text
Tao đang tiếp tục project **Adaptive Learning** trong repo GitHub `vidangquoc/adaptive-learning`.

Quan trọng: Adaptive Learning được tách ra từ project cũ **PTNK**. PTNK là predecessor/domain-specific evidence source và validation target, không phải tên của project hiện tại.

Trước khi làm việc, hãy đọc:
- `PROJECT-CONTEXT.md`
- `PROJECT-STATUS.md`
- `docs/methodology.md`
- `docs/learning-state-specification.md`
- `docs/knowledge-atom-pipeline.md`
- các file liên quan trong `docs/learning-material-principles/`
- các rule/source files liên quan tới task hiện tại.

Nguyên tắc cốt lõi:
- Adaptive Learning là knowledge + competency + challenge + learner-state + next-best-activity system, không phải vocabulary list.
- Destination C1 & C2 là initial curriculum/knowledge backbone.
- Challenge-first: challenge → diagnose gap → targeted learning → retest → update learner state.
- Static knowledge và learner state là hai lớp khác nhau.
- Knowledge atoms là flat và độc lập; một lexical sense là một atom theo mặc định.
- Evidence > intuition; accuracy > completeness.
- Không bịa definition, pronunciation, examples, patterns, CEFR, relationships hoặc provenance.
- PTNK papers chủ yếu dùng để calibration/validation; không biến Adaptive Learning thành PTNK-only project.
- PTNK-specific files có thể giữ tên `ptnk-*` vì chúng biểu diễn provenance/domain của dữ liệu.
- 700h là ceiling/learning budget, không phải quota.

Trước khi sửa code/data/docs, kiểm tra repository state hiện tại. Nếu context cũ mâu thuẫn với repo, ưu tiên repo và chỉ ra khác biệt.
```

## 2. Adaptive-learning architecture

```text
Goal
 ↓
Competency model
 ↓
Knowledge base
 ↓
Diagnostic / Challenge
 ↓
Learning State
 ↓
Learning Frontier
 ↓
Next-best Activity
 ↓
Assessment
 ↺
Learning State
```

Challenge-first:

```text
Knowledge / competency
        ↓
Challenge
   ↙         ↘
correct     wrong / uncertain
  ↓               ↓
skip/extend   trace exact gap
                  ↓
             targeted learning
                  ↓
                retest
```

## 3. Knowledge-model recovery

Read the candidate/official schemas and `docs/knowledge-atom-pipeline.md` before modifying knowledge extraction or promotion.

Stable decisions:
- flat independent atoms;
- one lexical sense = one atom by default;
- independently useful grammar uses/constructions/contrasts are separate atoms when supported;
- relationships are explicit typed links;
- learner mastery belongs in learner-state data;
- candidate and official representations remain separate;
- human review is the promotion gate where required.

## 4. Source-boundary recovery

For Destination C1/C2 extraction:
- the canonical structural source boundary is the **Unit**;
- use `sources/destination-c1-c2/units/unit-XX.txt` as authoritative Unit input;
- validate Unit boundaries before discovery;
- provenance points to the Unit plus a precise location/span;
- do not revive superseded section-based extraction as source-of-truth.

## 5. Learning-state recovery

Potential mastery dimensions:
- recognition
- recall
- usage
- collocation
- discrimination
- transfer
- retention

Working progression:

```text
UNSEEN → KNOWN → RECALLABLE → USABLE → MASTERED → MAINTENANCE
                                      ↘ EXTENDED
```

These are working concepts, not immutable constants.

## 6. PTNK boundary

PTNK is a predecessor and an important calibration/validation domain.

PTNK-specific artifacts such as `sources/ptnk-2026/`, `data/evidence/ptnk-2026-*`, and `docs/ptnk-2026-pipeline-report.md` remain valid and should not be renamed merely for cosmetic reasons.

Do not use PTNK naming for new project-level architecture unless the artifact is genuinely PTNK-specific.

## 7. Repository navigation

Before substantive work inspect:
- `PROJECT-CONTEXT.md`
- `PROJECT-STATUS.md`
- relevant `docs/`
- relevant schemas
- relevant `data/`
- relevant `sources/`
- relevant `scripts/`
- recent Git history when architectural state is uncertain.

## 8. Golden rule

```text
Khi context thiếu, không đoán.
Đọc repository hiện tại trước.
Ưu tiên repo hơn trí nhớ hội thoại cũ.
Evidence > intuition.
Accuracy > completeness.
Adaptive Learning > PTNK-specific framing.
```

## 9. Maintenance rule

Update this file when a major architectural, ontology, data-layer, or governance decision becomes stable. Remove superseded instructions so future recovery sessions do not revive obsolete project assumptions.
