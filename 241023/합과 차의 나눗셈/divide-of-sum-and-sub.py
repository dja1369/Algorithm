a, b = map(int, input().split())

result = (a + b) / (a - b)
print(f"{round(result, 2):.2f}")