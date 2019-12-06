#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 填充表单.py
# Author: MuNian
# Date  : 2019-12-03

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5000')

# 提交表单
# 找到name里面包含的选项卡
select = Select(driver.find_element_by_name('status'))

# 索引 从0开始的
# select.select_by_index(2)
# select.select_by_value('2')
select.select_by_visible_text('审核不通过')