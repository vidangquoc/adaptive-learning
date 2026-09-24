# Context Recovery Authoring Principles

## 1. Mục đích

File này định nghĩa các nguyên tắc chi phối việc **tạo, sửa, review và duy trì hệ thống context recovery** trong repository.

Đây là một **meta-level authoring specification**. Nó không phải recovery instruction và **không phải một bước trong quy trình khôi phục context thông thường**.

Các nguyên tắc trong file này được áp dụng khi AI được yêu cầu tạo mới, cập nhật, review, thiết kế lại hoặc tái cấu trúc các file thuộc hệ thống context recovery.

## 2. Các file trong hệ thống Context Recovery

Hệ thống context recovery gồm đúng bốn file:

- `context-recover/context-recover.md` — current conversation context recovery.
- `context-recover/project-knowledge-recover.md` — navigation/recovery procedure for project, learning-material / knowledge, and learner data.
- `context-recover/context-recovery-prompt.md` — user-facing recovery and verification prompts.
- `context-recover/context-recovery-authoring-principles.md` — meta-level authoring and maintenance rules.

Không tạo thêm một file verification/recovery snapshot chỉ để chứa project knowledge hoặc review state nếu vai trò đó đã thuộc một trong bốn file trên.

## 3. Authoring Principles

### CR-01 — Recovery Files Là Instructions, Không Phải Knowledge Stores

Recovery files MUST chủ yếu chỉ cho AI:

- cần khôi phục điều gì;
- cần tìm ở đâu;
- nguồn nào là authoritative;
- phải phân biệt các domain như thế nào;
- cần kiểm tra điều gì;
- phải xử lý thế nào khi thông tin thiếu hoặc mâu thuẫn.

Recovery files MUST NOT trở thành một kho project knowledge song song.

### CR-02 — Tách Authoring khỏi Execution

Các nguyên tắc trong file này chi phối **việc authoring và maintenance** của hệ thống recovery.

Quy trình recovery thông thường chỉ thực hiện các recovery instructions liên quan và không yêu cầu AI phải đọc file này như một bước recovery.

### CR-03 — Giữ đúng vai trò của từng file

Mỗi file phải có một trách nhiệm rõ ràng:

- `context-recovery-prompt.md` → prompt khôi phục và prompt kiểm tra cho người dùng.
- `context-recover.md` → current conversation context và điểm vào recovery.
- `project-knowledge-recover.md` → navigation/recovery procedure cho project knowledge, learning-material / knowledge data và learner data.
- `context-recovery-authoring-principles.md` → quy định cách tạo và duy trì chính hệ thống recovery.

Một file MUST NOT âm thầm tiếp nhận vai trò của file khác.

### CR-04 — Repository Là Source of Truth

Recovery instructions MUST hướng AI đến các nguồn authoritative trong repository khi độ chính xác phụ thuộc vào project state, data, implementation, provenance hoặc documented rules hiện tại.

Conversation memory và inference là nguồn phụ trợ và MUST NOT override repository evidence.

### CR-05 — Không Duplicate Authoritative Knowledge

Khi authoring recovery file, MUST NOT sao chép detailed project documentation, data inventories, learner state hoặc historical records chỉ để tiện sử dụng.

Recovery files nên chỉ đến thông tin authoritative thay vì tái tạo thông tin đó.

Context snapshot có thể chứa một lượng nhỏ thông tin cần thiết để nối tiếp conversation hiện tại, nhưng không được biến thành bản sao của project documentation.

### CR-06 — Giữ Domain Separation

Recovery instructions MUST giữ các domain sau độc lập:

- project knowledge;
- learning-material / knowledge data;
- learner / user learning data;
- current conversation context.

Đặc biệt, static knowledge MUST NOT bị nhầm với learner state hoặc historical learning activity.

### CR-07 — Progressive và Task-Driven Recovery

Recovery instructions SHOULD hướng AI khôi phục context theo từng bước, bắt đầu bằng lượng thông tin tối thiểu cần thiết cho task hiện tại và chỉ mở rộng khi cần.

Instructions SHOULD xác định các authoritative entry points và task-relevant sources thay vì yêu cầu AI đọc toàn bộ repository một cách không cần thiết.

### CR-08 — Recover Enough Context, Not Everything

Mục tiêu của recovery là cung cấp đủ thông tin để thực hiện task hiện tại một cách chính xác.

Khi authoring, SHOULD tránh các bước recovery không cần thiết làm tăng context size nhưng không cải thiện độ chính xác của task.

### CR-09 — Phải quy định Verification và Failure Handling

Recovery instructions SHOULD nêu rõ cách AI xử lý khi:

- thông tin bị thiếu;
- các source mâu thuẫn;
- repository state hiện tại khác với context được nhớ;
- không thể xác định chính xác một dữ liệu;
- không tìm thấy authoritative source.

Instructions SHOULD ưu tiên verification và thể hiện uncertainty rõ ràng thay vì đoán.

### CR-10 — Current Context Không Được Rewrite History

Recovery instructions MUST giữ khác biệt giữa historical records, current repository state và current conversation decisions.

Recovered conversation snapshot MUST NOT được xem là authoritative historical record.

### CR-11 — Recovery Phải Reproducible

Một AI session mới không có quyền truy cập conversation trước đó SHOULD có thể làm theo recovery instructions và tái tạo context cần thiết để tiếp tục công việc mà không phụ thuộc vào undocumented assumptions.

### CR-12 — Giữ Recovery System Stable và Minimal

Recovery files SHOULD chỉ thay đổi khi role, recovery procedure, verification requirements hoặc context structure liên quan thay đổi.

Project evolution SHOULD chủ yếu cập nhật authoritative project documentation và data, không tích lũy project knowledge vào recovery files.

## 4. Authoring Boundary

Khi tạo hoặc sửa một recovery file, cần xác định:

1. **File này chịu trách nhiệm về điều gì?**
2. **AI cần thực hiện hành động gì?**
3. **AI cần lấy thông tin ở đâu?**
4. **Nguồn nào là authoritative?**
5. **Phải xử lý ambiguity hoặc missing information như thế nào?**
6. **Nội dung đang viết là instruction, verification question, user-facing prompt hay actual project knowledge?**

Nếu nội dung là project knowledge thực tế, nó thường thuộc authoritative documentation hoặc data phù hợp thay vì recovery file.

Nếu nội dung là prompt khôi phục hoặc prompt kiểm tra dành cho người dùng, nó thuộc `context-recovery-prompt.md`.

Nếu nội dung là instruction để AI thực hiện recovery, nó thuộc recovery-instruction file phù hợp.
