# dict와 마찬가지로 인덱싱 불가. 검색 및 수정에 O(1)의 시간 복잡도를 갖는다

# set 초기화 1
data = set({1,2,3,4})
print(data)

# set 초기화 2
data = {1,2,3,4,5,6}
print(data)

# set에 원소 하나 추가
data.add(7)
print("set에 원소 하나 추가: ",data)

# set 데이터 삭제
data.remove(1)
print("set 데이터 삭제: ",data)

# set에 원소 여러개 추가
data.update({8,9,10})
print("set에 원소 여러개 추가: ",data)

a = {1,2,3,4}
b = {3,4,5,6}

#합집합
print("합집합: ",a|b)

#차집합
print("차집합: ",a-b)

#교집합
print("교집합: ",a&b)

