
N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.reverse()
count = 0
for coin in coins:
    count += K // coin
    K %= coin

print(count)