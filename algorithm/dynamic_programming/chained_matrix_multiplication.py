# 알고리즘 분석 과제 3-3

n = int(input())
d = []  #ai = di x d(i+1) 행렬, d0 = 0
# d0 = 0
d.append(0)

# di 입력 받기
for x in list(map(int, input().split())):
    d.append(x)

# opt는 행렬 ai 부터 aj 까지 행렬 곱을 진행 하는데 있어 계산의 최소 횟수를 담아두는 이차원 배열
# ex) opt[1][3] == a1xa2xa3를 계산하는데 필요한 최소 계산 횟수
opt = [['x']*(n+1) for _ in range(n+1)]

# p는 opt[i][j]를 계산시 k를 담아 두는 배열
# opt[i][j] = min(opt[i][k] + opt[k+1][j] + di*d(k+1)*dj)
p = [['x']*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    p[i][i] = 0

def cal_opt(n):
    for i in range(n + 1):
        # 대각선은 0으로 초기화
        opt[i][i] = 0
    for diagonal in range(1,n+1):
        for i in range(1,n-diagonal+1): # i의 접근 범위 [1:n-1], [1:n-2], ..., [1:1]
            result = int(1e9)
            result_k = -1
            j = i+diagonal  # k의 접근 범위 ([1:2], ..., [n:n]), ([1:3], ..., [n-2:n]), ..., ([1:n])
            for k in range(i,j):
                if result > opt[i][k]+opt[k+1][j]+d[i]*d[k+1]*d[j+1]:
                    result = opt[i][k]+opt[k+1][j]+d[i]*d[k+1]*d[j+1]
                    result_k = k
            # for문을 돌고 나온 result는 최소 opt[i][j]
            opt[i][j] = result
            # opt가 최소일 경우 k값
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



