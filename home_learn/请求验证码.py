import time
import requests

url = 'http://ntlias-stu.boxuegu.com/user/verifyCode?r=0.010145262830455026'

resp = requests.get(url)

print(resp)
with open('1.jpg', 'wb') as f:
    f.write(resp.content)

