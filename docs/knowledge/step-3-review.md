# Step 3 Review — Knowledge Atom Taxonomy + Structure

> **Status: OPEN — chưa chốt Step 3.**
>
> Đây là file để tao và mày bàn từng vấn đề còn mở. Những phần dưới đây là **nội dung đang được review**, không phải quyết định cuối cùng của project.

## Các phần còn lại cần review

1. Các field của atom
2. Semantic ID
3. Candidate / Official
4. Review status

Không cần giải quyết hết một lần.

---

# 1. Các field của atom

Schema hiện tại:

```yaml
id:
domain:
type:

name:

meaning:
mother_says:
explanation:
structure:

examples:

extra:
  source:
  is_tested:
  test_evidence:
  notes:
```

Cần xem từng field, không nên chốt cả schema một lúc.

### `meaning`

**Đã chốt:** ý nghĩa hoặc chức năng cốt lõi của knowledge represented by atom. Với vocabulary, đây là lexical sense cụ thể; với grammar, đây là grammatical meaning/function.

### `mother_says`

**Đã chốt:** đây là **bản dịch / cách diễn đạt của `name` bằng tiếng mẹ đẻ của learner**. Nó đặc biệt hữu ích với vocabulary.

### `explanation`

**Đã chốt:** phần giải thích đầy đủ hơn khi `meaning` chưa đủ để hiểu, dạy, phân biệt, hoặc chẩn đoán atom. Không được biến thành cái thùng chứa mọi thứ.

### `part_of_speech` và `pronunciation` cho `lexical_sense`

**Đã chốt:** đây là hai property chỉ dành cho `vocabulary.lexical_sense`, không thuộc common schema của mọi atom.

Thứ tự trong representation của `lexical_sense` là:

```yaml
name:
part_of_speech:
pronunciation:
```

- `part_of_speech` = từ loại của lexical sense;
- `pronunciation` = phiên âm/phát âm của lexical sense, thông thường dùng IPA khi có thể.

Cả hai đều là descriptive properties của lexical sense, không phải Knowledge Atoms riêng.

Nếu trong `explanation` xuất hiện một kiến thức có identity riêng thì phải xem nó có cần trở thành atom hay không.

### `structure`

**Đã chốt:** cấu trúc / hình thức mà knowledge được tạo thành hoặc biểu hiện.

Nó trả lời câu hỏi: **Nó được tạo thành / cấu trúc như thế nào?**

Ví dụ:

- vocabulary: `assess + noun`
- multiword expression: `strike + a + balance`
- grammar: `have/has + been + V-ing`
- word formation: mẫu hình thái học tạo từ

`structure` tập trung vào **form/pattern**, không phải khi nào hay trong hoàn cảnh nào kiến thức được dùng.

---

# 2. `examples`

### `examples`

**Đã chốt giữ field này.** Ý nghĩa của field đủ rõ: các ví dụ cụ thể minh họa knowledge represented by atom.

Một câu ví dụ có thể minh họa nhiều atom cùng lúc. Nếu câu ví dụ chứa một learning target khác thì learning target đó nên được extract riêng, thay vì biến cả câu thành atom.

---

# 3. `extra.source`

`extra.source` là provenance của Atom, dùng để truy nguyên Atom về source evidence.

**Đã chốt semantic contract:**

- phải truy nguyên được về source artifact;
- phải xác định được canonical Segment chứa evidence;
- phải xác định được precise location/span của supporting evidence trong Segment khi thông tin đó có sẵn;
- một Atom có thể có nhiều provenance records nếu có nhiều source evidence cùng hỗ trợ Atom;
- `source` chỉ là provenance, không chứa knowledge content, learner state, hay definition/explanation được normalize vào Atom;
- `source` không thay thế `extra.test_evidence`.

**Cấu trúc machine-readable đã chốt:**

```yaml
source:
  origin:
    - source_id:
      segment_id:
      location:
        page:
        section:
        line:
  atom_decision:
    - source_id:
      segment_id:
      location:
        page:
        section:
        line:
```

Trong đó:

- `origin` = nơi knowledge point xuất phát từ learning material;
- `atom_decision` = source evidence làm căn cứ quyết định knowledge point đó trở thành Knowledge Atom;
- cả hai là arrays vì một Atom có thể có nhiều source records;
- `location.line` là **starting line** của evidence trong Segment text, không phải line range;
- các thành phần của `location` là optional khi source không có độ chính xác tương ứng;
- `atom_decision` không nhất thiết phải là exercise/test; nó là evidence cho quyết định atomization nói chung.

---

# 4. Semantic ID

**Đang mở.**

Cấu trúc cơ sở:

```text
<domain>.<type>.<name>
```

Riêng với `vocabulary.lexical_sense`, `part_of_speech` là một phần của semantic identity và đứng sau `name`:

```text
<domain>.lexical_sense.<name>.<part_of_speech>
```

