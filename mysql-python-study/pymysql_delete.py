import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'dada')
cursor = db.cursor()
name = "update"
id = 1
sql = """
    DELETE FROM py_user WHERE id = %d;
""" % (id)
try:
    cursor.execute(sql)
    db.commit()
    print("delete successful")
except:
    print("delete error")
    db.rollback()

finally:
    db.close()