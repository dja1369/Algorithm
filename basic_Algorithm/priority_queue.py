import heapq
pq =[]
heapq.heappush(pq,123)
heapq.heappush(pq,1010)
heapq.heappush(pq,2)
heapq.heappush(pq,-2)

print(pq)
while len(pq) > 0 :
    print(heapq.heappop(pq))