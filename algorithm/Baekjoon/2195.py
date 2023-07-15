s = input()
p = input()

start = 0
result = 0
while start < len(p):
    end = start

    if p[start:] in s:
        result += 1
        break

    while True:
        if p[start:end + 1] in s:
            end += 1
        else:
            result += 1
            start = end
            break

print(result)
