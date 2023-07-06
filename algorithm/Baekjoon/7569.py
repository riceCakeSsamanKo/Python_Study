import sys
from collections import deque
read = sys.stdin.readline

m, n, h = list(map(int, read().split()))

tomato = [[[0]*(m) for _ in range(n)] for _ in range(h)] #1: 익은 토마토 0: 익지 않은 토마토, -1: 빈 공간
visited = [[[False]*(m) for _ in range(n)] for _ in range(h)]  # False 방문 안함, True 방문
roten_tomato = deque([])  # 익은 토마토의 인덱스

for k in range(h):

    for i in range(n):
        tomatos = list(map(int, read().split()))
        for j in range(m):
            tomato[k][i][j] = tomatos[j]
            if tomatos[j] == 1: # 처음부터 익어 있는 경우
                roten_tomato.append((k,i,j))

dx = [0,-1,0,1,0,0]
dy = [-1,0,1,0,0,0]
dh = [0,0,0,0,-1,1]

def bfs():
    max_value = -1

    while roten_tomato:
        height,x,y = roten_tomato.popleft()  # 익은 토마토 좌표
        visited[height][x][y] = True
        max_value = max(max_value,tomato[height][x][y]-1)

        # 동서남북 토마토 익을 수 있는지 여부 체크
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = height + dh[i]

            # out of index 체크
            if nx<0 or nx>=n or ny<0 or ny>=m or nh<0 or nh>=h :
                continue

            # 방문 여부 체크
            if visited[nh][nx][ny]:
                continue
            visited[nh][nx][ny] = True # 방문 안 했다면 방문으로 변경

            # 주위에 익지 않은 토마토가 있는 경우
            if tomato[nh][nx][ny] == 0:
                tomato[nh][nx][ny] = tomato[height][x][y] + 1 # 탐색 횟수
                roten_tomato.append((nh,nx,ny))
    return max_value

def solution():

    result = bfs()

    # 첨부터 모두 익은 경우: visited의 요소가 모두 True && tomato의 요소의 값 중 0이 없는 경우 => return 0 == (tomato의 최댓값(= 1) - 1)
    # 토마토가 모두 익는 최소 일수: visited의 모든 요소가 True=> return (tomato의 최대 값 - 1)
    # 토마토가 모두 익지는 못하는 경우: visited == False이면서 tomato의 요소 중 0이 존재하는 경우  => return -1 ??? 이게 문제?


    for k in range(h):
        for i in range(n):
            for j in range(m):
                if not visited[k][i][j] and tomato[k][i][j] == 0:
                    return -1

    return result

print(solution())