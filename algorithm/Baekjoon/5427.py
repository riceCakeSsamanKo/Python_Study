import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def show_array(graph):
    for line in graph:
        print(line)
    print()


def bfs():
    cnt = 0

    while q:
        cnt += 1
        x, y = q.popleft()
        # 1) cur == "fire": (x,y)에 불
        # 2) cur == "True": (x,y)에 사람
        # 3) cur == "false": (x,y)는 벽이거나 길
        cur = visited[x][y]

        show_array(visited)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if cur == "fire":
                    if visited[nx][ny] != "fire" and graph[nx][ny] != '#':
                        # 불꽃 이동
                        visited[nx][ny] = "fire"

                if cur == True:
                    if visited[nx][ny] != "fire" and graph[nx][ny] == '.':
                        # 사람 이동
                        visited[nx][ny] = True

                q.append([nx, ny])
            elif cur != "fire":
                return cnt
    return "impossible"


t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    graph = []
    visited = [[False] * w for _ in range(h)]
    q = deque([])

    # 통로(.) = 0, 벽(#) = 1, 불꽃(*) = 2
    for i in range(h):
        graph.append(list(input().strip()))
        for j in range(w):
            if graph[i][j] == '@':
                visited[i][j] = True
                start_x, start_y = i, j
            elif graph[i][j] == '*':
                visited[i][j] = "fire"
                # 불꽃의 초기 위치를 먼저 저장
                q.append([i, j])

    # 시작 초기 위치를 나중 저장
    q.append([start_x, start_y])
    result = bfs()
    print(result)
