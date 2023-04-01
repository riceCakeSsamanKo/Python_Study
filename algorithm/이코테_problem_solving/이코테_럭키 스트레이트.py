# 럭키 스트레이트
# 난이도 1
# 시간제한 1초
# 메모리 제한 256MB

n = int(input())
# 수 길이(총 자리수)
num_of_line = 1

while pow(10,num_of_line) < n:
    num_of_line+=2

num_of_line-=1

# 앞 자리수
forward = n // pow(10,num_of_line/2)
# 뒷 자리수
back = n % pow(10,num_of_line/2)

f_sum=0
while forward != 0:
    f_sum+=forward%10
    forward = forward//10

b_sum = 0
while back != 0:
    b_sum+=back%10
    back = back//10

if f_sum == b_sum:
    print("LUCKY")
else:
    print("READY")