Nếu `name + part_of_speech` vẫn chưa phân biệt được hai lexical-sense atoms, thêm một component cuối là **dạng rút gọn, ổn định của `meaning`**.

Ví dụ:

```text
vocabulary.lexical_sense.assume.verb
vocabulary.lexical_sense.compelling.adjective
vocabulary.lexical_sense.run.verb.move_quickly
vocabulary.lexical_sense.run.verb.operate_function
vocabulary.collocation.strike_a_balance
grammar.use.present_simple.current_habit
grammar.use.present_perfect.past_to_present
```

Đã chốt:

- `name` là semantic identifier của knowledge object;
- không có tầng `subtype`;
- với `lexical_sense`, `part_of_speech` đứng sau `name` trong Semantic ID;
- chỉ khi `name + part_of_speech` chưa đủ phân biệt lexical senses mới thêm dạng rút gọn ổn định của `meaning`;
- Không đặt ra một quy ước chuẩn hóa cứng cho meaning-slug. Khi cần phân biệt lexical senses, chỉ cần dùng một dạng rút gọn, dễ hiểu và ổn định của meaning; không kỳ vọng có thể chuẩn hóa hoàn toàn.

Ví dụ:

```text
move_quickly
operate_function
make_a_decision
have_a_particular_quality
```

**→ Quy tắc cấu trúc đã chốt; meaning-slug chỉ cần được đặt nhất quán và dễ hiểu qua từng trường hợp, không cần một thuật toán chuẩn hóa chung.**

---

# 5. Candidate / Official

**Đã chốt:** Candidate / Official là **lifecycle state của Knowledge Atom trong knowledge pipeline**, không phải một phần của atom ontology và không phải một `domain`, `type`, hay semantic property của atom.

Mô hình:

```text
Learning Material
       ↓
   Extraction
       ↓
Candidate Knowledge Atom
       ↓
     Review
       ↓
Official Knowledge Atom
```

### Candidate

Candidate là một **proposed Knowledge Atom**: hệ thống đã xác định một knowledge point và đề xuất nó như một atom, nhưng chưa được review để xác nhận là canonical/official.

Candidate vẫn là Knowledge Atom về mặt ontology; Candidate không phải một loại atom khác và không có `type` riêng.

**Đã chốt:** Candidate có **canonical semantic `id` ngay từ khi được tạo**. Không có `candidate_id` riêng và không dùng temporary/tracking ID thay cho semantic ID.

Ví dụ:

```text
id: vocabulary.lexical_sense.run.verb.move_quickly
review_status: pending
```

Khi Candidate bị reject rồi review lại, **giữ nguyên semantic ID**.

### Official

Official là một Knowledge Atom đã được review và chấp nhận là canonical knowledge của hệ thống.

**Đã chốt:** khi Candidate được officialize, **không tạo semantic ID mới**. Official sử dụng chính semantic ID đã được tạo cho Candidate.

Ví dụ:

```text
Candidate
id = vocabulary.lexical_sense.run.verb.move_quickly
        ↓
officialize
        ↓
Official
id = vocabulary.lexical_sense.run.verb.move_quickly
```

Official sử dụng canonical atom structure. Không thêm các field như `status: official`, `approved_by`, hoặc `approved_at` vào canonical schema chỉ để biểu diễn lifecycle state.

### Lifecycle direction

Candidate có thể được review nhiều lần:

```text
pending ↔ rejected
        │
        └────→ official
```

Một Candidate đã officialize thì **không quay lại Candidate và không bị reject trở lại**.

Không cần lưu review history để biểu diễn lifecycle này. Chỉ cần trạng thái hiện tại của Candidate và semantic ID cố định của atom.

### Official correction

Một Official Atom có thể được sửa đổi hoặc refine để làm knowledge chính xác hơn.

Các thay đổi như sửa `meaning`, `explanation`, `structure`, `examples`, hoặc provenance không tự động tạo lifecycle state mới và không làm thay đổi semantic ID nếu knowledge identity vẫn là cùng một knowledge point.

Nếu một thay đổi làm knowledge identity thực sự thay đổi, đó là vấn đề về semantic identity và phải được xem xét riêng; không mặc định coi đó là một correction thông thường.

**→ Candidate / Official identity và lifecycle direction đã chốt.**

---

# 6. Review status

**Để mở và bàn riêng ở phần tiếp theo.**

Hiện tại chỉ chốt được vai trò tổng quát:

- `review_status` thuộc Candidate/review lifecycle, không thuộc knowledge ontology;
- nó không tạo semantic identity mới;
- Candidate phải có semantic ID trước khi review;
- Candidate bị reject có thể được review lại;
- Candidate đã officialize thì không quay lại trạng thái Candidate/rejected;
- chưa chốt danh sách giá trị chính thức, transition rules chi tiết, hay cách representation cụ thể của `review_status`.

Đây là phần tiếp theo cần đào sâu.
