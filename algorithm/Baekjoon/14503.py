import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
r, c, d = map(int, input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = True
cnt = 1

while True:
    clean = False

    for i in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            r, c = nx, ny
            cnt += 1
            clean = True
            break

    if not clean:
        r -= dx[d]
        c -= dy[d]
        if graph[r][c] == 1:
            print(cnt)
            break
