import sys

input = sys.stdin.readline

f, s, g, u, d = list(map(int, input().split()))
#건물 높이, 시작 층, 목적지 층, 한번에 올라갈 수 있는 층, 한번에 내려갈 수 있는 층
visited = [False] * (f + 1)

cur = s
result = 0
while True:
    if cur == g:
        break
    elif cur < g:
        if cur + u > f:
            if cur - d < 1:
                result = "use the stairs"
                break
            elif visited[cur - d]:
                result = "use the stairs"
                break
            else:
                cur -= d
                visited[cur] = True
                result+=1
                continue
        else:
            if visited[cur + u]:
                result = "use the stairs"
                break
            cur += u
            visited[cur] = True
            result += 1

    elif cur > g:
        if cur - d < 1:
            if cur + u > f:
                result = "use the stairs"
                break
            elif visited[cur + u]:
                result = "use the stairs"
                break
            else:
                cur+=u
                visited[cur] = True
                result += 1
                continue
        else:
            if visited[cur - d]:
                result = "use the stairs"
                break
            cur -= d
            visited[cur] = True
            result += 1

print(result)