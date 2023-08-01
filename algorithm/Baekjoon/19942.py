import sys

input = sys.stdin.readline

n = int(input())
p, f, s, v = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(n)]

result = 99999999999999
result_idx = []
flag = False


def recur(idx, mp, mf, ms, mv, cost, idx_list):
    global result
    global result_idx
    global flag
    if idx == n:
        if mp >= p and mf >= f and ms >= s and mv >= v:
            if cost < result:
                result = cost
                result_idx = []
                flag = True
                for i in idx_list:
                    result_idx.append(i)
            elif cost == result:
                l = min(len(result_idx), len(idx_list))
                for i in range(l):
                    if result_idx[i] > idx_list[i]:
                        result_idx = []
                        for x in idx_list:
                            result_idx.append(x)
                        break
                    elif result_idx[i] < idx_list[i]:
                        break

                    if i == l-1 and len(result_idx) > len(idx_list):
                        result_idx = []
                        for x in idx_list:
                            result_idx.append(x)

        return

    # 재료 선택하는 경우
    idx_list.append(idx + 1)
    recur(idx + 1, mp + ingre[idx][0], mf + ingre[idx][1], ms + ingre[idx][2], mv + ingre[idx][3], cost + ingre[idx][4],
          idx_list)
    # 재료 선택 안하는 경우
    idx_list.pop()
    recur(idx + 1, mp, mf, ms, mv, cost, idx_list)


recur(0, 0, 0, 0, 0, 0, [])

if flag is False:
    print(-1)
else:
    print(result)
    for i in result_idx:
        print(i, end=" ")
