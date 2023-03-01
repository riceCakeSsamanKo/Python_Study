# 시각
# 난이도 1
# 시간제한 2초
# 메모리 제한 128MB

n = int(input())
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count+=1

print(count)

