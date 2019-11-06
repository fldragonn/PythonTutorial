'''
톡! 슬릭딜

사전 준비
pip install requests
pip install bs4
'''

import json
import time
import requests
from bs4 import BeautifulSoup

KAKAO_TOKEN = 'OXcheffkWNroqWb8yerEzndGm0dZ0fMHmHFJggo9dJkAAAFuPn4KQQ'

send_lists = []
def send_to_kakao(text):
    header = {'Authorization': 'Bearer ' + KAKAO_TOKEN}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }

    data = {'template_object': json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def search_sdeal(condition):
    keyword = condition['keyword']
    min_price = condition['min_price']
    max_price = condition['max_price']

    url = 'https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&searcharea=deals&searchin=first'.format(keyword)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # findAll은 결를 행별로 리스트에 보관한다.
    divs = soup.findAll('div', class_='resultRow')
    for one in divs:
        img = one.select_one('img.lazyimg')
        link = one.select_one('a.dealTitle')
        href = 'https://slickdeals.net'+link['href']
        title = link['title']
        price = one.select_one('span.price').text.replace('$', '').replace('Free', '0').replace(',','').replace('FREE', '0')
        if price == '':
            price = 0
        else:
            price = float(price)
        fire = bool(one.find('span', class_= 'icon icon-fire'))
        expire = bool(one.find('div', class_='expired'))
        if not expire:
            if min_price < price < max_price:
                send = True
                for s in send_lists:
                    if s['title'] == title:
                        # print("이미 전송한 데이터")
                        send = False
                if send:
                    text = '가격: {}, 제품명: {}, {}'.format(price, title, href)
                    r = send_to_kakao(text)
                    print(text)
                    print(r.text)
                    send_lists.append({
                        'title':title,
                        'price':price,
                        'fire':fire,
                        'href':href
                    })

if __name__ == '__main__':
    condition1 = {
        'keyword' : 'apple watch',
        'min_price' : 100,
        'max_price' : 300
    }

    condition2 = {
        'keyword': 'apple tv',
        'min_price': 50,
        'max_price': 300
    }

    while True:
         search_sdeal(condition1)
         time.sleep(60)