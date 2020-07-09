import requests

headers = {
    'X-Naver-Client-Id': 'H8ePWN2jh7Bu_BTvQZiM',
    'X-Naver-Client-Secret': 'pePJcG_C4E'
}
payload = {
    'source': 'en',
    'target': 'ko',
    'text': 'Five months into a still-raging pandemic that has killed more than 130,000 Americans, the long-simmering tensions between President Donald Trump and the health experts who staff his government have escalated from private griping to shrugging disagreement to now open dispute.'
}
res = requests.post('https://openapi.naver.com/v1/papago/n2mt',
              headers=headers, data=payload)

print(res.json())
