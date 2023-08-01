n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]
result = []
def recur(idx, sour, bitter):
    global result
    if idx == n:
        result.append(abs(sour - bitter))
        return

    recur(idx+1, sour*taste[idx][0], bitter+taste[idx][1])

    recur(idx+1, sour, bitter)

recur(0,1,0)
result = result[0:-1]
result.sort()
print(result[0])