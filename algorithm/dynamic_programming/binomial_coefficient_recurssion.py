count = 0
def bin(n,k):
    global count
    if n < 0 or k < 0 or n < k:
        return 0
    if k==0 or n==k:
        return 1
    else:
        count+=2  # 재귀간 생성되는 노드 개수
        return bin(n-1,k) + bin(n-1,k-1)

print(bin(20,14))
print(count)