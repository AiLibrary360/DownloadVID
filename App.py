import sys
import os
import subprocess
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QTextEdit, QCheckBox, QComboBox, QRadioButton,
    QHBoxLayout, QButtonGroup, QMessageBox, QProgressBar, QListWidget
)
from PySide6.QtCore import Qt, QThread, Signal

# ------------------- Worker -------------------
class DownloadWorker(QThread):
    message = Signal(str)
    progress_signal = Signal(int)
    finished = Signal(str)

    def __init__(self, urls, video_mode, audio_only, sub_mode, sub_lang, convert_srt, include_thumb, custom_folder_name=""):
        super().__init__()
        self.urls = urls
        self.video_mode = video_mode
        self.audio_only = audio_only
        self.sub_mode = sub_mode
        self.sub_lang = sub_lang
        self.convert_srt = convert_srt
        self.include_thumb = include_thumb
        self.custom_folder_name = custom_folder_name.strip()
        self.stop_flag = False
        self.process = None

    def stop(self):
        self.stop_flag = True
        if self.process:
            self.process.terminate()
            self.message.emit("⏹ Dừng tải...")

    def run(self):
        try:
            # --------- Tạo thư mục ---------
            base_folder = "Video"
            os.makedirs(base_folder, exist_ok=True)

            if self.custom_folder_name:
                download_folder = os.path.join(base_folder, self.custom_folder_name)
            else:
                date_str = datetime.now().strftime("%Y-%m-%d")
                download_folder = os.path.join(base_folder, date_str)

            original_folder = download_folder
            count = 1
            while os.path.exists(download_folder):
                download_folder = f"{original_folder}-{count}"
                count += 1
            os.makedirs(download_folder, exist_ok=True)
            # -------------------------------

            for i, url in enumerate(self.urls, 1):
                if self.stop_flag:
                    self.message.emit("⏹ Đã dừng tải.")
                    break

                self.message.emit(f"🔗 [{i}] Đang tải: {url}")

                # Ép định dạng MP4
                cmd = ["yt-dlp", url, "-f", "bv*+ba/b", "--merge-output-format", "mp4", "--progress"]

                # Template output
                output_template = f"video_{i}_%(title)s.%(ext)s" if self.video_mode else f"playlist_{i}_%(autonumber)03d_%(title)s.%(ext)s"
                cmd += ["-o", os.path.join(download_folder, output_template)]

                if not self.video_mode:
                    cmd.append("--yes-playlist")
                if self.audio_only:
                    cmd += ["--extract-audio", "--audio-format", "mp3"]

                # Phụ đề (đang cập nhật)
                if self.sub_mode != "❌ Không tải":
                    self.message.emit("⚠️ Chức năng phụ đề đang cập nhật, sẽ hoàn thiện trong bản tiếp theo.")

                if self.convert_srt:
                    cmd += ["--convert-subs", "srt"]
                if self.include_thumb:
                    cmd.append("--write-thumbnail")

                # Chạy process
                self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

                for line in self.process.stdout:
                    if self.stop_flag:
                        self.process.terminate()
                        self.message.emit("⏹ Đang dừng...")
                        break

                    line = line.strip()
                    if line:
                        self.message.emit(line)
                        if "%" in line:
                            try:
                                percent_str = line.split("%", 1)[0].split()[-1].replace(".", "").strip()
                                percent = int(percent_str)
                                if 0 <= percent <= 100:
                                    self.progress_signal.emit(percent)
                            except:
                                pass
                self.process.wait()

                if self.process.returncode == 0:
                    self.message.emit(f"✅ Hoàn tất link {i}")
                else:
                    self.message.emit(f"❌ Lỗi khi tải link {i}")

                self.progress_signal.emit(int(i / len(self.urls) * 100))

            self.finished.emit(f"📂 Video được lưu tại: {download_folder}")

        except Exception as e:
            self.message.emit(f"❌ Lỗi: {e}")


# ------------------- App -------------------
class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ai-Library360 DownloadVID v1.0")
        self.setMinimumWidth(520)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Donate label
        self.donate_label = QLabel(
            "<div style='text-align:center; font-size:15px; color:#2e7d32; font-weight:bold;'>"
            "💚 Hỗ trợ phát triển (Donate): <b>0121001367936</b> (VCB - Hoàng)</div><hr>"
        )
        self.donate_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.donate_label)

        # URL input
        self.url_input = QTextEdit()
        self.url_input.setPlaceholderText("📋 Mỗi dòng 1 link video hoặc playlist...")
        self.url_input.setFixedHeight(100)
        self.layout.addWidget(QLabel("Nhập URL video:"))
        self.layout.addWidget(self.url_input)

        # Folder name input
        self.folder_name_input = QTextEdit()
        self.folder_name_input.setPlaceholderText("Nhập tên thư mục (tuỳ chọn)")
        self.folder_name_input.setFixedHeight(30)
        self.layout.addWidget(QLabel("Tên thư mục tải (tuỳ chọn):"))
        self.layout.addWidget(self.folder_name_input)

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

        # Subtitle options
        self.sub_mode = QComboBox()
        self.sub_mode.addItems([
            "❌ Không tải",
            "📄 Phụ đề chính thức (đang cập nhật)",
            "🤖 Phụ đề tự động (đang cập nhật)"
        ])

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

        # Buttons
        self.download_button = QPushButton("🚀 Bắt đầu tải")
        self.download_button.clicked.connect(self.start_download)
        self.stop_button = QPushButton("⏹ Dừng tải")
        self.stop_button.clicked.connect(self.stop_download)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.download_button)
        button_layout.addWidget(self.stop_button)
        self.layout.addLayout(button_layout)

        # Progress and log
        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)

        self.output_list = QListWidget()
        self.layout.addWidget(self.output_list)

        # Style
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f7f7;
                font-size: 13px;
                font-family: "Segoe UI";
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QProgressBar {
                border: 1px solid #aaa;
                border-radius: 5px;
                text-align: center;
                height: 16px;
                background: #ddd;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 5px;
            }
            QListWidget {
                background-color: #222;
                color: #eee;
                border: 1px solid #444;
                font-family: Consolas, monospace;
                padding: 5px;
            }
            QTextEdit, QComboBox {
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 4px;
            }
            QLabel {
                color: #333;
            }
        """)

        self.worker = None

    def start_download(self):
        urls = [u.strip() for u in self.url_input.toPlainText().splitlines() if u.strip()]
        if not urls:
            QMessageBox.warning(self, "Cảnh báo", "Bạn chưa nhập URL nào.")
            return

        self.output_list.clear()
        self.progress.setValue(0)

        self.worker = DownloadWorker(
            urls,
            video_mode=self.video_radio.isChecked(),
            audio_only=self.audio_only.isChecked(),
            sub_mode=self.sub_mode.currentText(),
            sub_lang=self.langs_combo.currentText(),
            convert_srt=self.convert_srt.isChecked(),
            include_thumb=self.include_thumb.isChecked(),
            custom_folder_name=self.folder_name_input.toPlainText()
        )

        self.worker.message.connect(self.output_list.addItem)
        self.worker.progress_signal.connect(self.progress.setValue)
        self.worker.finished.connect(self.output_list.addItem)

        self.worker.start()

    def stop_download(self):
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.output_list.addItem("⏹ Đang dừng tiến trình...")
        else:
            QMessageBox.information(self, "Thông báo", "Hiện không có tác vụ nào đang chạy.")


# ------------------- MAIN -------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DownloaderApp()
    win.show()
    sys.exit(app.exec())
