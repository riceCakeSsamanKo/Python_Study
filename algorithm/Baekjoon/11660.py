# 누적합 풀이
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    data = list(map(int, input().split()))
    for j in range(n):
        graph[i][j+1] = data[j]


prefix = [[0] * (n+1) for _ in range(n+1)]
prefix[1][1] = graph[1][1]

for i in range(2, n+1):
    prefix[1][i] = prefix[1][i - 1] + graph[1][i]
    prefix[i][1] = prefix[i - 1][1] + graph[i][1]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix[i][j] = \
            prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + graph[i][j]

for _ in range(m):
    sum = 0
    x1,y1,x2,y2 = map(int,input().split())
    sum = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(sum)