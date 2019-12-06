#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : dome1.py
# Author: MuNian
# Date  : 2019-12-03

'''
selenium ---> Web自动化测试 类似 按键精灵

'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 创建一个浏览器
driver = webdriver.Chrome()
# 在创建的浏览器里面输入12306网页地址
driver.get('https://www.12306.cn/index/')

time.sleep(2)

# 网页定位到出发地  click() 点击选项框
# id语法
# driver.find_element_by_id('fromStationText').click()
# time.sleep(2)
# xapth语法
# driver.find_element_by_xpath('//*[@id="fromStationText"]').send_keys('长沙')

# 方法 整个网页 ---> class  --->
driver.find_element_by_class_name('//*[@id="fromStationText"]').send_keys('长沙')

# 类对象
# class_name
input_data = driver.find_element(By.CLASS_NAME, 'input inp-txt_select')
input_data.clear()


# 定位目的地
# driver.find_element_by_id('toStationText').click()
# time.sleep(2)
# driver.find_element_by_id('toStationText').send_keys('北京')



