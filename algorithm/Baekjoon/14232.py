import math

k = int(input())
r = math.ceil(math.sqrt(k))

divisor = []

# 1을 제외한 약수 구하기
for i in range(2, r + 1):
    if k % i == 0:
        divisor.append(i)
        if i != k // i:
            divisor.append(k // i)
divisor.append(k)
divisor.sort()
# print(divisor)

cnt = 0
result = []
while k > 1:
    for i in divisor:
        if k % i == 0:
            cnt += 1
            result.append(i)
            k //= i
            break

print(cnt)
for i in result:
    print(i, end=" ")
