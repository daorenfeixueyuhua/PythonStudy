import os
import zipfile


# 压缩base_path下的所有文件，并以该文件命名
def ZipFile(base_path):
    for zip_file in os.listdir(base_path):
        z = zipfile.ZipFile(base_path + zip_file + '.zip', 'w')
        for file in os.listdir(base_path + zip_file + '/'):
            z.write(base_path + zip_file + '/' + file)
        print('zip ' + zip_file + ' successful!')
        z.close()

# 删除改base_path下的所有 ".zip" 文件
def DeleteZip(base_path):
    for file in os.listdir(base_path):
        if zipfile.is_zipfile(filename=base_path + file):
            os.remove(base_path + file)
            print('delete ' + file)


if __name__ == '__main__':
    base_path = 'D:/Pictures/Saved Pictures/Images/full/'
    DeleteZip(base_path)
