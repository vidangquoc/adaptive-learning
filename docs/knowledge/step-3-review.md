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

# 3. `extra.source`

`extra.source` là provenance của Atom, dùng để truy nguyên Atom về source evidence.

**Đã chốt semantic contract:**

- phải truy nguyên được về source artifact;
- phải xác định được canonical Segment chứa evidence;
- phải xác định được precise location/span của supporting evidence trong Segment khi thông tin đó có sẵn;
- một Atom có thể có nhiều provenance records nếu có nhiều source evidence cùng hỗ trợ Atom;
- `source` chỉ là provenance, không chứa knowledge content, learner state, hay definition/explanation được normalize vào Atom;
- `source` không thay thế `extra.test_evidence`.

Cấu trúc machine-readable cụ thể của provenance chưa chốt; sẽ xử lý ở bước schema sau.

**→ Đã chốt semantic contract; serialization chưa chốt.**

---

# 4. Semantic ID

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
