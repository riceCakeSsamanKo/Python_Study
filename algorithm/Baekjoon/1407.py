a, b = list(map(int, input().split()))

# b!의 2의 개수 - (a-1)!의 2의 개수
a -= 1

# 1로 나누었을 때의 값을 더해줌
tmp_a = a

for i in range(1, 99):
    # tmp_a += (2^i으로 나눠지는 소인수의 개수) * (2^i - 2^(i-1))
    tmp_a += (a // (2 ** i)) * ((2 ** i) - (2 ** (i - 1)))

# 1로 나누었을 때의 값을 더해줌
tmp_b = b

for i in range(1, 99):
    tmp_b += (b // (2 ** i)) * ((2 ** i) - (2 ** (i - 1)))

print(tmp_b - tmp_a)
