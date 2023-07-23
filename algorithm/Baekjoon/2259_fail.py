import math
import sys

input = sys.stdin.readline

# n: 두더지 마릿수, s: 1초에 이동할 수 있는 최대 거리
n, s = map(int, input().split())

# dp[t]: 시간 t에 내가 존재할 수 있는 장소들
dp = [[] for _ in range(6667)]
dp[0] = [(0, 0, 0)]

graph = {0: [(0, 0)]}  # graph[i]: i번 두더지의 (x,y)좌표, 두더지 출몰 시간 t => [x,y,t]

for _ in range(n):
    x, y, t = list(map(int, input().split()))
    if t in graph:
        graph[t].append((x, y))
    else:
        graph[t] = [(x, y)]

times = list(graph.keys())
times.sort()

bef_t = 0
idx = 0
result = 0
for cur_t in times[1:]:
    flag = False  # bef_pos에서 cur_pos로 이동 가능한 케이스가 있는 경우 true
    cur_pos = graph[cur_t]
    bef_pos = dp[idx]

    for x, y in cur_pos:
        for bef_x, bef_y, bef_t in bef_pos:
            dis = math.sqrt((x - bef_x) ** 2 + (y - bef_y) ** 2)
            move_t = dis / s

            if cur_t - bef_t < move_t:
                continue
            # bef_pos들 중에서 cur_pos중 현재 선택된 위치로 이동이 가능한 경우
            else:
                dp[idx + 1].append((x, y, cur_t))
                flag = True
                break

        # bef_pos에서 cur_pos로 이동 가능한 케이스가 있는 경우
    if flag:
        bef_t = cur_t
        idx += 1
        result += 1

print(result)