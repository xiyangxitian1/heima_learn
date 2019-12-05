import socket

'''模拟浏览器访问百度，并获取返回的数据'''
client = socket.socket()
# client.connect(('39.156.69.79', 80))
client.connect(('wwww.baidu.com', 80))  # 200 OK
# client.connect(('220.181.38.150', 80)) # 302 重定向
req_h = 'GET / HTTP/1.1\r\n'  # 请求行（请求方式 资源路径 协议版本）
req_head = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n' \
           'Accept-Encoding: gzip, deflate, br\r\n' \
           'Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8\r\n' \
           'Cache-Control: no-cache\r\n' \
           'Connection: keep-alive\r\n' \
           'Host: www.baidu.com\r\n' \
           'Pragma: no-cache\r\n' \
           'Sec-Fetch-Mode: navigate\r\n' \
           'Sec-Fetch-Site: cross-site\r\n' \
           'Sec-Fetch-User: ?1\r\n' \
           'Upgrade-Insecure-Requests: 1\r\n' \
           'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36\r\n'
# req_head = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36\r\n'
req_data = req_h + req_head + '\r\n'
client.send(req_data.encode('utf-8'))

recv_data = client.recv(4096)
print('收到的数据:', recv_data.decode('utf-8'))
client.close()
