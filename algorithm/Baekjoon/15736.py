import math

n = int(input())

cnt = 0
i = 1
while True:
    if i**2 > n:
        break
    cnt+=1
    i+=1

print(cnt)