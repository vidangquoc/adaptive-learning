# Kiểm tra Context Recovery

## Mục đích

File này chứa các **câu hỏi kiểm tra bằng tiếng Việt** để người dùng hỏi AI sau khi AI đã khôi phục context.

Nó không phải là hướng dẫn để AI tự động thực thi trong quá trình recovery.

Mục đích của các câu hỏi là kiểm tra xem AI có:

- khôi phục đúng context cần thiết hay chưa;
- hiểu đúng project hay chưa;
- phân biệt đúng các domain dữ liệu hay chưa;
- dựa vào nguồn authoritative thay vì suy đoán hay không.

## Cách sử dụng

Sau khi AI đã thực hiện context recovery, người dùng có thể đặt các câu hỏi dưới đây cho AI.

Không yêu cầu AI phải đọc file này như một bước bắt buộc của recovery. Đây là **bộ câu hỏi kiểm tra**, không phải recovery procedure.

## Các câu hỏi kiểm tra

### 1. Kiểm tra hiểu biết về project

**Câu hỏi:**

> Hãy tóm tắt ngắn gọn project Adaptive Learning. Project đang cố gắng giải quyết vấn đề gì? Các thành phần khái niệm chính của hệ thống là gì và chúng liên hệ với nhau như thế nào?

**Mục đích kiểm tra:**

Câu trả lời phải thể hiện được hiểu biết nhất quán về project, không nhầm lẫn project với một domain hoặc một nguồn dữ liệu cụ thể, đồng thời không dựa trên những giả định không có căn cứ.

---

### 2. Kiểm tra hiểu biết về learning-material / knowledge data

**Câu hỏi:**

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

---

### 3. Kiểm tra hiểu biết về learner data

**Câu hỏi:**

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

---

### 4. Kiểm tra khả năng phân biệt các domain

**Câu hỏi:**

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

---

### 5. Kiểm tra nguồn của thông tin

**Câu hỏi:**

> Với những thông tin quan trọng trong các câu trả lời trên, hãy cho biết AI đã dựa vào những file hoặc nguồn authoritative nào trong repository để khôi phục chúng. Phân biệt thông tin được đọc trực tiếp từ repository với thông tin chỉ được suy luận hoặc chưa xác định được.

**Mục đích kiểm tra:**

Kiểm tra khả năng truy nguyên nguồn và phát hiện những phần context mà AI đang giả định thay vì thực sự xác minh.

## Nguyên tắc đánh giá

1. **Dựa trên repository hiện tại.** Các câu trả lời phải phản ánh trạng thái hiện tại của repository khi câu hỏi yêu cầu thông tin hiện tại.
2. **Không dùng trí nhớ thay cho dữ liệu.** Context từ cuộc hội thoại trước có thể giúp định hướng recovery nhưng không thay thế authoritative source.
3. **Không bịa dữ liệu.** Nếu không xác định được thông tin, AI phải nói rõ là chưa xác định được.
4. **Không nhầm domain.** Project knowledge, learning-material / knowledge data, learner data và conversation context phải được phân biệt rõ.
5. **Số liệu phải có nguồn.** Những con số hoặc inventory cụ thể phải được lấy từ nguồn dữ liệu authoritative khi có thể.
6. **Phân biệt fact và inference.** AI phải phân biệt thông tin đã xác minh với thông tin suy luận.
7. **Phát hiện thiếu context.** Nếu câu trả lời cho thấy một phần context chưa được recover đầy đủ, cần quay lại recovery procedure và đọc thêm authoritative sources trước khi tiếp tục công việc.

## Điều kiện đạt

Context recovery được xem là đạt khi AI có thể trả lời các câu hỏi một cách nhất quán, dựa trên evidence phù hợp, không đưa ra các giả định không có căn cứ, và giữ đúng ranh giới giữa các domain.
