# Ai360Hub - Thông báo Quan trọng & Hướng dẫn Sử dụng

Chào mừng bạn đến với Ai360Hub! Để đảm bảo bạn có trải nghiệm tốt nhất và an toàn nhất, vui lòng đọc kỹ các thông tin quan trọng dưới đây trước khi sử dụng.

---

## ⚠️ Lưu ý Quan trọng về Cảnh báo Bảo mật (Antivirus & Windows Defender)

Chúng tôi cam kết ứng dụng Ai360Hub **HOÀN TOÀN SẠCH VÀ AN TOÀN**. Ứng dụng không chứa virus, mã độc, phần mềm gián điệp hay bất kỳ thành phần nào gây hại cho máy tính của bạn.

Tuy nhiên, một số phần mềm diệt virus hoặc tính năng Windows Defender có thể hiển thị cảnh báo "hiểu lầm" (cảnh báo giả - false positive) khi bạn tải về hoặc sử dụng một số tính năng.

### Tại sao lại có cảnh báo này?

1.  **Ứng dụng Mới:** Ai360Hub là một dự án mới và chưa được các hãng phần mềm bảo mật lớn đưa vào "danh sách trắng" (whitelist) của họ.
2.  **Đóng gói bằng Python:** Ứng dụng được viết bằng ngôn ngữ Python và đóng gói thành file `.exe`. Một số phần mềm bảo mật có xu hướng "nghi ngờ" các file được tạo ra theo cách này vì kỹ thuật tương tự cũng bị các phần mềm độc hại lạm dụng.
3.  **Hành vi Ghi File Tạm:** Một số tính năng như Text-to-Speech (TTS) cần tạo và ghi các file âm thanh tạm thời vào thư mục Temp của hệ thống. Tính năng chống mã độc tống tiền (anti-ransomware) của Windows hoặc các AV khác có thể coi đây là hành vi đáng ngờ và chủ động chặn lại.

### ✅ Cách xử lý khi gặp cảnh báo

Nếu bạn gặp lỗi (đặc biệt là lỗi `PermissionError` - Lỗi Quyền Truy Cập) hoặc cảnh báo từ phần mềm bảo mật, đây là cách giải quyết an toàn và hiệu quả nhất:

**Giải pháp 1: Thêm Ai360Hub vào Danh sách Ngoại lệ (Exclusion/Whitelist)**

Đây là cách làm được khuyến nghị. Bằng cách này, bạn cho phép phần mềm bảo mật "tin tưởng" Ai360Hub và bỏ qua việc quét nó.

> **Đối với Windows Defender (Controlled Folder Access):**
> 1.  Mở **Windows Security**.
> 2.  Đi tới **Virus & threat protection**.
> 3.  Dưới mục "Ransomware protection", chọn **Manage ransomware protection**.
> 4.  Chọn **Allow an app through Controlled folder access**.
> 5.  Nhấn **Add an allowed app** -> **Browse all apps** và trỏ đến file `Ai360Hub.exe` của bạn.

> **Đối với các phần mềm Antivirus khác (Kaspersky, Bitdefender, ESET...):**
> Vui lòng tìm mục "Settings" -> "Exclusions" (hoặc "Whitelist", "Exceptions") và thêm file `Ai360Hub.exe` hoặc toàn bộ thư mục cài đặt Ai360Hub vào danh sách này.

**Giải pháp 2: Quét file trên VirusTotal để kiểm chứng**

