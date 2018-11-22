# 导入os模块
import os
fd= os.open('osFile.txt', os.O_CREAT | os.O_RDWR)

# 写入内容
n = os.write(fd, b'pengda')
print(n)

# 重置文件指针位置
l = os.lseek(fd, 0, os.SEEK_SET)
print(l)

# 读取文件
str1 = os.read(fd, 6)
print(str1)

# 文件关闭
os.close(fd)

os.remove('osFile.txt')

