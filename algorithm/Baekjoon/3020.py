import sys

input = sys.stdin.readline
n, h = map(int, input().split())

# --- 누적합 풀이 (이모스법) --- #
# graph = [0] * (h + 2)
# for i in range(n):
#     l = int(input())
#     if i % 2 == 0:
#         graph[1] += 1
#         graph[l + 1] -= 1
#     else:
#         graph[h - l + 1] += 1
#         graph[h + 1] -= 1
#
# num = 0
# min_value = graph[1]
# prefix = [0] * (h + 1)
# for i in range(1, h + 1):
#     prefix[i] = prefix[i - 1] + graph[i]
#     if prefix[i] < min_value:
#         num = 1
#         min_value = prefix[i]
#     elif prefix[i] == min_value:
#         num += 1
# print(min_value,num)

# --- 이진 탐색 풀이 --- #
up = []  # 석순
down = []  # 종유석

for i in range(n):
    if i % 2 == 0:
        up.append(int(input()))  # 석순 끝 높이: 석순 높이
    else:
        down.append(int(input()))  # 종유석 시작 높이: h - 종유석 높이

# 이진 탐색을 위한 정렬
up.sort()  # 1 ~ 석순 높이 (석순 높이 내림차순 정렬)
down.sort()  # (h - 종유석 높이) ~ h (종유석 시작 지점 내림차순 정렬)


def binary_search(graph, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if target == graph[mid]:
            return mid
        elif target < graph[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


num = 0
min_value = n

for i in range(1, h+1):
    # 개똥벌래 높이가 i 일때, 부딪히는 석순의 개수
    obstacle_up = n // 2 - binary_search(up, 0, n // 2 - 1, i - 0.5)
    obstacle_down = n // 2 - binary_search(down, 0, n // 2 - 1, h - i + 0.5)
    sum = obstacle_up + obstacle_down

    if min_value > sum:
        min_value = sum
        num = 1
    elif min_value == sum:
        num += 1

print(min_value, num)
