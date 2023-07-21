n = int(input())
graph = list(map(int, input().split()))


def gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

graph.sort()

cnt = 0
for i in range(n - 1):
    if gcd(graph[i], graph[i + 1]) == 1:
        continue
    else:
        for j in range(graph[i]+1, graph[i+1]):
            if gcd(graph[i], j) == 1 and gcd(graph[i + 1], j) == 1:
                cnt += 1
                break
            if j == graph[i+1]-1:
                cnt+=2
                break
print(cnt)