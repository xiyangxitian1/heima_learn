from selenium import webdriver
import time
import requests
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Login(object):

    def __init__(self):
        self.url = 'http://ntlias-stu.boxuegu.com/#/login'
        # yanz_url = 'http://ntlias-stu.boxuegu.com/user/verifyCode?r=0.1326260711495728'
        self.yaz_url = 'http://ntlias-stu.boxuegu.com/user/verifyCode?r=0.010145262830455026'
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)
        time.sleep(1)

        self.driver.find_element_by_name('username').send_keys('A191102326')
        self.driver.find_element_by_name('password').send_keys('liyan123')
        # 先输入一个错的验证码
        self.driver.find_element_by_name('verify').click()
        self.driver.find_element_by_name('verify').send_keys("我")
        time.sleep(1)
        # 点击登录
        self.driver.find_element_by_class_name('login-btn').click()
        time.sleep(1)
        # 清除输入的验证码
        self.driver.find_element_by_name('verify').click()
        self.driver.find_element_by_name('verify').clear()
        # self.driver.find_element_by_class_name('login-title').click()
        time.sleep(1)
        # 验证码
        yan = self.getYan()
        time.sleep(10)
        verify_input = self.driver.find_element_by_name('verify')
        ActionChains(self.driver).move_to_element(verify_input).send_keys(Keys.CLEAR)
        verify_input.send_keys()
        time.sleep(10)
        # 点击登录
        self.driver.find_element_by_class_name('login-btn').click()

    def getYan(self):
        yan = ""
        resp = requests.get(self.yaz_url)
        if resp.status_code == 200:
            with open('1.jpg', 'wb') as f:
                f.write(resp.content)
            img = Image.open('1.jpg')
            img.show()
            img.close()
            yan = input('请输入验证码：')
        else:
            print('请求验证码失败……')
        return yan

    def main(self):
        self.login()


if __name__ == '__main__':
    Login().main()

    time.sleep(100)
