# requests 모듈을 사용
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/')
# 웹에서 받아온 HTML(raw html)은 바로 파싱이 불가능하기 때문에
# parsable 한 데이터로 만드는 툴을 사용해야 함
# Beautifulsoup4 사용해야 함..

# Convert parsabel html
soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')

print(the_tag.text)