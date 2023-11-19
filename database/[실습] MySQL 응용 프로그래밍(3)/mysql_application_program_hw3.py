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
# create_table(생성할 테이블 명, 기본키(들)의 이름, 생성할 column(들)의 이름 및 도메인 정보, 외래키(들)의 테이블명 및 이름)
def create_table(table_name, pk_names, column_datas, fk_datas):
    # sql 작성
    sql = "create table " + table_name + "(\n "

    # 테이블에 존재하는 column에 대한 sql 작성
    for i in range(len(column_datas)):
        column_data = column_datas[i]

        column_name = column_data[0]
        column_type = column_data[1]

        if i != 0:
            sql += ",\n"
        sql += column_name + " " + column_type

    # 외래키에 대한 sql 작성
    if fk_datas is not None:
        for fk_data in fk_datas:
            # 가져올 외래키의 기본 테이블
            table = fk_data[0]
            # 외래키 이름
            fk_name = fk_data[1]

            sql += ",\n" + "foreign key(" + fk_name + ") references " + table + "(" + fk_name + ")"

    # 기본키에 대한 sql 작성
    sql += ",\nprimary key("
    for i in range(len(pk_names)):
        pk_name = pk_names[i]
        if i != 0:
            sql += ", "
        sql += pk_name
    sql = sql + "));"

    # query 날림
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as error:
        print(error)

    return sql


# select 문 함수
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
        result = cursor.fetchall()
        return sql, result
    except Exception as error:
        print(error)
        return sql, None


def file_write(file, results):
    for result in results:
        for data in result:
            file.write(str(data) + " ")
        file.write("\n")


# 테이블 초기화
init_table()

# 테이블 생성
## student 테이블 생성
sql = create_table("student", ["sno"], [["sno", "varchar(7)"], ["sname", "varchar(20)"],
                                        ["grade", "int default 1"], ["dept", "varchar(20)"]], None)
## course 테이블 생성
sql = create_table("course", ["cno"], [["cno", "varchar(4)"], ["cname", "varchar(30)"], ["credit", "int default 1"],
                                       ["profname", "varchar(20)"], ["dept", "varchar(20)"]], None)
## enroll 테이블 생성
sql = create_table("enroll", ["sno", "cno"],
                   [["sno", "varchar(7)"], ["cno", "varchar(4)"], ["final", "int"], ["lettergrade", "varchar(2)"]],
                   [["student", "sno"], ["course", "cno"]])

# student 데이터 삽입
cursor.execute("insert into student values('B922019','김영희',4,'기계')")
cursor.execute("insert into student values('B990617','홍철수',3,'컴퓨터')")
# course 데이터 삽입
cursor.execute("insert into course values('C101','동역학',3,'김공과','기계')")
cursor.execute("insert into course values('C102','데이터베이스',4,'유대학','컴퓨터')")


def doTask():
    read_file = open("input.txt", "r")
    write_file = open("output.txt", "w")

    while True:
        line = read_file.readline()
        if not line:
            break

        line = line.strip()
        if line == str(0):
            write_file.write("0. 종료")
            print()
            # 파일 닫기
            read_file.close()
            write_file.close()
            break
        elif line == str(1):
            write_file.write("1. student 레코드검색\n")
            sql, results = select("student", "*", None)

            file_write(write_file, results)

        elif line == str(2):
            write_file.write("2. course 레코드 검색\n")
            sql, results = select("course", "*", None)

            file_write(write_file, results)

        elif line == str(3):
            write_file.write("3. enroll 레코드 검색\n")
            sql, results = select("enroll", "*", None)

            file_write(write_file, results)

        elif line == str(4):
            write_file.write("4.enroll 레코드 삽입\n")
            enroll_column = read_file.readline().strip().split()

            # 검색 데이터
            sno = enroll_column[0]
            cno = enroll_column[1]
            final = enroll_column[2]
            letter_grade = enroll_column[3]

            sql = "insert into enroll values (" + "'" + sno + "'" + "," + "'" + cno + "'" + "," + str(final) + "," + "'" + letter_grade + "'" + ");"
            file_write(write_file,[[sno, cno,final, letter_grade]])
            try:
                cursor.execute(sql)
            except Exception as error:
                print(error)

doTask()
init_table()
cursor.close()
