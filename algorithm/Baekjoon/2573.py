# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# graph = []
# n, m = list(map(int, input().split()))
#
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def bfs(x, y):
#     visited[x][y] = True
#     queue = deque([(x, y)])
#
#     while queue:
#         x, y = queue.popleft()
#         sea = 0
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx > n or ny < 0 or nx > m:
#                 continue
#             if graph[nx][ny] == 0:
#                 sea += 1
#             if not visited[nx][ny] and graph[nx][ny] != 0:
#                 queue.append([nx, ny])
#                 visited[nx][ny] = True
#
#         adjacent_sea_num[x][y] = sea
#
#
# result = 0
# for k in range(10):
#     visited = [[False] * m for _ in range(n)]
#     adjacent_sea_num = [[0] * m for _ in range(n)]
#     partition = 0
#
#     for i in range(n):
#         for j in range(m):
#             if not visited[i][j] and graph[i][j] != 0:
#                 bfs(i, j)
#                 partition += 1
#
#     if partition >= 2:
#         result = k
#         break
#
#     for i in range(n):
#         for j in range(m):
#             graph[i][j] = max(0,graph[i][j]-adjacent_sea_num[i][j])
#
# print(result)

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)