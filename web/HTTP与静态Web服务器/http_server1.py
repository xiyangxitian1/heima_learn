import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server.bind(('', 8080))
server.listen(128)

while True:
    new_server, ip_port = server.accept()

    recv_data = new_server.recv(1024)
    recv_content = recv_data.decode('utf-8')
    print('收到的数据：', recv_content)

    with open(r'F:\英语晨读\EnglishWord\Chapter-1-page-1.html', 'rb') as f:
        send_data = f.read()
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_header = "Server: PWS1.0\r\n"


    # 响应体
    response_body = send_data

    # 拼接响应报文
    response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body

    new_server.send(response_data)
    new_server.close()


