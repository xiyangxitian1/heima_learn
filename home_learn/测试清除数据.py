import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()

driver.get(url)

a = driver.find_element_by_id('kw')

a.send_keys('搜索的内容')
time.sleep(3)
# a.clear()
ActionChains(driver).send_keys(a, Keys.CLEAR)
a.send_keys('李炎')
time.sleep(5)
driver.find_element_by_id('su').click()
time.sleep(100)
