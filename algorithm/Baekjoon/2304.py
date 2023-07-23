# 누적합 (왼쪽/가장 높은 기둥/오른쪽)
n = int(input())
graph = [0] * (1001)

max_value = 0
max_x = 0
for i in range(n):
    x, height = map(int, input().split())
    graph[x] = height

    if max_value < height:
        max_x = x
        max_value = height

# 가장 높은 텐트 높이 계산
result = graph[max_x]

# 좌측 텐트 높이 계산

for i in range(1, max_x):
    if graph[i - 1] > graph[i]:
        graph[i] = graph[i - 1]
    result += graph[i]

# 우측 텐트 높이 계산
result += graph[1000]
for i in range(999, max_x, -1):
    if graph[i + 1] > graph[i]:
        graph[i] = graph[i + 1]
    result += graph[i]

print(result)
