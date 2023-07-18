tc = int(input())

for _ in range(tc):
    n = int(input())
    for i in range(2, 1000001):
        if n % i == 0:
            print("NO")
            break
        if i == 1000000:
            print("YES")
