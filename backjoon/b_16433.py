"""
N * N 격자 생성
1. 각 칸에는 최대 하나의 당근
2. 각 칸의 변에 당근이 있다면 (상,하,좌,우) 심을수 없음
3. 최초에 1개 심은 칸이 주어짐
4. 이때 최대로 심을수 있는 당근 구하기
- 크기 설정 -> 최초 당근 설정 -> 행과 열이 같은지 검증 -> 같다면 행 이 짝수일때
- 이때 최대로 심을수 있은 경우의 밭 모습 출력
"""

N, R, C = map(int, input().split())

matrix = [["." for _ in range(N)] for _ in range(N)]

matrix[R-1][C-1] = "v"

for row in range(N):
    if (R + C) % 2 == 0: # 둘다 홀수거나 둘다 짝수거나
        if row % 2 == 0:
            for col in range(0, N, 2):
                matrix[row][col] = "v"
        elif row % 2 != 0:
            for col in range(1, N, 2):
                matrix[row][col] = "v"

    else:
        if row % 2 == 0:
            for col in range(1, N, 2):
                matrix[row][col] = "v"
        elif row % 2 != 0:
            for col in range(0, N, 2):
                matrix[row][col] = "v"

for row in matrix:
    print("".join(row))


