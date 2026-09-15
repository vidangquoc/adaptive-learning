# Adaptive Learning — Context Recovery

> Đây là **file duy nhất** chứa thông tin phục vụ khôi phục context và trạng thái làm việc của repository `vidangquoc/adaptive-learning`.
>
> File này chỉ phục vụ continuity/recovery. Chi tiết kỹ thuật, specification, schema, methodology và data documentation phải nằm trong `docs/` hoặc các file domain-specific tương ứng.

## 1. Project identity

- Project hiện tại: **Adaptive Learning**.
- Repository: `vidangquoc/adaptive-learning`.
- **PTNK là predecessor project từ đó Adaptive Learning được tách ra.**
- PTNK vẫn là một domain-specific evidence source và validation/calibration target quan trọng, nhưng không phải identity hay scope của toàn repository.
- Adaptive Learning không phải vocabulary-only project và không phải PTNK-only paper-analysis project.

## 2. Core objective

Xây dựng một hệ thống adaptive learning dựa trên evidence, tối đa hóa learning value dưới giới hạn thời gian và các ràng buộc thực tế bằng cách liên tục quyết định:

> **What should the learner do next, and why?**

Tối ưu learning value, không tối ưu số giờ, số trang, số từ hay syllabus completion.

## 3. Core adaptive loop

```text
Goal
 ↓
Competency model
 ↓
Knowledge sources
 ↓
Diagnostic / Challenge
 ↓
Learner state
 ↓
Learning frontier
 ↓
Next-best activity
 ↓
Assessment
 ↓
Updated learner state
 ↺
```

### Challenge-first

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

Các nguyên tắc:
- Khi prior knowledge là plausible, challenge nên đi trước routine instruction.
- Nếu learner đã biết, skip hoặc compress.
- Nếu learner học nhanh, accelerate.
- Nếu một dimension yếu, target dimension đó.
- Nếu competency đã mastered, stop/maintain/extend.
- Instruction là evidence-driven, không page-driven.

## 4. Curriculum backbone

**Destination C1 & C2** là initial curriculum/knowledge backbone, không phải mandatory textbook sequence.

Additional books/sources là expansion layers, chỉ mở rộng khi evidence cho thấy có giá trị cụ thể về breadth, depth, precision hoặc transfer.

PTNK papers chủ yếu là calibration/validation evidence: dùng để characterise competency coverage, task formats, difficulty/discrimination và transfer requirements. Không dùng PTNK để định nghĩa toàn bộ curriculum.

Working characterization của PTNK specialized English: C1-centered, có C1+ competitive/discrimination zone và một C2 tail nhỏ. Không coi toàn bộ exam là C2 nếu chưa có evidence.

## 5. Stable knowledge architecture decisions

```text
External sources
      ↓
RAW / EVIDENCE
      ↓
CURATED / NORMALIZED
      ↓
KNOWLEDGE BASE
      ↓
COMPETENCY / MODULE MODEL
      ↓
LEARNING STATE
      ↓
REVIEW QUEUE
      ↓
NEXT-BEST ACTIVITY
```

Các quyết định đã ổn định:
- Knowledge atoms là **flat và independently diagnosable**.
- Một lexical sense = một atom theo mặc định.
- Independently useful grammar uses/constructions/contrasts là các atom riêng khi được source evidence hỗ trợ.
- Relationships là explicit typed links; không tạo mandatory parent/child ancestry trees.
- Learner mastery thuộc learner-state data, không thuộc static knowledge.
- Candidate và official representations tách biệt.
- Human review là promotion gate ở những nơi project yêu cầu.
- Raw source, curated knowledge và generated practice/challenges là các lớp khác nhau.
- Generated practice/challenges không phải evidence rằng một item là required.

## 6. Evidence, provenance và accuracy rules

- **Evidence > intuition.**
- **Accuracy > completeness.**
- Preserve provenance và uncertainty.
- Không bịa definition, pronunciation, examples, patterns, CEFR, relationships hoặc source evidence.
- Structural extraction và provenance validation phải fail closed khi có lỗi.
- Khi context cũ mâu thuẫn với repository hiện tại, ưu tiên repository.

## 7. Source-boundary recovery

Đối với Destination C1/C2 extraction:
- canonical structural source boundary là **Unit**;
- dùng `sources/destination-c1-c2/units/unit-XX.txt` làm authoritative Unit input;
- validate Unit boundaries trước discovery;
- provenance phải trỏ tới Unit cùng location/span chính xác;
- không khôi phục section-based extraction đã superseded thành source-of-truth.

## 8. Learning-state recovery

Các mastery dimensions quan trọng:
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

Đây là working concepts/heuristics, không phải immutable constants.

## 9. Data architecture recovery summary

Hai lớp dữ liệu phải được giữ tách biệt:

```text
data/
├── knowledge/   # what there is to learn + evidence
└── learner/     # what the learner has done / knows / needs next
```

