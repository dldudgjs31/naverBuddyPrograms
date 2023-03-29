import selenium
from PyQt6 import QtCore, QtWidgets
import naver
from buddy import *
from PyQt6.QtWidgets import QPushButton, QMessageBox
import pymysql

class bott():
    user_id = ''
    user_start_dt =''
    user_end_dt=''
    def dbConnect(self):
        host = "my8002.gabiadb.com"
        user = "amsdb"
        password = "manager123!@"
        database = "amsdb"

        # 데이터베이스 연결
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database)
        return connection
    def dbSearch(self,query,connection):
        with connection.cursor() as cursor:
            sql = query
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def login(self):
        id = ui.lineEdit_loginid.text()
        pwd = ui.lineEdit_loginpwd.text()
        connection = self.dbConnect()
        result = self.dbSearch(query=f"SELECT * FROM user WHERE ID='{id}'",connection=connection)
        msgBox = QMessageBox()

        # 계정 유효성 검사 - 비밀번호
        if len(result)==0:
            print("없는 계정입니다.")
            msgBox.setText("없는 계정입니다.")
            msgBox.exec()
            return
        else:
            if result[0][1]==pwd:
                print("유효한 계정임")
                msgBox.setText("유효한 계정임")
                msgBox.exec()
            else:
                print("비밀번호 틀림")
                msgBox.setText("비밀번호 틀림")
                msgBox.exec()
                return
        # 계정 유효기간 검사 및 권한 검사
        try:
            remain = self.dbSearch(query=f"SELECT END_DT,START_DT," \
                      f"DATEDIFF(END_DT, START_DT)+1 AS `total`," \
                      f"DATEDIFF(END_DT, NOW())+1 AS `remain` " \
                      f"FROM auth WHERE ID ='{id}' AND AUTH='네이버서이추01'", connection=connection)
            if len(remain)==0:
                print("권한이 없는 계정")
                msgBox.setText("권한이 없는 계정")
                msgBox.exec()
                return
            else:
                start_dt = remain[0][1]
                end_dt = remain[0][0]
                total_dt = remain[0][2]
                remain_dt = remain[0][3]
            if remain_dt >= 0:
                print(f"유효한 계정입니다. 남은일수 {remain_dt}/{total_dt}일, 계정 만료일 : {end_dt}")
                msgBox.setText(f"유효한 계정입니다. 남은일수 {remain_dt}/{total_dt}일 \n 계정 만료일 : {end_dt}")
                msgBox.exec()
                currentpage = ui.stackedWidget.currentIndex()
                ui.stackedWidget.setCurrentIndex(currentpage+1)
                self.user_id = id
                self.user_start_dt = start_dt
                self.user_end_dt = end_dt
            else:
                print(f"해당 계정 만료일 : {end_dt}")
                msgBox.setText(f"해당 계정 만료일 : {end_dt}")
                msgBox.exec()
        except Exception as e:
            print(e)
            
            
        # 계정 권한 검사
        # currentpage = ui.stackedWidget.currentIndex()
        # ui.stackedWidget.setCurrentIndex(currentpage+1)

    def start(self):
        print("start....")
        keyword = '강릉 데이트'
        max_buddies = 50
        buddy_intro = '{nickname}님 안녕하세요~! 이초코와 최야삐입니다:) 강릉 관련 글 보고 이렇게 인사드립니다. 서로 이웃으로 정보 공유하면서 소통해요~!'
        naver_id = 'rhksdir12'
        naver_password = 'tkfkdgo!!'
        try:
            ui.textEdit_intro.append(str(self.user_start_dt))
            ui.textEdit_intro.append(str(self.user_end_dt))
            ui.textEdit_intro.append(self.user_id)
        except Exception as e:
            print(e)

        # 진행바 셋업
        # print(ui.progressBar.value())
        # ui.progressBar.setValue(ui.progressBar.value()+1)

        # 알림창 셋업
        # msgBox = QMessageBox()
        # msgBox.setText("작업을 완료했습니다.")
        # msgBox.exec()
        # try:
        #     bot = NaverBlogBuddyBot(keyword, max_buddies, buddy_intro, naver_id, naver_password)
        #     bot.run()
        # except Exception as e:
        #     print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = naver.Ui_MainWindow()
    ui.setupUi(MainWindow)
    bot = bott()
    ui.pushButton_login.clicked.connect(bot.login)
    ui.pushButton_start.clicked.connect(bot.start)
    MainWindow.show()
    sys.exit(app.exec())
