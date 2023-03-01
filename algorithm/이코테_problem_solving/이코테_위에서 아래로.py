# 위에서 아래로
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

n = int(input())
array = []*n

for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)
#array = sorted(array,reverse=True)

for i in array:
    print(i, end=" ")
