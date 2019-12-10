import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'dada')
cursor = db.cursor()
startIndex = 0
endIndex = 10
sql = """
    SELECT dict_id, dict_type_code, dict_type_name, dict_item_name, 
    dict_item_code, dict_sort, dict_enable, dict_memo FROM base_dict WHERE dict_enable = 1 LIMIT %d,%d;
""" % (startIndex, endIndex)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print("select successful")
    for row in results:
        id = row[0]
        typeCode = row[1]
        typeName = row[2]
        itemName = row[3]
        itemCode = row[4]
        Demo = row[7]
        print(row)

except:
    print("select error")
finally:
    db.close()