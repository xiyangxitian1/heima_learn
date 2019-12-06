#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 网站图片获取文字.py
# Author: MuNian
# Date  : 2019-12-04
import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver



image_set = set()

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
driver.find_element_by_id('imgBlkFront').click()
# imageslist = set()
# 等待页面加载完成
time.sleep(5)
# 点击右箭头 开始翻页
# 循环  driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style') 从里面取到 pointer
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # 获取已经加载的图片? 获取的是多张图片
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute('src')
        image_set.add(image)

# 退出浏览器
driver.quit()

# 机器识别图片
for image in image_set:
    # 保存图片
    urlretrieve(image, 'page.jpg')
    s = subprocess.Popen(['tesseract', 'page.jpg', 'page'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    f = open('page.txt', 'a')
    # s.wait()
    print(f.read())








