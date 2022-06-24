'''
문제 정의
올바른 괄호쌍 문제가 나온다면 전형적인 스택 문제이다.
'''


T = int(input())

for _ in range(T): #입력 여려번 반복받음
    stk = [] # 파이썬 에서의 스택은 리스트로 구현됨
    is_vps = True
    for ch in input(): #입력을 받아 (을 넣고 )가 나오면 pop 하여 쌍을 지어준다 전형적인 LIFO 구조
        if ch =='(':
            stk.append(ch)
        else:
            if len(stk) > 0:
                stk.pop()
            else:
                is_vps = False
                break

    if len(stk) > 0:
        is_vps = False




