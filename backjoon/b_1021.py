'''
1. n개의 원소를 포함하는 데크
2. 뽑아내려는 원소 갯수
3. 맞는 원소면 뽑아내고 아니라면 로테이트(왼쪽, 오른쪽)
4. 이때 모든 원소를 뽑을수있는 최소값 출력
    - 값을 검증해서 조건문 필요
        - 조건문은 타겟이 큐의 길이 절반보다 작거나 같다면 왼쪽으로 회전 아니라면 오른쪽으로 회전
'''
from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])

count = 0
for target in arr:  #
    while True:
        if target == queue[0]:
            queue.popleft()
            break
        else:
            if queue.index(target) <= len(queue)//2:
                queue.rotate(-1)    # 왼쪽으로 회전 [1,2,3] -> [2,3,1]
                count += 1
            else:
                queue.rotate(1)     # 오른쪽으로 회전 [1, 2, 3] -> [3, 1, 2]
                count += 1
print(count)








