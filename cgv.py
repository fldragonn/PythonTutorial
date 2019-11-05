# -*- coding: utf-8 -*-

import telegram
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

# 토큰 저장 및 봇 선언
my_token = '821727099:AAHNy3XYROWgjNnL2N3AnZ72Dyp6OXls1Pw'
bot = telegram.Bot(token = my_token)

# cgv 시간표 URL
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0181&date=20191106'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    # imax = soup.find('span', {'class':'imax'})
    imax = soup.select_one('span.imax')
    if imax:
        # imax_block = imax.find_parent('div', {'class':'col-times'})
        imax_block = imax.find_parent('div', class_='col-times')
        imax_title = imax_block.select_one('a')
        bot.sendMessage(chat_id='1031978397', text=imax_title.text.strip() + " 아이맥스 영화가 예매 가능합니다.")
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()
