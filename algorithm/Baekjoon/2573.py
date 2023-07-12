import sys
from collections import deque

def show_array(graph):
    for line in graph:
        print(line)
    print()

input = sys.stdin.readline

graph = []
n, m = list(map(int, input().split()))

max_height = 0
for _ in range(n):
    heights = list(map(int, input().split()))
    for height in heights:
        max_height = max(max_height, height)
    graph.append(heights)

print(max_height)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, visited, adjacent_sea_water):
    if graph[x][y] == 0:
        visited[x][y] = True
        return False

    queue = deque()
    queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 >= nx or nx >= n-1 or 0 >= ny or ny >= m-1:
                continue
            else:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
    return True

result = 0
for year in range(max_height):
    show_array(graph)
    visited = [[False] * m for _ in range(n)]
    adjacent_sea_water = [[0] * m for _ in range(n)]

    partition = 0  # 빙산 덩어리 개수
    for i in range(n):
        for j in range(m):
            if bfs(i, j, visited, adjacent_sea_water):
                partition += 1
    if partition > 1:
        result = year
        break

    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j] == 0:
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]

    print(f"year:{year}")
    print("<graph>")
    show_array(graph)
    print("<adjacent_sea_water>")
    show_array(adjacent_sea_water)
    print()


    for i in range(n):
        for j in range(m):
            if graph[i][j] - adjacent_sea_water[i][j] >= 0:
                graph[i][j] -= adjacent_sea_water[i][j]
            else:
                graph[i][j] = 0

print(result)
