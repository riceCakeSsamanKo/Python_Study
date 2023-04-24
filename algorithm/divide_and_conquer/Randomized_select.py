# Randomized Selection 알고리즘.
#
# 1) 배열 A에서 임의의 pivot을 선택.
# 2) pivot을 기준으로 A를 분할. pivot보다 작은 원소는 A_left에, 큰 원소는 A_right에 저장.
# 3) pivot이 A_left에 k-1개 이상 포함되어 있다면, A_left에서 k번째 작은 원소를 찾기 위해 재귀적으로 Randomized Selection 함수를 호출.
# 4) pivot이 A_left에 k-1개 미만으로 포함되어 있다면, A_right에서 (k-|A_left| - 1)번째 작은 원소를 찾기 위해 재귀적으로 Randomized Selection 함수를 호출.

import random

count = 0
def randomized_selection(A, k):
    global count
    count+=1
    """
    배열 A에서 k번째로 큰 원소를 찾는 함수
    """
    n = len(A)
    if n == 1:  # 기저 조건
        return A[0]

    # 임의의 pivot 선택
    pivot = random.choice(A)

    #      A_left  pivot  A_right
    # A = [1...j-1] [j] [j+1...N]
    A_left = [x for x in A if x < pivot]
    A_right = [x for x in A if x > pivot]

    # pivot의 인덱스
    j = len(A_left)+1

    print(f'{count}) 배열: {A}, pivot_idx: {j}, pivot: {pivot}')
    print(f"{A_left} [{pivot}] {A_right}",end=' ')
    if j > k:
        print('>> choose A_left')
        return randomized_selection(A_left, k)
    elif j < k:
        print('>> choose A_right')
        return randomized_selection(A_right, k - j)
    else:
        print('>> find')
        return pivot


a = [5,12,3,6,2,1,7,999,34,21,43,72,12,33]
k = int(input(f"{len(a)}개의 원소중에서 k번째로 큰 수 찾기. k 입력>>>"))
print(randomized_selection(a,k))