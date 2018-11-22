# 服务器
from socket import *
host = ''
port = 8888

socketObj = socket()
socketObj.bind((host, port))
socketObj.listen(5)

while True:
    connection, address = socketObj.accept()
    print('Server connected by', address)
    while True:
        data = connection.recv(1024)
        if not data:break
        connection.send(b'Echo=>'+data)
    connection.close()