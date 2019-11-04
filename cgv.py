import telegram
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

my_token = '821727099:AAHNy3XYROWgjNnL2N3AnZ72Dyp6OXls1Pw'   #토큰을 변수에 저장합니다.
bot = telegram.Bot(token = my_token)   #bot을 선언합니다.

# cgv 시간표 URL
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0181&date=20191105'

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
