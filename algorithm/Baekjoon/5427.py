# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# def show(graph):
#     for line in graph:
#         print(line)
#     print()
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def bfs():
#     while q:
#         x, y, cur = q.popleft()
#         move = False
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                 if cur == "path":
#                     return visited[x][y]
#                 else:
#                     continue
#
#             elif graph[nx][ny] != '#' and graph[nx][ny] != '*':
#                 if cur == "fire":
#                     graph[nx][ny] = '*'
#                 elif cur == "path":
#                     if visited[nx][ny] == 0:
#                         visited[nx][ny] = visited[x][y] + 1
#                         move = True
#                 q.append((nx, ny, cur))
#
#     return "impossible"
#
# t = int(input())
# for _ in range(t):
#     w, h = map(int, input().split())
#     graph = []
#     visited = [[0] * w for _ in range(h)]
#     q = deque([])
#     for i in range(h):
#         graph.append(list(input().strip()))
#         for j in range(w):
#             if graph[i][j] == '@':
#                 visited[i][j] = 1
#                 init_x, init_y = i, j
#             elif graph[i][j] == '*':
#                 q.append((i, j, "fire"))
#     q.append((init_x, init_y, "path"))
#     print(bfs())
#     # show(graph)
#     # show(visited)

# 불
from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != '#' and arr[nx][ny] != '*':
                    arr[nx][ny] = '*'
                    fire.append((nx, ny))


def move():
    isgo = False
    for _ in range(len(start)):
        x, y = start.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and arr[nx][ny] != '#' and arr[nx][ny] != '*':
                    isgo = True
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
            else:
                return visited[x][y]
    if not isgo:
        return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    arr = []
    fire = deque()
    start = deque()
    for i in range(N):
        arr.append(list(input().strip()))
        for j in range(M):
            if arr[i][j] == '*':
                fire.append((i, j))
            if arr[i][j] == '@':
                start.append((i, j))
    visited = [[0] * M for _ in range(N)]
    visited[start[0][0]][start[0][1]] = 1

    result = 0
    while True:
        burn()
        result = move()
        if result:
            break

    print(result)