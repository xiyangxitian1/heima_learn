import socket
import time

client_socket = socket.socket()

client_socket.connect(('192.168.18.33', 9000))
for i in range(50):
    client_socket.send('我是客户端。。'.encode('gbk'))
    recv_data = client_socket.recv(1024)
    if not recv_data:
        print('服务器断开连接了..')
    print('收到服务端的数据:', recv_data.decode('gbk'))
    time.sleep(1)
    if i == 4:
        client_socket.send('Bye'.encode('gbk'))
        # break

client_socket.close()
