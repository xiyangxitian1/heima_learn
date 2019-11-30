import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('192.168.18.31', 8989))

send_data = '你好'.encode('gbk')
client_socket.send(send_data)
recv_data = client_socket.recv(20000)
recv_content = recv_data.decode('gbk')
print('接收到的数据：', recv_content)
client_socket.close()

# scp 192.168.18.33:C:/Users/Administrator/Desktop/TLIAS客户端* F:/get
# Administrator

