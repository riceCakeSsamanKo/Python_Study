import sys
read = sys.stdin.readline

INF = 10**9

def show_array(graph):
    for line in graph[1:]:
        for num in line[1:]:
            if num == INF:
                num = "I"
            print(num, end=" ")
        print()

n = int(read()) # 노드 개수
m = int(read()) # 간선 수
# graph[a][b] = c, graph[b][a] = c
# a - b를 잇는 간선 길이의 최소 값 = c
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, read().split())
    if graph[a][b] == 0 or graph[a][b] > c:
        graph[a][b] = c

def floyd(graph):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])



floyd(graph)
show_array(graph)

