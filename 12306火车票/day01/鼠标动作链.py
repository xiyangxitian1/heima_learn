#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 鼠标动作链.py
# Author: MuNian
# Date  : 2019-12-03
import time

from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')

# 移动
# ac = driver.find_element_by_xpath('//*[@id="toStationText"]')
# ActionChains(driver).move_to_element(ac).perform()

time.sleep(2)

#点击
# ac = driver.find_element_by_xpath('//*[@id="toStationText"]')
# ActionChains(driver).move_to_element(ac).click(ac).perform()

# time.sleep(2)
# ac.send_keys('长沙')


# 鼠标右击
ac = driver.find_element_by_xpath('//*[@id="toStationText"]')
ActionChains(driver).move_to_element(ac).double_click(ac).perform()
