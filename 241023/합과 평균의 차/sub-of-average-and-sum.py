"""
입력받은 원소들 합, 평균 표기
"""
num_arr = list(map(int, input().split()))

print(sum(num_arr))
print(sum(num_arr) // len(num_arr))
print(sum(num_arr) - (sum(num_arr) // len(num_arr)))