# Ai360Hub - Thông báo Quan trọng & Hướng dẫn Sử dụng

Chào mừng bạn đến với Ai360Hub! Để đảm bảo bạn có trải nghiệm tốt nhất và an toàn nhất, vui lòng đọc kỹ các thông tin quan trọng dưới đây trước khi sử dụng.
<details>
<summary><strong>👉 Vấn đề: Ứng dụng bị văng (crash) khi nhấn "Bắt đầu Xử lý" trên card NVIDIA cấu hình cao (RTX 40/50 series).</strong></summary>

Nguyên nhân
Đây là hiện tượng không tương thích giữa thư viện llama-cpp-python được cài đặt mặc định (bản biên dịch sẵn) và kiến trúc phần cứng mới của các dòng card đồ họa cao cấp. Phiên bản mặc định không được tối ưu hóa cho các tính năng và bộ công cụ CUDA mới nhất, dẫn đến mất ổn định khi bắt đầu tác vụ tính toán nặng.

Giải pháp: Cài đặt lại llama-cpp-python từ mã nguồn ("May đo" lại thư viện)
Quá trình này sẽ biên dịch lại thư viện ngay trên máy của bạn, liên kết trực tiếp với driver và bộ công cụ CUDA đã cài đặt, đảm bảo tương thích 100%.

1. Chuẩn Bị Môi Trường

Bạn cần cài đặt đầy đủ 2 công cụ sau:

Visual Studio 2022 (Community Edition): Trong quá trình cài đặt, bắt buộc phải chọn workload "Desktop development with C++".

NVIDIA CUDA Toolkit: Tải phiên bản mới nhất phù hợp với driver của bạn từ trang chủ NVIDIA CUDA Toolkit.

2. Gỡ Bỏ Hoàn Toàn Phiên Bản Cũ

Mở Command Prompt (cmd) hoặc PowerShell và chạy lệnh sau (chạy lặp lại cho đến khi nhận được thông báo "package not found"):

Bash

pip uninstall llama-cpp-python
3. Cài Đặt "May Đo"

Vẫn trong PowerShell hoặc cmd, chạy lần lượt các lệnh sau:

PowerShell

# Lệnh 1: Bật cờ biên dịch với CUDA
set CMAKE_ARGS="-DLLAMA_CUDA=on"

# Lệnh 2: Ép buộc sử dụng CMake để build
set FORCE_CMAKE=1

# Lệnh 3: Cài đặt lại từ mã nguồn, không dùng cache
pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade
Lưu ý: Quá trình này sẽ mất khoảng 5-15 phút vì nó đang biên dịch thư viện trên máy bạn.

4. Kiểm Tra

Sau khi hoàn tất, chạy lệnh sau:

Bash

python -m llama_cpp.llama_cpp
Nếu trong kết quả trả về có dòng CUDA = 1, bạn đã cài đặt thành công! Ứng dụng sẽ hoạt động ổn định.

</details>

<br>
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

---

##  Lưu ý với user
- Người dùng phổ thông chỉ cần tải installer gốc từ trang chính thức.
- Các bạn kỹ thuật muốn xác minh có thể so sánh file tải xuống với checksum đăng trên GitHub.

---




