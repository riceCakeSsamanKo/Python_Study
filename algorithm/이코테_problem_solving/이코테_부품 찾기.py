# 부품 찾기
# 난이도 1.5
# 시간제한 1초
# 메모리 제한 128MB

### 1)이진 탐색을 이용한 풀이
def binarySearch(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)


# 재고
stocks = []
# 문의 부품
orders = []

n = int(input())
stocks = list(map(int, input().split()))
stocks.sort()

m = int(input())
orders = list(map(int, input().split()))

for order in orders:
    stock_index = binarySearch(stocks, order, 0, n - 1)

    if stock_index == -1:
        print("no", end=" ")
    else:
        print("yes", end=" ")

### 2)계수정렬을 이용한 풀이
n = int(input())
stocks = [0] * (1_000_000+1)  # 재고
for i in list(map(int, input().split())):
    stocks[i] += 1

m = int(input())
orders = list(map(int, input().split()))  # 문의 부품

for order in orders:
    if stocks[order] != 0:
        print("yes", end= " ")
    else:
        print("no", end= " ")