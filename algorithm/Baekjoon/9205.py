import sys

read = sys.stdin.readline

def dfs(start:int, dest:int):
    cur_x, cur_y = graph[start]
    visited[start] = True
    dest_x, dest_y = graph[dest]

    distance = abs(dest_x - cur_x) + abs(dest_y - cur_y)

    global flag
    if distance <= 1000:
        flag = True

    for i in range(1, n + 1):
        next_x, next_y = graph[i]
        distance = abs(next_x - cur_x) + abs(next_y - cur_y)
        if not visited[i] and distance <= 1000:
            dfs(i,dest)

t = int(read())

for _ in range(t):
    n = int(read())

    # graph[0]: 출발지, graph[1:n+1]: 경유지 ,graph[n+1]:목적지
    graph = []
    visited = [False] * (n+2)

    for _ in range(n+2):
        x, y = map(int, read().split())
        # graph[0]: 출발지, graph[1:n+1]: 경유지, graph[n+1]: 목적지
        graph.append((x, y))

    flag = False
    dfs(0,n+1)

    if flag:
        print("happy")
    else:
        print("sad")