Knowledge atom không chứa learner mastery. Learner state reference atom IDs thay vì duplicate knowledge definitions.

Assessment definitions thuộc knowledge layer; learner responses/outcomes thuộc learner layer.

Attempt history là historical evidence; review queue là derived state.

Thay đổi static knowledge không được silently rewrite historical learner attempts. Thay đổi learner state không được alter source evidence/canonical atom meaning.

Chi tiết authoritative nằm ở `docs/data-architecture.md`, `docs/learning-state-specification.md` và các specification liên quan.

## 10. PTNK boundary

PTNK-specific artifacts có thể giữ naming `ptnk-*` vì chúng thể hiện provenance/domain thật sự. Ví dụ:

- `docs/ptnk-2026-pipeline-report.md`
- `sources/ptnk-2026/`
- `data/evidence/ptnk-2026-*`
- PTNK-specific lexical datasets

Không rename các artifact này chỉ vì cosmetic consistency.

Không dùng PTNK naming cho project-level architecture mới nếu artifact không thực sự PTNK-specific.

## 11. Current implementation status

**Status:** Architecture established; implementation của executable adaptive learning loop là major next phase.

Đã thiết lập:
- RAW / EVIDENCE / CURATED / OFFICIAL separation
- provenance và accuracy-over-completeness policy
- flat knowledge-atom model
- candidate vs official knowledge separation
- Destination C1 & C2 as initial curriculum backbone
- PTNK evidence pipeline as calibration/validation subsystem
- challenge-first và diagnostic-first approach
- Learning State concept và mastery dimensions
- adaptive branching concept
- review queue concept
- expansion gate concept
- 700h là ceiling/learning budget, không phải quota
- canonical `data/knowledge/` và `data/learner/` boundaries
- assessment definitions tách khỏi learner attempts

## 12. Current implementation priorities

### Priority 1 — schemas và deterministic rules

- Define concrete learner-state schema
- Define attempt-history schema
- Define competency-state schema
- Define review-queue schema
- Define deterministic state-update rules
- Define deterministic review-priority rules

### Priority 2 — small adaptive pilot

- Select representative competencies
- Create challenge/diagnostic items
- Record learner attempts
- Update learner state
- Generate review queue
- Verify every recommendation has an explicit reason

### Priority 3 — expand knowledge coverage

Chỉ sau khi adaptive loop hoạt động:
- expand lexical coverage
- expand grammar competencies
- expand reading/cloze competencies
- expand word formation/transformation
- expand additional domains where evidence requires

**Không collect large amounts of knowledge without a learning-state purpose.**

## 13. Definition of success for next phase

Một attempt như:

```text
Learner answered a challenge incorrectly.
```

phải eventually được xử lý deterministic thành:

```text
Attempt recorded
      ↓
Relevant competency identified
      ↓
Weak dimension updated
      ↓
Mastery gate evaluated
      ↓
Review queue entry created
      ↓
Reason recorded
      ↓
Next-best targeted activity selected
```

Khi đạt được điều này, Adaptive Learning đã chuyển từ knowledge repository thành functioning closed-loop learning system.

## 14. Recovery protocol

Khi bắt đầu một conversation mới hoặc context bị mất:

1. Đọc **file này trước**.
2. Xác nhận repository là `vidangquoc/adaptive-learning`.
3. Đọc các authoritative docs liên quan tới task, đặc biệt:
   - `docs/methodology.md`
   - `docs/learning-state-specification.md`
   - `docs/knowledge-atom-pipeline.md`
   - `docs/data-architecture.md`
   - relevant `docs/learning-material-principles/`
   - relevant schemas, data, sources và scripts.
4. Inspect current Git/repository state trước khi sửa.
5. Khi cần, inspect recent Git history để xác định architectural state.
6. Nếu conversation memory mâu thuẫn với repository, trust repository và report the difference.
7. Không đoán khi context thiếu.

### Golden rule

```text
Khi context thiếu, không đoán.
Đọc repository hiện tại trước.
Ưu tiên repo hơn trí nhớ hội thoại cũ.
Evidence > intuition.
Accuracy > completeness.
Adaptive Learning > PTNK-specific framing.
```

## 15. Maintenance rule

**Tất cả thông tin phục vụ context recovery, project identity recovery, current status recovery và recovery instructions phải nằm trong file này.**

Không tạo thêm `PROJECT-CONTEXT.md`, `PROJECT-STATUS.md` hoặc các file context-recovery song song khác.

Khi một architectural/ontology/data-layer/governance decision trở nên stable:
- cập nhật authoritative detailed documentation trong `docs/` hoặc domain-specific files;
- sau đó cập nhật **summary cần thiết cho recovery** trong file này;
- xóa các recovery instructions đã obsolete để future sessions không revive quyết định cũ.

`context-recover/context-recover.md` là **single source of truth cho context recovery**, nhưng không phải source of truth cho detailed technical specifications.
