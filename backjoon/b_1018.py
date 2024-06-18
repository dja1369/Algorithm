n, m = map(int, input().split())
result = []
board = [input() for _ in range(n)]

for i in range(n-7):
    for j in range(m-7):
        is_black=0
        is_white=0
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 시작점의 색은 검정, 하양 이다
                if(a+b)%2==0: # 짝수 일 경우
                    if board[a][b] == 'B':  # 짝수의 경우 일정한 색을 가지게 됨
                        is_white+=1
                    else:
                        is_black+=1
                else:   # 홀수 일 경우
                    if board[a][b] == 'B':  # 홀수의 경우 일정한 색을 가지게 됨
                        is_black+=1
                    else:
                        is_white+=1
        result.append(is_black)
        result.append(is_white)

print(min(result))