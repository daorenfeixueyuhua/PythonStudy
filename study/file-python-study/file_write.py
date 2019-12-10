# 写文件
file = open('writeFile.txt', 'a+')
""""
    # write()测试
    file.write('hello,world!1111\n')
    contexts = iter(['我爱你', '吗？', '为何多情的人总被无情的伤'])
    print(type(contexts))
    # for i in contexts:
        # file.writelines(i)
    file.writelines(contexts)

"""
"""
    写缓存测试
"""
"""
    file.write('hello,world')
    file.flush()
"""
string = ''
for i in range(0, 10000):
    string = 'hello, world %d \n' % i
    file.write(string)


# 关闭文件
file.close()