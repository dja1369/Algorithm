"""
순서대로 입력 되어야함
순서대로 입력 되지 못하면 Sad, 순서대로 입력 되면 Nice 출력
"""
stack = []
n = int(input())
students = list(map(int, input().split()))
now_turn = 1
for student in students:
    stack.append(student)   # 일단 스택에 추가
    while stack and stack[-1] == now_turn:  # 스택이 비어있지 않고, 스택의 맨 위가 현재 순서와 같다면
        stack.pop() # 스택에서 빼기
        now_turn += 1   # 순서 증가
if stack:   # 스택이 남아있다면 못먹는다
    print("Sad")
else:   # 스택이 비어있다면 먹는다
    print("Nice")

