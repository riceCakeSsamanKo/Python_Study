#0부터 N까지의 피보나치 수열 구하기

n = int(input())
array = [0]*n
array[0],array[1] = 0,1

#using memoization
def fibo(array, start, n):
    while start<=n:
        if start == n or start <= 1:
            return
        array[start] = array[start - 1] + array[start - 2]
        start+=1

fibo(array,2,n)

count = 1
for x in array:
    print(x,end=" ")

    if count%5 ==0:
        print("\n")
    count+=1