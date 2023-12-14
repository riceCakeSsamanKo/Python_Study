import pymysql as pm

conn = pm.connect(host="localhost", user="root", password="password", db="school", charset="utf8mb4")

cursor = conn.cursor()

# 함수 이름 : select_student()
# 기능 : 모든 student 레코드를 검색한 후 출력함
# 반환값 : 없음
# 전달인자 : 없음
def select_student():
    print(">> student 레코드 검색 결과")
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    for cur_row in rows:
        sno = cur_row[0]
        sname = cur_row[1]
        grade = cur_row[2]
        dept = cur_row[3]
        print(sno + ' ' + sname + ' ' + str(grade) + ' ' + dept)


# 함수 이름 : insert_student()
# 기능 : 키보드로부터 속성들을 입력받아서 student 레코드를 삽입함
# 반환값 : 입력받은 값으로 작성한 insert 문장
# 전달인자 : 없음
def insert_student():
    print(">> student 레코드 삽입")
    sno = input("학번: ")
    sname = input("이름: ")
    grade = input("학년: ")
    dept = input("학과: ")
    if sno == "" :
        sql = "insert into student values(NULL, '" + sname + "', " + grade + ", '" + dept + "')"
    else :
        sql = "insert into student values('" + sno + "', '" + sname + "', " + grade + ", '" + dept + "')"

    return sql


# 함수 이름 : execute_transaction()
# 기능 : 트랜잭션을 수행한다. 트랜잭션은 다음과 같이 구성된다.
# 1) 학생들의 grade를 1 증가한다
# 2) 새로운 학생을 insert 한다.
# 트랜잭션은 두개의 sql 쿼리로 구성되며 중간에 error가 발생하는 경우 rollback 된다.
# 반환값 : 없음
# 전달인자 : 없음
def execute_transaction():

    insert_sql = insert_student()

    # set autocommit을 off로 설정하여 sql 여러개를 하나의 트랜잭션으로 구성할 수 있게 환경 설정
    cursor.execute("set autocommit = off")
    cursor.execute("start transaction")  # 트랜잭션 시작

    try:  # 트랜잭션이 실패한 경우 error 발생
        # 1) student들의 grade를 1 증가하는 sql
        sql = """update student 
                set grade = grade + 1"""
        cursor.execute(sql)  # 1번 sql 실행
        print(insert_sql)

        # student insert sql
        cursor.execute(insert_sql)
        # commit query
        cursor.execute("commit")

        # 정상적으로 트랜잭션이 실행된 경우 다음 문구가 실행된다.
        print('Transaction was executed succesfully !')

    except Exception as error:  # error가 발생한 경우 트랜잭션이 실패한 것이기 때문에 rollback을 실행함
        cursor.execute("rollback")
        print(error)
        print('Transaction failed !')

    # autocommit 설정을 on으로 재설정하여 sql 하나가 다시 트랜잭션으로 설정됨.
    cursor.execute("set autocommit = on")



##############
#  메인 코드  #
##############

# 데이터베이스 접속 및 커서 생성
conn = pm.connect(host='localhost', user='root', password='root', db='university', charset='utf8mb4')
cursor = conn.cursor()

# 기존 테이블 삭제
cursor.execute("set foreign_key_checks = 0")
cursor.execute("drop table IF EXISTS student")
cursor.execute("set foreign_key_checks = 1")

# student 테이블 생성
cursor.execute('''create table student(
                sno     char(7) not null,
                sname   varchar(20),
                grade   int,
                dept    varchar(20),
                primary key(sno)
                )''')


# student 레코드 하드코딩으로 삽입
cursor.execute('''insert into student
                  values('B922019', '김영희', 1,'기계')''')
cursor.execute('''insert into student
                  values('B990617', '홍철수', 3,'컴퓨터')''')

# 기존 student 레코드 출력
select_student()

# 트랜잭션을 수행 후 모든 student 레코드 출력
execute_transaction()
select_student()
