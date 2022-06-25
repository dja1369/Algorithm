from itertools import combinations

hobits = [int(input()) for _ in range(9)]
total = []
for i in combinations(hobits, 7):
    if sum(i) == 100:
        total = i

for i in sorted(total):
    print(i)