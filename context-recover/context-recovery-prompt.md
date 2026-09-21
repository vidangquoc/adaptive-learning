# Context Recovery Prompt

## Mục đích

File này chứa các **prompt dành cho người dùng** khi làm việc với hệ thống context recovery của project.

Các prompt được chia thành hai nhóm:

1. **Prompt khôi phục** — dùng khi bắt đầu một hội thoại mới hoặc khi cần khôi phục lại context.
2. **Prompt kiểm tra** — dùng sau khi recovery để kiểm tra xem AI đã khôi phục context đúng và đủ hay chưa.

File này là điểm vào dành cho **người dùng**. Nó không phải recovery instruction mà AI phải tự đọc trong quá trình recovery.

---

# 1. Prompt khôi phục

Dùng prompt này khi bắt đầu một hội thoại mới và muốn AI khôi phục context của project.

```text
Hãy khôi phục context của project từ GitHub repository `vidangquoc/adaptive-learning`.

Bắt đầu bằng cách đọc:
`context-recover/context-recover.md`

Sau đó thực hiện quy trình recovery được hướng dẫn trong các recovery files liên quan để khôi phục:

1. context của cuộc hội thoại hiện tại;
2. hiểu biết cần thiết về project;
3. learning-material / knowledge data;
4. learner / user learning data.

Hãy sử dụng repository và các nguồn authoritative được recovery instructions chỉ ra làm nguồn sự thật. Không đoán hoặc tự tạo thông tin khi repository chưa cung cấp đủ bằng chứng.

Chỉ đọc thêm các tài liệu, data, source hoặc implementation liên quan đến context và task cần khôi phục; không cần đọc toàn bộ repository một cách không cần thiết.

Sau khi hoàn tất recovery, hãy báo cáo ngắn gọn:
- context nào đã được khôi phục;
- những nguồn chính đã được sử dụng;
- những điểm nào còn thiếu, chưa chắc chắn hoặc cần xác minh thêm;
- task hiện tại đang dừng ở đâu và cần tiếp tục từ đâu.

Không cần đọc `context-recovery-authoring-principles.md` trong quá trình recovery thông thường. File đó chỉ được sử dụng khi tạo, sửa, review hoặc thiết kế lại hệ thống recovery.
```

---

# 2. Prompt kiểm tra

Các prompt dưới đây dùng **sau khi AI đã thực hiện recovery**. Mục đích là kiểm tra xem AI có thực sự khôi phục được context cần thiết hay không.

Không cần yêu cầu AI đọc file này như một bước của recovery. Đây là các câu hỏi để người dùng trực tiếp đặt cho AI.

## 2.1. Kiểm tra hiểu biết về project

> Hãy tóm tắt ngắn gọn project Adaptive Learning. Project đang cố gắng giải quyết vấn đề gì? Các thành phần khái niệm chính của hệ thống là gì và chúng liên hệ với nhau như thế nào?

**Mục đích kiểm tra:**

Câu trả lời phải thể hiện được hiểu biết nhất quán về project, không nhầm lẫn project với một domain hoặc một nguồn dữ liệu cụ thể, đồng thời không dựa trên những giả định không có căn cứ.

## 2.2. Kiểm tra hiểu biết về learning-material / knowledge data

> Hãy mô tả dữ liệu knowledge hiện đang có trong repository. Knowledge được tổ chức như thế nào? Hiện có những loại knowledge atom nào? Nếu cần đưa ra số lượng cụ thể, hãy lấy số liệu trực tiếp từ dữ liệu authoritative trong repository và cho biết nguồn đã sử dụng.

**Mục đích kiểm tra:**

Câu trả lời phải dựa trên dữ liệu hiện tại của repository, không sử dụng các con số được nhớ từ những cuộc hội thoại trước.

AI phải phân biệt được:

- source / evidence;
- curated knowledge;
- knowledge atoms;
- relations;
- assessments;
- learner data.

Nếu repository không đủ thông tin để xác định chính xác một số liệu, AI phải nói rõ điều đó thay vì ước lượng hoặc tự tạo số liệu.

## 2.3. Kiểm tra hiểu biết về learner data

> Hãy mô tả ngắn gọn learner data hiện đang được lưu trong repository. Có những loại thông tin nào về learner? Learning activity hoặc history nào được ghi nhận? Learner state được duy trì như thế nào? Learner state liên hệ với knowledge atoms ra sao?

**Mục đích kiểm tra:**

