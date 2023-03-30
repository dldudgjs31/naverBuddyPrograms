import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Worker(QThread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            print("안녕하세요")
            self.sleep(1)
            self.progress.emit()

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False

    progress = pyqtSignal()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(10, 90, 200, 25)
        self.progressbar.setValue(0)

        self.label = QTextEdit("안녕하세요 0", self)
        self.label.setGeometry(10, 130, 200, 25)

        btn1 = QPushButton("resume", self)
        btn1.move(10, 10)
        btn2 = QPushButton("pause", self)
        btn2.move(10, 50)

        # 시그널-슬롯 연결하기
        btn1.clicked.connect(self.resume)
        btn2.clicked.connect(self.pause)

        self.worker.progress.connect(self.on_progress)

    def resume(self):
        self.worker.resume()
        self.worker.start()

    def pause(self):
        self.worker.pause()

    def on_progress(self):
        value = self.progressbar.value() + 1
        self.progressbar.setValue(value)
        self.label.append("안녕하세요 " + str(value))


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec()