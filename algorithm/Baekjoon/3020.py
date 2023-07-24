import sys

input = sys.stdin.readline
n, h = map(int, input().split())

graph = [0] * (h + 2)
for i in range(n):
    l = int(input())
    if i % 2 == 0:
        graph[1] += 1
        graph[l + 1] -= 1
    else:
        graph[h - l + 1] += 1
        graph[h + 1] -= 1
# print(graph)

num = 0
min_value = graph[1]
prefix = [0] * (h + 1)
for i in range(1, h + 1):
    prefix[i] = prefix[i - 1] + graph[i]
    if prefix[i] < min_value:
        num = 1
        min_value = prefix[i]
    elif prefix[i] == min_value:
        num += 1
# print(prefix)
print(min_value,num)
