#현재 위치 받기
input_value = input()
cur_x = ord(input_value[0]) - ord('a')   #ord()는 문자를 아스키 코드로 반환
cur_y = int(input_value[1])-1

steps = [ (-2,1), (-2,-1),
         (2,1), (2,-1),
         (-1,2),(-1,-2),
         (1,2), (1,-2) ]

count = 0
for step in steps:
    next_x = cur_x+step[0]
    next_y = cur_y+step[1]

    if(0<=next_x<8 and 0<=next_y<8):
        count += 1
print(count)