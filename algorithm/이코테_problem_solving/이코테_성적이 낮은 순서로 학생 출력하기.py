# 성적이 낮은 순서로 학생 출력하기
# 난이도 1
# 시간 제한 1초
# 메모리 제한 128MB

n = int(input())
rank = [[]]*100

for _ in range(n):
    name,score = list(input().split())
    score = int(score)
    rank[score].append(name)

for i in range(100):
    for name in rank[i]:
        print(name,end=" ")


