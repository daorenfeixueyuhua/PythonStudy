# 文件编码的测试
# 导入codecs模块
import codecs
file = codecs.open('encodingFile.txt','r',codecs.BOM_UTF8 )
file.write('test')
file.close()
"""
    文件会乱码
    file = open('encodingFile.txt', 'w')
    file.write(u'彭达')
    file.close()

"""