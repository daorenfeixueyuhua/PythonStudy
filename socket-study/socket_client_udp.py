import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8889)

while True:
    msg_input = input("请输入要发送的消息")
    if msg_input == "exit":
        break
    sk.sendto(msg_input.encode(),ip_port)

sk.close()
