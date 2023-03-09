# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘
# O(N^3)의 시간 복잡도 (중간에 거쳐가는 노드 탐색:N, A에서 B로 가는 거리 탐색:N^2 -> N*N^2 == N^3)
# 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리를 2차원 배열에 담는다

# 1)모든 노드에서 다른 모든 노드로 가는 거리를 모두 구함. (도달할 수 없는 경우 INF(==1e9)로 초기화
# 2)A에서 B로 가는 거리보다 K를 거쳐서 가는 거리가 작다면 K를 거쳐서 가는 거리로 AB 최단 거리를 K를 거쳐가는 거리로 갱신 [Distance(A,B) = min(Distance(A,B), Distance(A,K) + Distance(K,B))]

INF = int(1e9)

# 노드 및 간선 개수 입력
n, m = map(int,input().split())
# 한 노드에서 다른 노드까지의 거리를 담는 2차원 그래프 생성 및 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# graph[a][b] = c: a에서 b까지 가는 최단거리는 c
# 자기 자신까지의 거리는 0으로 초기화(graph[a][a] = 0)
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 개수 만큼 graph 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1,n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("x",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()