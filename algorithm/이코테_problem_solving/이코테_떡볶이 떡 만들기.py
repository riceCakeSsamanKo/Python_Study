# 떡볶이 떡 만들기
# 난이도 1.5
# 시간제한 2초
# 메모리 제한 128MB


## 1)정렬을 이용한 풀이 (코드가 좀 ㅈ같음)
import sys

def sliced_length(r,h):
    if r > h:
        return r-h
    else:
        return 0

def find_height(array,m):
    result = array[0]+1
    sum = 0

    while sum<m:
        result-=1
        sum=0
        for i in array:
            each_sliced_length = sliced_length(i,result)
            if each_sliced_length == 0:
                break
            sum+=each_sliced_length
            if sum>=m:
                return result

        if result <= 0:
            return 0

    return result


n,m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))
array.sort(reverse=True) #O(nlogn)

print(find_height(array,m))

### 2)이진 탐색을 이용한 풀이
import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))


# 이진 탐색 수행
start = 0
end = max(array)

result = 0
while True:
    total=0
    mid = (start+end)//2

    for x in array:
        if x > mid:
            total+=x-mid

    # 잘린 떡 길이가 작은 경우 더 많이 자르기
    if total < m:
        end = mid-1
    # 잘린 떡 길이가 충분히 큰 경우 덜 자르기
    elif total > m:
        start = mid+1
    else:
        result = mid
        break

print(result)
