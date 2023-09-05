import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def recur(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 < ny < n:
            if graph[x][y] < graph[nx][ny]:
                # 인접 방향으로 이동할 수 있는 경우
                dp[x][y] = max(dp[x][y], recur(nx, ny) + 1)

    return dp[x][y]


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for i in range(n):
    for j in range(n):
        t = recur(i, j)
        result = max(result, t)

print(result)
