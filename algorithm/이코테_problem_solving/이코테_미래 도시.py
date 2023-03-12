# 미래 도시
# 난이도 2
# 시간제한 2초
# 메모리 제한 128MB

# 1번 회사에서 출발하여 k번 회사를 방문하고 x번 회사로 가는 최소거리 구하는 문제
# 1번에서 k번 가는 최소거리 + k번에서 x번 가는 최소거리

# 무한대
INF = int(1e9)

# 회사 개수 n, 간선 개수 m
n, m = map(int, input().split())

# graph[a] = b: a와 b는 양방향 이동이 가능함. 한 간선의 길이는 1로 고정
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 연결된 두 회사 입력
for _ in range(m):
    a, b = map(int, input().split())
    # a와 b는 양방향 통로
    graph[a][b] = 1
    graph[b][a] = 1

# 도착지 x, 경유지 k
x, k = map(int, input().split())


# 플로이드-워셜 알고리즘
def floyd_warshall(start):
    # 자기 자신의 거리는 0
    for i in range(1, n + 1):
        graph[i][i] = 0
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd_warshall(1)
distance = graph[1][k] + graph[k][x]
if distance == INF:
    print("Could not reach")
else:
    print(distance)
