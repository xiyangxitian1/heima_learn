with open(r'F:\英语晨读\EnglishWord\Chapter-1-page-1.html', 'r') as f:
    send_data = f.read()
# 响应行
response_line = "HTTP/1.1 200 OK\r\n"
# 响应头
response_header = "Server: PWS1.0\r\n"

# 响应体
response_body = send_data

# 拼接响应报文
response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
