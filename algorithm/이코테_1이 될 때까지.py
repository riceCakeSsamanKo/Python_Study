# 1이 될 때까지
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

# 1) N에서 1을 뺀다
# 2) N을 K로 나눈다 (단 N이 K로 나누어 떨어질 때만)

n,k = map(int,input().split())

count = 0

while(n > 1):
    count += 1

    if(n%k == 0):
        n = n//k
    else:
        n-=1

print(count)

