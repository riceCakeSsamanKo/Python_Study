# tn = t0tn-1 + t1tn-2 + ... + tn-1t0
# t0 = 1


def binary_tree(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1,n+1):  # i는 j의 최대 상한
        for j in range(i):  # j == 최대 i-1
            dp[i] += dp[j]*dp[i-j-1]

    return dp[n]
# n=4 14((0,3)(1,2)(2,1)(3,0))
# n=3 5 ((0,2)(1,1)(2,0))
# n=2 2 ((0,1)(1,0))
# n=1 1 (0,0)

