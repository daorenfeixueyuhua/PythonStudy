import os

base_path = 'D:/Pictures/Saved Pictures/Images/full/'

os.chdir(base_path)

file_list = os.listdir(base_path)

file_length = len(file_list)

i = 0
for file in file_list:
    file_pre_name = str(i // 100) + '/'
    if not os.path.exists(base_path + file_pre_name):
        os.mkdir(base_path + file_pre_name)
    i += 1
    os.rename(base_path + file, base_path + file_pre_name + file)
