# Step 3 Review — Knowledge Atom Taxonomy + Structure

> **Status: OPEN — chưa chốt Step 3.**
>
> Đây là file để tao và mày bàn từng vấn đề còn mở. Những phần dưới đây là **nội dung đang được review**, không phải quyết định cuối cùng của project.

## Các phần còn lại cần review

1. Các field của atom
2. Semantic ID
3. Candidate / Official
4. Review status

Các phần Candidate / Official và Review status bên dưới đã được chốt; chỉ các vấn đề còn lại của Step 3 mới tiếp tục mở.

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

**Đã chốt:** Candidate và Official là cùng một Knowledge Atom ở hai giai đoạn khác nhau của knowledge pipeline, nhưng **được lưu ở hai nơi khác nhau**.

```text
Learning Material
       ↓
Candidate Store
       ↓
     Review
       ↓
Officialize
       ↓
Official Store
```

### Candidate

Candidate là một Knowledge Atom hoàn chỉnh đã được hệ thống xác định và đưa vào Candidate Store để review.

**Đã chốt:** Candidate sử dụng **đầy đủ canonical atom schema giống Official**, chỉ thêm một field lifecycle là `review_status`.

Candidate không có schema knowledge riêng, không có `candidate_id`, và không có temporary/tracking ID. Semantic ID được tạo đúng ngay khi Candidate được tạo.

### Official

Official là Knowledge Atom đã được officialize và được lưu trong Official Store.

Official sử dụng chính canonical atom schema, không có `review_status` và không có các field review/lifecycle riêng như `candidate_id`, `approved_by`, hoặc `approved_at`.

Candidate và Official dùng **cùng semantic ID**. Officialization không tạo identity mới.

### Officialization

Bước `officialize` chỉ xử lý Candidate có:

```yaml
review_status: approved
```

Với mỗi Candidate phù hợp:

1. ghi Official Atom vào Official Store;
2. giữ nguyên semantic ID;
3. xóa Candidate khỏi Candidate Store.

Candidate `pending` và `rejected` không bị tác động.

Do Candidate được xóa sau khi officialize, Candidate Store **không có trạng thái `officialized`**.

### Lifecycle direction

```text
pending
   │
   ├────→ rejected ────→ review lại ────→ pending / approved / rejected
   │
   └────→ approved ────→ officialize ────→ Official Store
```

- Candidate mới tạo luôn bắt đầu ở `pending`.
- Reviewer có thể giữ `pending`, chọn `approved`, hoặc chọn `rejected`.
- `approved` chưa phải Official; nó chỉ là trạng thái chờ officialization.
- `rejected` có thể được review lại.
- Sau khi officialize, Candidate bị xóa khỏi Candidate Store và Official Atom tồn tại ở Official Store.
- Official Atom không quay lại Candidate/rejected lifecycle.
- Không cần lưu review history.

### Official correction

Official Atom có thể được sửa đổi hoặc refine để tăng độ chính xác.

Các thay đổi như sửa `meaning`, `explanation`, `structure`, `examples`, hoặc provenance không tự động tạo lifecycle state mới và không làm thay đổi semantic ID nếu knowledge identity vẫn là cùng một knowledge point.

Nếu thay đổi làm knowledge identity thực sự khác đi, đó là vấn đề về semantic identity và phải được xem xét riêng.

**→ Candidate / Official representation và lifecycle direction đã chốt.**

---

# 6. Review status

**Đã chốt.**

`review_status` chỉ tồn tại trên Candidate trong Candidate Store. Nó là lifecycle metadata, không phải knowledge ontology và không tham gia semantic identity.

### Giá trị chính thức

| Giá trị | Ý nghĩa |
|---|---|
| `pending` | Candidate mới tạo hoặc reviewer không thay đổi quyết định. |
| `approved` | Reviewer chấp thuận Candidate, nhưng Candidate vẫn ở Candidate Store cho đến khi officialize. |
| `rejected` | Reviewer từ chối Candidate; Candidate vẫn có thể được review lại. |

Không có `officialized` trong `review_status`. Khi officialize, Candidate được ghi sang Official Store rồi xóa khỏi Candidate Store.

### Review behavior

Khi reviewer xem xét một Candidate, có ba khả năng:

1. chọn `approved`;
2. chọn `rejected`;
3. không thay đổi gì, Candidate vẫn ở `pending`.

Reviewer không chuyển Candidate trực tiếp thành Official.

### Officialization behavior

Bước **officialize** chỉ xử lý những Candidate có:

```yaml
review_status: approved
```

Candidate được chuyển thành Official Atom trong Official Store với cùng semantic ID, sau đó bị xóa khỏi Candidate Store.

Candidate đang `pending` hoặc `rejected` không bị tác động.

### Lifecycle rule

- Candidate có thể được review lại sau khi `rejected`.
- `approved` là trạng thái chờ officialization, không phải Official.
- Officialization là storage transition, không phải reviewer decision.
- Candidate và Official sử dụng cùng semantic ID.
- Official Atom không quay lại Candidate hoặc `rejected`.

**→ Danh sách status và behavior của review/officialization đã chốt.**

