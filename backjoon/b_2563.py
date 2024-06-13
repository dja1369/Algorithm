n = int(input())
matrix = [[0] * 100 for _ in range(100)]    # 도화지 초기화

result = 0
for _ in range(n):  # 색종이 수 만큼 반복
    x, y = map(int, input().split())    # 색종이 좌표 입력
    for i in range(y, y+10):    # 색종이 시작점 부터 세로 길이 탐색
        for j in range(x, x+10):    # 색종이 시작점 부터 가로 길이 탐색
            matrix[i][j] = 1    # 색종이가 덮는 부분 1로 표시

for mat in matrix:  # 도화지 행 별로 탐색
    result += sum(mat)  # 도화지 행에 존재하는 1 개수 더하기 -> 넓이
print(result)

