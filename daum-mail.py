MY_PASS = ''


# 1. 스크래핑 할 해당 페이지로 이동 -> 페이지의 HTML 확보
#    -> 해당 페이지 이동을.. selenium 으로
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.facebook.com/')
browser.find_element(By.ID, 'email')\
    .send_keys('soongon@gmail.com', Keys.TAB, MY_PASS, Keys.ENTER)
time.sleep(1)
html = browser.page_source

# 2. HTML 확보 후 -> bs4 으로 파싱.. -> list of list 형태로 구성
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(soup)
browser.close()



# 3. 저장(CVS) with pandas DataFrame 을 이용해서 저장

