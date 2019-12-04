import selenium
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(0.5)
search_input = driver.find_element(By.ID, 'kw')
su_btn = driver.find_element(By.ID, 'su')
ActionChains(driver).move_to_element(search_input).send_keys('aaa').perform()
ActionChains(driver).click(su_btn).perform()
