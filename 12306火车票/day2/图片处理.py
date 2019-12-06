#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 图片处理.py
# Author: MuNian
# Date  : 2019-12-04

from PIL import Image
import subprocess


def cleaFile(filePath):
    # 读取这张图片 red --> 225,0,0
    image = Image.open(filePath)
    # 阈值过滤
    image = image.point(lambda x: 0 if x < 143 else 255)  # 低于143为黑色 否则为白色
    image.save('123.png')
    # 调用系统的tesseract命令  output 识别后保存的文件名称
    subprocess.call(['tesseract', '123.png', 'output'])
    # with open('output.txt', 'r') as f:
    #     print(f.read())

    # f = open('output.txt', 'r')
    # f.read()


cleaFile('tess2.png')
