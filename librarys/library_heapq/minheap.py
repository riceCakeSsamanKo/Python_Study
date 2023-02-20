import heapq

minHeap = []
array = [3,4,1,18,5,6,2,34]

#최소힙 만들기
for value in array:
    heapq.heappush(minHeap,value)  #minHeap은 최소힙으로 원소가 삽입된 리스트

print(minHeap)

#최소힙에서 루트를 pop해서 다른 리스트에 담아 정렬하기
sortByMeanHeap = []
for _ in range(len(minHeap)):
    root = heapq.heappop(minHeap) # 최소 힙을 루트부터 pop한 뒤 다시 재정렬
    sortByMeanHeap.append(root)

print(sortByMeanHeap) #정렬됨



