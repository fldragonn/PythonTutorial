# 크롬과 셀레니움을 사용해 웹 게임 자동화 하기

from selenium import webdriver

driver = webdriver.Chrome('/Users/jeondaelyong/PycharmProjects/PythonTutorial/chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
print(len(btns))
print(btns[0].text)
print()