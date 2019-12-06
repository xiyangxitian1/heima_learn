#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 豆瓣模拟登陆作业.py
# Author: MuNian
# Date  : 2019-12-04

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 创建一个类
class Douban():

    def __init__(self):
        # 创建一个驱动
        self.driver = webdriver.Chrome()
        # 访问豆瓣登陆网页
        self.driver.get('https://accounts.douban.com/passport/login?source=music')

    def log_in(self):
        time.sleep(3)
        # self.driver.find_element_by_class_name('account-tab-account').click()
        self.driver.find_element_by_xpath("//div[@class='account-body-tabs']/ul/li[2]").click()

douban = Douban()
douban.log_in()



