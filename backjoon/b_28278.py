"""
커맨드 5가지
1 스택 넣기
2 스택 빼기
3 스택 개수출력
4 비어있으면 1 아니면 0
5 스택 맨위 정수 출력 없으면 -1
입력
명령수 주어짐 -> 명령주어짐 -> 명령 대로 시행
"""
import sys

stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        stack.append(command[1])
        continue
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)

