
'''
피보나치 함수를 재귀 함수로 구현 이렇게 하면 이미 게산된 값이 추가로 계산되면서 비효율적임
'''

def fibo(x):
    if x == 0 or x == 1:
        return 1
    return fibo(x-1) + fibo(x-2)

# dp = [0] * 101 # DP테이블 생성
def dp_fibo_Top_down(x): # 탑 다운 > 메모이제이션 방식
    if x == 0 or x == 1:
        return 1
    if dp[x] != 0: # 0으로 초기화된 DP테이블중 0이 아니라면 즉 계산된 값이 있다면
        return dp[x] # 값 반환
    dp[x] = dp_fibo_Top_down(x-1) + dp_fibo_Top_down(x-2) # 계산된 적이 없다면 점화식에 따라서 피보나치 결과 반환
    return dp[x]

# dp[1], dp[2] = 1, 1 # 바텀업 방식은 DP테이블의 초기값 지정 필요
# x = 99
# for x in range(3, x+1): # 99까지 하나식 올라가며
#     dp[x] = dp[x-1] + dp[x-2] # DP테이블에 값 저장.

'''
    개미 전사 첫째 줄에 식량창고 개수 N이 주어짐 이때 연속으로 인접한 식량창고를 털수 없음 
    둘째 줄에 공백을 기준으로 각 식량 창고에 저장된 식량의 개수 K개가 주어짐 
# '''
# dp = [0] * 100 # DP 테이블 정의
# n = int(input()) # 정수 n 입력받음
# k = list(map(int,input().split())) # 식량창고의 식량수 배열로 입력받음.
# dp[0] = k[0] # DP의 시작점은 k의 0번째 인덱스로 선언
# dp[1] = max(k[0], k[1]) # DP의 첫번째 값은 배열의 0 과 1중 큰값으로 선택 그래야 가장 높은값이 선택가능
# for i in range(2, n): # 2부터 정수 n까지 반복문 시작
#     dp[i] = max(dp[i-1],dp[i-2] + k[i])
#     # dp의 i번째 인덱스는 dp의 i-1 과 dp의 i-2 중 k를 더했을때 큰값으로 결정함
#
# print(dp[n-1]) # 인덱스가 0부터 시작하므로 출력시엔 -1

'''
    1로 만들기 연산은 4가지만 사용가능 5로 나누어지면 5로 나눔 3으로 나누어지면 3으로 나눔 , 2로 나누어 지면 2로 나눔 
    x에서 1을 뺄수있음 이때 연산을 최소한 으로 사용하여 출력 
'''

dp = [0] * 10001
n = int(input())

for i in range(2, n + 1): # 반복문을 수행하며 DP의 값을 업데이트 한다 즉 더 나은 방법이(더 낮은값)이 있다면 업데이트
    dp[i] = dp[i-1] + 1 # 현재의 수에서 1을 빼는 경우
    if i % 2 == 0: # 현재의 수가 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1) # dp의 i인덱스는 dp의 i인덱스와 dp의 i인덱스 나누기 2에 1을 더한값
    if i % 3 == 0: # 현재의 수가 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0: # 현재의 수가 5로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[n])