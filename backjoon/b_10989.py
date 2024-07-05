from sys import stdin
N = int(stdin.readline())
container = [0 for _ in range(10001)]
for _ in range(N):
    num = int(stdin.readline())
    container[num] += 1

for i in range(len(container)):
    if container[i] != 0:
        for _ in range(container[i]):
            print(i)
