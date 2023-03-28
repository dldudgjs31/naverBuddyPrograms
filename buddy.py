from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip as pp
import time
import random
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')
options.add_argument("disable-gpu")
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
driver = webdriver.Chrome(options=options)
class buddy():
    def inputkeys(myId, placeholder):
        pp.copy(myId)
        idInput = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
        idInput.click()
        time.sleep(2)
        pp.copy(myId)
        #time.sleep(random.uniform(3.0, 10.0))
        time.sleep(2)
        idInput.send_keys(Keys.COMMAND, 'v')

    def openBlog(url):
        driver.execute_script(f"window.open('{url}');")
        driver.switch_to.window(driver.window_handles[1])

    def closeBlog():
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def checkBuddyPossible():
        checkurl = driver.find_elements(By.XPATH,"//input[@id='bothBuddyRadio'][@name='relation'][@ng-disabled='true']")
        if len(checkurl) > 0:
            print("서로 이웃 추가할 수 없는 블로그입니다.")
            return "false"
        else:
            print("서로 이웃 추가 가능한 블로그입니다.")
            return "true"

    def alreadyBuddyCheck():
        #//*[@id="lyr6"]/div/div[1]/p
        checkurl = driver.find_elements(By.XPATH, "//*[@id='lyr6']/div/div[1]/p")
        cnt = len(checkurl)
        if cnt >0:
            print("이미 이웃입니다.")
            return "false"
        else:
            print("이웃이 아닙니다.")
            return "true"

    def clickBuddyRadio():
        time.sleep(3)
        radio = driver.find_elements(By.XPATH, "//*[@id='bothBuddyRadio']")
        if len(radio) > 0:
            radio[0].click()

    def introBuddy(nickname):
        time.sleep(2)
        pp.copy(bothBuddyIntro.format(nickname=nickname))
        message = driver.find_elements(By.XPATH, "//textarea[@ng-model='data.inviteMessage']")
        message[0].click()
        message[0].send_keys(Keys.COMMAND, 'a')
        message[0].send_keys(Keys.COMMAND, 'v')

    def checkDuplicatedBuddy():
        ##//*[@id="lyr4"]/div/div[1]/p
        time.sleep(2)
        message = driver.find_elements(By.XPATH,"//*[@id='lyr4']/div/div[1]/p")
        if len(message)>0:
            print("이미 서이추 신청한 계정입니다.")
            return "false"
        else:
            print("아직 서이추 신청 안한 계정입니다.")
            return "true"

    def clickOkBtn():
        time.sleep(3)
        btn = driver.find_elements(By.XPATH, '//a[@class="btn_ok"]')
        btn[0].click()
        print(nickname[x] + "님 서이추 완료")

    # 서이추 추가 방법 1 : 관련 키워드 검색 후 추가
    # input data : keyword / 이웃 수 설정(one day : max 100) / 서이추 인사말
    # output data : 서이추 성공시 {userid} 서이추 추가 완료 (num/100) log 설정 필요
    searchKeyword = '강릉 여행'
    bothBuddyMax = 30
    bothBuddyIntro = '{nickname}님 안녕하세요~! 이초코와 최야삐입니다:) 강릉 여행 글 보고 이렇게 인사드립니다. 서로 이웃으로 정보 공유하면서 소통해요~!'
    yourid = 'rhksdir12'
    yourpassword = 'tkfkdgo!!'


    driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")
    time.sleep(2)
    inputkeys(yourid, "아이디")
    inputkeys(yourpassword, "비밀번호")
    driver.find_element(By.XPATH, f"//input[@placeholder='비밀번호']").send_keys(Keys.ENTER)
    time.sleep(2)

    # 1. 네이버 view 키워드 검색(블로그/최신글)
    blogSearchUrl = "https://m.search.naver.com/search.naver?where=m_blog&query=" + searchKeyword + "&nso=so%3Add%2Cp%3Aall"
    driver.get(blogSearchUrl)

    # 2. 원하는 수량 만큼 스크롤 진행(max 100)
    total_posts = 0
    #첫 로딩화면의 글 개수 로딩
    total_posts = len(driver.find_elements(By.XPATH, "//ul[@class='lst_total _list_base'][@id='addParemt']/li"))
    print("초기 글 개수 : "+ str(total_posts))
    while total_posts < bothBuddyMax:
        SCROLL_PAUSE_TIME = 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        total_posts = len(driver.find_elements(By.XPATH, "//ul[@class='lst_total _list_base'][@id='addParemt']/li"))
        print(total_posts)
    print(total_posts)
    # 3. 해당 스크롤만큼의 블로그 id 저장하기 (이때 중복인 경우 스킵)
    nickname = list()
    realID = list()
    buddyCnt = 0
    for x in range(bothBuddyMax):
        #id 추출
        url = driver.find_elements(By.XPATH,'//span[@class="elss etc_dsc_inner"]/a[@class="sub_txt sub_name"]')
        url = (url[x].get_attribute('href'))
        user_id = url[url.rfind('/') + 1:]
        realID.append(user_id)
        #닉네임 추출
        name = driver.find_elements(By.XPATH,'//span[@class="elss etc_dsc_inner"]/a[@class="sub_txt sub_name"]')
        name =name[x].text
        nickname.append(name)

    # 4. 1번부터 for통해 새창열기 https://m.blog.naver.com/BuddyAddForm.naver?blogId=dldudgjs31
    for x in range(len(realID)):
        url = f"https://m.blog.naver.com/BuddyAddForm.naver?blogId={realID[x]}"
        openBlog(url)
        #중복 신청 여부 확인

        checkDuplicated = checkDuplicatedBuddy()
        if checkDuplicated == "true":
            # 서이추 가능 여부 확인
            possibleCheck = checkBuddyPossible()
            # 이미 이웃 여부 확인
            alreadyCheck = alreadyBuddyCheck()

            if possibleCheck =="true" and alreadyCheck =="true":
                #서이추 버튼 클릭
                clickBuddyRadio()

                #서이추 인사말 복사
                introBuddy(nickname[x])

                #서이추 확인 버튼클릭
                clickOkBtn()
                buddyCnt+=1
                print(f"서이추 신청 현황 ({buddyCnt}/{bothBuddyMax})")
        time.sleep(3)
        closeBlog()
    driver.quit()
    # 5. 서이추 가능 여부/ 이미 이웃 여부 확인/ 서이추 중복 신청 여부 확인/하루 이웃 추가 회수 여부 확인
    # 5. 가능한 경우 서이추 버튼 클릭 / 서이추 인사말 과 함께 신청하기
    # 6. 글 닫기 다음 글



    # def searchBlog(searchWord: str, articleLimit: int):
    #     adress = "https://m.search.naver.com/search.naver?where=m_blog&query=" + searchWord + "&nso=so%3Add%2Cp%3Aall"
    #     driver.get(adress)
    #
    #     articles = driver.find_elements(By.XPATH, "//div[@class='total_wrap']/a")
    #     numOfArticles = len(articles)
    #     SCROLL_PAUSE_TIME = 0.5
    #     while numOfArticles < articleLimit:
    #         articles = driver.find_elements(By.XPATH, "//div[@class='total_wrap']/a")
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(SCROLL_PAUSE_TIME)
    #         numOfArticles = len(driver.find_elements(By.XPATH, "//div[@class='total_wrap']/a"))
    #
    #     articles = driver.find_elements(By.XPATH, "//div[@class='total_wrap']/a")
    #     numOfArticles = len(articles)
    #     urls = []
    #     for i in range(numOfArticles):
    #         url = str(articles[i].get_attribute("href"))
    #         urls.append(url)
    #     return urls
    #
    #

    #
    #
    # def availableLike():
    #     global stopTagNum
    #     try:
    #         confirmlike = driver.find_element(By.XPATH, "//*[@id='body']/div[10]/div/div[1]/div/div/a").get_attribute(
    #             "class").split(" ")
    #         if "on" in confirmlike:
    #             stopTagNum += 1
    #             print(f'이미 좋아요 누른 게시물 {stopTagNum}개')
    #             return False
    #         elif "off" in confirmlike:
    #             return True
    #     except Exception as e:
    #         print(e)
    #         print('좋아요가 제한된 게시물')
    #         return False
    #
    #
    # def clickLike():
    #     document_height = driver.execute_script("return document.body.scrollHeight")
    #     while True:
    #         driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_DOWN)
    #         time.sleep(random.uniform(likeminPauseTime, likemaxPauseTime))
    #         now_scroll_height = driver.execute_script("return window.scrollY+window.innerHeight")
    #         if now_scroll_height >= document_height:
    #             break
    #         document_height = driver.execute_script("return document.body.scrollHeight")
    #
    #     like_btn = driver.find_element(By.XPATH, "//div[@class='btn_like']/div")
    #     driver.execute_script("arguments[0].scrollIntoView({block : 'center'});", like_btn)
    #     like_btn.click()
    #     global clickedLikeNum
    #     clickedLikeNum += 1
    #     print(f"블로그 좋아요를 {clickedLikeNum}개 누름")
    #     closeBlog()
    #
    #
    # for searchWord in searchWords:
    #     urls = searchBlog(searchWord, random.randrange(tagMinNum, tagMaxNum))
    #     for url in urls:
    #         openBlog(url)
    #         # 블로그 페이지 로딩을 위한 시간
    #         time.sleep(random.uniform(3.0, 7.0))
    #
    #         # 좋아요가 클릭 가능한지 확인 후 클릭, 아니면 창 닫기
    #         if availableLike():
    #             clickLike()
    #         else:
    #             closeBlog()
    # driver.quit()