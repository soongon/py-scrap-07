from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import configparser

config = configparser.ConfigParser()
config.read('./settings.conf')
config = config['KAKAO']

browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.naver.com/')
browser.find_element(By.CSS_SELECTOR, '#inner_login > a.link_login.link_kakaoid')\
    .send_keys(config['kakao_password'])
browser.find_element(By.ID, 'search_btn').click()

# .. do something..
time.sleep(5)


#inner_login > a.link_login.link_kakaoid

browser.close()
