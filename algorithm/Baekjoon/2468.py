import sys
sys.setrecursionlimit(10**9)

read = sys.stdin.readline

# def show_array(graph):
#     for line in graph:
#         print(line)
#     print()

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, h)


n = int(input())
graph = []  # graph = nxn 배열
visited = [[False] * n for _ in range(n)]

# 시계 방향(북,동,남,서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가장 고지대의 높이
max_height = 0
for _ in range(n):
    data = list(map(int, read().split()))

    # 최대 높이 구하기
    for value in data:
        max_height = max(max_height, value)

    graph.append(data)

# 물에 잠기지 않는 영역의 최대 개수
max_cnt = 0

# 물에 잠기지 않는 영역 구하기
# 물에 잠기지 않는 영역의 최대 개수를 구하기 위해서 최저 높이(1)부터, 최대 높이(max_height)-1 높이까지 구함
for height in range(0, max_height):
    cnt = 0  # 물의 높이에 따라 물에 잠기지 않는 영역의 높이가 다름(목표: 가장 큰 cnt를 구함)
    visited = [[False] * n for _ in range(n)]  # 영역마다 다시 검사해야 하므로 visited를 초기화

    for x in range(n):
        for y in range(n):
            # 탐색 시작 조건
            if graph[x][y] > height and not visited[x][y]:
                cnt += 1  # 영역 개수 +1
                dfs(x, y, height)  # x,y부터 인접한 노드들을 검사. 방문한 노드는 visited = True 처리

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
