> **Status: OPEN**
>
> File này chỉ dùng để theo dõi các vấn đề **chưa chốt** trong Step 3. Những quyết định đã chốt phải được lưu trong các canonical docs tương ứng.

## Các phần còn open

1. **Các field của atom** — chỉ còn những field chưa được chốt semantics.
2. **Taxonomy domain/type** — rà soát các type còn chồng lấn hoặc chưa có decision rule đủ rõ.
3. **Các boundary còn lại giữa Atom / Property / Relation** nếu phát sinh trong quá trình rà soát taxonomy.

Các quyết định đã chốt về schema, semantic ID, Candidate / Official và review status đã được loại khỏi review log này và nằm trong canonical docs.

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

