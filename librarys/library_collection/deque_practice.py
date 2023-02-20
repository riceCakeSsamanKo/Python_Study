from collections import deque

#deque은 queue처럼 사용
data = deque([1,2,3,4,5])

#삽입
data.append(100) #맨 오른쪽
data.appendleft(-100) #맨 왼쪽
print(list(data))

#삭제
data.pop()  #맨 오른쪽
print(list(data))

data.popleft() # 맨 왼쪽
print(list(data))

