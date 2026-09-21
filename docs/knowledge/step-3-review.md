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

# 3. Semantic ID

Cần chốt quy tắc tạo ID sao cho ID nói về **knowledge**, không nói về nơi knowledge xuất hiện.

Ví dụ:

```text
lex.assume
lex.compelling
```

hoặc khi cần phân biệt:

```text
gram.present-perfect-continuous.duration
gram.present-perfect-continuous.recently-stopped-activity
```

Không nên có kiểu:

```text
atom-001
page-37-assume
unit1-exercise4
```

vì những thứ đó là provenance/source information, không phải identity của knowledge.

Cần tiếp tục chốt:

- khi nào cần thêm semantic case;
- quy tắc đặt tên case;
- mức độ ổn định cần có khi knowledge model thay đổi.

**→ Chưa chốt.**

---

# 4. Candidate / Official

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
