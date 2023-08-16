import sys

input = sys.stdin.readline


def recur(idx):
    global answer

    if idx == n:
        return 0
    if idx > n:
        return -999999999

    if dp[idx] != -1:
        return dp[idx]

    # 상담을 받거나, 안받거나, 그 중에서 더 많은 돈을 버는 경우를 내 DP 테이블에 저장하겠다!
    dp[idx] = max(recur(idx + graph[idx][0]) + graph[idx][1], recur(idx + 1))

    return dp[idx]

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [-1 for _ in range(n + 1)]

recur(0)
print(dp[0])
