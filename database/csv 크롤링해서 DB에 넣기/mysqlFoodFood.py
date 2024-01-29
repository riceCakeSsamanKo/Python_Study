import csv
import mysqlDbQuery

dbConn = mysqlDbQuery.mysqlDbConnection('root', '7721', '127.0.0.1', 3306, 'foodfood_db')
cursor = dbConn.cursor()

file = open('C://Users/mulso//Desktop//food_data.csv', 'r', encoding='UTF8')
fReader = csv.reader(file)

cnt = 0
for line in fReader:
    # if cnt == 0:
    #     continue
    # print(line)
    cnt += 1
    query = "INSERT INTO example VALUES ('{0}', '{1}', '{2}', '{3}','{4}','{5}','{6}','{7}','{8}', '{9}','{10}','{11}')".format(
        line[0], line[1], line[2], line[3], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10],
        line[11])
    cursor.execute(query)

file.close()

dbConn.commit()
cursor.close()
mysqlDbQuery.mysqlDbClose(dbConn)
