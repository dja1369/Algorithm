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
                    if board[a][b] == 'B':  # 인덱스의 합을 보고 홀수의 경우와 짝수의 경우의 색상이 나옴
                        is_white+=1
                    else:
                        is_black+=1
                else:   # 홀수 일 경우
                    if board[a][b] == 'B':
                        is_black+=1
                    else:
                        is_white+=1
        result.append(is_black)
        result.append(is_white)

print(min(result))