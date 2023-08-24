import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = i+dp[i-1]

print(dp)

answer = 0
