# BFS 알고리즘
# 1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
# 2) 큐에서 노드를 꺼내 해당 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다
# 3) (2)를 더 이상 수행할 수 없을 때까지 반복한다.

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    #큐가 빌 때까지 반복함
    while queue:
        
        #정점 하나 뽑음
        v = queue.popleft()
        #뽑은 정점과 인접하고 방문하지 않은 정점을 모두 큐에 넣어줌
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        print(v, end=" ")


n, start = list(map(int,input().split()))
graph = [[]]
visited = [False]*(n+1)

for _ in range(n):
    graph.append(list(map(int,input().split())))

BFS(graph,start,visited)
