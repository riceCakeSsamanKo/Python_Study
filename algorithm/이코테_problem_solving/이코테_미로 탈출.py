# 미로 탈출
# 난이도 1.5
# 시간제한 1초
# 메모리 제한 128MB

### <내 풀이> ###
from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]

n,m = list(map(int,input().split()))
graph = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(graph,x,y,visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            #방문하지 않을 조건
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny]==True:
                continue

            #방문하는 경우
            queue.append((nx,ny))
            visited[nx][ny] = True
            graph[nx][ny]=graph[x][y]+1

bfs(graph,0,0,visited)
print(graph[n-1][m-1])

### <답> ###

#시계방향 탐색
dx = [-1,0,1,0]
dy = [0,-1,0,1]

#search
def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: #처음 방문한 경우
                queue.append((nx,ny))
                graph[nx][ny] += graph[x][y]

#미로 사이즈 입력
n,m = list(map(int,input().split()))
graph = []


#미로 내용 입력 (1:통과 가능, 0:통과 불가능)
for _ in range(n):
    graph.append(list(map(int,input())))

bfs(graph,0,0)
print(graph[n-1][m-1])


