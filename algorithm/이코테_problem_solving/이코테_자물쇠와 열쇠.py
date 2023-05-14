# 미로 탈출
# 난이도 1.5
# 시간제한 1초
# 메모리 제한 128MB

# 2차원 배열 lock nxn, 2차원 배열 key mxm
# 1: 돌기(bump), 0: 구멍
n, m = list(map(int, input().split()))

lock = [[0] * n for _ in range(n)]
key = [[0] * m for _ in range(m)]
# key의 1이 나오는 인덱스
key_bump_position = []

# 예시
lock = [[1,0,1,0],
        [1,0,1,0],
        [1,0,1,0],
        [1,0,1,0]]
key =  [[1,1,1,1],
        [0,0,0,0],
        [1,1,1,1],
        [0,0,0,0]]

for i in range(m):
    for j in range(m):
        if key[i][j] == 1:
            key_bump_position.append((i,j))

print(key_bump_position)

def show_list(array):
    for line in array:
        print(line)

def clockwise_lotation(key):
    m = len(key[0])
    temp = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            temp[i][j] = key[m - j - 1][i]

    return temp


def move_left(key)->bool:
    m = len(key[0])

    # 이동 실패
    for i in range(m):
        # 이동 불가 조건
        if key[i][0] == 1:
            print("unable to move left")
            return False

    for i in range(m):
        for j in range(1, m):
            key[i][j - 1] = key[i][j]
        key[i][m - 1] = 0

    # 이동 성공
    return True


def move_right(key)->bool:
    m = len(key[0])

    # 이동 실패
    for i in range(m):
        # 이동 불가 조건
        if key[i][m - 1] == 1:
            print("unable to move right")
            return False

    for i in range(m):
        for j in range(1, m):
            key[i][j] = key[i][j - 1]
        key[i][0] = 0
    # 이동 성공
    return True

def move_up(key)->bool:
    m = len(key[0])

    # 이동 실패
    for j in range(m):
        # 이동 불가 조건
        if key[0][j] == 1:
            print("unable to move up")
            return False

    for i in range(1, m):
        for j in range(m):
            key[i - 1][j] = key[i][j]

    # 이동 성공
    return True

def move_down(key)->bool:
    m = len(key[0])

    # 이동 실패
    for j in range(m):
        # 이동 불가 조건
        if key[m-1][j] == 1:
            print("unable to move down")
            return False

    for i in range(1, m):
        for j in range(m):
            key[i][j] = key[i-1][j]
    # 이동 성공
    return True

def is_open(lock, bump_position):
    for i,j in bump_position:
        if lock[i][j] == 1:
            return False

    return True

def solution(lock, key, key_bump_position):
    show_list(key)
    for _ in range(4):
        # 최좌측 최상단에서 시작하여 우측으로 이동하며 열쇠가 다 맞으면 return True,
        # 없다면 한칸 아래로 내려감. 최우측 최하단에 도착 시 return False

        # 최상단으로 초기화
        while move_up(key):
            pass
        # 최좌측으로 초기화
        while move_left(key):
            pass

        for i in range(m):
            for j in range(m):
                if is_open(lock, key_bump_position):
                    return True
                move_right(key)
            move_down(key)

        # 상하좌우 이동시 열쇠가 맞지 않아 회전함
        clockwise_lotation(key)
        print("turn")

    return False

answer = solution(lock, key, key_bump_position)
print(answer)