# PTNK Context Recovery Prompts

> Mục đích: dùng file này để khôi phục nhanh ngữ cảnh làm việc nếu cuộc hội thoại hiện tại bị chặn, mất ngữ cảnh, hoặc phải chuyển sang một cuộc hội thoại mới.

## 1. Prompt khôi phục đầy đủ — dùng trước tiên

```text
Tao đang tiếp tục project PTNK của tao. Hãy đọc và dùng các file trong repo GitHub `vidangquoc/PTNK`, đặc biệt:
- `docs/data-collection-rules.md`
- `docs/methodology.md`
- `docs/vocabulary-profile.md`
- các file dữ liệu trong `data/`
- `sources/ptnk-2026/README.md`

Hãy coi `docs/data-collection-rules.md` là source of truth cho nguyên tắc thu thập và chuẩn hóa dữ liệu.

Ngữ cảnh quan trọng:
- Mục tiêu là xây dựng một learning dataset từ vựng tiếng Anh phục vụ ôn thi chuyên Anh PTNK, không phải generic C1/C2 word list và không phải training data cho AI.
- Dataset và flashcard program là hai thứ khác nhau: dataset là content/knowledge source; Google Sheet + flashcard program là learning engine.
- Flashcard program của tao đã hoạt động tương đối hoàn chỉnh và dùng giao diện rất đơn giản `Nhớ / Quên`; không đề xuất chuyển sang Anki nếu tao không hỏi.
- Google Sheet hiện được tổ chức theo priority `P1 / P2 / P3 / P4`, không chia tab theo word type.
- Vocabulary, expression, idiom, phrasal verb, collocation đều nằm trong cùng một Lexicon; `word_type` dùng các mã đơn giản như `n`, `v`, `adj`, `adv`, `exp`, `idi`.
- Word Formation không có sheet riêng; answer của word formation được đưa vào Lexicon như lexical item bình thường, với `word_formation` là metadata nếu cần.
- Schema hiện tại:
  `id | word | word_type | pronunciation | meaning_en | meaning_vi | examples | patterns | usage_note | priority | word_formation | ptnk_evidence | source_quality`
- `examples` dùng dấu `|` để phân cách nhiều ví dụ.
- Mỗi lexical item có tối thiểu 3 ví dụ ngắn, tự nhiên, khoảng 5–10 từ khi có thể.
- `patterns` là field riêng. Chỉ ghi genuine collocations / grammatical or lexical patterns có giá trị học và có bằng chứng; tuyệt đối không biến patterns thành danh sách synonym/paraphrase hay các combination đoán mò.
- `ptnk_evidence` và provenance phải được giữ rõ ràng.
- Không tự bịa CEFR. Nếu chưa verify thì ghi rõ chưa xác minh.
- Priority phản ánh giá trị học cho PTNK, không phải độ khó thuần túy. P4 vẫn giữ trong dataset nhưng có thể không vào default flashcard queue.
- Nguyên tắc cốt lõi: evidence over intuition; accuracy over completeness; useful patterns over long lists; PTNK relevance over generic difficulty; simple learner experience over unnecessary complexity.

Trước khi làm việc tiếp, hãy kiểm tra repo hiện tại và tóm tắt ngắn trạng thái dữ liệu/schema/rules mà mày tìm thấy. Nếu có khác biệt giữa ngữ cảnh prompt này và repo, ưu tiên repo và chỉ ra khác biệt.
```

## 2. Prompt khôi phục nhanh — khi chỉ cần tiếp tục công việc

```text
Tiếp tục project PTNK của tao. Đọc `docs/data-collection-rules.md` trong repo `vidangquoc/PTNK` và coi đó là source of truth. Sau đó kiểm tra dữ liệu hiện tại trước khi sửa/thêm gì.

Nhớ các nguyên tắc: PTNK-specific learning dataset; Lexicon thống nhất cho word/expression/idiom/phrasal verb/collocation; P1–P4 là priority; Word Formation chỉ là metadata; mỗi word có English definition + Vietnamese meaning + IPA + ít nhất 3 ví dụ ngắn + patterns riêng; patterns chỉ là collocations/structures có bằng chứng, không phải synonym/paraphrase; không bịa CEFR/provenance.

Hãy tiếp tục từ trạng thái hiện tại của repo, không tự tạo lại schema khác.
```

## 3. Prompt khi đang làm vocabulary v0.3

```text
Tao đang xây PTNK Lexicon v0.3. Hãy lấy dữ liệu hiện có trong `vidangquoc/PTNK` làm nguồn đầu vào và tuân thủ `docs/data-collection-rules.md`.

Với mỗi lexical item cần chuẩn hóa:
- `word`: canonical lexical item
- `word_type`: n / v / adj / adv / exp / idi (chỉ dùng loại phù hợp)
- `pronunciation`: American English IPA
- `meaning_en`: định nghĩa tiếng Anh ngắn, chính xác
- `meaning_vi`: nghĩa tiếng Việt phù hợp với sense đang xét
- `examples`: ít nhất 3 câu ngắn, tự nhiên, hữu ích cho người học
- `patterns`: chỉ genuine collocations/patterns; không đưa paraphrase hoặc synonym vào đây
- `usage_note`: chỉ khi thực sự cần để phân biệt cách dùng
- `priority`: P1–P4 dựa trên giá trị học cho PTNK
- `word_formation`: chỉ điền khi item là kết quả/đối tượng của word formation
- `ptnk_evidence`: năm + section + question/nguồn
- `source_quality`: phản ánh đúng chất lượng nguồn, không nâng cấp provenance.

Nếu một expression đã có trong expression/idiom data thì không tách nó thành vocabulary word một cách sai lệch. Ví dụ `run errands` là expression/collocation, còn `errand` là noun.
```

