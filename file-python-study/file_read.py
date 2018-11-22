# 文件的打开
file = open('openFile.txt','r')

# # read()方法
# read_str = file.read(32)
# print(read_str)
#
# # readline()方法
# readline_str =file.readline()
# print(readline_str)
#
# readlines_str = file.readlines(64)
# # print(readlines_str)
# for row in readlines_str:
#     print(row)

# iter（）方法
iter_str = iter(file)
lines = 0
for line in iter_str:
    print(type(line))
    line += 1
print(lines)