import sys

input = sys.stdin.readline

n, max_weight = map(int, input().split())

w = []
v = []

for _ in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

answer = 0

def recur(idx, weight):
    global answer

    if weight > max_weight:
        return -9999999

    if idx == n:
        return 0

    if dp[idx][weight] != -1:  # 이미 탐색한 경우
        return dp[idx][weight]

    # 물건을 넣은 경우
    weight_in = recur(idx + 1, weight + w[idx]) + v[idx]

    # 물건을 넣지 않은 경우
    weight_not_in = recur(idx + 1, weight)

    dp[idx][weight] = max(weight_in, weight_not_in)

    return dp[idx][weight]


dp = [[-1 for _ in range(max_weight + 1)] for _ in range(n + 1)]

recur(0, 0)
print(dp[0][0])
