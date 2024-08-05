"""
- n, m 사이트가 주어짐
- 이때 서로 중복 안되면서 1개로 이루어진 다리를 짓는 경우의 수
"""
from math import comb
r = int(input())

for _ in range(r):
    n, m = map(int, input().split())

    print(comb(m, n))
