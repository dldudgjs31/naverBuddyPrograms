import time
import traceback

import selenium
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import *
import naver
from buddy import *
from PyQt6.QtWidgets import QPushButton, QMessageBox
import pymysql
import threading


class bott():
    user_id = ''
    user_start_dt = ''
    user_end_dt = ''

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

    def dbSearch(self, query, connection):
        with connection.cursor() as cursor:
            sql = query
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def login(self):
        id = ui.lineEdit_loginid.text()
        pwd = ui.lineEdit_loginpwd.text()
        connection = self.dbConnect()
        result = self.dbSearch(query=f"SELECT * FROM user WHERE ID='{id}'", connection=connection)
        msgBox = QMessageBox()

        # 계정 유효성 검사 - 비밀번호
        if len(result) == 0:
            print("없는 계정입니다.")
            msgBox.setText("없는 계정입니다.")
            msgBox.exec()
            return
        else:
            if result[0][1] == pwd:
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
            if len(remain) == 0:
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
                ui.stackedWidget.setCurrentIndex(currentpage + 1)
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

    def logging(self, text):
        ui.plainTextEdit_log.appendPlainText(text)

    def start(self):
        print("start....")
        keyword = '강릉 데이트'
        max_buddies = 50
        buddy_intro = '{nickname}님 안녕하세요~! 이초코와 최야삐입니다:) 강릉 관련 글 보고 이렇게 인사드립니다. 서로 이웃으로 정보 공유하면서 소통해요~!'
        naver_id = 'rhksdir12'
        naver_password = 'tkfkdgo!!'
        print(ui.checkBox_securityYN.isChecked())
        try:
            # 로그인
            # ui.plainTextEdit_log.appendPlainText("네이버 로그인 시작")
            bot = NaverBlogBuddyBot(keyword, max_buddies, buddy_intro, naver_id, naver_password)
            bot.first_login(naver_id, naver_password)
            ##로그 남기기            ui.plainTextEdit_log.appendPlainText("네이버 로그인 완료 (보안 퀴즈 나올시 보안퀴즈 여부 체크 후 재실행")
            time.sleep(2)
            # 키워드 검색

            ui.plainTextEdit_log.appendPlainText(f"'{keyword}' 키워드 검색 시작")
            bot.searchKeyword(keyword)
            # 목표 수량 읽기
            total_posts = bot.total_post(max_buddies)
            # 목표 수량 만큼 id/nickname 저장
            nickname, real_id = bot.save_id_nickname(max_buddies)
            print(nickname)
            print(real_id)
            ui.plainTextEdit_log.appendPlainText(f"'{keyword}' 키워드 검색 완료")
            buddy_cnt = 0
            num_cnt = 0
            # while buddy_cnt < max_buddies:
            #     # 서이추 창 열기
            #     bot.buddy_form(real_id[num_cnt])
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
    def start2(self):
        print("start")
        self.worker = Worker()
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.signal.connect(self.evt_update)
        self.worker.progress.connect()
    def evt_worker_finished(self):
        try:
            ui.plainTextEdit_log.appendPlainText("test")
        except Exception as e:
            print(e)
    def evt_update(self,val):
        ui.plainTextEdit_log.appendPlainText(val)

    def evt_progress_update(self,val):
        ui.progressBar.setValue(val)
class Worker(QThread):
    signal = pyqtSignal(str)
    progress = pyqtSignal(int)
    def run(self):
        print("start....")
        keyword = ui.lineEdit_keyword.text()
        max_buddies = int(ui.spinBox_maxBuddy.value())
        buddy_intro = ui.textEdit_intro.toPlainText()
        naver_id = ui.lineEdit_id.text()
        naver_password = ui.lineEdit_pwd.text()
        print(ui.checkBox_securityYN.isChecked())
        try:
            # 로그인
            self.signal.emit("네이버 로그인 시작")
            # ui.plainTextEdit_log.appendPlainText("네이버 로그인 시작")
            bot = NaverBlogBuddyBot(keyword, max_buddies, buddy_intro, naver_id, naver_password)
            bot.first_login(naver_id, naver_password)
            ##로그 남기기            ui.plainTextEdit_log.appendPlainText("네이버 로그인 완료 (보안 퀴즈 나올시 보안퀴즈 여부 체크 후 재실행")
            time.sleep(2)
            self.signal.emit("네이버 로그인 완료")
            # 키워드 검색
            self.signal.emit(f"'{keyword}' 키워드 검색 시작")
            # ui.plainTextEdit_log.appendPlainText(f"'{keyword}' 키워드 검색 시작")
            bot.searchKeyword(keyword)
            # 목표 수량 읽기
            total_posts = bot.total_post(max_buddies)
            # 목표 수량 만큼 id/nickname 저장
            nickname, real_id = bot.save_id_nickname(max_buddies)
            print(nickname)
            print(real_id)
            self.signal.emit(f"'{keyword}' 키워드 검색 완료")
            # ui.plainTextEdit_log.appendPlainText(f"'{keyword}' 키워드 검색 완료")
            buddy_cnt = 0
            num_cnt = 0
            while buddy_cnt < max_buddies and num_cnt < len(real_id):
                # 서이추 창 열기
                bot.buddy_form(real_id[num_cnt])
                check_duplicated = bot.check_duplicated_buddy()
                if check_duplicated:
                    # 서이추 가능 여부 확인
                    possible_check = bot.check_buddy_possible()
                    # 이미 이웃 여부 확인
                    already_check = bot.already_buddy_check()
                    if possible_check and already_check:
                        # 서이추 버튼 클릭
                        bot.click_buddy_radio()

                        # 서이추 인사말 복사
                        bot.intro_buddy(nickname[num_cnt])

                        # 서이추 확인 버튼클릭
                        bot.click_ok_btn(nickname[num_cnt])
                        buddy_cnt += 1
                        self.signal.emit(f"서이추 신청 현황 ({buddy_cnt}/{max_buddies})")
                        print(f"서이추 신청 현황 ({buddy_cnt}/{max_buddies})")

                time.sleep(3)
                bot.close_blog()
                num_cnt += 1
            bot.driver.quit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = naver.Ui_MainWindow()
    ui.setupUi(MainWindow)
    bot = bott()
    ui.pushButton_login.clicked.connect(bot.login)
    ui.pushButton_start.clicked.connect(bot.start2)
    MainWindow.show()
    sys.exit(app.exec())
