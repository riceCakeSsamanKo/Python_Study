# 음료수 얼려 먹기
# 난이도 1.5
# 시간 제한 1초
# 메모리 제한 128MB

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    print(graph[i])
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


count = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count+=1

print(count)