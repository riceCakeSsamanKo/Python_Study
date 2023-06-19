def dfs(graph, start, visit):
    global result
    visit[start] = True

    for x in graph[start]:
        if visit[x] == False:
            result += 1
            dfs(graph,x,visit)

n = int(input())
m = int(input())
result = 0
visit = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


dfs(graph,1,visit)
print(result)