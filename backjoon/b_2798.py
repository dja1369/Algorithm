from itertools import combinations
n, m = map(int, input().split())
deck = list(map(int, input().split()))

result = combinations(deck, 3)

answer = 0
for r in result:
    if sum(r) <= m:
        answer = max(answer, sum(r))
print(answer)
