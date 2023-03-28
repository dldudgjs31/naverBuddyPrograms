from PyQt6 import QtCore, QtWidgets
import naver
# from buddy import *

def nextpage():
    currentpage = ui.stackedWidget.currentIndex()
    ui.stackedWidget.setCurrentIndex(currentpage+1)


def start():
    print("start....")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = naver.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_login.clicked.connect(nextpage)
    ui.pushButton_start.clicked.connect(start)
    MainWindow.show()
    sys.exit(app.exec())
