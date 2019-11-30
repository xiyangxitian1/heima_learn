import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用  关闭服务器的时候立即释放端口
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

socket_server.bind(('', 8989))

socket_server.listen(128)
#
print('服务端已经启动')
service_client_socket, ip_port = socket_server.accept()
service_client_socket.close()
print('客户端的ip地址和端口号：', ip_port)

recv_data = service_client_socket.recv(1024)
print('接收到客户端信息为：', recv_data.decode('gbk'))

service_client_socket.send('我是服务端，已经收到你的信息'.encode('gbk'))

#
# socket_server.close()
