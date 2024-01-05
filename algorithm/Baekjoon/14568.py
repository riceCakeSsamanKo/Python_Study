# 택희 : 2*y : A
# 영훈 : x : B
# 남규 : x + 2 + z : C
#
# N = 2*x+2+z+2*y
#
# N = 2(x+y+1)+z

# n = int(input())
# result = 0
# for x in range(1,50):
#     for y in range(1,50):
#         for z in range(100):
#             if n == 2*(x+y+1)+z:
#                 result+=1
#
# print(result)


# a >= b+2
# a, b, c >0
# c % 2 == 0

n = int(input())
cnt = 0

for c in range(2, n + 1, 2):
    left = n - c
    for b in range(1, left + 1):
        a = left - b
        if a >= b + 2:
            cnt += 1

print(cnt)
