#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 显示等待.py
# Author: MuNian
# Date  : 2019-12-03

from selenium import webdriver
from selenium.webdriver.common.by import By
# 循环等待
from selenium.webdriver.support.ui import WebDriverWait
# 条件触发
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://www.baidu.com')


try:
    # 页面一直循环直到出现某一个条件
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'kw'))
    )


# 如果代码没有异常就会执行这个
finally:
    driver.quit()






