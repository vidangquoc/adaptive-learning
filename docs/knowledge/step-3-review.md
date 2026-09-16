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
Điểm quan trọng đầu tiên là phải xác định rõ **Knowledge Atom là đơn vị gì**.

Tao và mày đang thống nhất theo hướng:

> **Knowledge Atom là một đơn vị kiến thức có ý nghĩa riêng, có thể được xác định, học và đánh giá như một learning target riêng.**

Ở đây có một điểm rất quan trọng:

### Knowledge Atoms là flat

Các atom **không tạo thành hierarchy**.

Tức là không có mô hình kiểu:

```text
Present perfect
├── present perfect + since
└── present perfect + for
```

trong đó `present perfect + since` và `present perfect + for` là các atom con của `present perfect`.

Thay vào đó, tất cả đều là những atom độc lập trong cùng một tập knowledge:

```text
present perfect
present perfect + since
present perfect + for
present perfect + ever
present perfect + never
```

Chúng có thể liên quan rất chặt với nhau, nhưng **quan hệ đó không tạo ra cấp bậc cha/con giữa các atom**.

Nếu cần biểu diễn mối liên hệ, ta dùng **relation**:

```text
present perfect
        │
        ├── related_to → present perfect + since
        └── related_to → present perfect + for
```

Relation ở đây chỉ mô tả mối liên hệ; nó không biến một atom thành parent của atom khác.

### Vì sao flat lại quan trọng?

Vì một knowledge unit có thể có **learning value riêng** dù nó liên quan hoặc phụ thuộc về mặt kiến thức vào atom khác.

Ví dụ:

```text
present perfect + since
present perfect + for
```

Hai cái này đều liên quan đến present perfect, nhưng người học vẫn cần biết riêng:

- dùng `since` như thế nào;
- dùng `for` như thế nào;
- phân biệt chúng trong ngữ cảnh;
- và có thể được kiểm tra riêng về mức độ thuần thục.

Vì vậy, không nên nói:

> “Nó chỉ là một đặc điểm của present perfect nên phải là property.”

Chỉ vì một kiến thức liên quan đến atom khác **không có nghĩa nó không thể là một atom riêng**.

### Atom không cần độc lập tuyệt đối

Một atom có thể dựa trên hoặc liên quan đến kiến thức khác mà vẫn là một atom.

Điều cần hỏi không phải là:

> “Nó có hoàn toàn độc lập với các kiến thức khác không?”

mà là:

> **“Nó có phải là một learning target riêng mà ta muốn học và đánh giá riêng không?”**

Nếu câu trả lời là có, nó có thể là một Knowledge Atom.

Ví dụ:

```text
present perfect
present perfect + since
present perfect + for
```

cả ba đều có thể là atom.

Chúng không cần nằm trong hierarchy để được xem là những đơn vị knowledge khác nhau.

### Một atom có thể rất nhỏ

Không nên đặt trước một giới hạn rằng atom phải là một “khối kiến thức lớn”.

Một atom có thể là:

```text
assume

present perfect + since

present perfect + for

một cách dùng cụ thể của một cấu trúc

một quy tắc ngữ pháp cụ thể
```

Miễn là nó đại diện cho một knowledge target có ý nghĩa và đáng được học/đánh giá riêng.

### Một atom cũng có thể liên quan đến nhiều atom khác

Ví dụ:

```text
present perfect
present perfect + since
present perfect + for
present perfect + duration
```

Không cần chọn một cái làm “cha” của những cái còn lại.

Ta giữ chúng flat rồi biểu diễn quan hệ giữa chúng khi cần.

### Nguyên tắc tạm thời

Tao đề xuất dùng nguyên tắc này:

