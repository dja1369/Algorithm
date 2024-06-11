n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = [ i for i in arr if i < x ]
print(' '.join(map(str, result)))