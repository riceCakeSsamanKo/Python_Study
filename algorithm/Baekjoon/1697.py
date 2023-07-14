from collections import deque

def bfs(start, dest):
    q = deque([start])
    next_list = deque([])
    result = 0

    while True:
        cur = q.popleft()
        if cur == dest:
            return result

        for next in graph[cur]:
            if 0 <= next <= 100000:
                if not visited[next]:
                    visited[next] = True
                    next_list.append(next)
        if not q:  # q가 비었다면 q에 next_list를 대입
            result += 1 # depth 1 증가
            q = next_list
            next_list = deque([])  # next_list 초기화

n, k = list(map(int, input().split()))
visited = [False] * (100001)

graph = []
for i in range(100001):
    graph.append((i - 1, i + 1, 2 * i))

print(bfs(n, k))
