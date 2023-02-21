# 여러 개의 수를 한줄로 받는 경우
values = list(map(int, input().split()))
print(values)

# 한번에 여러 변수 값(정수) 받기
n,m,k = map(int, input().split())
print(n,m,k)

# 빠르게 한줄 입력받기
import sys

data = sys.stdin.readline().rstrip()  #import보다 빠름
print(data)

datas = list(map(int, sys.stdin.readline().rstrip().split()))
print(datas)