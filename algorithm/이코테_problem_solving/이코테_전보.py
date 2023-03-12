# 전보
# 난이도 3
# 시간제한 1초
# 메모리 제한 128MB

# 시작노드 정하고, 해당노드가 갈 수있는 모든 노드 출력, 가중치 출력
# 다익스트라 구현

import heapq
import sys

input = sys.stdin.readline

# 무한대
INF = int(1e9)
# 도시개수 n, 통로개수 m, 출발노드 c
n, m, c = map(int, input().split())
# graph 간선, 노드 리스트
graph = [[] for i in range(n+1)]  # graph[a] = (b,c) : a에서 b로 가는 거리 c
# 거리 리스트
distance = [INF] * (n + 1)  # distance[b] : 출발점에서 b로 가는 거리

# graph 초기화
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # x에서 y로가는 거리 z


# 다익스트라 알고리즘
def diijkstra(start):
    q = []
    # 자기 자신에게 향하는 거리는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # dist는 start부터 now까지의 거리
        # 이미 처리된 경우 continue
        if distance[now] < dist:
            continue
        # start부터 node까지의 거리 구하기
        for next_node in graph[now]:
            index = next_node[0]
            # start부터 다음 노드까지의 총 길이
            # = min(distance[다음노드], start부터 현재 노드까지의 길이 + 현재 노드부터 다음노드까지의 길이)
            cost = min(distance[index], dist + next_node[1])
            distance[index] = cost
            heapq.heappush(q, (cost, index))  # 최소힙의 경우 맨앞 요소를 기준으로 정렬되므로 cost가 index보다 앞에 들어간다

diijkstra(c)

# 도달할 수 있는 노드 개수
count = -1
# 도달할 수 있는 노드 중 가장 먼 노드 길이
max_distance = 0
for i in range(1, n+1):
    if distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])

print(count,max_distance)