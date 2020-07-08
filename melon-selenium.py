# 1. 해당 페이지로 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome('./chromedriver.exe', options=options)
print('browser 생성 완료')

browser.get('https://www.melon.com/')
print('멜론 메인화면 이동 완료')
browser.find_element(By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth1 > a > span.menu_bg.menu01').click()

WebDriverWait(browser, timeout=5)\
    .until(EC.presence_of_all_elements_located)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth2 > a > span.menu_bg.menu02').click()
print('두번째 클릭')
time.sleep(1)
browser.get_screenshot_as_file('./screenshot/melon.png')
print('스크린샷 완료')
html = browser.page_source

# 2. 페이지에서 데이터 파싱
soup = BeautifulSoup(html, 'html.parser')
print(soup)
browser.close()

# 3. 저장