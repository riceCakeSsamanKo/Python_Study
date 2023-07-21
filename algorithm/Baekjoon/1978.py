n = int(input())
numbers = list(map(int, input().split()))

prime_num = [True] * (1000 + 1)
prime_num[0], prime_num[1] = False, False

for i in range(2, 1000 + 1):
    j = 2
    while i * j <= 1000:
        prime_num[i * j] = False
        j += 1

result = 0
for number in numbers:
    if prime_num[number]:
        result += 1
print(result)
