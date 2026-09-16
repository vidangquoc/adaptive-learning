# Step 3 Review — Knowledge Atom Taxonomy + Structure

> **Status: OPEN — chưa chốt Step 3.**
>
> Đây là file để tao và mày bàn từng vấn đề. Những phần dưới đây là **đề xuất ban đầu của tao**, không phải quyết định của project.

## Mình sẽ xem từng phần một

Thứ tự tao đề xuất:

1. Atom là gì?
2. Atom khác property và relation thế nào?
3. Grammar taxonomy
4. Vocabulary taxonomy
5. `word_formation` và `morphological_form`
6. Các field của atom
7. `examples` và `related_atoms`
8. Semantic ID
9. Candidate / Official

Không cần giải quyết hết một lần.

---

# 1. Atom là gì?

### Vấn đề
Không phải thông tin nào trong sách cũng nên biến thành một atom.

Ví dụ với `assume`:

- `assume` có nghĩa gì → kiến thức chính → có thể là atom.
- `assume` thường đi với object → đặc điểm của atom → chưa chắc cần atom riêng.
- `assume` là formal → đặc điểm của atom → chưa chắc cần atom riêng.

### Đề xuất của tao
Tao nghiêng về nguyên tắc:

> **Một atom là một mẩu kiến thức có ý nghĩa tương đối độc lập và có thể trở thành một learning target riêng.**

Không nhất thiết phải có một câu hỏi test riêng mới được coi là atom.

Nhưng nếu tách một mẩu kiến thức ra mà nó không có giá trị học riêng, thì giữ nó làm property của atom khác.

**→ Cần mày xem và phản biện.**

---

# 2. Atom vs Property vs Relation

Tao nghĩ nên chia rất đơn giản thành 3 loại:

### Atom
Là **thứ cần học**.

Ví dụ:

```text
lex.assume
lex.compelling
```

### Property
Là **đặc điểm của một atom**.

Ví dụ:

```text
assume → formal
assume → transitive
assume → structure/pattern nào đó
```

### Relation
Là **mối quan hệ giữa hai atom**.

Ví dụ:

```text
assume → related_to → presume
assume → contrasts_with → suppose
```

### Đề xuất của tao
Mặc định:

> **Thứ gì tự nó là learning target → atom.**
>
> **Thứ gì chỉ mô tả atom khác → property.**
>
> **Thứ gì nối hai atom → relation.**

Đây có lẽ là nguyên tắc quan trọng nhất để giữ cho ontology không bị rối.

**→ Cần mày xem và phản biện.**

---

# 3. Grammar taxonomy

Hiện tại grammar có:

```text
form
meaning
use
pattern
rule
constraint
exception
```

### Vấn đề tao thấy
`rule` và `constraint` khá dễ đụng với field `constraints`.

Ví dụ:

```text
Present continuous thường dùng cho action đang xảy ra.
```

Đây có thể là một grammar atom.

Nhưng:

```text
Construction này không dùng được trong trường hợp X.
```

Có thể chỉ là constraint của atom.

### Đề xuất của tao
Tạm thời:

- `form`, `meaning`, `use`, `pattern` → khá rõ.
- `rule` → cần xem có thực sự cần là subtype hay không.
- `constraint` → tao **nghi ngờ nên bỏ khỏi subtype** nếu nó chỉ trùng với field `constraints`.
- `exception` → thường là property; chỉ thành atom nếu bản thân exception là một learning target đáng học.

Tao chưa muốn chốt taxonomy này.

**→ Đây là một trong những phần tao muốn mày phản biện kỹ.**

---

# 4. Vocabulary taxonomy

Hiện tại:

```text
lexical_sense
multiword_expression
phrasal_verb
idiom
collocation
word_formation
morphological_form
```

### Đề xuất của tao
Tao nghiêng về việc mỗi atom có **một type chính**.

`multiword_expression` có thể là loại fallback:

```text
phrasal verb → phrasal_verb
idiom → idiom
collocation → collocation
không thuộc các loại trên nhưng vẫn là một lexical unit nhiều từ
→ multiword_expression
```

Lý do: tao muốn tránh một atom phải có kiểu:

```text
type:
  - idiom
  - collocation
```

