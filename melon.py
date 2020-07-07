import requests
from bs4 import BeautifulSoup

res = requests.get('https://m2.melon.com/index.htm')
print(res)