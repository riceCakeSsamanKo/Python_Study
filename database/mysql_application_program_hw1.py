import pymysql as pm

conn = pm.connect(host="localhost", user="root", password="password", db="university", charset="utf8mb4")

cursor = conn.cursor()

# 테이블이 존재하는 경우 기존 테이블 제거
sql = "drop table if exists student"
cursor.execute(sql)

# 테이블 생성
sql = '''create table student(  
        sno varchar(255) not null,
        sname varchar(255),
        grade int default 1,
        dept varchar(255),
        primary key (sno));'''
cursor.execute(sql)

try:  # 예외처리
    sql = "insert into student values('B123456', 'Park', 2, 'Computer')"
except Exception as error:  # 예외의 경우 메시지 출력
    print(error)

# update 문
sql = '''update student   
        set grade = grade+1
        where grade <= 1;'''

try:
    cursor.execute(sql)
except Exception as error:
    print(error)

# delete 문
sql = '''delete
        from student
        where grade <= 1;'''

try:
    cursor.execute(sql)
except Exception as error:
    print(error)

# select 문: grade가 4이상인 학생 조회
sql = '''select *
        from student
        where grade >=4;'''

cursor.execute(sql)

selected_rows = cursor.fetchall()
for row in selected_rows:
    sno = row[0]
    sname = row[1]
    grade = row[2]
    dept = row[3]

    # 조회한 내영 출력
    print("%7s %20s %5d %20s" % (sno, sname, grade, dept))

# 공백 입력전까지 계속해서 데이터 입력하는 프로그램

