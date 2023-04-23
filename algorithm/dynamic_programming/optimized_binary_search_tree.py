# 알고리즘 분석 과제 3-5

n = int(input())

p = []
p.append(0.)

for x in list(map(float, input().split())):
    p.append(x)

opt = [[0] * (n + 1) for _ in range(n + 2)]  # opt 배열
array_k = [[0] * (n + 1) for _ in range(n + 1)]  # 최소 k를 담는 배열

def sum_probability(i, j):
    result = 0
    for idx in range(i, j+1):
        result += p[idx]
    return result


def cal_opt(n):
    for i in range(1, n + 1):
        opt[i][i] = 1.0
        array_k[i][i] = i

    for diagonal in range(1, n + 1):
        for i in range(1, n - diagonal + 1):
            result = int(1e9)
            result_k = -1
            j = i + diagonal

            for k in range(i, j+1):
                tmp = 1 + (sum_probability(i, k - 1) / sum_probability(i, j)) * opt[i][k - 1] + (sum_probability(k + 1, j) / sum_probability(i, j)) * opt[k + 1][j]
                if result > tmp:
                    result = tmp
                    result_k = k
            opt[i][j] = result
            array_k[i][j] = result_k


cal_opt(n)

for i in range(1, n + 1):
    for j in range(1,n+1):
        x = opt[i][j]
        if x!=0:
            print(round(x,2), end=" ")
        else:
            print(end="    ")
    print()
print()

for i in range(1, n + 1):
    for x in array_k[i]:
        if x != 0:
            print(x, end=" ")
        else:
            print(end="  ")
    print()
