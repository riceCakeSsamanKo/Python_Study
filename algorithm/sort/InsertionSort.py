# 삽입 정렬 알고리즘
# 거의 정렬되어 있는 상태에서 효율적이다
# 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
# 두번째 데이터부터 정렬을 시작한다.

# 1) i-1번까지의 데이터들 중 i번 데이터보다 작은 값이 최초로 나오는 인덱스를 찾을 때까지
#    i번 데이터를 앞으로 한칸씩 이동한다
# 2) 인덱스를 찾았다면 이동을 멈춘다
# 3) 배열 길이가 n이라 할 때, 총 n-1번 반복한다

array = [5,7,1,8,3,9,0,12]

def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1): # i부터 1까지 1씩 감소
            if array[j]<array[j-1]:
                # (앞의 값이 더 큰 경우) 앞으로 한칸씩 이동
                array[j],array[j-1] = array[j-1],array[j]
            else:
                # 자기보다 작거나 같은 데이터를 만나면 해당 자리에서 멈춤
                break

insertionSort(array)
print(array)
