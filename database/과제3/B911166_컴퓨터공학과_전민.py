import pymysql as pm

conn = pm.connect(host="localhost", user="root", password="password", db="hotel_booking", charset="utf8mb4")
cursor = conn.cursor()


# 함수 이름 : init_table()
# 기능 : 테이블이 존재하는 경우 drop한다.
# 반환값 : 없음
# 전달인자 : 없음
def init_table():
    cursor.execute("set foreign_key_checks = 0")
    cursor.execute("drop table if exists hotel cascade")
    cursor.execute("drop table if exists hotel_room cascade")
    cursor.execute("drop table if exists customer cascade")
    cursor.execute("drop table if exists booking cascade")
    cursor.execute("set foreign_key_checks = 1")


# 함수 이름 : create_table()
# 기능 : 테이블을 생성한다.
# 반환값 : 없음
# 전달인자 : table_name : 테이블 이름,
#          pk_names : [기본키1 이름, 기본키2 이름..., 기본키n 이름](단, n은 1 이상),
#          column_datas : [[column1 이름, column1 도메인], ... [columnN 이름, columnN 도메인], ....] (단, N은 1 이상)
#          fk_datas: [[외래키를 가져올 테이블 명1, 외래키 명1], ... [외래키를 가져올 테이블 명n, 외래키 명n]] (단, n은 1이상)
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
    except Exception as error:
        print("create_table")
        print(error)

    return sql


# 함수 이름 : insert()
# 기능 : 테이블에 정보를 주입
# 반환값 : 없음
# 전달인자 : table_name : 테이블 이름,
#           datas : 해당 테이블의 정보 리스트
def insert(table_name, datas):
    l = len(datas)
    sql = "insert into " + table_name + " values("

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
        conn.commit()
    except Exception as error:
        print("insert:\n" + sql)
        print(error)

    return sql


# 함수 이름 : select()
# 기능 : 테이블에서 정보 조회
# 반환값 : 없음
# 전달인자 : table_name : 테이블 이름,
#          select_target : 조회 대상
#           where_text : 조건문 (없으면 None)
def select(table_names, select_targets, where_text):
    sql = "select "
    num_of_columns = len(select_targets)  # 조회할 column 수
    num_of_tables = len(table_names)

    for i in range(num_of_columns):
        # target == 조회 대상
        target = select_targets[i]
        sql += target

        # ',' 붙이는 조건
        if i != num_of_columns - 1:
            sql += ", "

    sql += "\nfrom "
    for i in range(num_of_tables):
        table = table_names[i]
        sql += table

        # ',' 붙이는 조건
        if i != num_of_tables - 1:
            sql += ", "

    if where_text is not None:
        sql += ("\nwhere " + where_text + ";")

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as error:
        print("select: " + sql)
        print(error)
        return None


# 함수 이름 : delete()
# 기능 : 테이블에서 데이터 삭제.
# 반환값 : 없음
# 전달인자 : table_name: 테이블 명
#          where_text: 조건문
def delete(table_name, where_text):
    sql = "delete\nfrom " + table_name

    if where_text is not None:  # where 문 존재시 작성해줌
        sql += "\nwhere " + where_text
    sql += ";"

    # query 날림
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as error:
        print(error)

    return sql


# 함수 이름 : join()
# 기능 : 파일에서 데이터 읽어들임.
# 반환값 : 없음
# 전달인자 : 없음
def join():
    # 입력 형식: 고객 ID, 이름, 전화번호 정보를 입력 파일로부터 읽기
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = column_values[0]
    name = column_values[1]
    phone = column_values[2]

    insert("customer", [CID, name, phone])

    # 출력 형식
    w_file.write("1.1. 회원가입\n")
    w_file.write("> " + CID + ' ' + name + ' ' + phone + "\n")


user = None  # 로그인한 유저 정보


# 함수 이름 : customer_menu()
# 기능 : 각 선택에 맞는 고객 기능 수행
# 반환값 : 없음
# 전달인자 : 없음
def customer_menu(menu_level_2):
    global user

    if menu_level_2 == 1:
        if user is not None:
            print("이미 로그인 되어있습니다")
        w_file.write("2.1 로그인\n")
        log_in()  # 로그인
    elif menu_level_2 == 2:
        hotel_room_booking()
    elif menu_level_2 == 3:
        hotel_room_reservation_inquiry()
    elif menu_level_2 == 4:
        cancel_booking()
    elif menu_level_2 == 5:
        if user is None:
            print("로그인 필요")
        w_file.write("2.5 로그아웃\n")
        log_out()  # 로그아웃
    else:
        print("잘못된 입력")


# ----- customer_menu 세부 기능 구현
# 2.2
def hotel_room_booking():
    line = r_file.readline()
    line = line.strip().split()

    hid = line[0]
    cid = user
    room_number = line[1]
    check_in = line[2]
    check_out = line[3]

    insert("booking", [hid, cid, room_number, check_in, check_out])
    w_file.write("2.2 호텔방 예약\n")
    w_file.write("> " + hid + " " + room_number + " " + check_in + " " + check_out + "\n")


# 2.3
def hotel_room_reservation_inquiry():
    select_data_list = select(["booking"], ["hid", "room_number", "check_in", "check_out"], None)
    w_file.write("2.3 호텔방 예약 조회\n")

    for select_datas in select_data_list:
        result = "> {"
        for data in select_datas:
            result += (str(data) + " ")
        result += "}"
        w_file.write(result + "\n")


