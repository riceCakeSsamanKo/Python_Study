import csv

# CSV 파일 경로
csv_file_path = './Desktop/petplate_food_data.csv'
# SQL 파일 경로
sql_file_path = './Desktop/insert_petplate_food.sql'

# INSERT 문을 저장할 리스트
insert_statements = []

# CSV 파일 읽기
with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # 첫 번째 줄은 헤더
    
    for row in csv_reader:
        values = ', '.join([f"'{value}'" if i == 1 else value for i, value in enumerate(row)])
        insert_statement = f"INSERT INTO raw ({', '.join(headers)}) VALUES ({values});"
        insert_statements.append(insert_statement)

# SQL 파일에 INSERT 문 저장
with open(sql_file_path, mode='w', encoding='utf-8') as file:
    for statement in insert_statements:
        file.write(statement + '\n')

print(f"INSERT statements have been written to {sql_file_path}")
