from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import *
import chatgpt
from buddy import *
from PyQt6.QtWidgets import QPushButton, QMessageBox, QRadioButton
import pymysql
import threading


class bott():
    chatgpt_api_key =''

    def saveApiKey(self):
        chatgpt_api_key = ui.lineEdit_apikey.text()
        msgBox = QMessageBox()
        msgBox.setText("chat gpt key가 등록되었습니다.")
        msgBox.exec()
    # 오류 해결사 함수
    def errorSolution(self):
        print("error")
        #유효성 체크
        #유효성 체크 1) 오류 코드 작성 여부
        err_code = ui.plainTextEdit_err.toPlainText()
        if err_code=='':
            msgBox = QMessageBox()
            msgBox.setText("오류 코드를 입력하세요.")
            msgBox.exec()
            return
        #유효성 체크 2) 언어 선택 여부 확인



    # 쿼리 메이커 함수
    def querySolution(self):
        print("query")

    # 함수 메이커 함수
    def functionSolution(self):
        print("function")
    def logging(self, text):
        ui.plainTextEdit_log.appendPlainText(text)


    def start2(self):
        print("start")
        self.worker = Worker()
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.signal.connect(self.evt_update)
    def evt_worker_finished(self):
        try:
            ui.plainTextEdit_log.appendPlainText("test")
        except Exception as e:
            print(e)
    def evt_update(self,val):
        ui.plainTextEdit_log.appendPlainText(val)

class Worker(QThread):
    signal = pyqtSignal(str)
    progress = pyqtSignal(int)
    def run(self):
        print("start....")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = chatgpt.Ui_MainWindow()
    ui.setupUi(MainWindow)
    bot = bott()
    ##chat-gpt api key 등록
    ui.pushButton_save_api.clicked.connect(bot.saveApiKey)
    ##오류 해결사) 오류 분석
    ui.radioButton_err_java.setChecked(True)
    ui.pushButton_err_sol.clicked.connect(bot.errorSolution)
    ##쿼리 메이커) 쿼리 생성
    ui.pushButton_query.clicked.connect(bot.querySolution)
    ##함수 메이커) 함수 생성
    ui.pushButton_func_make.clicked.connect(bot.functionSolution)
    MainWindow.show()
    sys.exit(app.exec())
