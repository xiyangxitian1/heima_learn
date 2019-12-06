from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

import time


class Weblogin(object):

    def __init__(self, username, pwd, url):
        """
         初始化方法
        """
        self.username = username
        self.pwd = pwd
        self.url = url

    def Browerdriver(self):
        driver = webdriver.Chrome()
        driver.get(self.url)

        # 等待用户操作 替换成验证码破解
        WebDriverWait(driver, 10, 0.5)

        UnameLogin = driver.find_element_by_xpath('//div[@class="login-box"]/ul/li[2]').click()  # xpath

        # 要先点击再输入，否则会被12306检测出来
        # 用户账号
        Unameblank = driver.find_element_by_id('J-userName').click()
        Unameinput = driver.find_element_by_id('J-userName').send_keys(self.username)

        # 用户账号
        Pwdblank = driver.find_element_by_id('J-password').click()
        Pwdinput = driver.find_element_by_id('J-password').send_keys(self.pwd)

        time.sleep(10)

        # 显示等待 第一种
        TicketPage = driver.find_element_by_id('J-index').click()
        # 第二种
        # TicketPage = WebDriverWait(driver, 10).until(lambda elem: elem.find_element_by_xpath('//*[@class="nav-hd"]'))
        # TicketPage.click()
        time.sleep(5)
        driver.find_element_by_id('fromStationText').click()
        driver.find_element_by_id('fromStationText').send_keys('深圳')
        driver.find_element_by_id('fromStationText').send_keys(Keys.ENTER)




if __name__ == '__main__':
    login = Weblogin('13129597923', 'munian1234', 'https://kyfw.12306.cn/otn/resources/login.html')
