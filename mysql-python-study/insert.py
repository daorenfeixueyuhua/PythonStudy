# 插入数据
from pymysql import *
import pymysql
db = pymysql.connect('localhost', 'root', 'root', 'dada')
cursor = db.cursor()
sql = "insert into py_user (name) values('hello');"
try:
    cursor.execute(sql)
    db.commit()
    print("插入成功")
except:
    print("插入失败")
    db.rollback()

cursor.close()
db.close()