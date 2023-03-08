# Priority Queue는 우선순위가 가장 높은 데이터가 가장 먼저 추출된다. 우선순위 큐는 내부적으로는 최소힙(파이썬 기준)을 사용한다.
# Priority와 heapq 라이브러리 모두 우선순위 큐 기능을 제공하지만 일반적으로는 heapq가 더 빠르므로 heapq를 사용한다.

import heapq

heap = []
array = [(14,'a',1), (3,'b',2), (8,'c',3), (1,'d',4), (5,'e',5)]


for e in array:
    heapq.heappush(heap,e)  # e[0]을 기준으로 최소힙으로 정렬됨 == 첫번재 원소가 우선순위의 기준이 된다

sorted_by_priority_queue = []
for i in range(len(heap)):
    e = heapq.heappop(heap)
    sorted_by_priority_queue.append(e)

print(sorted_by_priority_queue)
