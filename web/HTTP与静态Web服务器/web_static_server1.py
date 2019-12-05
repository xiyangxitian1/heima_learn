import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
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

            while True:
                self.data = self.request.recv(1024)  #
                print('接收到的数据：' + self.data)

                print("{} send:".format(self.client_address), self.data)
                if not self.data:
                    print("connection lost")
                    break
                self.request.sendall(self.data.upper())
                self.request.close()  # 一次连接就断开
        except Exception as e:
            print(self.client_address, "连接断开")

    # finally:
    #     self.request.close()

    def setup(self):
        print("before handle,连接建立：", self.client_address)

    def finish(self):
        print("finish run  after handle")


if __name__ == "__main__":
    # HOST, PORT = "localhost", 9998
    HOST, PORT = '', 8080
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.allow_reuse_address = True  # 设置端口可复用  默认是False
    server.request_queue_size = 128  # 默认为5
    server.serve_forever()
