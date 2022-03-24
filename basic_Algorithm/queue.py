from collections import deque

q = deque()
q.append(123)
q.append(456)
q.append(789)

print("size : ", len(q)) # 데이터의 크기 출력
while len(q) > 0: # q의 크기가 0보다 클때 동안
    print(q.popleft()) # 왼쪽에서 하나씩 빼게됨