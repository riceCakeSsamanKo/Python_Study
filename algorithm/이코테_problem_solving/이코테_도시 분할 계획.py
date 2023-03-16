# 도시 분할 계획
# 난이도 2
# 시간제한 2초
# 메모리 제한 256MB

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

max_edge = 0
result = 0
for i in range(m):
    c,a,b = edges[i]
    # 사이클 여부 확인
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        if c>max_edge:
            result+=max_edge
            max_edge = c
        else:
            result+=c

print(result)