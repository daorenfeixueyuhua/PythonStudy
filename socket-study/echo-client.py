import sys
from socket import *
serverHost = 'localhost'
serverPort = 8888

message = [b'hello network world']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

socketObj = socket()
socketObj.connect((serverHost, serverPort))

for line in message:
    socketObj.send(line)
    data = socketObj.recv(1024)
    print('Client received:', data)
socketObj.close()