> **Một Knowledge Atom là một đơn vị kiến thức có ý nghĩa riêng và có thể được xác định, học và đánh giá như một learning target riêng.**
>
> **Knowledge Atoms là flat: không có quan hệ hierarchy hoặc parent/child giữa các atom.**
>
> **Một atom có thể liên quan, phụ thuộc hoặc chồng lấn về mặt kiến thức với atom khác; điều đó không ngăn nó trở thành một atom riêng.**

**→ Đây là định nghĩa tao và mày vừa thống nhất về hướng. Các phần còn lại của Step 3 vẫn chưa chốt.**

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

Tuy nhiên, phần 1 vừa làm rõ một điểm cần xem lại: **một thông tin có liên quan đến atom khác vẫn có thể là atom riêng nếu nó có learning value và cần được đánh giá riêng.** Vì vậy, ranh giới Atom vs Property cần được bàn tiếp, không nên hiểu property là “bất cứ thứ gì mô tả một atom khác”.

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

Hiện tại vocabulary có:

```text
lexical_sense
multiword_expression
phrasal_verb
idiom
collocation
```

### `multiword_expression` là fallback

Tao và mày đồng ý theo hướng:

```text
phrasal verb
→ phrasal_verb

idiom
→ idiom

collocation
→ collocation

không thuộc các loại trên nhưng vẫn là một lexical unit nhiều từ
→ multiword_expression
```

Tức là `multiword_expression` đóng vai trò **fallback**, không phải là một nhãn cần cạnh tranh với `phrasal_verb`, `idiom` và `collocation` trong cùng một trường hợp.

Mục đích là tránh phải ép một lexical unit nhiều từ vào một category cụ thể khi nó không thực sự phù hợp với các loại chuyên biệt hơn.

Ví dụ:

```text
phrasal verb
→ phrasal_verb

idiom
→ idiom

collocation
→ collocation

một lexical unit nhiều từ khác
→ multiword_expression
```

Mỗi atom vẫn có **một type chính**.

**→ Phần `multiword_expression` fallback đã thống nhất về hướng.**

---

# 5. `word_formation` và `morphological_form`

Hai loại này **không thuộc Vocabulary domain**.

Tao và mày thống nhất đưa chúng sang **Grammar domain**. Vấn đề chi tiết về ranh giới giữa chúng và các subtype grammar khác sẽ giải quyết sau.

Vì vậy taxonomy hiện tại được hiểu là:

```text
Vocabulary
├── lexical_sense
├── multiword_expression
├── phrasal_verb
├── idiom
└── collocation

Grammar
├── form
├── meaning
├── use
├── pattern
├── rule
├── constraint
├── exception
├── word_formation
└── morphological_form
```

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

Nhưng không phải cứ:

```text
A → B
```

là phải tạo một `word_formation` atom.

Nếu chỉ là quan hệ giữa hai từ thì có thể chỉ cần relation.

Nếu có một pattern có thể học và áp dụng lại, ví dụ một quy tắc tạo từ, thì mới đáng cân nhắc `word_formation` atom.

**→ Việc đưa `word_formation` và `morphological_form` sang Grammar đã thống nhất. Ranh giới chi tiết với các subtype Grammar khác sẽ bàn sau.**

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

Đã có một số điểm được thống nhất trong quá trình review, nhưng **Step 3 vẫn chưa hoàn thành**.

Các điểm đã thống nhất/điều chỉnh trong phần đang review:

- Knowledge Atoms là flat, không có hierarchy/parent-child.
- Một knowledge unit vẫn có thể là atom riêng dù liên quan hoặc phụ thuộc vào atom khác, nếu nó là learning target riêng.
- `multiword_expression` là fallback cho lexical unit nhiều từ không thuộc `phrasal_verb`, `idiom` hoặc `collocation`.
- `word_formation` và `morphological_form` thuộc **Grammar domain**, không thuộc Vocabulary domain.

> Mọi phần khác vẫn tiếp tục là nội dung để tao và mày thảo luận. Chỉ khi tao và mày thống nhất thì mới cập nhật canonical docs và mới coi Step 3 là hoàn thành.
