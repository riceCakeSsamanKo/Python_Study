count = 0

def bin(n,k):
    global count
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n+1):  # i <= n 대응
        for j in range(k+1): # j <= k 대응
            if i < j or j < 0:  # 여기선 사실 k < 0인 경우는 존재하지 않지만, 조건상 표시
                break

            count+=1 # 총 계산횟수
            if j==0 or i == j:  #nC0 = 1, nCn = 1
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
    return dp[n][k]

print(bin(20,14))
print(count)  # 재귀 이용시 count = 77518. ㅋㅋㅋ