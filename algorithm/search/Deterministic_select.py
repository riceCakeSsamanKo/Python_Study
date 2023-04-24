# Deterministic Select 알고리즘
# 시간 복잡도 O(N)

# 1) 배열 A를 5개 원소의 그룹으로 나눕니다. 마지막 그룹은 5개 미만의 원소를 가질 수 있음.
# 2) 각 그룹에서 중간값(median)을 찾음.
# 3) 중간값들의 중간값(median of medians)을 pivot으로 선택.
# 4) pivot을 기준으로 배열 A를 분할합.
# 5) 분할된 부분 배열 중 k번째로 작은 원소를 찾음.
# 6) 찾은 원소를 반환.
count = 0

def deterministic_selection(A, k):
    """
    배열 A에서 k번째로 작은 원소를 찾는 함수
    """
    global count
    count += 1

    n = len(A)
    if n <= 5:
        return sorted(A)[k - 1]  # 배열이 작으면 정렬해서 k번째 원소 반환

    # 5개 원소씩 그룹으로 나누기
    groups = [A[i:i + 5] for i in range(0, n, 5)]

    # 각 그룹에서 중간값 찾기
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # 중간값들의 중간값 찾기(MoM = Medians of median)
    mom = deterministic_selection(medians, len(medians) // 2 + 1)

    # pivot을 기준으로 배열 A를 분할
    A_left = [x for x in A if x < mom]
    A_right = [x for x in A if x > mom]

    if k <= len(A_left):
        return deterministic_selection(A_left, k)
    elif k > n - len(A_right):
        return deterministic_selection(A_right, k - (n - len(A_right)))
    else:
        return mom

a = [5,12,3,6,2,1,7,999,34,21,43,72,12,33]
k = int(input(f"{len(a)}개의 원소중에서 k번째로 큰 수 찾기. k 입력>>>"))
print(deterministic_selection(a,k))