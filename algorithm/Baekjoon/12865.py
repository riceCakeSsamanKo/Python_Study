import sys

input = sys.stdin.readline

n, max_weight = map(int, input().split())
w = [0]
v = [0]

for i in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

# dp[i][j] i번째 물건 까지 탐색할 때 현재 담을 수 있는 최대 무게가 j일때 물건들의 최대 가치의 합
dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for cur_weight in range(1, max_weight + 1):
        if cur_weight - w[i] >= 0:
            dp[i][cur_weight] = max(v[i] + dp[i - 1][cur_weight - w[i]], dp[i - 1][cur_weight])
        else:
            dp[i][cur_weight] = dp[i - 1][cur_weight]

print(dp[n][max_weight])
