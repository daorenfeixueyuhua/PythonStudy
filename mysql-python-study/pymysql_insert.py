import pymysql
db = pymysql.connect("localhost", 'root', 'root', 'dada')
cursor = db.cursor()

sql = """
    insert into py_user (name) values("pengda");
"""

try:
    cursor.execute(sql)
    db.commit()
except:
    print("insert error")
    db.rollback()

db.close()