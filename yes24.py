import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.yes24.com/24/Category/BestSeller')
soup = BeautifulSoup(res.text, 'html.parser')

li_tags = soup.select('#bestList > ol > li')

titles = []
for li_tag in li_tags:
    title = li_tag.select_one('li > p.copy > a').text.strip()
    titles.append(title)

import pprint
pprint.pprint(titles)
