a, b = map(int, input().split())

result = a
for _ in range(a, b+1):
    if result > b:
        break
    print(result, end=" ")
    if result % 2 != 0:
        result *= 2  

    else:
        result += 3