"""
man7-3.py
2022.03.16 수정사항
1. https://kr.investing.com 사이트의 개편됨 기존의 코드 동작안됨
2. containers = content.find('span', {'data-test': 'instrument-price-last'}) 로 코드 변경
"""

import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)


get_exchange_rate('usd', 'krw')