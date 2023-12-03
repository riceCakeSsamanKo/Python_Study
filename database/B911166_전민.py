import pymysql as pm

conn = pm.connect(host="localhost", user="root", password="password", db="school", charset="utf8mb4")

cursor = conn.cursor()


# 테이블이 존재하는 경우 기존 테이블 제거
def init_table():
    cursor.execute("set foreign_key_checks = 0")  # fk 체크 안함
    cursor.execute("drop table if exists teacher cascade")
    cursor.execute("set foreign_key_checks = 1")  # fk 체크


# teacher 테이블 정의
def create_table():
    cursor.execute("create table teacher("
                   "t_id varchar(10) not null,"
                   "t_no varchar(30),"
                   "primary key (t_id));")


def insert_into_teacher(t_id, t_no):
    sql = "insert into teacher values (" + "'" + t_id + "'" + "," + "'" + t_no + "'" + ");"
    print(sql)
    cursor.execute(sql)


init_table()
create_table()

record_num = int(input("생성할 teacher 테이블의 레코드 수를 입력하시오: "))

for i in range(record_num):
    t_id = "t" + str(i)
    t_no = "t" + str(i) +str(i)
    print(t_no)
    insert_into_teacher(t_id, t_no)

conn.commit()
conn.close()
