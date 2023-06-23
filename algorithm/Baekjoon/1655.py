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
