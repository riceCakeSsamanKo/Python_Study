# 상하좌우
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

# 초기 입력
n = int(input())
x, y = 1, 1
plans = list(input().split())

# 이동 방향들
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동하기
for plan in plans:  # 이동 계획 확인
    for i in range(len(move_types)):  # 확인한 계획에서 이동 방향 좌표 확인 후 이동
        if move_types[i] == plan:
            if (1 <= x + dx[i] <= n and
                    1 <= y + dy[i] <= n):
                x += dx[i]
                y += dy[i]
print(x, y)

"""
ps: 풀이가 좀 별론거 같음

dir = dict({"L" : (0, -1),
            "R" : (0, 1),
            "U" : (-1, 0),
            "D" : (1, -0)})

position = [0]*2
n = int(input())
def move(pos:list, dir:set):
    if(0 <= pos[0]+dir[0] < n and
        0 <= pos[1]+dir[1] < n ):
        pos[0]+=dir[0]
        pos[1]+=dir[1]


dirList = list(input().split())

for d in dirList:
    move(position, dir[d])

print(position[0]+1, position[1]+1)

"""
