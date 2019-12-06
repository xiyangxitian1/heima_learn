from selenium import webdriver
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://ntlias-stu.boxuegu.com/#/login'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
username = driver.find_element_by_name('username').send_keys('A191102326')
password = driver.find_element_by_name('password').send_keys('liyan123')
yan = input('请输入验证码：')
driver.find_element_by_name('verify').send_keys(yan)
driver.find_element_by_class_name('login-btn').click()
time.sleep(3)
print(driver.current_window_handle)
print(driver.window_handles)
# 这里会报找不到的错误，可以设置个循环等待  可以导入包 Wait，  现在我自己设置个whileTrue试试
while True:
    try:
        fan_kui_btn = driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
    except Exception:
        print('出错..')
        time.sleep(3)
        # 再次点击登录
        try:
            driver.find_element_by_class_name('login-btn').click()
        except Exception:
            continue
    else:
        print('成功登录')
        break
fan_kui_btn = driver.find_element_by_xpath(
    '//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
fan_kui_btn.click()
print(driver.current_window_handle)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])  # 转换到最新的这个页面中
WebDriverWait(driver, 10).until(lambda elem: elem.find_element_by_class_name('subject-list'))
subject_list = driver.find_element_by_class_name('subject-list')
# driver.find_elements()  找到所有的反馈，都点上
lis = subject_list.find_elements_by_tag_name('li')
for l in lis:
    time.sleep(1)
    l.find_element_by_class_name('el-radio__inner').click()

# 提交
time.sleep(2)
driver.find_element_by_class_name('sub').find_element_by_tag_name('a').click()
time.sleep(5)
driver.close()

# 点击提交
