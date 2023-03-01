# 게임 개발
# 난이도 2
# 시간제한 1초
# 메모리 제한 128MB

#맵 크기 받기
n,m = map(int,input().split())

#방문한 위치를 위한 맵 생성
visit = [[0]*m for _ in range(n)]
#현 위치와 바라보는 방향 받기
x,y,direction = map(int, input().split())
visit[x][y] = 1  #현 위치 방문 처리

#육지(0)와 바다(1)로 구성된 맵
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnLeft():
    global direction
    direction-=1

    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turnTime = 0

while True:
    turnLeft()
    nx = x+dx[direction]
    ny = y+dy[direction]
    turnTime+=1

    if(visit[nx][ny]==0 and array[nx][ny]==0):
        x = nx
        y = ny
        visit[nx][ny] = 1
        count+=1
        turnTime=0
        continue

    # 네 방향 이미 모두 가본 칸 혹은 바다인 경우
    if turnTime == 4:
        # backDirection = (direction+2)%4
        # nx = x+dx[backDirection]
        # ny = y+dy[backDirection]
        nx = x-dx[direction]
        ny = y-dy[direction]

        #뒤가 바다인 경우
        if array[nx][ny]==1:
            break
        #뒤가 바다가 아니라서 뒤로 한 칸 이동
        else:
            x = nx
            y = ny
            visit[nx][ny] = 1
            turnTime = 0

print(count)




