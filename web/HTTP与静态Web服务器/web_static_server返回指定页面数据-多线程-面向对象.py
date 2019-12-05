import socket
import threading


class HttpWebServer(object):
    """面向对象HttpWebServer"""

    def __init__(self):
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        server_socket.bind(('', 8080))
        server_socket.listen(128)
        self.server_socket = server_socket

    @staticmethod
    def handle_req(new_server, ip_port):
        recv_data = b''
        while True:
            recv_data1 = new_server.recv(10)
            print(recv_data1)
            if recv_data1:
                recv_data += recv_data1

            if not recv_data1:
                print('浏览器关闭了..')
                print(ip_port, '关闭连接')
                new_server.close()
                return
            if recv_data.endswith(b'\r\n\r\n'):
                break
        recv_content = recv_data.decode('utf-8')
        print('收到的数据：', recv_content)

        # 请求页面
        req_page = recv_content.split(maxsplit=2)[1]
        print('请求页面：', req_page)
        if req_page == '/':
            req_page = '/index.html'
        try:
            with open('static' + req_page, 'rb') as f:
                send_data = f.read()
        except FileNotFoundError as e:
            print('请求页不存在……')
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            with open('static/error.html', 'rb') as f:
                send_data = f.read()
            # 响应体
            response_body = send_data
        else:
            print('请求存在……')
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 响应体
            response_body = send_data
        finally:
            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            new_server.send(response_data)
            new_server.close()

    def start(self):
        print('服务器启动，正在监听……')
        while True:
            new_server, ip_port = self.server_socket.accept()
            print('建立连接:', ip_port)
            threading.Thread(target=self.handle_req, args=(new_server, ip_port), daemon=True).start()


def main():
    httpWebServer = HttpWebServer()
    httpWebServer.start()


if __name__ == '__main__':
    main()