Để hoàn toàn yên tâm, bạn có thể tự mình kiểm tra độ an toàn của file `Ai360Hub.exe` bằng cách tải nó lên trang web [VirusTotal.com](https://www.virustotal.com/). Đây là một dịch vụ uy tín của Google, sử dụng bộ máy của hơn 70 trình diệt virus khác nhau để phân tích file.

---

## ⚙️ Hướng dẫn Cấu hình Tính năng "Không Gian LLM"

Tính năng này cho phép bạn chạy các mô hình ngôn ngữ lớn (LLM) ngay trên máy tính của mình. Để sử dụng, bạn cần chuẩn bị và cấu hình một vài thứ.

### 1. Yêu cầu cần thiết

* **Phần cứng:**
    * **RAM:** Tối thiểu 16GB RAM để chạy các mô hình 7B-8B. Càng nhiều RAM, bạn càng chạy được các mô hình lớn hơn.
    * **GPU (Khuyến nghị):** Card đồ họa NVIDIA (GTX 16xx / RTX 20xx trở lên) với ít nhất 6GB VRAM. Việc chạy bằng GPU sẽ nhanh hơn rất nhiều so với CPU.
* **Phần mềm:**
    * **Driver NVIDIA:** Nếu dùng GPU, hãy đảm bảo bạn đã cài đặt driver mới nhất từ trang chủ của NVIDIA.
    * **Microsoft Visual C++ Redistributable:** Tải và cài đặt phiên bản mới nhất (thường là 2015-2022) từ trang chủ của Microsoft.

### 2. Các bước Cài đặt

**Bước 1: Tải về một Model GGUF**

* Mô hình cần có định dạng `.gguf`. Đây là định dạng file được tối ưu để chạy trên phần cứng người dùng.
* Bạn có thể tìm và tải các mô hình này từ trang web **Hugging Face**.
* **Gợi ý model tốt để bắt đầu:** Tìm kiếm "Llama-3-8B-Instruct-GGUF" trên Hugging Face và tải về một phiên bản lượng tử hóa (quantized), ví dụ như phiên bản `Q4_K_M`.

**Bước 2: Đặt Model vào đúng thư mục**

* Sau khi tải về, hãy sao chép file `.gguf` vào thư mục có tên là `models`.
* Thư mục `models` này phải nằm **ngay bên cạnh file `Ai360Hub.exe`** của bạn.

    ```
    Thư mục cài đặt Ai360Hub/
    ├── Ai360Hub.exe
    └── models/
        └── Llama-3-8B-Instruct-Q4_K_M.gguf  <-- Đặt file model của bạn ở đây
    ```

**Bước 3: Sử dụng trong Ứng dụng**

1.  Mở Ai360Hub và truy cập tab **"Không gian LLM"**.
2.  Nhấn nút **"Làm mới"** (Refresh). File model của bạn sẽ xuất hiện trong danh sách "Chọn Model".
3.  Chọn model bạn vừa thêm.
4.  **Tùy chỉnh Cài đặt:**
    * **Context Size (n_ctx):** Để mặc định (ví dụ: 8192) nếu bạn không chắc.
    * **Sử dụng GPU:** **Tích vào ô này** nếu bạn có card đồ họa NVIDIA đủ mạnh.
5.  Nhấn nút **"Tải Model"**. Quá trình này có thể mất một vài phút tùy thuộc vào tốc độ ổ cứng và dung lượng model.
6.  Khi thanh trạng thái báo "Model ... đã sẵn sàng!", bạn đã có thể bắt đầu sử dụng các tính năng dịch thuật file hoặc chat với trợ lý ảo.
Download Model LLM: https://huggingface.co/bartowski
---

## 🔑 Quản lý API Key

Một số tính năng online (Gemini, FPT.AI, AuSyncLab) yêu cầu bạn phải cung cấp API Key của riêng mình.
* Vui lòng truy cập tab **"Cài đặt chung"** để nhập và lưu các key này.
* Các API Key được lưu trữ cục bộ trên máy tính của bạn và không được gửi đi bất cứ đâu ngoài các dịch vụ chính chủ (Google, FPT...).

Cảm ơn bạn đã tin tưởng và sử dụng Ai360Hub!
<img width="1277" height="830" alt="image" src="https://github.com/user-attachments/assets/311bfbd5-fadd-4147-9027-aeb8be44db44" />
<img width="1276" height="827" alt="image" src="https://github.com/user-attachments/assets/a30f84b3-2faa-4cc7-b376-64ee32bad50a" />
<img width="1277" height="830" alt="image" src="https://github.com/user-attachments/assets/9d1796b8-985f-4708-9767-021c4cf4b3f6" />

------------------

# Ai360Hub Auto-Updater (DownloadVID)

**Repo này chỉ chứa các tệp dùng cho auto-updater của Ai360Hub.**

---

##  Mục đích
- Cung cấp dữ liệu phiên bản mới nhất (`version.json`) để ứng dụng Ai360Hub kiểm tra và tự cập nhật.
- Giữ quá trình cập nhật **minh bạch & công khai**: phiên bản và link tải luôn rõ ràng, không “đen hộp”.

---

##  Bên trong repo
- **version.json**  
  Định dạng JSON chứa các trường như `version`, `download_url`, và (nếu có) `sha256`.

- (Có thể thêm) **checksums.json**  
  Chứa SHA-256 checksum để người dùng kiểm tra tính toàn vẹn của file sau khi tải.

---

##  Cách hoạt động (đối với Ai360Hub)
1. Ứng dụng tự kiểm tra `version.json` từ repo.
2. So sánh phiên bản hiện tại với phiên bản được thông báo.
3. Nếu có bản mới, hiện thông báo cho user, tải file từ `download_url`.
4. (Nếu có) Kiểm tra checksum để đảm bảo file an toàn.
5. Cập nhật hoàn tất.

---

##  Vì sao minh bạch lại quan trọng?
- Xây dựng **độ tin cậy** với người dùng: không lo bị cài phần mềm độc hại.
- Dễ dàng **debug hoặc xác nhận phiên bản** khi có sự cố.
- Mở cửa cho **cộng đồng tham gia kiểm chứng**, nâng cao chất lượng.

---

##  Gợi ý cải tiến trong tương lai
- Thêm trường `sha256` vào `version.json` — để kiểm tra hash ngay trong app.
- Sử dụng `releases` của GitHub để tạo bản phát hành chính thức (kèm tag, release notes).
- (Tùy chỉnh) Thêm `downloads.md` để liệt kê lịch sử các bản phát hành nếu cần.

---

##  Lưu ý với user
- Người dùng phổ thông chỉ cần tải installer gốc từ trang chính thức.
- Các bạn kỹ thuật muốn xác minh có thể so sánh file tải xuống với checksum đăng trên GitHub.

---




