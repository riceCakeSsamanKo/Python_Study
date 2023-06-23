# 물건 수, 배낭에 담을 수 있는 최대 무게
import sys
input = sys.stdin.readline
n, max_weight = map(int, input().split())

# 무게, 가치
w , v = [0], [0]

# dp[a][b] == 최대로 담을 수 있는 무게가 a 일때 물건을 b번 째까지 탐색했을 때 최대 가치
dp = [[0]*(max_weight+1) for _ in range(n + 1)]

for i in range(n):
    weight, value = map(int,input().split())
    w.append(weight)
    v.append(value)

for i in range(1,n+1):
    for mw in range(1, max_weight+1):
        if mw - w[i] >= 0:
            dp[i][mw] = max(v[i]+dp[i-1][mw - w[i]], dp[i-1][mw])
        else:
            dp[i][mw] = dp[i-1][mw]

print(dp[n][max_weight])