import sys

input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))

result = 0
for i in range(n):
    while graph[i] > 0:
        if i < n - 2:
            if graph[i + 1] > 0 and graph[i + 2] > 0:
                min_value = min(graph[i], graph[i + 1])
                min_value = min(min_value, graph[i + 2])
                graph[i] -= min_value
                graph[i + 1] -= min_value
                graph[i + 2] -= min_value
                result += 7 * min_value
                continue
        if i < n - 1:
            if graph[i + 1] > 0:
                min_value = min(graph[i], graph[i + 1])
                graph[i] -= min_value
                graph[i + 1] -= min_value
                result += 5 * min_value
                continue

        result += 3 * graph[i]
        graph[i] = 0


print(result)