# 뱀
# 난이도 2
# 시간제한 1초
# 메모리 제한 128MB

from collections import deque

n = int(input())
k = int(input())

# 뱀:1, 사과:2
board = [[0] * n for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 2

l = int(input())
dir_dict = dict()
# 뱀 몸통. 선입(꼬리) 후입(머리). 선출(꼬리)
queue = deque()

for _ in range(l):
    x, c = input().split()
    dir_dict[int(x)] = c

# 방향: 동,남,서,북 (시계)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_idx = 0

x, y = 0, 0
board[x][y] = 1
# [0,0]은 뱀이 존재하는 시작점. queue에 초기화
queue.append((x, y))

# timer cnt
cnt = 0


def turn(turn_dir):
    global dir_idx

    if turn_dir == "L":  # 좌로 회전
        dir_idx = (dir_idx - 1) % 4
    elif turn_dir == "D":  # 우로 회전
        dir_idx = (dir_idx + 1) % 4


while True:
    cnt += 1

    x += dx[dir_idx]
    y += dy[dir_idx]

    # 범위 벗어나면 종료
    if not (0 <= x <= n - 1 and 0 <= y <= n - 1):
        break

    # 사과 없는 경우
    if board[x][y] == 0:
        board[x][y] = 1
        queue.append((x, y))  # 머리 위치 큐에 append

        # 사과를 못먹었으니 꼬리가 위치한 칸은 비워져야함.
        tail_x, tail_y = queue.popleft()
        board[tail_x][tail_y] = 0

        # 방향 전환
        if cnt in dir_dict:
            turn(dir_dict[cnt])

    # 사과 존재
    elif board[x][y] == 2:
        # 꼬리의 위치는 유지되므로 머리만 append하고 꼬리 pop은 진행하지 않는다.
        queue.append((x, y))
        board[x][y] = 1

        # 방향 전환
        if cnt in dir_dict:
            turn(dir_dict[cnt])
    else:  # 몸통과 부딪힘
        break

print(cnt)
