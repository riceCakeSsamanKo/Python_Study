import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken_buttons = []
if m == 0:
    pass
else:
    broken_buttons = list(map(int,input().split()))

result = abs(n-100)
for i in range(1000001):
    #틀 수있는 채널 0~100000
    flag = True # 모든 버튼이 사용 가능한 버튼인 경우 flag = True
    channel =str(i)
    for num in channel:
        if int(num) in broken_buttons:
            flag = False
            break

    if flag:
        up_down_button = abs(n-i) # +, - 버튼 횟수
        number_button = len(channel)
        if result > up_down_button + number_button:
            result = up_down_button + number_button
print(result)