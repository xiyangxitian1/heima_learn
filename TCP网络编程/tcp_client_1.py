import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.18.31', 8989))
# while True:
# message = input('请输入你要给服务端的信息：')
message = 'a'
send_data = message.encode('gbk')
client_socket.send(send_data)
recv_data = client_socket.recv(2)
while recv_data:
    recv_content = recv_data.decode('gbk')
    print('接收到的数据：', recv_content)
    recv_data = client_socket.recv(2)
    print('a:', recv_data)

print('结束')

# client_socket.close()
# time.sleep(2)

client_socket.close()

# scp 192.168.18.33:C:/Users/Administrator/Desktop/TLIAS客户端* F:/get
# Administrator
