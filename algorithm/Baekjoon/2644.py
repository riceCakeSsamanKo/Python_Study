from collections import deque

def bfs(start, target):
    global visited
    global count

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for u in relations[v]:
            if not visited[u]:
                count[u] = count[v] + 1
                queue.append(u)
                visited[u] = True

n = int(input())
p1, p2 = list(map(int,input().split()))
num_of_relations = int(input())

relations = [[] for _ in range(n+1)] # y는 x의 자식

for _ in range(num_of_relations):
    x, y = list(map(int,input().split()))
    relations[x].append(y)
    relations[y].append(x)

visited = [False] * (n + 1)  # 방문 여부
count = [0]*(n+1)

bfs(p1,p2)

if count[p2] == 0:
    print(-1)
else:
    print(count[p2])

