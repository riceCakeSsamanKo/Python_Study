# dict()는 자체적인 hashing function을 통해 인덱싱을 하기 때문에 검색 및 수정에 있어 O(1)의 시간 복잡도를 갖는다

# dict 초기화
data = dict({"딸기":"strawberry"})

# (key,value) 삽입 . dict[key] = value
data["사과"] = "apple"
data["바나나"] = "banana"
data["코코아"] = "cocoa"

print(data)
print(data["사과"])

# 사전 내부에 키값에 해당하는 데이터가 있는지 검색
if "사과" in data:
    print(f"내부에 키값 사과가 존재하며 그 값은 {data['사과']}이다")

# dict의 key값 가져오기
keys = data.keys()
print(keys)

# dict의 value 가져오기
values= data.values()
print(values)

for key in keys:
    print(f"data[{key}] = {data[key]}", end = "     ")