Câu trả lời phải thể hiện rằng AI hiểu learner data là một domain riêng biệt với static knowledge.

AI phải phân biệt được:

- learner profile;
- historical attempts;
- sessions / learning activity;
- current learner state;
- review queue.

Khi cần giải thích learner state, AI phải có thể liên hệ state với knowledge-atom IDs tương ứng.

## 2.4. Kiểm tra khả năng phân biệt các domain

> Hãy phân biệt rõ bốn loại context sau trong Adaptive Learning:
>
> 1. project knowledge;
> 2. learning-material / knowledge data;
> 3. learner / user learning data;
> 4. current conversation context.
>
> Với mỗi loại, hãy cho biết nó trả lời câu hỏi gì và nguồn nào là authoritative đối với nó.

**Mục đích kiểm tra:**

AI không được trộn lẫn kiến thức về project, dữ liệu về thứ cần học, dữ liệu về learner và context của cuộc hội thoại hiện tại.

## 2.5. Kiểm tra nguồn của thông tin

> Với những thông tin quan trọng trong các câu trả lời trên, hãy cho biết AI đã dựa vào những file hoặc nguồn authoritative nào trong repository để khôi phục chúng. Phân biệt thông tin được đọc trực tiếp từ repository với thông tin chỉ được suy luận hoặc chưa xác định được.

**Mục đích kiểm tra:**

Kiểm tra khả năng truy nguyên nguồn và phát hiện những phần context mà AI đang giả định thay vì thực sự xác minh.

## 2.6. Kiểm tra khả năng tiếp tục công việc đang review

> Hãy cho biết công việc hiện tại đang ở bước nào, những quyết định nào đã được thống nhất, những điểm nào vẫn chưa chốt, và tôi nên tiếp tục từ đâu.

**Mục đích kiểm tra:**

AI phải phân biệt được quyết định đã thống nhất trong conversation/review với proposal chưa chốt và canonical project decisions trong authoritative docs.

AI không được tự đánh dấu Step 3 hoàn thành chỉ vì đã có một số quyết định trung gian.

## 2.7. Kiểm tra nguồn của quyết định

> Với từng quyết định quan trọng được nói là đã thống nhất, hãy cho biết quyết định đó đang nằm ở đâu: conversation/review state hay canonical project documentation. Nếu chỉ có trong review/conversation thì không được trình bày nó như một canonical rule của project.

**Mục đích kiểm tra:**

Đảm bảo recovery không biến working discussion thành authoritative project knowledge.

## 2.6. Nguyên tắc đánh giá

Khi đánh giá câu trả lời của AI:

1. **Dựa trên repository hiện tại.** Các câu trả lời phải phản ánh trạng thái hiện tại của repository khi câu hỏi yêu cầu thông tin hiện tại.
2. **Không dùng trí nhớ thay cho dữ liệu.** Context từ cuộc hội thoại trước có thể giúp định hướng recovery nhưng không thay thế authoritative source.
3. **Không bịa dữ liệu.** Nếu không xác định được thông tin, AI phải nói rõ là chưa xác định được.
4. **Không nhầm domain.** Project knowledge, learning-material / knowledge data, learner data và conversation context phải được phân biệt rõ.
5. **Số liệu phải có nguồn.** Những con số hoặc inventory cụ thể phải được lấy từ nguồn dữ liệu authoritative khi có thể.
6. **Phân biệt fact và inference.** AI phải phân biệt thông tin đã xác minh với thông tin suy luận.
7. **Phát hiện thiếu context.** Nếu câu trả lời cho thấy một phần context chưa được recover đầy đủ, cần quay lại recovery procedure và đọc thêm authoritative sources trước khi tiếp tục công việc.

8. **Không tự chốt Step 3.** Step 3 chỉ hoàn thành khi người dùng và AI đã thống nhất và người dùng quyết định chốt.

### Điều kiện đạt

Context recovery được xem là đạt khi AI có thể trả lời các câu hỏi một cách nhất quán, dựa trên evidence phù hợp, không đưa ra các giả định không có căn cứ, và giữ đúng ranh giới giữa các domain.

---

## Cách sử dụng

Trong hội thoại mới:

1. Copy **Prompt khôi phục** và gửi cho AI.
2. Chờ AI hoàn tất recovery.
3. Dùng các **Prompt kiểm tra** để kiểm tra chất lượng recovery nếu cần.
4. Nếu phát hiện thiếu hoặc sai context, yêu cầu AI quay lại recovery procedure và bổ sung việc xác minh từ các nguồn authoritative.
