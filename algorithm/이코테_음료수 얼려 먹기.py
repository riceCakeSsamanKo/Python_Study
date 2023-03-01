# 음료수 얼려 먹기
# 난이도 1.5
# 시간 제한 1초
# 메모리 제한 128MB

### <풀이1 - DFS를 사용한 풀이> ###
n,m = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        #재귀 이용
        dfs(x - 1, y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


count = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count+=1

print(count)


### <풀이 2 - BFS 사용한 풀이> ###
from collections import deque

# 탐색 알고리즘
def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 탐색 불가 조건
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue

            # 탐색 시작(큐에 담고 방문 처리)
            queue.append((nx, ny))
            visited[nx][ny] = True
    return 1

# 아이스크림 개수 반환 함수
def numsOfIceCream(graph, visited):
    result = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                result += bfs(graph, i, j, visited)

    return result
# 그래프 사이즈 입력
n,m = list(map(int,input().split()))

# 시계방향 탐색
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 방문 그래프
visited = [[False]*m for _ in range(n)]

# 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

print(numsOfIceCream(graph,visited))
print(visited)
