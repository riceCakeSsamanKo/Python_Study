# 미완
import sys

input = sys.stdin.readline

n = int(input())
graph = [0]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [0 for _ in range(n + 2)]

for idx in range(n, 0, -1):
    if idx + graph[idx][0] > n+1:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[idx + graph[idx][0]] + graph[idx][1], dp[idx + 1])

print(dp[1])