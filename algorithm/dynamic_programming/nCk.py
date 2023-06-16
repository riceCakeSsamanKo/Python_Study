n, k = map(int, input("n,k>>>").split())
dp = [[0] * (k + 1) for k in range(n + 1)]

for i in range(n+1):
    #nC0, nCn == 1
    dp[i][0],dp[i][i] = 1, 1

def showArray(array):
    for line in array:
        print(line)
    print()

def make_dp_table():

    global dp
    global n

    for i in range(2,n+1):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

def bin(n,k):
    if n<=0 or k<=0 or n<k:
        return False
    else:
        return dp[n][k]


make_dp_table()
# showArray(dp)
print(bin(n,k))