# Ai-Library360 Downloader (PySide6 GUI version - open web in app)

import sys
import os
import subprocess
import threading
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QLineEdit, QTextEdit, QFileDialog, QCheckBox, QComboBox, QRadioButton,
    QHBoxLayout, QButtonGroup, QMessageBox, QProgressBar, QListWidget
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📥 Ai-Library360 Video Downloader")
        self.setMinimumWidth(500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.url_input = QTextEdit()
        self.url_input.setPlaceholderText("📋 Mỗi dòng 1 link video hoặc playlist...")
        self.url_input.setFixedHeight(100)
        self.layout.addWidget(QLabel("Nhập URL video:"))
        self.layout.addWidget(self.url_input)

        # Chế độ tải
        self.mode_group = QButtonGroup(self)
        self.video_radio = QRadioButton("🎬 Video đơn")
        self.playlist_radio = QRadioButton("📃 Playlist")
        self.video_radio.setChecked(True)
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(self.video_radio)
        mode_layout.addWidget(self.playlist_radio)
        self.mode_group.addButton(self.video_radio)
        self.mode_group.addButton(self.playlist_radio)
        self.layout.addLayout(mode_layout)

        # Tùy chọn nâng cao
        self.sub_mode = QComboBox()
        self.sub_mode.addItems(["❌ Không tải", "📄 Phụ đề chính thức", "🤖 Phụ đề tự động"])

        self.langs_combo = QComboBox()
        self.langs_combo.addItems(["vi", "en", "zh-Hans", "zh-Hant", "ko", "ja", "fr", "es"])
        self.langs_combo.setCurrentText("vi")

        self.convert_srt = QCheckBox("🔁 Chuyển phụ đề sang .srt")
        self.audio_only = QCheckBox("🎵 Tải âm thanh MP3")
        self.include_thumb = QCheckBox("🖼️ Tải ảnh thumbnail")

        self.layout.addWidget(QLabel("Chế độ phụ đề:"))
        self.layout.addWidget(self.sub_mode)
        self.layout.addWidget(QLabel("Ngôn ngữ phụ đề:"))
        self.layout.addWidget(self.langs_combo)
        self.layout.addWidget(self.convert_srt)
        self.layout.addWidget(self.audio_only)
        self.layout.addWidget(self.include_thumb)

        # Trình duyệt tích hợp hiển thị video
        self.browser = QWebEngineView()
        self.layout.addWidget(QLabel("🌐 Trình duyệt tích hợp:"))
        self.layout.addWidget(self.browser)

        self.open_web_button = QPushButton("🌐 Mở liên kết đầu trong trình duyệt tích hợp")
        self.open_web_button.clicked.connect(self.load_web_preview)
        self.layout.addWidget(self.open_web_button)

        # Nút tải và hiển thị tiến trình
        self.download_button = QPushButton("🚀 Bắt đầu tải")
        self.download_button.clicked.connect(self.run_download_in_thread)
        self.layout.addWidget(self.download_button)

        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)

        self.output_list = QListWidget()
        self.layout.addWidget(self.output_list)

        # Thêm phần donate cuối giao diện
        self.donate_label = QLabel("<hr><div style='text-align:center;'>💚 Donate VCB: <b>01210013679036</b> (Hoàng)</div>")
        self.donate_label.setAlignment(Qt.AlignCenter)
        self.donate_label.setStyleSheet("color: green; margin-top: 10px;")
        self.layout.addWidget(self.donate_label)

    def run_download_in_thread(self):
        threading.Thread(target=self.run_download, daemon=True).start()

    def run_download(self):
        urls = [u.strip() for u in self.url_input.toPlainText().splitlines() if u.strip()]
        if not urls:
            QMessageBox.warning(self, "Cảnh báo", "Bạn chưa nhập URL nào.")
            return

        base_folder = "Video"
        os.makedirs(base_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        download_folder = os.path.join(base_folder, f"Download_{timestamp}")
        os.makedirs(download_folder, exist_ok=True)

        for i, url in enumerate(urls, 1):
            self.output_list.addItem(f"🔗 [{i}] Đang tải: {url}")
            QApplication.processEvents()

            cmd = ["yt-dlp", url, "--progress"]
            output_template = f"video_{i}_%(title)s.%(ext)s" if self.video_radio.isChecked() else f"playlist_{i}_%(autonumber)03d_%(title)s.%(ext)s"
            cmd += ["-o", os.path.join(download_folder, output_template)]

            if self.playlist_radio.isChecked():
                cmd.append("--yes-playlist")
            if self.audio_only.isChecked():
                cmd += ["--extract-audio", "--audio-format", "mp3"]

            sub_mode = self.sub_mode.currentText()
            if sub_mode == "📄 Phụ đề chính thức":
                cmd += ["--write-subs", "--sub-lang", self.langs_combo.currentText()]
            elif sub_mode == "🤖 Phụ đề tự động":
                cmd += ["--write-auto-subs", "--sub-lang", self.langs_combo.currentText()]

            if self.convert_srt.isChecked():
                cmd += ["--convert-subs", "srt"]
            if self.include_thumb.isChecked():
                cmd.append("--write-thumbnail")

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            for line in process.stdout:
                QApplication.processEvents()
                line = line.strip()
                if line:
                    self.output_list.addItem(line)
                    self.output_list.scrollToBottom()
                    if "%" in line:
                        try:
                            percent_str = line.split("%", 1)[0].split()[-1].replace(".", "").strip()
                            percent = int(percent_str)
                            if 0 <= percent <= 100:
                                self.progress.setValue(percent)
                        except:
                            pass
            process.wait()

            if process.returncode == 0:
                self.output_list.addItem(f"✅ Đã tải xong link {i}")
            else:
                self.output_list.addItem(f"❌ Lỗi link {i}")
            self.progress.setValue(int(i / len(urls) * 100))
            QApplication.processEvents()

        self.output_list.addItem(f"📂 Video và phụ đề được lưu tại: {download_folder}")

    def load_web_preview(self):
        urls = [u.strip() for u in self.url_input.toPlainText().splitlines() if u.strip()]
        if not urls:
            QMessageBox.warning(self, "Cảnh báo", "Bạn chưa nhập URL nào.")
            return
        url = urls[0]
        self.browser.load(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DownloaderApp()
    win.show()
    sys.exit(app.exec())
