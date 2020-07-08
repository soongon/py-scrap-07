import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

products = []
for product in soup.select('#productList > li'):
    products.append([
        product.select_one('li > a > dl > dd > div.name').text.strip(),
        int(product.select_one(
            'li > a > dl > dd > div.price-area > div > div.price > em > strong')
            .text.strip().replace(',', '')),
        bool(product.select_one(
            'li > a > dl > dd > div.price-area > div > div:nth-child(3) > span.badge.falcon > img')),
        int(product.select_one(
            'li > a > dl > dd > div.other-info > div > span.rating-total-count')
            .text.strip()[1:-1])
    ])


import pprint
pprint.pprint(products)