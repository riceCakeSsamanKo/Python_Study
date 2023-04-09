# 알고리즘 분석 과제 3-5

n = int(input())
d = []  #ai = di*di+1, d0 = 0
d.append(0) 
for x in list(map(int, input().split())):
    d.append(x)

opt = [['x']*(n+1) for _ in range(n+1)]
p = [['x']*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    p[i][i] = 0

def cal_opt(n):
    for i in range(n + 1):
        opt[i][i] = 0
    for diagonal in range(1,n+1):
        for i in range(1,n-diagonal+1):
            result = int(1e9)
            result_k = -1
            j = i+diagonal
            for k in range(i,j):
                if result > opt[i][k]+opt[k+1][j]+d[i]*d[k+1]*d[j+1]:
                    result = opt[i][k]+opt[k+1][j]+d[i]*d[k+1]*d[j+1]
                    result_k = k
            opt[i][j] = result
            p[i][j] = result_k

cal_opt(n)
for i in range(1,n+1):
    for x in opt[i]:
        if x!=-1:
            print(x,end=" ")
        else:
            print(end=" ")
    print()
print()

for i in range(1,n+1):
    print(f"{i}:",end=" ")
    for x in p[i]:
        if x!=-1:
            print(x,end=" ")
        else:
            print(end=" ")
    print()

def order (i,j):
    if i == j:
        print('A',i,end=" ")
    else:
        k = p[i][j]
        print("(", end=" ")
        order(i, k)
        order(k + 1, j)
        print(")",end=" ")

order(1,n)



