# 1. 해당 페이지로 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from bs4 import BeautifulSoup
import time
browser = webdriver.Chrome('./chromedriver.exe')

browser.get('https://www.melon.com/')
browser.find_element(By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth1 > a > span.menu_bg.menu01').click()
WebDriverWait(browser, timeout=3)\
    .until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth2 > a > span.menu_bg.menu02')))
browser.find_element(By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth2 > a > span.menu_bg.menu02').click()
time.sleep(1)
html = browser.page_source

# 2. 페이지에서 데이터 파싱
soup = BeautifulSoup(html, 'html.parser')
print(soup)
browser.close()

# 3. 저장