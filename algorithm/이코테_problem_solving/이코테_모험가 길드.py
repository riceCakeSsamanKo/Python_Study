# 모험가 길드
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

n = int(input())
members = list(map(int, input().split()))

members.sort()

# 팀 개수
result = 0
# 팀원 수
count = 0
for i in range(n):
    count += 1
    if count >= members[i]:
        result += 1  # 팀 개수 추가
        count = 0


print(result)