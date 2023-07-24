# GCD(최대 공약수)
# 1. 갭을 줄여도 된다.
# GCD(90,16) == GCD(74,16) == GCD(58,16) == GCD(42,16)
# == GCD(26,16) == GCD(10,16) == GCD(10,6) == GCD(4,6)
# == GCD(4,2) == GCD(2,2)  ==> 최대 공약수는 "2"

# 두 수 A,B를 둘 중 작은 수로 서로 같은 수가 될 때 까지 계속 뺀다. A,B가 같아질 때가 최대 공약수이다.
# 90 % 16 = 10, 16 % 10 = 6, 10 % 6 = 4, 6 % 4 = 2, 4 % 2 = 2(끝)

# 1. 갭을 줄여도 된다.
# 8 12
# 8 4

# 2. 최대 공약수라는 말은 두 수 중 하나로 나누어서 나머지가 생기지 않는 수

# 3. 한수를 가능한 만큼 갭을 줄인다.
# 하나의 수를 작은 수로 되는 만큼 뺀다는 말은
# 나누고 나서 나머지를 뜻한다.


# 최대 공약수
def _gcd(a, b):
    while a % b != 0:  # 나머지가 0이 되는 순간 멈춘다.
        tmp = a % b
        a = b
        b = tmp
    return b


# 최소 공배수
def _lcm(a, b, gcd):
    # 최소 공배수: 두 수의 곱 // 최대 공약수
    return a * b // gcd


g, l = map(int, input().split())
div = l // g  # == a * b
a, b = 1, div
for i in range(1, div // 2 + 1):
    if div % i == 0:
        c = i
        d = div // i
        if _gcd(c, d) != 1:  # c,d는 서로소
            continue
        if a + b > c + d:
            a = c
            b = d
print(a*g,b*g)