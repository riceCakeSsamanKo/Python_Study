# 서로소 집합을 이용한 사이클 판별 알고리즘

# 만일 두 원소의 부모가 동일한 경우 사이클이 발생한 것. 이를 통해서 사이클을 판별한다.

# 원소가 속한 집합을 찾기
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

# 사이클 발생여부 탐색 후 사이클이 없을 시 union
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent,a) == find_parent(parent, b):
        print("사이클이 발생")
    else:
        union_parent(parent, a, b)

for i in range(1, v+1):
    cycle = False
    for j in range(1, v+1):
        if i == j:
            continue
        if parent[i] == parent[j]:
            print(f"({i},{j}) 사이클이 발생")
            break