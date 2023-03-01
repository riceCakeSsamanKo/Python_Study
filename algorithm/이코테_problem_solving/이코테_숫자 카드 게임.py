# 숫자 카드 게임
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

import math

n,m = map(int,input().split())
maxNum=0

for i in range(n):
    array = list(map(int, input().split()))
    minNumInArray = min(array)
    maxNum = max(minNumInArray,maxNum)

print(maxNum)
