import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_value = 0


def recur(idx, total):
    global max_value

    day = graph[idx][0]
    profit = graph[idx][1]

    if idx+day > n:
        max_value = max(max_value, total)
        return
    elif idx+day == n:
        max_value = max(max_value,total+profit)
        return

    # 상담하는 경우
    recur(idx + day, total + profit)
    # 상담하지 않는 경우
    recur(idx + 1, total)


recur(0, 0)

print(max_value)
