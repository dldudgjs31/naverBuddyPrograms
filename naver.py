# Form implementation generated from reading ui file 'naver.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 565)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 50, 671, 501))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(70, 20, 521, 81))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(200, 110, 58, 21))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.page)
        self.label_3.setGeometry(QtCore.QRect(200, 140, 58, 21))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_loginid = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_loginid.setGeometry(QtCore.QRect(300, 110, 171, 21))
        self.lineEdit_loginid.setObjectName("lineEdit_loginid")
        self.lineEdit_loginpwd = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_loginpwd.setGeometry(QtCore.QRect(300, 140, 171, 21))
        self.lineEdit_loginpwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_loginpwd.setObjectName("lineEdit_loginpwd")
        self.pushButton_login = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_login.setGeometry(QtCore.QRect(200, 170, 271, 51))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(18)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setAutoFillBackground(False)
        icon = QtGui.QIcon.fromTheme("address-book-new")
        self.pushButton_login.setIcon(icon)
        self.pushButton_login.setObjectName("pushButton_login")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setGeometry(QtCore.QRect(120, 0, 431, 31))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.page_2)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_id = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_id.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_7 = QtWidgets.QLabel(parent=self.page_2)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_pwd = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(20, 110, 131, 21))
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.label_8 = QtWidgets.QLabel(parent=self.page_2)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_keyword = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_keyword.setGeometry(QtCore.QRect(20, 180, 131, 21))
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.label_9 = QtWidgets.QLabel(parent=self.page_2)
        self.label_9.setGeometry(QtCore.QRect(170, 40, 161, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.checkBox_securityYN = QtWidgets.QCheckBox(parent=self.page_2)
        self.checkBox_securityYN.setGeometry(QtCore.QRect(20, 130, 101, 20))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.checkBox_securityYN.setFont(font)
        self.checkBox_securityYN.setObjectName("checkBox_securityYN")
        self.spinBox_maxBuddy = QtWidgets.QSpinBox(parent=self.page_2)
        self.spinBox_maxBuddy.setGeometry(QtCore.QRect(170, 60, 121, 22))
        self.spinBox_maxBuddy.setMaximum(100)
        self.spinBox_maxBuddy.setObjectName("spinBox_maxBuddy")
        self.label_10 = QtWidgets.QLabel(parent=self.page_2)
        self.label_10.setGeometry(QtCore.QRect(170, 90, 161, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.spinBox_delay_from = QtWidgets.QSpinBox(parent=self.page_2)
        self.spinBox_delay_from.setGeometry(QtCore.QRect(170, 110, 41, 22))
        self.spinBox_delay_from.setMinimum(2)
        self.spinBox_delay_from.setMaximum(100)
        self.spinBox_delay_from.setProperty("value", 2)
        self.spinBox_delay_from.setObjectName("spinBox_delay_from")
        self.label_11 = QtWidgets.QLabel(parent=self.page_2)
        self.label_11.setGeometry(QtCore.QRect(170, 160, 81, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.spinBox_buddygroup = QtWidgets.QSpinBox(parent=self.page_2)
        self.spinBox_buddygroup.setGeometry(QtCore.QRect(170, 180, 121, 22))
        self.spinBox_buddygroup.setMaximum(100)
        self.spinBox_buddygroup.setProperty("value", 2)
        self.spinBox_buddygroup.setObjectName("spinBox_buddygroup")
        self.textEdit_intro = QtWidgets.QTextEdit(parent=self.page_2)
        self.textEdit_intro.setGeometry(QtCore.QRect(20, 260, 271, 161))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.textEdit_intro.setFont(font)
        self.textEdit_intro.setObjectName("textEdit_intro")
        self.label_12 = QtWidgets.QLabel(parent=self.page_2)
        self.label_12.setGeometry(QtCore.QRect(20, 240, 81, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.progressBar = QtWidgets.QProgressBar(parent=self.page_2)
        self.progressBar.setGeometry(QtCore.QRect(320, 430, 341, 31))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.plainTextEdit_log = QtWidgets.QPlainTextEdit(parent=self.page_2)
        self.plainTextEdit_log.setGeometry(QtCore.QRect(320, 60, 341, 361))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.plainTextEdit_log.setFont(font)
        self.plainTextEdit_log.setObjectName("plainTextEdit_log")
        self.label_13 = QtWidgets.QLabel(parent=self.page_2)
        self.label_13.setGeometry(QtCore.QRect(320, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("BM Jua")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_start = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 430, 131, 51))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_stop.setGeometry(QtCore.QRect(160, 430, 131, 51))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.spinBox_delay_to = QtWidgets.QSpinBox(parent=self.page_2)
        self.spinBox_delay_to.setGeometry(QtCore.QRect(250, 110, 41, 22))
        self.spinBox_delay_to.setMinimum(2)
        self.spinBox_delay_to.setMaximum(100)
        self.spinBox_delay_to.setProperty("value", 2)
        self.spinBox_delay_to.setObjectName("spinBox_delay_to")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        self.label_5.setGeometry(QtCore.QRect(220, 110, 21, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_buddy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_buddy.setGeometry(QtCore.QRect(20, 0, 101, 51))
        self.pushButton_buddy.setObjectName("pushButton_buddy")
        self.pushButton_sympathy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_sympathy.setGeometry(QtCore.QRect(130, 0, 101, 51))
        self.pushButton_sympathy.setObjectName("pushButton_sympathy")
        self.pushButton_buddymanage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_buddymanage.setGeometry(QtCore.QRect(240, 0, 101, 51))
        self.pushButton_buddymanage.setObjectName("pushButton_buddymanage")
        self.pushButton_logout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(570, 0, 101, 51))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_id2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_id2.setGeometry(QtCore.QRect(450, 10, 58, 16))
        self.label_id2.setObjectName("label_id2")
        self.label_id = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(410, 10, 51, 16))
        self.label_id.setObjectName("label_id")
        self.label_enddate = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_enddate.setGeometry(QtCore.QRect(410, 30, 58, 16))
        self.label_enddate.setObjectName("label_enddate")
        self.label_enddate2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_enddate2.setGeometry(QtCore.QRect(450, 30, 58, 16))
        self.label_enddate2.setObjectName("label_enddate2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "네이버 서이추 자동화 프로그램"))
        self.label_2.setText(_translate("MainWindow", "아이디 :"))
        self.label_3.setText(_translate("MainWindow", "비밀번호 :"))
        self.pushButton_login.setText(_translate("MainWindow", "로그인"))
        self.label_4.setText(_translate("MainWindow", "네이버 서이추 자동화 프로그램"))
        self.label_6.setText(_translate("MainWindow", "네이버 아이디"))
        self.label_7.setText(_translate("MainWindow", "네이버 비밀번호"))
        self.label_8.setText(_translate("MainWindow", "검색 키워드"))
        self.label_9.setText(_translate("MainWindow", "신청 이웃 수 설정(최대100)"))
        self.checkBox_securityYN.setText(_translate("MainWindow", "보안퀴즈여부"))
        self.label_10.setText(_translate("MainWindow", "딜레이 랜덤 시간(기본 2초)"))
        self.label_11.setText(_translate("MainWindow", "서이추 그룹 선택"))
        self.textEdit_intro.setPlaceholderText(_translate("MainWindow", "{nickname}님 안녕하세요~! 00글 보고 신청합니다. 서로 통하면서 지내요 :)"))
        self.label_12.setText(_translate("MainWindow", "서이추 인사말"))
        self.label_13.setText(_translate("MainWindow", "작업 로그"))
        self.pushButton_start.setText(_translate("MainWindow", "시작"))
        self.pushButton_stop.setText(_translate("MainWindow", "중지"))
        self.label_5.setText(_translate("MainWindow", "~"))
        self.pushButton_buddy.setText(_translate("MainWindow", "네이버 서이추"))
        self.pushButton_sympathy.setText(_translate("MainWindow", "네이버 공감"))
        self.pushButton_buddymanage.setText(_translate("MainWindow", "네이버 이웃관리"))
        self.pushButton_logout.setText(_translate("MainWindow", "로그아웃"))
        self.label_id2.setText(_translate("MainWindow", "{name}"))
        self.label_id.setText(_translate("MainWindow", "아이디"))
        self.label_enddate.setText(_translate("MainWindow", "만료일"))
        self.label_enddate2.setText(_translate("MainWindow", "{enddate}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
