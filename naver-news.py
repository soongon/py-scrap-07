import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.naver.com/')
soup = BeautifulSoup(res.text, 'html.parser')

li_tags = soup.select('#today_main_news > div.hdline_news > ul > li')
# li_tags = ['<li>...</li>', '<li>...</li>', ... , '<li>...</li>']

result_list = []
for li_tag in li_tags:
    result_list.append(li_tag.select_one('li > div.hdline_article_tit > a').text.strip())

import pprint
pprint.pprint(result_list)