# 2.4
def cancel_booking():
    line = r_file.readline().strip().split()
    hid = str(line[0])
    room_number = str(line[1])
    cid = user

    where = "hid = " + "'" + hid + "'" + " and room_number = " + "'" + room_number + "'" + " and cid = " + "'" + cid + "'"
    delete("booking", where)

    w_file.write("2.4 호텔방 예약 취소\n")
    w_file.write("> " + hid + " " + room_number + "\n")


# 함수 이름 : admin_menu()
# 기능 : 각 선택에 맞는 관리자 기능 수행
# 반환값 : 없음
# 전달인자 : 없음
def admin_menu(menu_level_2):
    global user

    if menu_level_2 == 1:
        if user is not None:
            print("이미 로그인 되어있습니다")
        w_file.write("3.1 로그인\n")
        log_in()  # 로그인
    elif menu_level_2 == 2:
        hotel_booking()  # 호텔방 예약
    elif menu_level_2 == 3:
        register_hotel_room_information()  # 호텔방 정보 등록
    elif menu_level_2 == 4:
        check_booking_history()  # 예약 내역 조회
    elif menu_level_2 == 5:
        if user is None:
            print("로그인 필요")
        w_file.write("3.5 로그아웃\n")
        log_out()  # 로그아웃
    else:
        print("잘못된 입력")


# ----- admin_menu 세부 기능 구현 ----- #
# 3.1
def log_in():
    global user
    read_user = r_file.readline().strip()

    user = read_user
    w_file.write("> " + user + "\n")


# 3.2
def hotel_booking():
    line = r_file.readline()
    line = line.strip().split()

    hid = line[0]
    hname = line[1]
    address = line[2]
    insert("hotel", [hid, hname, address])
    w_file.write("3.2 호텔 정보 등록\n")
    w_file.write("> " + hid + " " + hname + " " + address + "\n")


# 3.3
def register_hotel_room_information():
    line = r_file.readline()
    line = line.strip().split()

    hid = line[0]
    room_number = line[1]
    price = line[2]

    insert("hotel_room", [hid, room_number, price])
    w_file.write("3.3 호텔방 정보 등록\n")
    w_file.write("> " + hid + " " + room_number + " " + price + "\n")


# 3.4
def check_booking_history():
    select_data_list = (
        select(["booking b", "hotel h", "hotel_room hr, customer c"],
               ["b.cid", "c.cname", "b.hid", "h.hname", "h.address", "hr.room_number", "hr.price",
                "b.check_in", "b.check_out"],
               "b.cid = c.cid and b.hid = h.hid and b.hid = hr.hid and b.room_number = hr.room_number"))

    w_file.write("3.4 예약 내역 조회\n")

    # 수정부분! date의 -를 /로 변환해야 함.
    for select_datas in select_data_list:
        cid = select_datas[0]
        cname = select_datas[1]
        hid = select_datas[2]
        hname = select_datas[3]
        address = select_datas[4]
        room_number = select_datas[5]
        price = str(select_datas[6])
        check_in = str(select_datas[7]).replace("-", "/")
        check_out = str(select_datas[8]).replace("-", "/")

        sql_data = []
        sql_data.append(cid)
        sql_data.append(cname)
        sql_data.append(hid)
        sql_data.append(hname)
        sql_data.append(address)
        sql_data.append(room_number)
        sql_data.append(price)
        sql_data.append(check_in)
        sql_data.append(check_out)

        result = ""
        for data in sql_data:
            result += (str(data) + " ")
        w_file.write("> " + result + "\n")


# 3.5
def log_out():
    global user
    w_file.write("> " + user + "\n")
    user = None


def exit():
    w_file.write("1.2. 종료\n")


def doTask():
    # 종료 메뉴(1 2)가 입력되기 전까지 반복함
    while True:
        # 입력파일에서 메뉴 숫자 2개 읽기
        line = r_file.readline()
        line = line.strip()
        menu_levels = line.split()

        # 메뉴 파싱을 위한 level 구분
        menu_level_1 = int(menu_levels[0])
        menu_level_2 = int(menu_levels[1])

        # 메뉴 구분 및 해당 연산 수행
        if menu_level_1 == 1:
            if menu_level_2 == 1:
                join()
            elif menu_level_2 == 2:
                exit()
                break
        elif menu_level_1 == 2:
            customer_menu(menu_level_2)
        elif menu_level_1 == 3:
            admin_menu(menu_level_2)


##############
#  메인 코드  #
##############
init_table()

# 테이블 생성
create_table("hotel", ["hid"],
             [["hid", "varchar(30) not null"], ["hname", "varchar(30)"], ["address", "varchar(30)"]],
             None)
create_table("hotel_room", ["hid", "room_number"],
             [["hid", "varchar(30) not null"], ["room_number", "varchar(30) not null"], ["price", "int"]],
             [["hotel", "hid"]])
cursor.execute("create index index_name on hotel_room(room_number);")
create_table("customer", ["cid"],
             [["cid", "varchar(30) not null"], ["cname", "varchar(30)"], ["phoneNumber", "varchar(30)"]],
             None)
create_table("booking", ["hid", "cid", "room_number"],
             [["hid", "varchar(30) not null"], ["cid", "varchar(30) not null"], ["room_number", "varchar(30) not null"],
              ["check_in", "date"],
              ["check_out", "date"]],
             [["hotel", "hid"], ["customer", "cid"], ["hotel_room", "room_number"]])

r_file = open("input.txt", "r", encoding="utf-8")
w_file = open("output.txt", "w")

doTask()
r_file.close()
w_file.close()
init_table()
