#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 弹窗.py
# Author: MuNian
# Date  : 2019-12-03

# 页面切换
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5000')

handle = driver.switch_to.window('弹窗名称')


for i in handle:
    driver.switch_to_window(i)


