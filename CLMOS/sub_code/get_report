from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.options import Options
from datetime import datetime as dt

options = Options()
options.add_argument('--headless')


driver = webdriver.Chrome('./chromedriver')
USERNAME = '122A31003'
PASSWORD = 'Amatsuki0'
wait = WebDriverWait(driver,10)

def get_report_info():
    # manabaのログインページへアクセス
    URL = 'https://unipa.thu.ac.jp/uprx/up/pk/pky501/Pky50101.xhtml'
    driver.get(URL)
    driver.implicitly_wait(10)

    # ログインページへ移動
    login_page = driver.find_element(By.XPATH, '/html/body/div/div/section/div/div[1]/div/p[2]/button')
    login_page.click()
    driver.implicitly_wait(10)

    # ログインページにてメールアドレスを入力・「次へ進む」をクリック
    sleep(5)
    mail_field = driver.find_element(By.XPATH, '//*[@id="i0116"]')
    mail_field.send_keys(USERNAME)
    next_botton = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
    next_botton.click()
    driver.implicitly_wait(10)

    # パスワードを入力・「サインイン」をクリック
    sleep(1)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="lightbox"]')))
    password_field = driver.find_element(By.XPATH, '//*[@id="i0118"]')
    password_field.send_keys(PASSWORD)
    driver.implicitly_wait(10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]')))
    signin_botton = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
    signin_botton.click()
    driver.implicitly_wait(10)

    # 「いいえ」をクリック
    sleep(1)
    driver.implicitly_wait(10)
    refuse_botton = driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]')
    refuse_botton.click()


    def access_to_report_page():
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, '/html')))
        report_button = driver.find_element(By.XPATH, '//*[@id="coursereport"]/img')
        report_button.click()


    sleep(1)
    print("**************************************************")
    course_taken = driver.find_elements(By.CLASS_NAME, 'stdlist')
    course_taken2 = course_taken[0].find_elements(By.CLASS_NAME, 'course.course-cell')
    print("あなたは%sコマ履修しています。" %(len(course_taken2)))

    # 履修科目の時間割のURLを取得
    URLs = []
    for i in course_taken2:
        a_tag = i.find_elements(By.TAG_NAME, 'a')
        URL = a_tag[0].get_attribute('href')
        URLs.append(URL)

    # 未提出レポートのある科目名とその期限を取得
    report_info = []
    for i in URLs:
        # 履修登録科目へ遷移
        driver.get(i)
        sleep(1)
        access_to_report_page()
        # 科目名を取得
        class_name = driver.find_element(By.ID, 'coursename').text
        # 未提出レポートがある科目の科目名と期限を取得し、report_info[]に追加
        tr_tags = driver.find_elements(By.TAG_NAME, 'tr')
        for tr_tag in tr_tags:
            tr_text = tr_tag.text
            if tr_text != '' and '未提出' in tr_text:
                tr_text_list = tr_text.split(' ')
                try:
                    # Google Calendar APIに合うようにフォーマットを修正
                    deadline = tr_text_list[-2] + ' ' + tr_text_list[-1]
                    deadline = dt.strptime(deadline, '%Y-%m-%d %H:%M')
                    deadline = dt.strftime(deadline, "%Y-%m-%dT%H:%M:00")
                    report_info.append((class_name,deadline))
                except:
                    pass
    # 科目名と期限のリストを返す。[(科目名,期限), (科目名,期限), ・・・(科目名,期限)]
    return report_info