##### TÍCH HỢP TÍNH NĂNG MỚI - DỰ KIẾN SẮP TỚI - AI360HUB_CUT - VIDEO EDITOR

<img width="1393" height="849" alt="image" src="https://github.com/user-attachments/assets/a856ea69-0e73-438f-812f-f85ee8771e12" />
<img width="1398" height="847" alt="image" src="https://github.com/user-attachments/assets/45aa03de-b6ec-40bf-9ad7-e6ce7498e720" />
<img width="1912" height="1015" alt="image" src="https://github.com/user-attachments/assets/361c2e17-d807-4768-aca5-02798f50aab4" />

<img width="1395" height="843" alt="image" src="https://github.com/user-attachments/assets/c0919d7c-06bd-4da2-b79a-325a7ac5eadd" />










## ⚙️ Hướng dẫn Cấu hình Tính năng "Không Gian LLM"



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




