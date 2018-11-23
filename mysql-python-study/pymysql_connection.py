import pymysql

db = pymysql.connect("localhost", 'root', 'root', 'dada')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("DataBase version: %s" % data)
db.close()
