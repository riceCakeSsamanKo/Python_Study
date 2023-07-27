def recur(num):
    if num == m:
        print(*graph)
        return

    for i in range(1,n+1):
        if i in graph:
            continue
        if num != 0 :
            if graph[num-1] > i:
                continue
        graph.append(i)
        recur(num + 1)
        graph.pop()


n, m = map(int, input().split())
graph = []

recur(0)