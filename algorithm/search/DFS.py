# DFS 알고리즘
# 1) 탐색을 시작하고자 하는 정점을 스택에 push.
# 2) 스택의 top에 인접한 정점 중 방문하지 않은 정점이 있다면 인접 정점을 스택에 push하고 방문 처리한다.
# 3) 방문하지 않은 인접노드가 없으면 스택에서 top울 pop한다.
# 4) (2),(3)의 과정을 더 이상 수행할 수 없을때까지 반복한다

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [
    [],
    [2,6],
    [3,4],
    [2,8],
    [2,5],
    [4],
    [1,7,8],
    [6],
    [3,6]
]

visited = [False]*9

dfs(graph,1,visited)