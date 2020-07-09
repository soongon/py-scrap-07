import requests

params = {
    'q': 'suwon,KR',
    'appid': '5df3f1b99c9227bb6bb15d61c2b5bf9b',
    'units': 'metric'
}
res = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

import pprint
pprint.pprint(res.json())
