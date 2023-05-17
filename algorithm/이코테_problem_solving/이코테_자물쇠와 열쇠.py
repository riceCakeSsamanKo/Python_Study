# 미로 탈출
# 난이도 1.5
# 시간제한 1초
# 메모리 제한 128MB

# 2차원 배열 lock nxn, 2차원 배열 key mxm
# 1: 돌기(bump), 0: 구멍
n, m = list(map(int, input().split()))

lock = [[0] * n for _ in range(n)]
key = [[0] * m for _ in range(m)]

# 예시
lock = [[0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0]]

key =  [[1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1]]

def set_key_bump_position(key)->list:
    l = len(key[0])
    arr = []

    for i in range(l):
        for j in range(l):
            if key[i][j] == 1:
                arr.append((i,j))
    return arr


def show_list(array):
    for line in array:
        print(line)

def clockwise_lotation(array):
    m = len(array[0])
    temp = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            temp[i][j] = array[m - j - 1][i]

    for i in range(m):
        for j in range(m):
            array[i][j] = temp[i][j]



def move_left(array)->bool:
    m = len(array[0])

    # 이동 실패
    for i in range(m):
        # 이동 불가 조건
        if array[i][0] == 1:
            print("unable to move left")
            return False

    for i in range(m):
        for j in range(1, m):
            array[i][j - 1] = array[i][j]
        array[i][m - 1] = 0

    # 이동 성공
    return True


def move_right(array)->bool:
    m = len(key[0])

    # 이동 실패
    for i in range(m):
        # 이동 불가 조건
        if array[i][m - 1] == 1:
            print("unable to move right")
            return False

    print("move right (->)")
    for j in range(m-1,0,-1):
        for i in range(m):
            array[i][j] = array[i][j-1]

    for i in range(m):
        array[i][0] = 0

    # 이동 성공
    return True

def move_up(array)->bool:
    m = len(array[0])

    # 이동 실패
    for j in range(m):
        # 이동 불가 조건
        if array[0][j] == 1:
            print("unable to move up")
            return False

    for i in range(1,m):
        for j in range(m):
            array[i-1][j] = array[i][j]

    array[m-1] = [0]*m

    # 이동 성공
    return True

def move_down(array)->bool:
    m = len(array[0])

    # 이동 실패
    for j in range(m):
        # 이동 불가 조건
        if array[m-1][j] == 1:
            print("unable to move down")
            return False
    print("move down")
    for i in range(m-1, 0, -1):  # m-1 ~ 1
        for j in range(m):
            array[i][j] = array[i-1][j]

    array[0] = [0]*m
    # 이동 성공
    return True

def is_open(lock, key_bump_position):
    for i, j in key_bump_position:
        if lock[i][j] == 1:
            return False

    return True

def solution(lock, key):
    print("-----[lock]-----")
    show_list(lock)
    print()
    print("-----[key]-----")
    show_list(key)
    print()

    for cnt in range(4):
        # 최좌측 최상단에서 시작하여 우측으로 이동하며 열쇠가 다 맞으면 return True,
        # 없다면 한칸 아래로 내려감. 최우측 최하단에 도착 시 return False

        # bump 위치 리스트 초기화
        key_bump_position = set_key_bump_position(key)

        # 최상단으로 초기화
        print(f"initializing.... try: {cnt}")
        while move_up(key):
            pass
        # 최좌측으로 초기화
        while move_left(key):
            pass
        print()

        for i in range(m):
            for j in range(m):
                if is_open(lock, key_bump_position):
                    return True
                if not move_right(key):
                    continue
            if not move_down(key):
                continue
        # 상하좌우 이동시 열쇠가 맞지 않아 회전함
        clockwise_lotation(key)
        print("turn")

    return False

answer = solution(lock, key)
print(answer)