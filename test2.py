import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Worker(QThread):
    timeout = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.num = 0

    def run(self):
        while True:
            self.timeout.emit("안녕하세요")
            self.sleep(1)

    def set_num(self, text):
        self.num = text


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()
        self.worker.timeout.connect(self.timeout)

        self.edit = QPlainTextEdit(self)
        self.edit.move(10, 10)
        self.edit.setGeometry(QtCore.QRect(50, 50, 301, 361))

        self.btn = QPushButton(self)
        self.btn.setText("시작")
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.startWorker)

        self.name = QLineEdit(self)
        self.name.move(200, 20)

    @pyqtSlot(str)
    def timeout(self, text):
        self.edit.appendPlainText(text)

    def startWorker(self):
        text = self.name.text()
        self.worker.set_num(text)


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec()
