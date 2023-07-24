n = int(input())
graph = list(map(int, input().split()))
prefix = [0] * (n + 1)

max_value = graph[0]
for i in range(n):
    prefix[i + 1] = max(prefix[i] + graph[i], graph[i])
    max_value = max(max_value, prefix[i+1])

print(max_value)
