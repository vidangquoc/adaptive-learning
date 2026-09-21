# Step 3 Review — Knowledge Atom Taxonomy + Structure

> **Status: OPEN — chưa chốt Step 3.**
>
> Đây là file để tao và mày bàn từng vấn đề còn mở. Những phần dưới đây là **nội dung đang được review**, không phải quyết định cuối cùng của project.

## Các phần còn lại cần review

1. Các field của atom
2. Semantic ID
3. Candidate / Official

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

Cấu trúc đang xem xét và tạm thời sử dụng:

```text
<domain>.<type>.<name>
```

Ví dụ:

```text
vocabulary.lexical_sense.assume
vocabulary.collocation.strike_a_balance
grammar.use.present_simple.current_habit
grammar.use.present_perfect.past_to_present
```

Đã đồng ý rằng `name` là semantic identifier của knowledge object và có thể chứa thêm các component phân cách bằng `.` khi cần biểu diễn semantic distinction. Điều này **không tạo ra tầng `subtype`**.

Tuy nhiên, Semantic ID **chưa được chốt** vì cần làm rõ trước cách xác định semantic identity của `lexical_sense`, đặc biệt là ranh giới giữa các lexical senses và cách đặt `name` cho chúng.

**→ Tạm thời để OPEN.**

---

# 5. Candidate / Official

Cần xác định Candidate / Official là **trạng thái của knowledge trong pipeline** hay có ảnh hưởng đến canonical atom structure.

Mô hình đang xem xét:

```text
Evidence
  ↓
Candidate
  ↓
Review
  ↓
Official
```

Candidate có thể cần thông tin phục vụ review như:

```text
source span
confidence
warnings
validation status
review notes
```

Cần xác định:

- những thông tin nào thuộc candidate/review layer;
- khi nào candidate trở thành official;
- official atom có cần lưu trạng thái này hay không;
- provenance và validation evidence được liên kết như thế nào.

**→ Chưa chốt.**
