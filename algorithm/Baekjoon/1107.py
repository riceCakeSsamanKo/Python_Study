import sys
read = sys.stdin.readline


channel = int(read()) # 틀고자 하는 채널
difference = channel - 100

m = int(read()) # 0~9 중 못 쓰는 버튼 수
num_size = len(str(channel)) # channel = num_size 자리 숫자
not_used_button = list(map(int,read().split())) # 못 쓰는 버튼
button = [] # 사용 가능한 버튼

# 사용 가능 버튼 입력
for i in range(10):
    if i in not_used_button:
        continue
    else:
        button.append(i)

has_button = [False]*(num_size)
for i in range(num_size):
    number = str(channel)[i]
    if int(number) in button:
        has_button[i] = True  # i번째 자리 숫자 버튼이 존재함
print(has_button)

numbers = []
for i in range(num_size):
    if has_button[i]:
        numbers.append(int(str(channel)[i]))
    else:
        numbers.append(button)

print(numbers)


