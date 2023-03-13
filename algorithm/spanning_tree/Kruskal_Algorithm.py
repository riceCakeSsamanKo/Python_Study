# - 신장 트리(Spanning Tree): 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# - 최소 신장 트리 알고리즘: 모든 노드들을 연결할 때 각 간선당 가중치가 부여되어 있을 때, 최소한의 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘

# 크루스칼 알고리즘
# 1)간선 데이터를 비용에 따라 오름차순으로 정렬.
# 2)비용이 작은 간선부터 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# 2-1)사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다. (두 노드의 조상(= 루트)이 동일한 경우)
# 2-2)사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다. (두 노드의 조상이 다른 경우)
# 3) 모든 간선에 대해 (2)를 반복한다.

# 최소 신장트리의 간선의 개수는 노드개수 - 1이다.
# 시간 복잡도: O(간선 개수)

# 특정 원소가 속한 집합 찾기(루트 찾기)
def find_parent(parent, x):  # O(v)
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 집합 합치기
def union_parent(parent, a, b):  # O(v)
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드와 간선의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):  # O(v)
    parent[i] = i  # 초기에는 자기 자신으로 부모를 초기화

# 모든 간선의 비용을 담는 edge, 최종 비용을 담을 result
edges = []
result = 0

# 모든 간선의 정보 입력받기
for i in range(e):  # O(e)
    # 양방향 그래프에서 노드 a에서 노드 b로 가는 비용은 cost
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# cost에 대한 오름차순 정렬
edges.sort()  # O(elog e)

for edge in edges:  # O(e)
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
