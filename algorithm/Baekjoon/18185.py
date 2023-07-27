# 사용횟수가 7원 > 5원 > 3원 일수록 유리함.

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(N - 2):
    if A[i + 1] > A[i + 2]:
        m = min(A[i], A[i + 1] - A[i + 2])
        answer += m * 5
        A[i] -= m
        A[i + 1] -= m

    if A[i] > 0 and A[i + 1] > 0 and A[i + 2] > 0:
        m = min(A[i], A[i + 1])
        answer += m * 7
        A[i] -= m
        A[i + 1] -= m
        A[i + 2] -= m

    if A[i] > 0:
        answer += A[i] * 3

if A[-2] > 0 and A[-1] > 0:
    m = min(A[-2], A[-1])
    answer += (m * 5)
    A[-2] -= m
    A[-1] -= m

if A[-2] > 0:
    answer += (A[-2] * 3)
else:
    answer += (A[-1] * 3)

print(answer)