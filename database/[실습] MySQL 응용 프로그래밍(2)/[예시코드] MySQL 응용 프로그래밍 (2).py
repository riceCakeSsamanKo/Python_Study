import pymysql


# 함수 이름 : insert_student()
# 기능 : 키보드로부터 속성들을 입력받아서 student 레코드를 삽입함
# 반환값 : 없음
# 전달인자 : 없음
def insert_student():
    print(">> 1. student 레코드 삽입")
    sno = input("학번: ")
    sname = input("이름: ")
    grade = input("학년: ")
    dept = input("학과: ")
    sql = "insert into student values('" + sno + "', '" + sname + "', " + grade + ", '" + dept + "')"
    cursor.execute(sql)


# 함수 이름 : insert_course()
# 기능 : 키보드로부터 속성들을 입력받아서 course 레코드를 삽입함
# 반환값 : 없음
# 전달인자 : 없음
def insert_course():
    print(">> 2. course 레코드 삽입")
    cno = input("과목번호: ")
    cname = input("과목이름: ")
    credit = input("학점: ")
    profname = input("교수이름: ")
    dept = input("학과: ")
    sql = "insert into course values('" + cno + "', '" + cname + "', " + credit + ", '" + profname + "', '" + dept + "')"
    cursor.execute(sql)


# 함수 이름 : select_student()
# 기능 : student 레코드를 검색해서 출력함
# 반환값 : 없음
# 전달인자 : 없음
def select_student():
    print("%7s %20s %5s %20s" % ("학번", "이름", "학년", "학과"))
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    for cur_row in rows:
        sno = cur_row[0]
        sname = cur_row[1]
        grade = str(cur_row[2])
        dept = cur_row[3]
        print("%7s %20s %5s %20s" % (sno, sname, grade, dept))


# 함수 이름 : select_course()
# 기능 : course 레코드를 검색해서 출력함
# 반환값 : 없음
# 전달인자 : 없음
def select_course():
    print("%4s %30s %5s %20s %20s" % ("번호", "과목이름", "학점", "교수이름", "학과"))
    cursor.execute("select * from course")
    rows = cursor.fetchall()
    for cur_row in rows:
        cno = cur_row[0]
        cname = cur_row[1]
        credit = str(cur_row[2])
        profname = cur_row[3]
        dept = cur_row[4]
        print("%4s %30s %5s %20s %20s" % (cno, cname, credit, profname, dept))




# 데이터베이스 접속 및 커서 생성
conn = pymysql.connect(host = 'localhost', user = 'root',
    password = 'root', db ='university', charset = 'utf8mb4')
cursor = conn.cursor()

# 기존 테이블 삭제
cursor.execute("set foreign_key_checks = 0")
cursor.execute("drop table IF EXISTS student cascade")
cursor.execute("drop table IF EXISTS course cascade")
cursor.execute("drop table IF EXISTS enroll cascade")
cursor.execute("set foreign_key_checks = 1")

# student 테이블 생성
cursor.execute('''create table student(
                sno char(7) not null,
                sname   varchar(20),
                grade   int,
                dept    varchar(20),
                primary key (sno)
                )''')

# course 테이블 생성
cursor.execute('''create table course(
                cno char(4) not null,
                cname   varchar(30),
                credit  int,
                profname    varchar(20),
                dept    varchar(20),
                primary key (cno)
                )''')

# 기능 선택 및 실행
while True:
    print("0. 종료")
    print("1. student 레코드 삽입")
    print("2. course 레코드 삽입")
    print("3. student 레코드 검색")
    print("4. course 레코드 검색")
    input_function_num = int(input("기능을 선택하시오: "))
    if input_function_num == 0:
        break
    elif input_function_num == 1:
        insert_student()
    elif input_function_num == 2:
        insert_course()
    elif input_function_num == 3:
        select_student()
    elif input_function_num == 4:
        select_course()

# 데이터베이스 접속 종료
conn.close()