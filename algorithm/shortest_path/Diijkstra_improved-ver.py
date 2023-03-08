# 다익스트라 알고리즘(Priority Queue를 이용한 개선.ver)
# 1)출발 노드를 설정한다.
# 2)최단 거리 테이블을 초기화한다. ( 출발지점=0, 나머지=int(1e9)=INF )
# 3)방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.(선택된 노드는 최단거리가 결정된 노드 == 한 단계당 하나의 최단거리를 확실히 찾는다.)
# 4)해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5)위 과정에서 (3), (4)를 반복한다.

# 출발 노드에서 특정 노드들까지 이동하는데 필요한 거리들(가중치)들을 나타내주는 알고리즘
import heapq
import sys

input = sys.stdin.readline  # 함수 재정의
INF = int(1e9)  # 1 * 10^9 (무한대로 가정)

# n: 노드 개수, m: 간선 개수
n, m = map(int, input().split())
# 출발 노드 설정
start = int(input())
# 노드 정보 리스트  ex)graph[a] = (b,c) -> a노드에서 b노드로 가는 거리는 c
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블. 초기 거리를 무한대로 설정
distance = [INF] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # ex)graph[a] = (b,c) -> a노드에서 b노드로 가는 거리는 c


# 개선된 다익스트라. 우선순위 큐를 사용해서 O(ElogV). E는 간선 개수, V는 노드 개수
def diijkstra(start):
    q = []  # 최소 힙
    # 출발 노드 설정
    heapq.heappush(q, (0, start))  # 거리를 최소힙으로 q에 (거리, 노드)를  삽입
    distance[start] = 0
    while q:  # q가 비지 않았다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)  # dist: start부터 now까지의 최단 거리
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (한번 처리된 경우 최단 거리가 된다, 한번 처리된 노드는 더 이상 처리되지 않아 속도가 빠름)
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 다른 노드들 확인
        for node in graph[now]:  # node: now와 직접 연결되고 방문하지 않은 다른 노드
            node_index = node[0]
            cost = dist + node[1]
            if cost < distance[node_index]:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))


diijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print(f"{i}: Could not reach")
    else:
        print(f"{i}: {distance[i]}")
