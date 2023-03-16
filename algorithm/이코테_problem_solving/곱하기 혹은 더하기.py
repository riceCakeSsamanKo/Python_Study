# 곱하기 혹은 더하기
# 난이도 1
# 시간제한 1초
# 메모리 제한 128MB

nums = list(map(int, input()))
result = nums[0]

for num in nums[1:]:
    if num <= 1 or result <= 0:
        result += num
    else:
        result *= num

print(result)
