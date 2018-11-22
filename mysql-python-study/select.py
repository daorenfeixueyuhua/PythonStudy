# 查询数据
# import pymysql
from pymysql import *
db = connect("127.0.0.1", "root", "root", "dada")
# db = pymysql.connect("127.0.0.1", "root", "root", "dada")
# db = pymysql.connect('127.0.0.1', 'root', 'root', 'dada')
cursor = db.cursor()

sql = "select * from py_user;"

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
except:
    print("查询失败")