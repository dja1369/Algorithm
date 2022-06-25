import heapq as hq
import sys
N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap,(abs(x),x))
    else:
        print(hq.heappop(heap)[1] if heap else 0)