và sau đó phải xử lý hàng đống trường hợp chồng lấn.

Nhưng thứ tự ưu tiên giữa các loại vẫn cần xem bằng ví dụ thật.

**→ Chưa chốt.**

---

# 5. `word_formation` và `morphological_form`

Đây là chỗ tao nghĩ cần giữ ranh giới rõ.

### `morphological_form`
Nói về **các dạng của cùng một từ**.

Ví dụ:

```text
be → was / were
```

Không nên tạo atom riêng cho mọi dạng bình thường:

```text
walk → walked
```

### `word_formation`
Nói về **cách tạo lexical item mới**.

Ví dụ:

```text
assume → assumption
```

Nhưng tao nghĩ không phải cứ:

```text
A → B
```

là phải tạo một `word_formation` atom.

Nếu chỉ là quan hệ giữa hai từ thì có thể chỉ cần relation.

Nếu có một pattern có thể học và áp dụng lại, ví dụ một quy tắc tạo từ, thì mới đáng cân nhắc `word_formation` atom.

**→ Chưa chốt.**

---

# 6. Các field của atom

Schema hiện tại:

```yaml
id:
domain:
type:
subtype:

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

Tao nghĩ cần xem từng nhóm, không nên chốt cả schema một lúc.

### `meaning`
Tao đề xuất đây là **ý nghĩa / chức năng cốt lõi của kiến thức**.

### `mother_says`
Tao đề xuất đây là **cách giải thích bằng tiếng Việt cho người học**, tự nhiên và dễ hiểu hơn `meaning`.

### `explanation`
Tao đề xuất dùng cho **phần giải thích thêm**, nhưng không được biến thành cái thùng chứa mọi thứ.

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

**→ Đây là proposal, chưa chốt.**

---

# 7. `examples` và `related_atoms`

### `examples`
Tao nghiêng về việc xem example là **minh họa / evidence**, không phải atom.

Một câu ví dụ có thể minh họa nhiều atom cùng lúc.

Nếu câu ví dụ chứa một learning target khác thì learning target đó nên được extract riêng, thay vì biến cả câu thành atom.

### `related_atoms`
Tao muốn nó chỉ dùng để nói:

> Atom này có quan hệ gì với atom kia?

Ví dụ:

```yaml
related_atoms:
  - id: lex.assume
    relation: near_synonym_of
```

Sau này nếu data architecture cần tách relations thành bảng/file riêng thì vẫn được. Ý nghĩa của relation phải chỉ định một lần, không tạo hai hệ khác nhau.

**→ Chưa chốt.**

---

# 8. Semantic ID

Tao đề xuất ID phải nói về **knowledge**, không nói về nơi nó xuất hiện.

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

Tao cũng nghiêng về việc chỉ thêm phần cuối (`.duration`, `.case`, ...) khi thật sự cần phân biệt hai knowledge atom khác nhau.

**→ Chưa chốt.**

---

# 9. Candidate / Official

Tao nghĩ đây **không phải type của atom**.

Nó là trạng thái của quá trình xử lý:

```text
Evidence
  ↓
Candidate
  ↓
Review
  ↓
Official
```

Candidate có thể có thêm thông tin phục vụ review như:

```text
source span
confidence
warnings
validation status
review notes
```

Những thứ này không nên biến thành field bản chất của knowledge atom nếu chúng chỉ phục vụ extraction/review.

**→ Chưa chốt.**

---

# Các điểm tao muốn bàn kỹ nhất

Nếu phải chọn vài chỗ để bắt đầu, tao đề xuất bắt đầu từ:

1. **Atom là gì?**
2. **Atom vs Property vs Relation**
3. **Grammar: `rule` / `constraint` / `exception`**
4. **Vocabulary: MWE / idiom / collocation / phrasal verb**

Sau khi bốn chỗ này rõ thì những phần còn lại sẽ dễ hơn nhiều.

---

# Decision log

Chưa có quyết định nào được chốt trong Step 3.

> Mọi phần ghi là **Đề xuất của tao** chỉ là proposal để thảo luận. Chỉ khi tao và mày thống nhất thì mới cập nhật canonical docs và mới coi Step 3 là hoàn thành.
