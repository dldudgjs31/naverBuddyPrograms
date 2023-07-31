from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import *
import chatgpt
from buddy import *
from PyQt6.QtWidgets import QPushButton, QMessageBox, QRadioButton
import pymysql
import threading


class bott():
    #전역 변수 : API KEY / MODEL 유형
    chatgpt_api_key = ''
    chatgpt_api_model = ''

    #api key 와 model 필수 값 validation 체크
    def validSetting(self):
        if self.chatgpt_api_key =='':
            msgBox = QMessageBox()
            msgBox.setText("API KEY를 입력하세요.")
            msgBox.exec()
            return True
        elif self.chatgpt_api_model  =='':
            msgBox = QMessageBox()
            msgBox.setText("CHATGPT MODEL를 입력하세요.")
            msgBox.exec()
            return True
        else:
            return False

    def validCheck(self,text,type):
        if text =='':
            msgBox = QMessageBox()
            msgBox.setText(f"{type}을(를) 입력하세요.")
            msgBox.exec()
            return True
        else:
            return False


    def saveApiKey(self):
        #api key 와 model 유형 선택
        self.chatgpt_api_key = ui.lineEdit_apikey.text()
        start_index = ui.comboBox.currentText().find(']')+1
        model= ui.comboBox.currentText()[start_index:].strip()
        self.chatgpt_api_model = model
        msgBox = QMessageBox()
        msgBox.setText("chat gpt key가 등록되었습니다.")
        msgBox.exec()
    # 오류 해결사 함수
    def errorSolution(self):
        print("error")
        #유효성 체크
        # 유효성 체크 1) api-key 및 유형 선택 여부
        if self.validSetting():
            return

        #유효성 체크 2) 오류 코드 작성 여부
        err_code = ui.plainTextEdit_err.toPlainText()
        if self.validCheck(text=err_code,type="에러코드"):
            return

        #선택된 언어
        prgLanguage=''
        if ui.radioButton_err_java.isChecked():
            prgLanguage = ui.radioButton_err_java.text()
        elif ui.radioButton_err_py.isChecked():
            prgLanguage = ui.radioButton_err_py.text()
        elif ui.radioButton_err_c.isChecked():
            prgLanguage = ui.radioButton_err_c.text()
        elif ui.radioButton_err_cpl.isChecked():
            prgLanguage = ui.radioButton_err_cpl.text()
        elif ui.radioButton_err_js.isChecked():
            prgLanguage = ui.radioButton_err_js.text()

        #prompt 설정
        prompt = f"{prgLanguage}에서 발생한 에러 {err_code} 의 에러 원인과 해결 방안에 대해서 설명해줘."
        print(prompt)

        #CHAT GPT 함수 실행
        result = ''

        #결과값 입력
        ui.plainTextEdit_err_sol.appendPlainText(result)



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
