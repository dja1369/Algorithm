"""
a, b 를 받아서 합을 차로 나눈걸 반올림해서 소수점 둘째 자리 까지 표기
"""
a, b = map(int, input().split())

result = (a + b) / (a - b)
print(f"{round(result, 2)}")