import heapq

#내림차순 정렬 함수
def descendingSort(iterable):
    if(isinstance(iterable,list)==False):
        return -1


    maxHeap = []
    result = []

    for value in iterable:
        heapq.heappush(maxHeap,-value)  #최소힙을 최대힙으로 사용하기 위해서 -를 붙여서 정렬해줌

    for _ in range(len(maxHeap)):
        result.append(-heapq.heappop(maxHeap))  #값을 꺼낼때 -를 다시 붙여 값을 원복 해줌
    return result

array = [4,5,1,3,17,76,-44,28]
print(array)

print(descendingSort(array))