## 4. Prompt kiểm tra một entry trước khi đưa vào dataset

```text
Hãy audit lexical item này theo rulebook PTNK hiện tại. Kiểm tra lần lượt:
1. canonical form có đúng không;
2. word_type có đúng không;
3. English definition có đúng sense không;
4. Vietnamese meaning có khớp sense không;
5. IPA có hợp lý không;
6. ít nhất 3 examples có tự nhiên và ngắn không;
7. patterns có phải genuine collocations/structures không;
8. patterns có vô tình chỉ là synonym/paraphrase không;
9. PTNK evidence/provenance có chính xác không;
10. priority P1–P4 có hợp lý không;
11. có trùng lexical item/sense với dữ liệu hiện có không.

Không được tự bịa evidence, CEFR hoặc collocation. Nếu không chắc, đánh dấu cần verify thay vì đoán.
```

## 5. Prompt khi cần tiếp tục từ một exam cụ thể

```text
Tao muốn tiếp tục khai thác lexical evidence từ đề PTNK [NĂM]. Hãy trước hết đọc `sources/ptnk-[NĂM]/README.md` và dữ liệu hiện có trong repo.

Mục tiêu không phải gom tất cả từ khó. Hãy phân loại lexical evidence thành các nhóm có giá trị cho PTNK: advanced general vocabulary, idioms/fixed expressions, phrasal verbs, collocations/patterns, word families/word formation, và topic-specific recognition vocabulary.

Giữ provenance tới năm + section + question khi có thể. Không tự nâng một từ topic-specific thành P1 chỉ vì nó khó.
```

## 6. Prompt khôi phục tư duy về priority

```text
Nhắc lại và áp dụng đúng priority model của PTNK:
- P1 = Core: nên học trước; advanced general vocabulary, high-value idioms/fixed expressions, phrasal verbs, collocations, word families và lexical patterns có giá trị rõ cho PTNK.
- P2 = Important: hữu ích và đáng học nhưng thấp hơn P1.
- P3 = Recognition: nên nhận biết/đọc hiểu, giá trị học thuộc thấp hơn.
- P4 = Low/specialized: hiếm, rất chuyên biệt hoặc giá trị học thấp; vẫn giữ trong dataset nhưng không nhất thiết vào default flashcard queue.

Priority không đồng nghĩa với difficulty. Không xóa P3/P4 chỉ vì chúng không phải default learning queue.
```

## 7. Prompt khôi phục kiến trúc học tập

```text
Giữ đúng kiến trúc của project PTNK:
`PTNK exam corpus → curated learning dataset → P1/P2/P3/P4 → Google Sheet → flashcard program → spaced repetition → learner progress`.

Spaced repetition trả lời câu hỏi “khi nào ôn lại?”. Adaptive testing là khái niệm khác, trả lời “câu tiếp theo nên hỏi gì dựa trên năng lực hiện tại?”. Không cần xây adaptive testing nếu tao không yêu cầu.

Flashcard UI cố ý chỉ có `Nhớ / Quên`. Complexity nên nằm ở algorithm/backend, không đẩy thêm lựa chọn đánh giá vào learner UI.
```

## 8. Prompt khi cần chỉnh sửa file/repo

```text
Trước khi sửa bất kỳ file nào trong repo `vidangquoc/PTNK`, hãy đọc file hiện tại và xác định schema/version đang dùng. Không overwrite dữ liệu chỉ dựa trên trí nhớ của cuộc hội thoại.

Nếu thay đổi rule/schema, phải nói rõ đó là thay đổi version/rule. Nếu chỉ sửa dữ liệu, giữ nguyên schema hiện hành. Sau khi sửa, báo rõ file nào thay đổi và commit/message nếu có.
```

## 9. Prompt tối thiểu nếu cuộc hội thoại mới hoàn toàn không còn context

```text
Tao có project GitHub `vidangquoc/PTNK` để xây dựng bộ dữ liệu từ vựng phục vụ ôn thi chuyên Anh PTNK. Hãy đọc repo trước khi trả lời.

File quan trọng nhất là `docs/data-collection-rules.md`. Đây là source of truth. Hãy đọc nó, sau đó đọc README/methodology liên quan, rồi báo cho tao mày đã khôi phục được những gì. Đừng tự suy đoán schema hoặc quy tắc nếu repo đã có quy định.
```

## 10. Golden rule

```text
Khi ngữ cảnh bị thiếu, đừng cố nhớ bằng suy đoán. Hãy đọc `docs/data-collection-rules.md` + dữ liệu hiện tại trong repo trước, rồi mới tiếp tục. Evidence > intuition; accuracy > completeness; PTNK relevance > generic difficulty; useful patterns > long lists; simple learner experience > unnecessary complexity.
```

---

## Current project snapshot

- Repository: `vidangquoc/PTNK`
- Rulebook: `docs/data-collection-rules.md`
- Current conceptual target: PTNK Lexicon v0.3
- Google Sheet architecture: `P1 / P2 / P3 / P4`
- Unified Lexicon: words + expressions + idioms + phrasal verbs + collocations
- Word Formation: metadata, not a separate sheet
- Learner UI: `Nhớ / Quên`
- Spaced repetition: existing learning engine
- Adaptive testing: separate concept; not required unless explicitly requested
