# Context Recovery Prompt

## Mục đích

File này chứa **prompt mở đầu dùng để bắt đầu một hội thoại mới và yêu cầu AI khôi phục context của project**.

Nó là điểm vào dành cho **người dùng**, không phải recovery instruction mà AI phải tự đọc trong quá trình recovery.

Prompt này được thiết kế để AI bắt đầu từ `context-recover/context-recover.md` và thực hiện đúng hệ thống context recovery của repository.

## Prompt

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
- những điểm nào còn thiếu, chưa chắc chắn hoặc cần xác minh thêm.

Không cần đọc `context-recovery-authoring-principles.md` trong quá trình recovery thông thường. File đó chỉ được sử dụng khi tạo, sửa, review hoặc thiết kế lại hệ thống recovery.
```

## Cách sử dụng

Trong một hội thoại mới, copy toàn bộ prompt ở trên và gửi cho AI.

Sau khi AI hoàn tất recovery, có thể dùng `context-recover/context-recover-verification.md` để đặt các câu hỏi kiểm tra xem context đã được khôi phục đúng và đủ hay chưa.
