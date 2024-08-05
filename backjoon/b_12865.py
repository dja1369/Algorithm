"""
"""
N, K = map(int, input().split())
items = []

for _ in range(N):
    items.append(list(map(int, input().split())))

dp = [0 for _ in range(K + 1)]
for item in items:
    w, v = item
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)

print(dp[-1])

