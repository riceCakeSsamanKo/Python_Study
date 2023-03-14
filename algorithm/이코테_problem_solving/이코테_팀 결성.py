# 팀 결성
# 난이도 2
# 시간제한 1초
# 메모리 제한 128MB

# 학생(노드) 수 0번부터 n번까지 n+1개. 연산(연산은 '팀 합치기', '같은 팀 여부확인' 2종류) m개
n, m = map(int, input().split())

# 각 학생이 속한 집합의 루트 리스트 parent[]
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i


# 특정 노드의 루트 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 합집합 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 동일 루트(=부모)를 가지는지 판별
def is_same_parent(parent, a, b) -> bool:
    if find_parent(parent, a) == find_parent(parent, b):
        return True
    else:
        return False


# 팀 합치기(0 a b): a, b를 하나의 팀으로 만듦,
# 같은 팀 여부 확인(1 a b): a, b가 하나의 팀인지를 확인
for _ in range(m):
    cal, a, b = map(int, input().split())
    # cal == 0인 경우, 팀 합치기
    if cal == 0:
        union_parent(parent, a, b)
    elif cal == 1:
        if is_same_parent(parent, a, b):
            print("YES")
        else:
            print("NO")