# Step 3 Review — Knowledge Atom Taxonomy + Structure

> **Status: OPEN — chưa chốt Step 3.**
>
> Đây là file để tao và mày bàn từng vấn đề còn mở. Những phần dưới đây là **nội dung đang được review**, không phải quyết định cuối cùng của project.

## Các phần còn lại cần review

1. Các field của atom
2. `examples` và `related_atoms`
3. Semantic ID
4. Candidate / Official

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
usage:
constraints:

examples:
related_atoms:

extra:
  source:
  is_tested:
  test_evidence:
  notes:
```

Cần xem từng field, không nên chốt cả schema một lúc.

### `meaning`

Tạm thời xem đây là **ý nghĩa / chức năng cốt lõi của kiến thức**.

### `mother_says`

Tạm thời xem đây là **cách giải thích bằng tiếng Việt cho người học**, tự nhiên và dễ hiểu hơn `meaning`.

### `explanation`

Dùng cho **phần giải thích thêm**, nhưng không được biến thành cái thùng chứa mọi thứ.

Nếu trong `explanation` xuất hiện một kiến thức có identity riêng thì phải xem nó có cần trở thành atom hay không.

### `structure`

**Nó được cấu tạo như thế nào?**

### `usage`

**Dùng khi nào / trong hoàn cảnh nào?**

### `constraints`

**Có giới hạn hay điều kiện gì?**

Một cách nhớ đơn giản:

```text
structure   → nó được tạo như thế nào?
usage       → dùng như thế nào / khi nào?
constraints → có giới hạn gì?
```

**→ Chưa chốt.**

---

# 2. `examples` và `related_atoms`

### `examples`

Cần xác định rõ example là **minh họa / evidence** đến mức nào và provenance của từng example được biểu diễn ra sao.

Một câu ví dụ có thể minh họa nhiều atom cùng lúc.

Nếu câu ví dụ chứa một learning target khác thì learning target đó nên được extract riêng, thay vì biến cả câu thành atom.

### `related_atoms`

Cần xác định chính xác field này dùng để biểu diễn những loại relation nào và relation được biểu diễn trực tiếp trong atom hay tách thành cấu trúc riêng.

Ví dụ:

```yaml
related_atoms:
  - id: lex.assume
    relation: near_synonym_of
```

**→ Chưa chốt.**

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
