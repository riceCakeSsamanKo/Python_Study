# 볼링공 고르기
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB


# 볼링공 개수 n, 1<= 볼링공 무게 <= m
n, m = map(int, input().split())

# 공의 무게 별 개수
# ex) weights[3] == 무게가 3인 공의 개수
weights = [0]*(m+1)

# 각 공의 무게를 리스트로 받기
balls = list(map(int,input().split()))

for weight in balls:
    weights[weight] += 1

result = 0
for i in range(1,m+1):
    for j in range(i+1,m+1):
        result += weights[i] * weights[j]

print(result)
