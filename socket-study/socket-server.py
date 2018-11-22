import socket
sk = socket()
#鼠标放在内建函数上，Ctrl+B，看源码
ip_port = ("127.0.0.1",8888)

sk.bind(ip_port)
sk.listen(5)
print("正在接受数据")
conn,address =sk.accept()
msg ="hello world"
#verson 3.7.0
conn.send(msg.encode())
conn.close()