from itertools import combinations

N, M = map(int, input().split())
result = combinations([i for i in range(1, N + 1)], M)
print(len(list(result)))
