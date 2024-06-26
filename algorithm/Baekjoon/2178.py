from collections import deque

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs():
    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs())