import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(graph, x, y):
    if visited[x][y]:
        return 0
    queue = deque([(x,y)])

    while queue:




for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input())
        graph[x][y] = 1
