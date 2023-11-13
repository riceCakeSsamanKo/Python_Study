import pymysql as pm

conn = pm.connect(host="localhost", user="root", password="password", db="university", charset="utf8mb4")

cursor = conn.cursor()

sql = "select * from student"

cursor.execute(sql)

rows = cursor.fetchall()
print(rows)

conn.close()
