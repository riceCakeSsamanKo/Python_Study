from collections import deque

# 정사각형 graph 한 줄 크기
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def show_graph(graph):
    for line in graph:
        print(line)

def bfs(graph:list,start_x,start_y):
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 0
    cnt = 1

    while queue:
        cur = queue.popleft()
        x = cur[0]
        y = cur[1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny]==0:
                continue
            cnt+=1
            queue.append((nx,ny))
            graph[nx][ny] = 0
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph,i,j))

result.sort()
print(len(result))
for x in result:
    print(x)
