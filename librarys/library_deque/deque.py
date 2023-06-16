# 스택과 큐를 합쳐 놓은 것과 동일한 역할을 하는 deque.
# 차이점이라면 front와 rear 모두에서 pop 가능

from collections import deque

q = deque([1,2,3,4,5,6,7])

while q:
    # queue.pop()_ == deque.popleft()
    front = q.popleft()
    print(front, end=" ")
print()

for i in range(10):
    # queue.push() == deque.append()
    q.append(i)
    print(q[i], end=" ")
print()

while q:
    # stack.pop() == deque.pop()
    rear = q.pop()
    print(rear, end=" ")

