# 1. 해당 페이지로 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome('./chromedriver.exe', options=options)

browser.get('https://www.melon.com/')

browser.find_element(By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth1 > a > span.menu_bg.menu01').click()

WebDriverWait(browser, timeout=5)\
    .until(EC.presence_of_all_elements_located)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#gnb_menu > ul:nth-child(1) > li.nth2 > a > span.menu_bg.menu02').click()

time.sleep(1)
# browser.get_screenshot_as_file('./screenshot/melon.png')

html = browser.page_source

# 2. 페이지에서 데이터 파싱
soup = BeautifulSoup(html, 'html.parser')
browser.close()

melon_chart = []
for tr in soup.select('#frm > div > table > tbody > tr'):
    # 이미지 저장..
    res = requests.get(tr.select_one('tr > td:nth-child(3) > div > a > img')['src'])
    file_name = tr.select_one('tr > td:nth-child(3) > div > a > img')['src'].split('/')[-7]
    with open('./melon_images/' + file_name, 'wb') as file:
        file.write(res.content)

    melon_chart.append([
        tr.select_one('tr > td:nth-child(5) > div > div > div.ellipsis.rank01 > span > a').text,
        tr.select_one('tr > td:nth-child(5) > div > div > div.ellipsis.rank02 > a').text,
        tr.select_one('tr > td:nth-child(6) > div > div > div > a').text,
        int(tr.select_one('tr > td:nth-child(7) > div > button > span.cnt')
            .text.replace('총건수', '').strip().replace(',', '')),
        file_name
    ])

import pprint
pprint.pprint(melon_chart)
# 3. 저장
df = pd.DataFrame(melon_chart)
df.to_csv('melon_chart.csv', index=False)