# 효율적인 화폐 구성
# 난이도 2
# 시간제한 1초
# 메모리 제한 128MB

# n = 화폐 종류 개수, m = 가치의 합
n, m = map(int, input().split())
coins = [0]*n
dp = [-1]*10001  # i번째 값을 만드는데 필요한 동전의 최소 개수

for i in range(n):
    coins[i] = int(input())
    dp[coins[i]] = 1

coins.sort()

for i in range(m+1):
    before_value = 10000

    for coin in coins:
        before = i - coin
        if before < 0:
            break
        elif dp[before] == -1:  # dp[before]이 -1이라면 해당 값은 만들 수 없다
            continue
        else:
            before_value = min(before_value, dp[before])

    if before_value != 10000:
        dp[i] = before_value+1


print(dp[m])