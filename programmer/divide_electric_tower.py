from collections import defaultdict, deque

def bfs(start, blocked, n, nodes):
    count = 0
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in nodes[node]:
            if visited[i] or i == blocked:
                continue
            count += 1
            queue.append(i)
            visited[i] = True
    return count

def solution(n, wires):
    answer = 100
    data = defaultdict(list)
    for k, v in wires:
        data[k].append(v)
        data[v].append(k)
    for wire in wires:
        result1 = bfs(wire[0], wire[1], n, data)
        result2 = bfs(wire[1], wire[0], n, data)
        answer = min(answer, abs(result1 - result2))
    return answer