<<<<<<< HEAD
# 일단 피벗을 맨 마지막 원소로 항상 고른다.
def choose_pivot(data, start, end):
    return end

def partition(data, start, end, pivot_pos):
    # 우리의 partition 알고리즘은 피벗이 맨 마지막 원소라고 가정하므로
    # pivot_pos 의 원소와 맨 마지막 원소의 위치를 바꾼다.
    data[end], data[pivot_pos] = data[pivot_pos], data[end]

    pivot = data[end] # 피봇은 마지막 원소로
    current_small_loc = start # 빨간색 지시자

    # i 는 검은색 지시자
    for i in range(start, end + 1):
        if data[i] <= pivot:
            # swap 을 수행
            data[i], data[current_small_loc] = data[current_small_loc], data[i]
            current_small_loc += 1
    return current_small_loc - 1

# start 부터 end 까지 중 k 번째 원소를 찾는다.
def quickselect(data, start, end, k):
    if start == end :
        return data[start]

    # 피벗을 하나 고른다.
    pivot_pos = choose_pivot(data, start, end)

    # 파티션 후 피벗의 위치를 받는다. (파티션 후에 피봇의 위치가 바뀌므로
    # 새로운 피벗 위치를 리턴한다.)
    pivot_pos = partition(data, start, end, pivot_pos)

    if pivot_pos == k: # 빙고!
        return data[pivot_pos]
    elif pivot_pos < k: # 찾고자 하는 원소는 피벗 오른쪽에 있다.
        return quickselect(data, pivot_pos + 1, end, k)
    else: # 찾고자 하는 원소는 피벗 왼쪽에 있다.
        return quickselect(data, start, pivot_pos - 1, k)

n = int(input())
data = []

for cnt in range(n): # 1, 2, .., 10 까지 나올 것입니다.
    i = int(input())
    data.append(i)

    print(quickselect(data, 0, cnt, cnt//2))
=======
# leftHeap은 최대힙으로 구성, rightHeap은 최소힙으로 구성하여 번갈아가면서 pop함.

import sys
import heapq

n = int(sys.stdin.readline())

leftHeap = []  # 최대힙
rightHeap = [] # 최소힙

for i in range(n):
    num = int(sys.stdin.readline())

    # 짝수번 째 수인 경우에는 일단 leftHeap에, 홀수번 수인경우 rightHeap에 넣음
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap,num)

    # -leftHeap[0]은 leftHeap에서의 최댓값
    # rightHeap[0]은 rightHeap에서의 최솟값

    # rightHeap에 값이 존재하고 leftHeap의 최댓값이 rightHeap의 최솟값보다 큰 경우
    # rightHeap[0]가 중간 값
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap) # leftHeap[0] pop
        rightValue = heapq.heappop(rightHeap) # rightHeap[0] pop

        # 중간값을 leftHeap에 넣어주고, 중간값이 아닌 leftValue는 rightHeap에 넣어준다
        heapq.heappush(leftHeap,-rightValue)
        heapq.heappush(rightHeap,-leftValue)
        # 결과적으로 -leftHeap[0]가 중간값이 된다.

    # 중간값 출력
    print(-leftHeap[0])
>>>>>>> 0857ebdfd0345d45720ae3d6fea3bce4b26ea6eb
