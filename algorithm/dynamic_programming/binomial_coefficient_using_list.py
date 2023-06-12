#nCk를 계산하는 메소드(좀 효율적인.ver)
def bin(n,k):
    dp = [[0]*(i+1) for i in range(n+1)]

    # 배열 초기화
    for i in range(n+1):
        dp[i][0] = 1
        dp[i][i] = 1

    for i in range(2,n+1):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    return dp[n][k]

print(bin(1000,500))