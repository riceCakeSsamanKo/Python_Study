from collections import deque

n, m = map(int, input("n(정점 개수), m(간선 개수) >>>").split())
visit = [False]*(n+1)
finding_sequence = []
edge = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input("간선(u, v)>>> ").split())

    edge[u].append(v)
    edge[v].append(u)

print(edge)
def BFS(s:int):
    q = deque([s])
    visit[s] = True  # s 방문 처리

    while q:
        u = q.popleft()
        finding_sequence.append(u)

        print(f"u:{u}")
        for v in edge[u]:
            if visit[v] == False:
                q.append(v)
                visit[v] = True

BFS(1)
print(finding_sequence)