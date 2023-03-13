# 서로소 집합 알고리즘(경로압축.ver):
# 단순.ver과 find_parent 함수만 차이 존재.
# parent 리스트가 모두 각 원소들이 속하는 집합의 루트로 초기화 되었으므로 합집합 연산시 더 유리하다.

# 1)초기에는 모든 노드가 자기자신을 부모로 갖는다.
# 2)union(합집합) 연산을 진행하며 각 루트 노드끼리를 연결한다. 이때 일반적으로 번호가 작은 노드가 부모가 된다.

# 시간 복잡도: 대략 O(v+e(1+log v))

# 특정 원소가 속한 집합을 찾기
def find_parent(parents: list, x: int) -> int:  # O(V)
    # 단순.ver과 차이점: 각 원소가 속한 집합의 루트 == 각 원소의 부모
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parents: list, a: int, b: int):  # O(V)
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)  # O(ve)

# 각 원소가 속한 집합 출력
print("<각 원소가 속한 집합(각 원소의 루트)>")
for i in range(1, v + 1):
    print(f"root[{i}]= {find_parent(parent, i)}", end=" ")
print("\n")

# 부모 테이블 내용 출력
print("<부모 테이블>")
for i in range(1, v + 1):
    print(f"parent[{i}]= {parent[i]}", end=" ")
print()
