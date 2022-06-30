'''
문제 정의
NM개의 단위 정사각형의 보드 를 잘라 8 * 8 의 체스판을 만들려고 함
완전 탐색
'''
N, M = map(int,input().split()) # 입력값 받기
board = [input()for _ in range(N)] # 체스보드 판 생성
ans = N * M # ans는 일단 최대값으로 설정후 점점 줄여나감

def solution(y,x, bw):
    global ans
    count = 0
    for i in range(8): # 문제에서 정의된대로 8 * 8 로 이중 반복문 실행
        for j in range(8):
            if (i + j) % 2: # i + j 가 짝수라면
                if board[y + i][x+j] == bw: # e.g. 1+1번 인덱스 1+1번 인덱스가 b라면 count+1
                    count += 1
        else:
            if board[y + i][x + j] != bw: # e.g. 1+1번 인덱스 1+1번 인덱스가 w라면 count+1
                count += 1
    ans = min(ans, count) # 모든 경우의 수를 반복해 최소값 업데이트

for i in range(N-7):
    for j in range(M-7):
        solution(i,j,'B')
        solution(i,j,'W')


print(ans)


'''
좀더 쉽게 설명된 코드 
n, m = map(int, input().split()) #입력값을 받기 
l = [] # 보드판 생성 
mini = [] # 최소값 리스트 생성 

for _ in range(n):
    l.append(input()) # 보드판 생성 

for a in range(n - 7): # 보드에서 8 * 8을 벗어나지 않기위해 -7 로 패딩 
    for i in range(m - 7): # 보드에서 8 * 8을 벗어나지 않기위해 -7 로 패딩 
        idx1 = 0 # w로 시작할 경우
        idx2 = 0 # b로 시작할 경우
        for b in range(a, a + 8): # 1부터 8 까지 반복
            for j in range(i, i + 8): # 1부터 8 까지 반복    # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0: # (j + b)가 짝수라면 
                    if l[b][j] != 'W': idx1 += 1  # l[1][1]이 w가 아니라면 w로 칠할횟수 +1
                    if l[b][j] != 'B': idx2 += 1  # l[1][1]이 b가 아니라면 b로 칠할횟수 +1
                else :
                    if l[b][j] != 'B': idx1 += 1  # 홀수로 시작하여 l[1][1]이 b가 아니라면 b로 칠할횟수 +1
                    if l[b][j] != 'W': idx2 += 1  # 홀수로 시작하여 l[1][1]이 w가 아니라면 w로 칠할횟수 +1
        mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        mini.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(mini))                                   # 칠해야 하는 개수의 최소값
'''