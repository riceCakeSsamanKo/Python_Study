import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())


def show(graph):
    for line in graph:
        print(line)
    print()


graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1) 시간 초과 bfs
answer = 0


def bfs(x, y):
    global answer
    q = deque([[x, y]])

    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
                q.append([nx, ny])
                print(f"{cnt}: ({nx},{ny}) {graph[nx][ny]}")
                # 우측 하단 도달
                if nx == m - 1 and ny == n - 1:
                    answer += 1


bfs(0, 0)
print(answer)

# graph = [list(map(int, input().split())) for _ in range(m)]
# dp = [[0] * n for _ in range(m)]
# visited = [[0] * n for _ in range(m)]
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# answer = 0
#
#
# def dfs(x, y):
#     global answer
#     if dp[x][y] != 0:
#
#     dp[x][y] = 1
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
#             if nx == m - 1 and ny == n - 1:
#                 answer += 1
