# 퀵정렬 알고리즘
# 1) 리스트에서 첫번째 데이터를 피벗으로 정한다.
# 2) 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 3) 큰 데이터와 작은 데이터를 서로 교환환다.
# 4) 큰 데이터의 인덱스가 작은 데이터의 인덱스보다 커진 경우, 작은 데이터와 피벗의 위치를 서로 변경한다.
# 5) 현재 피벗의 왼쪽 파티션은 피벗보다 작은 데이터가 위치하고, 피벗의 오른쪽에는 피벗보다 큰 데이터가 위치한다.
# 6) 각 파티션들도 (1)~(4)를 수행한다. 각 파티션 내부 데이터 개수가 1인 경우에 종료한다.

array = [5,7,9,0,3,1,6,2,4,8]

def quickSort(array,start,end):
    if start>=end:  # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while start<right and array[right]>=array[pivot] :
            right-=1
        if left>right: # 엇갈렸다면 작은데이터(right)와 pivot을 swap (종료)
            array[right],array[pivot] = array[pivot],array[right]
            pivot = right
        else:# 엇갈리지 않았다면 left와 right를 swap
            array[left],array[right] = array[right],array[left]

    #분할 이후 왼쪽과 오른쪽에 대해서도 quick sort 수행
    quickSort(array,start,pivot-1)
    quickSort(array,pivot+1,end)

quickSort(array,0,len(array)-1)
print(array)