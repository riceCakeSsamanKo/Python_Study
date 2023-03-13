# 위상 정렬 알고리즘
# 방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열하는 것"
# 진입차수: 특정한 노드로 들어오는 간선의 개수

# 1) 진입차수가 0인 노드를 큐에 넣는다.
# 2) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 제거한다.
# 3) 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.
# 4) 큐가 빌 때까지 (2), (3)을 반복한다.

# 시간복잡도: O(v+e)

from collections import deque

# 노드의 개수와 간선 개수 입력받기
v, e = map(int,input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0]*(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 연결된 간선 정보 입력 받기
for _ in range(e):
    a, b = map(int,input().split())
    # a에서 b로 이동 가능(역은 불가)
    graph[a].append(b)
    indegree[b] += 1  # b의 진입 차수 1증가

# 위상 정렬 함수
def topology_sort():
    # 정렬 결과를 담는 result 리스트
    result = []
    # 진입 차수가 0인 노드들이 q에 담긴다
    q = deque()

    # 진입 차수가 0인 노드들이 큐에 담김
    for i in range(1,v+1):  # O(v)
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 수행
    while q:
        # 출발 노드 now
        now = q.popleft()
        result.append(now)

        # now와 연결된 노드들의 진입 차수 1빼기 (now를 큐에서 제거하므로)
        for dest in graph[now]:
            indegree[dest] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[dest] == 0:
                q.append(dest)

    # 정렬 결과 출력
    for i in range(len(result)):
        if i != len(result) -1:
            print(result[i], end=" -> ")
        else:
            print(result[i])

topology_sort()