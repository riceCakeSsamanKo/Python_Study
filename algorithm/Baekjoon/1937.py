import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# def show(graph):
#     for line in graph:
#         print(line)
#     print()

# dp와 dfs 사용
# 이차원 dp 테이블 만들고 각 그래프 칸을 dfs로 탐색해서 최대 값을 dp에 저장
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 탐색 조건
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


n = int(input())

dp = [[0] * n for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    for j in range(n):
        result = dfs(i, j)
        answer = max(result, answer)

# show(dp)
print(answer)
