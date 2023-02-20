a=[1,4,3]

# 리스트에 원소 삽입
a.append(2)
print(f"삽입:{a}\n")

# 정렬
a.sort()
print(f"정렬:{a}\n")

a.sort(reverse=True)
print(f"내림차순 정렬:{a}\n")

# 원소 뒤집기
a.reverse()
print(f"원소 뒤집기:{a}\n")

# 삽입
a.insert(1,3)
print(f"1번 인덱스에 3 삽입:{a}\n")

# 특정 원소 수 세기
print(f"3의 개수: {a.count(3)}\n")

# 특정 데이터 삭제
a.remove(1)
print(f"값이 3인 데이터 삭제:{a}")
a.remove(3)
print(f"값이 3인 데이터 삭제:{a}\n")

# 리스트에서 특정 데이터를 뺀 리스트 생성
remove_set = {3,5}
b = [1,2,2,3,3,4,4,4,5,5,5,5,5]
print(f"리스트 b: {b}")
result = [i for i in b if i not in remove_set]
print(f"리스트b 에서 특정 데이터{remove_set}를 뺀 리스트 생성{result}")