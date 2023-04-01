# 만들 수 없는 금액
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

# target 미만의 수는 모두 구현이 가능하다.
# ex) target == 10 이라면 1부터 9까지의 수는 모두 만들 수 있다.
target = 1

for coin in coins:
    # 종료 조건
    if target < coin:
        break
    target += coin

print(target)
