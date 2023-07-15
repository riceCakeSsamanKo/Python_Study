import sys

input = sys.stdin.readline

n = int(input())
data = []
dp = [1] * n

for _ in range(n):
    data.append(int(input()))

lis = 0
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            lis = max(lis,dp[i])

print(len(data) - lis)
