import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
import speedtest

class SpeedTestThread(QThread):
    result_ready = pyqtSignal(str)

    def run(self):
        try:
            st = speedtest.Speedtest()
            self.result_ready.emit("Fetching best server...\n")
            st.get_best_server()

            self.result_ready.emit("Measuring download speed...\n")
            download = st.download() / 8_000_000
            self.result_ready.emit(f"Download speed: {download:.2f} MBps\n")

            self.result_ready.emit("Measuring upload speed...\n")
            upload = st.upload() / 8_000_000
            self.result_ready.emit(f"Upload speed: {upload:.2f} MBps\n")

            ping = st.results.ping
            self.result_ready.emit(f"Ping: {ping:.2f} ms\n")

        except Exception as e:
            self.result_ready.emit(f"Error: {e}\n")

class SpeedTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internet Speed Test - PyQt5")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.start_button = QPushButton("Start Speed Test")
        self.start_button.clicked.connect(self.start_test)

        self.layout.addWidget(self.output)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

    def start_test(self):
        self.output.clear()
        self.thread = SpeedTestThread()
        self.thread.result_ready.connect(self.output.append)
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeedTestApp()
    window.show()
    sys.exit(app.exec_())
