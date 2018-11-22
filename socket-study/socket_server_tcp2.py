# 导入模块
import socketserver
import random

# 定义一个类
class MyServer(socketserver.BaseRequestHandler):
    # 如果handle方法报错
    # 首先执行setup
    def setup(self):
        pass

    #  然后实行handle
    def handle(self):
        # 定义连接变量
        conn = self.request
        # 发送消息定义
        msg = "Hello，World"
        # 消息发送
        conn.send(msg.encode())
        # 进入循环，不断接受客户端的消息
        while True:
            # 接受客户端消息
            data = conn.recv(1024)
            # 打印消息
            print(data.decode())
            if data == b'exit':
                break
            # 返回消息
            conn.send(data)
            # 发送随机数
            conn.send(str(random.randint(1,1000)).encode())
            conn.close()
    # 最后之心finish
    def finish(self):
        pass


if __name__ == "__main__":
    # 创建多线程实例
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8888),MyServer)
    # 开启异步多线程，等待连接
    server.serve_forever()
