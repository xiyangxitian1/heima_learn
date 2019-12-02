# 实现局域网内的点对点聊天机器人程序。
# 使用TCP协议编写 socket 程序，分别实现消息的发送端和接收端
# 服务端记录客户端发送的消息，并进行随机回复
# 当客户端发送Bye时结束聊天

import socket
import random
import threading


def handle_client_service(server_client_socket, ip_port):
    while True:
        recv_data = server_client_socket.recv(1024)
        if not recv_data:
            break
        recv_content = recv_data.decode('gbk')
        if recv_content == 'Bye':
            print('客户端说Bye了……')
            break
        print('收到{}发来的数据:{}'.format(ip_port, recv_content))
        server_client_socket.send('发送随机数:{}'.format(random.randint(1, 100)).encode('gbk'))

    print('客户端{}下线了'.format(ip_port))
    server_client_socket.close()


def createServer():
    server_socket = socket.socket()
    # 设置端口可重用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9000))
    server_socket.listen(128)
    print('服务器成功启动了')
    while True:
        server_client_socket, ip_port = server_socket.accept()
        print('已经和客户端{}建立连接'.format(ip_port))
        # handle_client_service(server_client_socket, ip_port)
        threading.Thread(target=handle_client_service, args=(server_client_socket, ip_port), daemon=True).start()


if __name__ == '__main__':
    createServer()
