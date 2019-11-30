import socket
import time
import threading

threadNum = 0



def handle_client_req(service_client_socket, ip_port):
    while True:
        recv_data = service_client_socket.recv(1024)
        if len(recv_data) == 0:
            print(ip_port, '下线了')
            break
        print('接收到客户端信息为：', recv_data.decode('gbk'))
        service_client_socket.send('我是服务端，已经收到你的信息'.encode('gbk'))
    service_client_socket.close()


if __name__ == '__main__':
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用  关闭服务器的时候立即释放端口
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    socket_server.bind(('', 8989))

    socket_server.listen(128)
    begin = time.time()
    #
    print('服务端已经启动')
    while True:
        service_client_socket, ip_port = socket_server.accept()
        print('现在连接的客户端的ip地址和端口号：', ip_port)
        # 设置守护线程并且启动
        threading.Thread(target=handle_client_req, args=(service_client_socket, ip_port), daemon=True).start()
        # handle_client_req(service_client_socket, ip_port)

        # if time.time() - begin > 1000 * 60:  #  大于1分钟就关服务器
        #     break
        # print('退出')
        # exit()


    #
    socket_server.close()
