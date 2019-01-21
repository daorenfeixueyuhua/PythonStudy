## Socket网络编程：
### Socket简介：
	Socket是电脑网络中进程间数据流的端点
	Socket操作系统的通信机制
	应用程序通过Socket进行网络数据的传输
	
	Tcp
	
	Socket通信方式：
		UDP和TCP
		
	为什么选择Socket
		1.Socket能够适应多种网络协议
		2.Socket是基础应用，了解Socket可以举一反三
		3.服务器传输大量涉及网络协议，离不开socket应用

### Socket参数
	family：地址簇
		socket.AF_INET IPv4（默认）
		socket.AF_INET6 IPv6
		socket.AF_UNIX 只能用于单一的Unix系统之间的进程通信
	type：类型
		socket.SOCK_STREAM		流式socket，for TCP（）默认
		socket.SOCK_DGRAN		数据报式socket，for UDP
		socket.SOCK_RAW			原始套接字
		socket.SOCK_RDM			可靠UDP形式
		socket.SOCK_SEQPACKET	可靠的连续数据包服务
	proto：协议号
		0：默认
		CAN_RAM或者CAN_BCM:地址簇未AF_CAN时

### Socket的非堵塞

### Socket用处
	文件上传