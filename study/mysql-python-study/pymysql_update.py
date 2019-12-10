import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'dada')
cursor = db.cursor()
name = "update"
id = 1
sql = """
    UPDATE py_user SET name = 'pengda' where id = %d;
""" % (id)
try:
    cursor.execute(sql)
    db.commit()
    print("update successful")
except:
    print("update error")
    db.rollback()

finally:
    db.close()