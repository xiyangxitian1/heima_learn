#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 图片验证码破解.py
# Author: MuNian
# Date  : 2019-12-04

'''
从事python这方面的工作的吗？
数据分析 数据挖掘 AI
flask  django  --> 详细的课程体系

1 3 5正课
2 4 6 解答课
20:30 - 22:30
线上直播  课后高清录播 ==> 课后一对一的解答 辅导和补课

'''

import requests
from PIL import Image
import urllib3
from urllib3.exceptions import InsecureRequestWarning


class LoginTic(object):
    ''' 12306验证码破解 '''

    def __init__(self):
        # 保持用户的登录状态
        self.session = requests.session()
        # 构造请求头
        self.headers = {
            'Cookie': '_passport_ct=6e71e77657004e6d97802543f11d6b17t0670; _passport_session=1c4f76d3d89847a38afdb0df0c37535b9198; RAIL_EXPIRATION=1575632871632; RAIL_DEVICEID=D8DqGelPP3Du1TJRZCPgcWW-o177_rB4ilyH-KmwC3cp0XDmPLJpZlrObVzDIm-T8b_TNMfDoJMU7bDqMynBHSY8S1Kv94ocVjuqYTDNafwJ8vmS6PMVokuJJVWHzDu3jvB3w4I-MzrnuTO6Njic6Y1zYyUDfr67; _jc_save_fromDate=2019-12-03; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u5317%u4EAC%u5317%2CVAP; _jc_save_toDate=2019-12-03; _jc_save_wfdc_flag=dc; BIGipServerpool_passport=334299658.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=1172832522.24610.0000; BIGipServerpassport=988283146.50215.0000',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'
        }

    def getImg(self):
        ''' 获取验证码 '''
        # 图片验证码的地址
        url = 'https://kyfw.12306.cn/passport/captcha/captcha-image'
        # 请求图片验证码的地址 获取到图片数据
        response = self.session.get(url=url, headers=self.headers, verify=False)
        with open('img.jpg', 'wb') as f:
            f.write(response.content)
        try:
            im = Image.open('img.jpg')
            im.show()
            im.close()
        except Exception as e:
            print('请输入验证码')
        '''
        0 | 1 | 2 | 3
        4 | 5 | 6 | 7
        '''
        captcha_solution = input('请输入验证码的位置, 以","分割 [2, 5]:')
        return captcha_solution

    def checkYanZheng(self, solution):
        # 分割用户的输入验证码的位置  split 字符串的分割
        soList = solution.split(',')
        # 找到12306提供官方验证码坐标
        yanSol = ['35,35', '105,35', '175,35', '245,35', '35,105', '105,105', '175,105', '245,105']
        yanList = []
        for item in soList:
            print(item)
            yanList.append(yanSol[int(item)])
        # 正确的验证码拼接成字符串 请求验证码验证的时候  转换成参数的形式
        yanStr = ','.join(yanList)
        # 验证请求网址
        checkUrl = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        data = {
            'answer': yanStr,  # 验证码的坐标 请求参数
            'rand': 'sjrand',
            'login_site': 'E'
        }
        # 请求 12306验证码地址 并且进行验证
        cont = self.session.post(url=checkUrl, headers=self.headers, data=data, verify=False).json()
        # 4  成功 5 失败  7 过期
        if str(cont['result_code']) == '4':
            print('验证成功')
            return True
        elif str(cont['result_code']) == '7':
            print('验证码过期')
            return False
        else:
            print('验证码错误')
            return False

    def LoginTo(self):
        """
            12306模拟登录
        :return:
        """
        username = input('请输入用户名：')
        password = input("请输入你的密码：")

        # 12306验证地址
        loginUrl = 'https://kyfw.1306.cn/passport/web/login'
        # 请求12306验证地址的时候代入的参数
        data = {
            'username': username,
            'password': password,
            'appid': 'otn',
        }
        result = self.session.post(url=loginUrl, data=data, headers=self.headers, verify=False)
        ret = result.json()['result_message']
        if str(ret) == '登录成功':
            print(result.cookies)
            return result.cookies
        else:
            print('登录失败')


if __name__ == '__main__':
    login = LoginTic()
    # 获取到12306图片验证码,并且返回用户输入的坐标
    yan = login.getImg()
    chek = False
    while not chek:
        chek = login.checkYanZheng(yan)
        if chek:
            print('验证通过')
        else:
            print('验证失败')

    login.LoginTo()

# login = LoginTic()
# user = login.getImg()
# login.checkYanZheng(user)
