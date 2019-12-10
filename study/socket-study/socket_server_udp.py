import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ('127.0.0.1',8889)
sk.bind(ip_port)
while True:
    data = sk.recv(1024)
    print(data.decode())

# 没有关闭方式
