import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    sea_list = []  # 인접한 바닷물이 1이상인 경우 (x,y,sea)가 append. sea == 인접 바닷물

    while q:
        x,y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:  # graph[nx][ny] = 바닷물
                    sea += 1
                elif graph[nx][ny] > 0 and not visited[nx][ny]:  # graph[nx][ny] = 빙산
                    q.append((nx, ny))
                    visited[nx][ny] = True
        if sea > 0:
            sea_list.append((x, y, sea))
    for x, y, sea in sea_list:
        if graph[x][y] - sea >= 0:
            graph[x][y] -= sea
        else:
            graph[x][y] = 0
    return 1


n, m = list(map(int, input().split()))

graph = []

for i_ in range(n):
    graph.append(list(map(int, input().split())))

has_ice = [] # 바닷물이 아닌 인덱스
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            has_ice.append((i,j))

result = 0
year = 0
while has_ice:
    visited = [[False]*m for _ in range(n)]
    partition = 0
    del_list = []
    for x,y in has_ice:
        if graph[x][y] != 0 and not visited[x][y]:
            partition += bfs(x,y)  # bfs 1회 실행 시 마다, 탐색된 빙산이 녹으므로 has_ice에 들어있는 인덱스일지라도 검사시엔 0일 수도 있다.
        if graph[x][y] == 0: # 초기엔 빙산이었다가 나중에 녹아 바닷물이 된 인덱스 (graph!=0 -> graph == 0이 된 인덱스ㅓ)
            del_list.append((x,y))
    if partition>=2:
        result = year
        break

    # has_ice에서 현재는 바닷물이 된(값 > 0 -> 값==0) 인덱스 제거
    has_ice = sorted(list(set(has_ice) - set(del_list)))
    year += 1


print(result)
