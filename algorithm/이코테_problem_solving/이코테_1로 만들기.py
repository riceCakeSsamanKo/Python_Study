# 1로 만들기
# 난이도 1.5
# 시간제한 1초
# 메모리 제한 128MB

x = int(input())
# dp table
dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    elif i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])