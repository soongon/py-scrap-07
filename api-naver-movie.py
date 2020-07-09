# 1. 엔드포인트로 요청 (파라미터, 헤더에 키를 설정 포함)
import requests

params = {
    'query': '사라진시간'
}
headers = {
    'X-Naver-Client-Id': 'H8ePWN2jh7Bu_BTvQZiM',
    'X-Naver-Client-Secret': 'pePJcG_C4E'
}
res = requests.get('https://openapi.naver.com/v1/search/movie.json'
             , params=params, headers=headers)

# 2. JSON으로 온 응답을 파싱해서 csv 형태로 만들어 저장..
# print(res.json().get('items'))

movie_list = []
for item in res.json().get('items'):
    movie_list.append([
        item.get('title'),
        item.get('link'),
        item.get('image'),
        item.get('pubDate'),
        item.get('director')
    ])

import pandas as pd
df = pd.DataFrame(movie_list)
df.to_csv('movie.csv', index=False)
print('save ok..')