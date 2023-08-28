import sys
from collections import deque


def show_array(graph):
    for line in graph:
        print(line)
    print()


input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,-1,0,1]

w, h = map(int, input().split())
graph = [[] for _ in range(h)]
visited = [False * (w + 1) for _ in range(h)]

for i in range(h):
    line = input()
    for j in range(w):
        word = line[j]
        graph[i].append(word)

show_array(graph)

# 시작 인덱스 (x,y)
x, y = 0, 0
# 통로(.) = 0, 벽(#) = 1, 불꽃(*) = 2
for i in range(h):
    for j in range(w):
        if graph[i][j] == ".":
            graph[i][j] = 0
        if graph[i][j] == "#":
            graph[i][j] = 1
        if graph[i][j] == "*":
            graph[i][j] = 2
        if graph[i][j] == "@":
            x, y = i, j


def solution(graph, x, y):
    q = deque([x, y])

    while q:
        x, y = q.popleft()

