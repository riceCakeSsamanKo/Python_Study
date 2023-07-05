import sys
import heapq


read = sys.stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def cal_max_pos():
    x, y = 0, 0

    max_value = sticker[0][0]
    for j in range(n):
        if sticker[0][j] > sticker[1][j]:
            i = 0
        else:
            i = 1

        if max_value < sticker[i][j]:
            max_value = sticker[i][j]
            x = i
            y = j

    return (x,y)



def cut_sticker(x,y):
    sticker[x][y] = 0

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > 1 or ny < 0 or ny >= n:
            continue
        sticker[nx][ny] = 0

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = []

    sticker.
    for _ in range(2):
        sticker.append(list(map(int, read().split())))

    sum = 0
    while True:
        pos = cal_max_pos()
        x = pos[0]
        y = pos[1]
        if sticker[x][y] == 0:
            break

        sum += sticker[x][y]
        cut_sticker(x,y)

    print(sum)