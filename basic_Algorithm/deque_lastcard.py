'''
문제정의 카드는 정렬된 상태로 1번이 제일위 N번이 제일 밑인 상태로 되어있다
이 동작을 1장 남을때 까지 반복해서 마지막 남은 카드를 구한다
배열은 시간 복잡도가 O(N)인데 삽입 삭제가 일어나니까 O(N^)이 되어버림
그렇기에 시간 복잡도를 줄이기 위해 dequeue를 사용함.
'''
from collections import deque
N = int(input())
# N = 4
queue = deque()
for i in range(1,N+1): # 1, 2, 3, 4, ... N
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop)