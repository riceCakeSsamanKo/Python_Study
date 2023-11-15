import pymysql as pm

conn = pm.connect(host="localhost", user="root", password="password", db="university", charset="utf8mb4")

cursor = conn.cursor()


# 테이블이 존재하는 경우 기존 테이블 제거
def init_table():
    cursor.execute("set foreign_key_checks = 0")  # fk 체크 안함
    cursor.execute("drop table if exists student cascade")
    cursor.execute("drop table if exists course cascade")
    cursor.execute("drop table if exists enroll cascade")
    cursor.execute("set foreign_key_checks = 1")  # fk 체크


# 테이블 생성 함수
def create_table(table_name, pk_data, column_datas):
    # sql 작성
    sql = "create table " + table_name + "(\n "
    pk_name = pk_data[0]
    pk_type = pk_data[1]

    sql += pk_name + " " + pk_type + \
           " not null,\n primary key " + "(" + pk_name + ")"
    for column_data in column_datas:
        column_name = column_data[0]
        column_type = column_data[1]

        sql += ",\n " + column_name + " " + column_type
    sql = sql + ");"

    # query 날림
    try:
        cursor.execute(sql)
    except Exception as error:
        print(error)

    return sql


# insert문 함수
def insert(table_name, datas):
    l = len(datas)
    sql = "insert into " + table_name + "\nvalues("

    # 길이 카운트(',' 넣을지 말지 결정)
    cnt = 0
    for data in datas:
        cnt += 1

        if type(data) == str:  # 숫자의 경우에는 별도로 따옴표를 붙이지 않는다.
            data = "'" + data + "'"
        sql += str(data)

        if cnt != l:
            sql += ","
    sql += ");"

    # query 날림
    try:
        cursor.execute(sql)
    except Exception as error:
        print(error)

    return sql


# update문 함수
def update(table_name, set_text, where_text):
    # sql 생성
    sql = "update " + table_name + "\nset " + set_text

    if where_text is not None:  # where 문 사용 유무 체크. 존재시 where 문 삽입
        sql += "\nwhere " + where_text + ";"

    # query 날림
    try:
        cursor.execute(sql)
    except Exception as error:
        print(error)

    return sql


# delete문 함수
def delete(table_name, where_text):
    sql = "delete\nfrom " + table_name

    if where_text is not None:  # where 문 존재시 작성해줌
        sql += "\nwhere " + where_text

    sql += ";"

    # query 날림
    try:
        cursor.execute(sql)
    except Exception as error:
        print(error)

    return sql


def select(table_name, select_targets, where_text):
    sql = "select "
    num_of_columns = len(select_targets)  # 조회할 column 수

    for i in range(num_of_columns):
        # target == 조회 대상
        target = select_targets[i]
        sql += target

        # ',' 붙이는 조건
        if i != num_of_columns - 1:
            sql += ", "
    sql += "\nfrom " + table_name

    if where_text is not None:
        sql += "\nwhere " + where_text + ";"

    try:
        cursor.execute(sql)
    except Exception as error:
        print(error)

    result = cursor.fetchall()
    return sql, result


# 테이블 초기화
init_table()

# 테이블 생성
create_table("student", ["sno", "varchar(7)"],
             [["sname", "varchar(20)"], ["grade", "int default 1"], ["dept", "varchar(20)"]])
create_table("course", ["cno", "varchar(4)"],
             [["cname", "varchar(30)"], ["credit", "int default 1"],
              ["profname", "varchar(20)"], ["dept", "varchar(20)"]])

while True:
    zero = "0. 종료"
    one = "1.student 레코드 삽입"
    two = "2.course 레코드 삽입"
    three = "3.student 레코드 검색"
    four = "4.course 레코드 검색\n"
    print(zero)
    print(one)
    print(two)
    print(three)
    print(four)

    user_select = input("기능을 선택하시오: ")
    # 종료
    if user_select == str(0):
        break
    elif user_select == str(1):
        print(">> " + one)

        sno = input("학번: ")
        sname = input("이름: ")
        grade = int(input("학년: "))
        dept = input("학과: ")

        insert("student", [sno, sname, grade, dept])
    elif user_select == str(2):
        print(">> " + two)

        cno = input("과목번호: ")
        cname = input("과목이름: ")
        credit = int(input("학점: "))
        profname = input("교수이름: ")
        dept = input("학과: ")

        insert("course", [cno, cname, credit, profname, dept])
    elif user_select == str(3):
        # 조회
        sql, results = select("student", "*", None)

        # 출력
        print("%7s %20s %5s %20s" % ("학번", "이름", "학년", "학과"))
        for result in results:
            sno = result[0]
            sname = result[1]
            grade = result[2]
            dept = result[3]

            print("%7s %20s %5s %20s" % (sno, sname, grade, dept))
    elif user_select == str(4):
        # 조회
        sql, results = select("course", "*", None)
        # 출력
        print("%4s %20s %5s %20s %20s" % ("과목번호", "과목이름", "학점", "교수이름", "학과"))
        for result in results:
            cno = result[0]
            cname = result[1]
            credit = result[2]
            profname = result[3]
            dept = result[4]

            print("%4s %20s %5d %20s %20s" % (cno, cname, credit, profname, dept))
