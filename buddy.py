from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip as pp
import time
import random

class NaverBlogBuddyBot:
    def __init__(self, keyword, max_buddies, buddy_intro, naver_id, naver_password):
        self.keyword = keyword
        self.max_buddies = max_buddies
        self.buddy_intro = buddy_intro
        self.naver_id = naver_id
        self.naver_password = naver_password
        self.driver = self.get_chrome_driver()

    def get_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--no-sandbox')
        options.add_argument("disable-gpu")
        options.add_argument('window-size=1920x1080')
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        driver = webdriver.Chrome(options=options)
        return driver

    def input_keys(self, my_id, placeholder):
        pp.copy(my_id)
        id_input = self.driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
        id_input.click()
        time.sleep(2)
        pp.copy(my_id)
        time.sleep(2)
        id_input.send_keys(Keys.CONTROL, 'v')

    def open_blog(self, url):
        self.driver.execute_script(f"window.open('{url}');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_blog(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def check_buddy_possible(self):
        check_url = self.driver.find_elements(By.XPATH, "//input[@id='bothBuddyRadio'][@name='relation'][@ng-disabled='true']")
        if len(check_url) > 0:
            print("서로 이웃 추가할 수 없는 블로그입니다.")
            return False
        else:
            print("서로 이웃 추가 가능한 블로그입니다.")
            return True

    def already_buddy_check(self):
        check_url = self.driver.find_elements(By.XPATH, "//*[@id='lyr6']/div/div[1]/p")
        cnt = len(check_url)
        if cnt > 0:
            print("이미 이웃입니다.")
            return False
        else:
            print("이웃이 아닙니다.")
            return True

    def click_buddy_radio(self):
        time.sleep(3)
        radio = self.driver.find_elements(By.XPATH, "//*[@id='bothBuddyRadio']")
        if len(radio) > 0:
            radio[0].click()

    def intro_buddy(self, nickname):
        time.sleep(2)
        pp.copy(self.buddy_intro.format(nickname=nickname))
        message = self.driver.find_elements(By.XPATH, "//textarea[@ng-model='data.inviteMessage']")
        message[0].click()
        message[0].send_keys(Keys.CONTROL, 'a')
        message[0].send_keys(Keys.CONTROL, 'v')

    def check_duplicated_buddy(self):
        time.sleep(2)
        message = self.driver.find_elements(By.XPATH, "//*[@id='lyr4']/div/div[1]/p")
        if len(message) > 0:
            print("이미 서이추 신청한 계정입니다.")
            return False
        else:
            print("아직 서이추 신청 안한 계정입니다.")
            return True
    def click_ok_btn(self, nickname):
        time.sleep(3)
        btn = self.driver.find_elements(By.XPATH, '//a[@class="btn_ok"]')
        btn[0].click()
        print(nickname + "님 서이추 완료")

    def run(self):
        self.driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")
        time.sleep(2)
        self.input_keys(self.naver_id, "아이디")
        self.input_keys(self.naver_password, "비밀번호")
        self.driver.find_element(By.XPATH, f"//input[@placeholder='비밀번호']").send_keys(Keys.ENTER)
        time.sleep(30)

        # 1. 네이버 view 키워드 검색(블로그/최신글)
        blog_search_url = "https://m.search.naver.com/search.naver?where=m_blog&query=" + self.keyword + "&nso=so%3Add%2Cp%3Aall"
        self.driver.get(blog_search_url)

        # 2. 원하는 수량 만큼 스크롤 진행(max 100)
        total_posts = len(self.driver.find_elements(By.XPATH, "//ul[@class='lst_total _list_base'][@id='addParemt']/li"))
        print("초기 글 개수 : "+ str(total_posts))
        while total_posts < self.max_buddies:
            SCROLL_PAUSE_TIME = 1
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            total_posts = len(self.driver.find_elements(By.XPATH, "//ul[@class='lst_total _list_base'][@id='addParemt']/li"))
            print(total_posts)
        print(total_posts)

        # 3. 해당 스크롤만큼의 블로그 id 저장하기 (이때 중복인 경우 스킵)
        nickname = list()
        real_id = list()
        buddy_cnt = 0
        for x in range(self.max_buddies):
            # id 추출
            url = self.driver.find_elements(By.XPATH, '//span[@class="elss etc_dsc_inner"]/a[@class="sub_txt sub_name"]')
            url = (url[x].get_attribute('href'))
            user_id = url[url.rfind('/') + 1:]
            real_id.append(user_id)
            # 닉네임 추출
            name = self.driver.find_elements(By.XPATH, '//span[@class="elss etc_dsc_inner"]/a[@class="sub_txt sub_name"]')
            name =name[x].text
            nickname.append(name)

        # 4. 1번부터 for통해 새창열기 https://m.blog.naver.com/BuddyAddForm.naver?blogId=dldudgjs31
        for x in range(len(real_id)):
            url = f"https://m.blog.naver.com/BuddyAddForm.naver?blogId={real_id[x]}"
            self.open_blog(url)
            # 중복 신청 여부 확인
            check_duplicated = self.check_duplicated_buddy()
            if check_duplicated:
                # 서이추 가능 여부 확인
                possible_check = self.check_buddy_possible()
                # 이미 이웃 여부 확인
                already_check = self.already_buddy_check()
                if possible_check and already_check:
                    # 서이추 버튼 클릭
                    self.click_buddy_radio()

                    # 서이추 인사말 복사
                    self.intro_buddy(nickname[x])

                    # 서이추 확인 버튼클릭
                    self.click_ok_btn(nickname[x])
                    buddy_cnt += 1
                    print(f"서이추 신청 현황 ({buddy_cnt}/{self.max_buddies})")
            time.sleep(3)
            self.close_blog()
        self.driver.quit()


# if __name__ == "__main__":
#     keyword = '강릉 데이트'
#     max_buddies = 50
#     buddy_intro = '{nickname}님 안녕하세요~! 이초코와 최야삐입니다:) 강릉 관련 글 보고 이렇게 인사드립니다. 서로 이웃으로 정보 공유하면서 소통해요~!'
#     naver_id = 'rhksdir12'
#     naver_password = 'tkfkdgo!!'
#     bot = NaverBlogBuddyBot(keyword, max_buddies, buddy_intro, naver_id, naver_password)
#     bot.run()
