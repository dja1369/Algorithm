a, b = map(int, input().split())

a, b = max(a, b), min(a, b)

for i in range(a, b-1, -1):
    print(i, end=" ")