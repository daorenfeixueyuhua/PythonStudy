file = open('openFile.txt', 'r')

# 文件描述符
print(file.fileno())

# 文件打开权限
print(file.mode)

# 文件编码格式
print(file.encoding)

# 文件是否关闭
print(file.closed)

file.close()

# 文件是否关闭
print(file.closed)