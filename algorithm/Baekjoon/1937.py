import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def show(graph):
    for line in graph:
        print(line)
    print()


# dp와 dfs 사용
# 이차원 dp 테이블 만들고 각 그래프 칸을 dfs로 탐색해서 최대 값을 dp에 저장

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, cnt):
    global max_value
    max_value = max(cnt, max_value)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 종료 조건
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        # 탐색 조건
        if graph[nx][ny] > graph[x][y]:
            if dp[nx][ny] == -1:
                dfs(nx, ny, cnt + 1)
            else:
                max_value = max(max_value, dp[nx][ny] + cnt + 1)


n = int(input())

dp = [[-1] * n for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0
max_value = 0
for i in range(n):
    for j in range(n):
        max_value = 0
        dfs(i, j, 0)
        dp[i][j] = max_value
    result = max(result, max_value)

show(graph)
show(dp)
print(result + 1)
