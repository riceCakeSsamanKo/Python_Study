# 개미 전사
# 난이도 2
# 시간제한 1초
# 메모리 제한 128MB

n = int(input())
array = list(map(int, input().split()))
dp = [0] * n

# 초기 설정 dp[i]는 i번째 창고까지 가장 많이 털 수 있는 식량 개수
dp[0] = array[0]
dp[1] = max(array[0], array[1])

# 바텀업 다이내믹 프로그래밍
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])


print(dp[n-1])