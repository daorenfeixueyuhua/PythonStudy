
# 文件发送机
# 导入模块
import socket

# 实例化模块
sk = socket.socket()

# 定义连接IP和port
ip_port = ('127.0.0.1',9999)
# 服务器连接
sk.connect(ip_port)
# 文件上传
# 打开文件
with open('doc.md', 'rb') as f:
    # 按每一段分割文件
    for i in f:
        # 数据上传
        sk.send(i)
        data = sk.recv(1024)
        if data != b'success':
            continue
# 给服务器发送结束信号
sk.send('quit'.encode())
