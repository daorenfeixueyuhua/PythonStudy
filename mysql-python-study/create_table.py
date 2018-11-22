import pymysql

db = pymysql.connect('localhost', 'root', 'root','dada')
cursor = db.cursor()

cursor.execute("drop table if exists py_user")

# SQL
sql = "create table py_user(id int not null auto_increment primary key, name varchar(20) not null);"

cursor.execute(sql)
cursor.close()
db.close()
