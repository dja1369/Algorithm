a, b = map(int, input().split())

result = a
for _ in range(a, b):
    if result > b:
        break 
    if result % 2 != 0:
        print(result, end=" ")
        result *= 2  
    else:
        print(result, end=" ")
        result += 3