from selenium import webdriver
import time
import requests
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self):
        self.url = 'http://ntlias-stu.boxuegu.com/#/login'
        # yanz_url = 'http://ntlias-stu.boxuegu.com/user/verifyCode?r=0.1326260711495728'
        self.yaz_url = 'http://ntlias-stu.boxuegu.com/user/verifyCode?r=0.010145262830455026'
        self.driver = webdriver.Chrome()
        self.ac = ActionChains(self.driver)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        self.headers = headers

    def login(self):
        self.driver.get(self.url)
        time.sleep(1)
        # """
        # drag_and_drop(source,target)：拖动
        # source：开始位置；需要拖动的元素
        # target：结束位置；拖到后需要放置的目的地元素
        #
        # move_to_element()：鼠标悬停
        # """
        username = self.driver.find_element(By.NAME, 'username')
        # 鼠标悬停
        # self.ac.move_to_element(username).click().perform()
        self.ac.send_keys_to_element(username, "A191102326").perform()
        # time.sleep(1)
        self.ac.reset_actions()
        password = self.driver.find_element(By.NAME, 'password')

        # self.ac.move_to_element(password).click().perform()
        self.ac.send_keys_to_element(password, 'liyan123').perform()
        # time.sleep(1)
        self.ac.reset_actions()
        verify_input = self.driver.find_element(By.NAME, 'verify')
        # self.ac.move_to_element(verify_input).perform()
        yan = input('请输入验证码：')
        self.ac.send_keys_to_element(verify_input, yan).perform()
        time.sleep(1)
        self.ac.reset_actions()
        login_btn = self.driver.find_element(By.CLASS_NAME, 'login-btn')
        # 点击登录
        # self.ac.move_to_element(login_btn).click().perform()
        self.ac.click(login_btn).perform()
        self.ac.reset_actions()

        time.sleep(3)

        f_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/a')
        f_btn.click()

        # time.sleep(2)
        # 清空验证码
        # self.ac.send_keys_to_element(verify_input, Keys.BACK_SPACE).perform()
        # self.ac.reset_actions()
        # self.ac.reset_actions()
        #
        # time.sleep(5)
        # self.ac.move_to_element(verify_input).perform()
        # self.ac.send_keys(Keys.CLEAR).perform()

        # self.driver.find_element_by_name(By.NAME,'password').send_keys('liyan123')
        # # 先输入一个错的验证码
        # self.driver.find_element_by_name(By.NAME,'verify').click()
        # self.driver.find_element_by_name(By.NAME,'verify').send_keys("我")
        # time.sleep(1)
        # # 点击登录
        # self.driver.find_element_by_class_name('login-btn').click()
        # time.sleep(1)
        # # 清除输入的验证码
        # self.driver.find_element_by_name('verify').click()
        # self.driver.find_element_by_name('verify').clear()
        # # self.driver.find_element_by_class_name('login-title').click()
        # time.sleep(1)
        # # 验证码
        # yan = self.getYan()
        # time.sleep(10)
        # verify_input = self.driver.find_element_by_name('verify')
        # ActionChains(self.driver).move_to_element(verify_input).send_keys(Keys.CLEAR)
        # verify_input.send_keys()
        # time.sleep(10)
        # # 点击登录
        # self.driver.find_element_by_class_name('login-btn').click()

    def getYan(self):
        yan = ""
        resp = requests.get(self.yaz_url, headers=self.headers)
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

    # 10秒后关闭
    time.sleep(10)
