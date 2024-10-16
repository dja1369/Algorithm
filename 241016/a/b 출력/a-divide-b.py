n, m = map(int, input().split())

# 나머지를 제외한 정수 출력
print(f"{n // m}.", end="")

# 나머지 저장 
n = n % m
for _ in range(20):
    # 나머지를 정수로 바꿈 
    n *= 10
    # 정수로 바꾼 나머지에서 다시 나누기 
    print(n // m, end="")
    # 나머지값의 나머지를 다시 구하기 -> 반복 
    n = n % m