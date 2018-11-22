import pymysql

# 打开数据库
db = pymysql.connect('localhost', 'root', 'root', 'dada')
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print(data)
cursor.close()
db.close()