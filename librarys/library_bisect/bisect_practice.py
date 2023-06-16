from bisect import bisect_left,bisect_right

# bisect_left(): 찾고자 하는 값 중 가장 작은 인덱스 반환(lower_bound)
# bisect_right(): 찾고자 하는 값보다 큰 수중 가장 작은 인덱스 반환(upper_bound)

def numOfRange(iterable,leftValue,rightValue):
    iterable.sort()
    left_index = bisect_left(iterable,leftValue)
    right_index = bisect_right(iterable,rightValue)

    return right_index - left_index

array = [4,2,5,1,5,6,12,3,42,1,8,10]
print(numOfRange(array,3,8))  # 3과 8사이의 수 개수 반환



