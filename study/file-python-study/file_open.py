# 文件的打开
file = open('openFile.txt', 'a+')

# 要写入的内容
context = 'hello,world\n'

# 写入文件
file.write(context)

# 关闭文件
file.close()