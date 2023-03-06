# 바닥 공사
# 난이도 2
# 시간제한 1초
# 메모리 제한 128MB

n = int(input())

dp = [0] * 1001

# 초기 설정
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

print(dp[n])
