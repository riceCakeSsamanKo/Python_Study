# 백트래킹을 이용한 풀이
# 시간이 오래 걸려서 백준에서 실패 뜬다. 하지만 이런식으로도 풀이가 가능
import sys

input = sys.stdin.readline

n, max_weight = map(int, input().split())

w = []
v = []

for _ in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

result = 0


def recur(idx, w, v, weight, value):
    global result
    if idx == n:
        result = max(result, value)
        return

    if weight + w[idx] <= max_weight:
        # 해당 물품을 가방에 집어 넣은 경우
        recur(idx + 1, w, v, weight + w[idx], value + v[idx])
        # 해당 물품을 가방에 집어 넣지 않은 경우
        recur(idx + 1, w, v, weight, value)
    else:
        # 해당 물건을 집어 넣은 경우 무게가 최대 한도를 넘어가므로 해당 물건은 가방에 집어넣지 않는다.
        recur(idx + 1, w, v, weight, value)


recur(0, w, v, 0, 0)
print(result)
