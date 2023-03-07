# 다익스트라 알고리즘
# 1)출발 노드를 설정한다.
# 2)최단 거리 테이블을 초기화한다. ( 출발지점=0, 나머지=int(1e9)=INF )
# 3)방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.(선택된 노드는 최단거리가 결정된 노드 == 한 단계당 하나의 최단거리를 확실히 찾는다.)
# 4)해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5)위 과정에서 (3), (4)를 반복한다.

# 출발 노드에서 특정 노드들까지 이동하는데 필요한 거리들(가중치)들을 나타내주는 알고리즘
import sys
input = sys.stdin.readline  # 함수 재정의
INF = int(1e9) # 1 * 10^9 (무한대로 가정)


# n: 노드 개수, m: 간선 개수
n, m = map(int, input().split())
# 출발 노드 설정
start = int(input())
# 노드 정보 리스트  ex)graph[a] = (b,c) -> a노드에서 b노드로 가는 거리는 c
graph = [[] for _ in range(n+1)]
# 방문 체크 그래프
visited = [False]*(n+1)
# 최단 거리 테이블. 초기 거리를 무한대로 설정
distance =[INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))   # ex)graph[a] = (b,c) -> a노드에서 b노드로 가는 거리는 c


# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n):  # 모든 노드를 탐색 해야한다 (simple.ver의 단점)
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def diijkstra_simple(start):
    # 출발 노드 설정
    distance[start] = 0
    visited[start] = True
    # node는 (출발 노드 연결 노드, 거리)
    for node in graph[start]:
        connected_node_index = node[0]
        cost = node[1]
        distance[connected_node_index] = cost  #출발 노드부터 출발노드에 직접 연결된 노드까지의 거리 그래프 초기화
    for i in range(n-1):
        # 최단거리가 가장짧은 노드
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for connected_node in graph[now]:
            connected_node_index = connected_node[0]
            now_to_connected_node_cost = connected_node[1]
            cost = distance[now] + now_to_connected_node_cost
            # 현재 노드를 거쳐서 다른 노드로 이동하는 경우가 더 짧은 경우
            if distance[connected_node_index] > cost:
                distance[connected_node_index] = cost

diijkstra_simple(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print(f"{i}: Could not reach")
    else:
        print(f"{i}: {distance[i]}")
