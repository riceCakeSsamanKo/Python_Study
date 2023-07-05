# (a/b)%p = (a*b^-1)%p = (a%p)*(b^-1)%p = (a%p)*(b^p-2)%p

import sys
input = sys.stdin.readline

def power(a,b): # a^b
    if b == 0:
        return 1
    if b % 2: # 홀수
        return (power(a,b//2)**2*a)%p
    else: # 짝수
        return (power(a,b//2)**2)%p

p = 1000000007

n, k = map(int, input().split())
fact = [1 for i in range(n+1)]

for i in range(2,n+1):
    fact[i] = fact[i-1] * i % p

A = fact[n]
B = (fact[n-k] * fact[k]) % p
result = ((A % p) * (power(B,p-2) % p) % p)

print(result)
