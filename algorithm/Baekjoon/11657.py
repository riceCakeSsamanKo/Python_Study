import sys
read = sys.stdin.readline

INF = int(1e9)
n, m = map(int, read().split())

d = []

distance = [INF]*(n+1)  # distance[x]: 1번에서 x번 까지의 거리
distance[1] = 0

for _ in range(m):
    a, b, c = map(int, read().split())
    d.append((a,b,c))


cycle = False

for i in range(n):
    for cur in range(1,n+1):
        for next in d[cur]:
            next_idx = next[0]
            l = next[1] # start에서 cur_idx 까지의 거리

            if distance[cur] != INF and distance[next_idx] > distance[cur] + l:
                distance[next_idx] = distance[cur] + l
                if i == n-1:
                    cycle = True

# 0보다 새롭게 갱신된 값이 더 작은 경우 + 향하는 노드가 1번 인 경우
# 계속 작아짐 -> 사이클 내부의 노드들은 모두 출력 안함
if cycle:
        print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])