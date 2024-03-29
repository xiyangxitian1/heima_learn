import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用  关闭服务器的时候立即释放端口
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

socket_server.bind(('', 8989))

socket_server.listen(128)
#
print('服务端已经启动')
service_client_socket, ip_port = socket_server.accept()
print('客户端的ip地址和端口号：', ip_port)

while True:
    recv_data = service_client_socket.recv(1024)
    if len(recv_data) == 0:
        print('对方下线了')
        break
    print('接收到客户端信息为：', recv_data.decode('gbk'))

    service_client_socket.send('我是服务端，已经收到你的信息'.encode('gbk'))

service_client_socket.close()
#
socket_server.close()
