# 선택 정렬 알고리즘
# 1) i번 부터 마지막 인덱스 까지중 가장 작은 값을 찾는다
# 2) 가장 작은 값과 array[i]를 swap한다
# 3) i가 마지막 인덱스가 될때까지 반복한다

def selectionSort(array):
    for i in range(len(array)):
        minIndex = i

        for j in range(i+1,len(array)):
            if array[minIndex]>array[j]:
                minIndex = j
        #swap
        array[i],array[minIndex] = array[minIndex],array[i]

array = [0,4,2,7,1,3,9,12,27]
selectionSort(array)
print(array)