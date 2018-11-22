# 导入os模块
import os

# 文件指针操作
file = open('pointerFile.txt', 'r')
# 读第一个
print(file.read(3))
# 读最后一个
print(file.read(3))
file.seek(0, os.SEEK_CUR)
print(file.read(3))