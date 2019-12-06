from selenium import webdriver
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'http://ntlias-stu.boxuegu.com/#/login'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
driver.switch_to.window(driver.current_window_handle[-1])
driver.get('https://baidu.com')
time.sleep(2000)
driver.close()
