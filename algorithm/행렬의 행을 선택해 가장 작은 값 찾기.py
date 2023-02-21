# 행 선택해 가장 작은 값 찾기
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

def minNumOfArray(array:list):
    min = array[0]
    for value in array:
        if (min > value):
            min = value
    return min

print(f"NxM 크기의 행렬을 생성함.")
print("N,M을 차례로 입력>>>", end=" ")
N,M = map(int,input().split())

#행렬 생성
cards = [[0]*M for _ in range(N)]

#행렬 내부 초기화
print("행렬 내부 값 입력")
for i in range(N):
    print(f"{i+1}번째 행>>>",end = " ")
    cards[i] = list(map(int, input().split()))

#최소 값을 뽑을 행렬 선택
print("최소값을 뽑을 행 선택>>>",end=" ")
minRowIndex:int = int(input())-1
selectedRow = cards[minRowIndex]

#가장 작은 값 선택
result = minNumOfArray(selectedRow)
print(result)