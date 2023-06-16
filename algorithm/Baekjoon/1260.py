from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)


def BFS(iterable: list, start: int):
    n = len(iterable)
    visit = [False]*n
    print(start, end=" ")

    q = deque([start])
    visit[start] = True

    while q:
        u = q.popleft()
        for v in iterable[u]:
            if visit[v] == False:
                q.append(v)
                visit[v] = True
                print(v, end = " ")


# 빠르게 데이터 입력받는 함수
import sys
def input_data():
    return sys.stdin.readline().rstrip().split()

n, m, start = map(int, input_data())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input_data())

    graph[u].append(v)
    graph[v].append(u)

for line in graph:
    line.sort()

visited = [False]*(n+1)
DFS(graph,start,visited)
print()

BFS(graph, start)

