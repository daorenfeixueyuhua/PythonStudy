
# 文件的接受
# 导入模块
import socket
# 实例化
sk = socket.socket()
# 定义连接IP和port
ip_port = ('127.0.0.1',9999)
# 绑定IP和port
sk.bind(ip_port)
# 最大连接数
sk.listen(5)
# 进入循环
while True:
    # 等待客户端连接
    conn,address=sk.accept()
    # 一直使用当前连接进行数据发送
    # 知道结束标志出现
    # 打开文件等待数据写入
    while True:
        with open('file', 'ab') as f:
            # 接受数据
            data = conn.recv(1024)
            if data == b'quit':
                break
            # 写入文件
            f.write(data)
        conn.send("success".encode())
    print("数据接受完成")
# 打印信息
print("关闭连接")
# 关闭连接
conn.close()