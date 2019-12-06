import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests

driver = webdriver.Chrome()
url = 'https://www.zhihu.com/signin?next=%2F'
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/form/div[1]/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/form/div[2]/div/label/input').send_keys(
    'username')
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/form/div[3]/div/label/input').send_keys(
    'passsword')
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/form/button').click()
time.sleep(5)
# img_url = driver.find_element(By.CLASS_NAME, 'Captcha-englishImg').get_attribute('src')
# captcha = driver.find_element_by_class_name('Captcha-englishImg')
# img_url = captcha.get_attribute('src')
# img = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/form/div[4]/div/div[2]/img')
img = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/form/div[4]/div/div[2]/img')
img_url = img.get_attribute('src')
print(img_url)
resp_content = requests.get(img_url)
if resp_content.status_code == 200:
    with open('3.jpg', 'w') as f:
        f.write(resp_content.content)
