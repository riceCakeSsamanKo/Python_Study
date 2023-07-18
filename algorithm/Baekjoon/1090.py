# import itertools
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# x_list = []
# y_list = []
#
# n = int(input())
# numbers = [i for i in range(n)]
#
# for i in range(n):
#     x,y = map(int,input().split())
#     # i번 체커의 좌표 == (x_list[i],y_list[i])
#     x_list.append(x)
#     y_list.append(y)
#
#
# # x_list: k개의 x 좌표가 들어있는 리스트(외부의 x_list와 다름)
# def calculate_the_least_cost(x_list, y_list):
#     x_list.sort()
#     y_list.sort()
#
#     # x,y 중간값(k개의 x, y 좌표들 중 x좌표 중간값, y좌표 중간값)
#     x = x_list[len(x_list)//2]
#     y = y_list[len(y_list)//2]
#
#     cost = 0
#     for i in range(len(x_list)):
#         cost += (abs(x-x_list[i])+abs(y-y_list[i]))
#     return cost
#
# for k in range(1,n+1):
#     indexes = list(itertools.combinations(numbers,k)) # 조합 배열의 경우의수가 너무 많음
#     cost = 10_000_000_000
#
#     for index in indexes:
#         temp_x = []
#         temp_y = []
#         for i in index:
#             temp_x.append(x_list[i])
#             temp_y.append(y_list[i])
#         cost = min(cost,calculate_the_least_cost(temp_x, temp_y))
#
#     print(cost)
import heapq


import sys

input = sys.stdin.readline

x_list = []
y_list = []

n = int(input())
numbers = [i for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    # i번 체커의 좌표 == (x_list[i],y_list[i])
    x_list.append(x)
    y_list.append(y)

# x, y 좌표의 조합으로 만들 수 있는 모든 (x,y)의 경우의 수
index_list = []
for i in range(n):
    for j in range(n):
        index_list.append([x_list[i], y_list[j]])
cost_list = [[] for _ in range(n**2)]

for i in range(n**2):
    x = index_list[i][0]
    y = index_list[i][1]
    for j in range(n):
        cost = abs(x - x_list[j]) + abs(y - y_list[j])
        cost_list[i].append(cost)
    cost_list[i].sort()

for k in range(1, n+1):
    result = 10000000000
    for costs in cost_list:
        cost = 0
        for i in range(k): # 뽑는 원소 개수 k
            cost += costs[i]
        result = min(result,cost)
    print(result)

