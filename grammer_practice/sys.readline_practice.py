### 빠르게 입력받기 ###

import sys
# sys.stdin.readline() 함수는 기존의 input()보다 입력 속도가 빠르다.
# 일반적으로 입력받는 데이터의 개수가 1000만 개를 넘어가는 경우 readline()을 쓰는 것이 좋다.
# input()은 시간 초과가 날 수도 있다.


# 하나의 문자열 데이터 입력받기. rstrip()은 엔터 제거
input_data_int = sys.stdin.readline().rstrip()
input_data_int = list(map(int, input_data_int.split()))  #문자열을 int들로 구성된 list로 바꿈
print(input_data_int)


input_data = sys.stdin.readline().rstrip()
print(input_data)