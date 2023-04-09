count = 0

def fibo(n):
    global count
    memo = [0]*(n+1)
    memo[0] = 0
    memo[1] = 1
    count+=3

    for i in range(2,n+1):
        memo[i] = memo[i-1]+memo[i-2]
        count+=1

    count+=1
    return memo[n]

print(fibo(100))  #O(n)
print(f"count={count}")
