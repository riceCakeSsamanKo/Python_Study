# 메모이제이션을 이용한 피보나치(속도업)
def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


n = int(input())
fibo = memoize(fibo)
print(fibo(n))




