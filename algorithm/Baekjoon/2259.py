import math
import sys
input = sys.stdin.readline

# n: 두더지 마릿수, s: 1초에 이동할 수 있는 최대 거리
n, s = map(int, input().split())

graph = [[0, 0, 0]]  # graph[i]: i번 두더지의 (x,y)좌표, 두더지 출몰 시간 t => [x,y,t]
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(1, n + 1):
    cur_x, cur_y, cur_t = graph[i - 1]
    x, y, t = graph[i]

    # 현재 위치부터 다음 두더지 등장 위치까지의 거리
    dis = math.sqrt((x-cur_x)**2 + (y-cur_y)**2)
    # 현재 위치에서 다음 두더지 등장 위치까지 이동시 걸리는 시간
    move_t = dis / s

    if cur_t + move_t > t:
        graph[i] = graph[i-1]
    else:
        result+=1

print(result)