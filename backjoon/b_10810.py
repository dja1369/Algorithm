n, m = map(int, input().split())
result = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for i in range(i, j+1):
        result[i-1] = k
print(" ".join(map(str, result)))