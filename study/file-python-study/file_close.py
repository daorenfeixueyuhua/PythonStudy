file_list = []
for i in range(10000):
    file_list.append(open('openFile.txt', 'r'))
    print(i)