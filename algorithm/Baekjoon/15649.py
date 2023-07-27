def recur(number, output):
    if number == m:
        print(output)
        return

    values = list(map(int,output.split()))
    for i in range(1,n+1):
        if i in values:
            continue
        recur(number+1,output+str(i)+" ")

n, m = map(int,input().split())

recur(0, "")

# recur(0) -> [ recur(1), recur(2), recur(3) ]
# recur(1) -> [ recur(2), recur(3) ]
# recur(2) -> [ recur(3) ]


