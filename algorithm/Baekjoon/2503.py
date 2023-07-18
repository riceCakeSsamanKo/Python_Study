n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]

result = 0
for a in range(1, 10):  # 100의 자릿수
    for b in range(10):  # 10의 자릿수
        if b == a:
            continue
        for c in range(10):  # 1의 자릿수
            if c == a or c == b:
                continue
            count = 0
            for number, strike, ball in hint:
                num_strike = 0  # Strike 개수
                num_ball = 0  # Ball 개수

                A = int(str(number)[0])
                B = int(str(number)[1])
                C = int(str(number)[2])

                if a == A:
                    num_strike += 1
                if b == B:
                    num_strike += 1
                if c == C:
                    num_strike += 1

                if a == B or a == C:
                    num_ball += 1
                if b == A or b == C:
                    num_ball += 1
                if c == B or c == A:
                    num_ball += 1

                # 만족안하면 break
                if num_strike == strike and num_ball == ball:
                    count += 1
                else:
                    break
            if count == n:
                result += 1

print(result)
