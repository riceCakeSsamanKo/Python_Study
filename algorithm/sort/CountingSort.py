# 계수정렬
# 기존 정렬법처럼 직접 데이터 값을 비교한 뒤에 위치를 변경하며 정렬하는 방식이 아니다.
# 데이터의 크기가 제한되어 있을 때에 한해서 데이터의 개수가 매우 많더락도 빠르게 동작한다.
# 1) 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있는 리스트를 생성한다.
# 2) 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.
# 3) 마지막 데이터까지 (2)의 과정을 반복한다.

array = [7,7,2,2,4,3,9,11,0,2,8,3,15]
count = [0]*(max(array)+1)

def countingSort(array):
    for i in array:
        count[i]+=1

countingSort(array)

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=" ")
