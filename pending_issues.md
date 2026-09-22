# Pending Issues

## Next steps after Step 3

1. **Formal Atom Schema**
   - Rà soát/cập nhật `schemas/` để phản ánh đầy đủ canonical Atom Structure.
   - Bao gồm `part_of_speech` và `pronunciation`, chỉ áp dụng cho `vocabulary.lexical_sense`.
   - Candidate dùng canonical schema + `review_status: pending | approved | rejected`.

2. **Taxonomy Decision Rules**
   - Rà soát `atom-types.md` để bảo đảm mỗi `domain/type` có decision rule đủ rõ cho extraction/implementation.
   - Đặc biệt: vocabulary type boundaries và grammar `rule/use/exception/word_formation/morphological_form`.

3. **Test Fixtures**
   - Tạo fixtures để kiểm tra extraction và atomization từ source thật.
   - Bao phủ: multi-sense, vocabulary type ambiguity, grammar rule/use, split/merge, property→atom khi trực tiếp tested, một exercise test nhiều atoms, nhiều source spans → một atom, và semantic ID stability.

4. **Knowledge Extraction / Pipeline**
   - Sau khi schema và taxonomy rules ổn định, triển khai/kiểm thử pipeline:
     `source → evidence → Candidate → validation → review → Official`.

5. **Assessment Model**
   - Tiếp tục thiết kế assessment model sau khi Knowledge Atom pipeline ổn định.

6. **Learner State**
   - Thiết kế learner state sau knowledge + assessment, không làm sớm hơn để tránh phụ thuộc vào schema chưa ổn định.

7. **Adaptive Algorithm**
   - Thiết kế adaptive decision/next-activity logic sau khi learner state đã ổn định.
