
'''Factorial 재귀 로 구현'''

def factorial_recursion(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

'''Factorial 반복문 구현'''

def factorial_for(n):
    answer = 1
    for i in range(2,n+1):
        answer *= i
    return answer


'''유클리드 호제법 재귀 구현'''

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)

'''DFS 깊이 우선 탐색 >> 깊은 부분을 우선적으로 탐색하는 알고리즘 >> 스택, 재귀 함수 이용
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리 
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리 
    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼내기 
3. 더이상 2번의 과정이 수행되지 않을때 까지 반복
'''
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [False] * 9 # 0번째 인덱스를 쓰지 않기위해 1더 큰 크기로 스택 생성

def dfs(graph, v, visited):
    visited[v] = True # 첫번째 노드 방문처리
    print(f'현제 방문 노드 {v}')
    for i in graph[v]: # 그래프를 순회하며 탐색
        if not visited[i]: # 만약 방문하지 않은 노드라면
            dfs(graph, i ,visited) # 재귀함수로 그래프 와 노드 정보 전달후 재귀 이는 처음의 방문처리 구문으로 돌아가 방문처리가 된다

# dfs(graph, 1, visited) # 그래프, 1번째 노드, 방문정보 전달

# for i in range(len(graph)): # 2차원 배열 출력
#     for j in range(len(graph[i])): 그래프[i]의 길이만큼 j 인덱스 증가
#         print(graph[i][j])

'''BFS 너비 우선 탐색 >> 그래프에서 가까운 노트부터 우선적으로 탐색하는 알고리즘 >> 큐 자료구조 사용
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼낸뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리 
3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복.
'''
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start]) # 큐 생성
    visited[start] = True # 큐의 시작 노드 방문 처리
    while queue: # 큐가 빌때까지 반복
        v = queue.popleft() # 출발 노드 pop
        print(f'현재 방문한 노드 : {v}')
        for i in graph[v]: # 그래프에서 인접 노드 반복
            if not visited[i]: # 인접 노드가 방문되지 않았다면
                queue.append(i) # 큐에 인접노드 추가후 방문 처리 >> 이후 반복하기
                visited[i] = True
# bfs(graph, 1, visited)

'''음료수 얼려먹기 >> 얼음 틀의 모양이 주어 졌을때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성'''

# n, m = map(int, input().split()) # n, m 공백기준으로 입력
# graph = [] # 그래프 생성
# for i in range(n): # n번만큼 반복해서 리스트 형태로 입력 받기 [ [n],[n],... ] 2차원 배열로 생성됨
#     graph.append(list(map(int, input())))

# def dfs_ice(x,y):
#     if x <= -1 or y <= -1 or x >= n or y >= m: # x, y가 범위를 벗어난다면 즉시 종료
#         return False
#     if graph[x][y] == 0: # 현재 그래프의 방문노드가 0 이라면 즉 방문하지 않았다면
#         graph[x][y] = 1 # 시작 노드 방문처리
#         dfs_ice(x-1 ,y) # 상하 좌우 재귀적으로 방문
#         dfs_ice(x+1,y)
#         dfs_ice(x,y-1)
#         dfs_ice(x, y+1)
#         return True
#     return False

# result = 0
# for i in range(n): # 행
#     for j in range(m): # 열
#         if dfs_ice(i,j) == True: # 값이 True면 결과값 1 증가
#             result += 1
# print(result)

'''미로 탈출 이동시 최소 거리를 구해라 BFS'''
n, m = map(int, input().split()) # n, m 공백기준으로 입력
graph = [] # 그래프 생성
for i in range(n): # n번만큼 반복해서 리스트 형태로 입력 받기 [ [n],[n],... ] 2차원 배열로 생성됨
    graph.append(list(map(int, input())))
movex = [-1,1,0,0] # 이동할수 있는 방향 정의
movey = [0,0,-1,1]

from collections import deque
def bfs_maze(x,y):
    queue = deque() # BFS 구현을 위해 deque 라이브럴 ㅣ사용
    queue.append((x,y)) # 시작점 추가
    while queue: # 큐가 빌때까지 반복
        x,y = queue.popleft() # x, y는 queue의 첫번째 pop
        for i in range(4): # 상 하 좌 우로 이동
            nx = x + movex[i] # x + 상 하 좌 우 값 더해주기
            ny = y + movey[i] # y + 상 하 좌 우 값 더해주기
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 범위를 벗어나면 컨티뉴
                continue
            if graph[nx][ny] == 0: # 갈수 없는곳 이라면 컨티뉴
                continue
            if graph[nx][ny] == 1: # 만약 그래프에서 이동한 노드가 1 이라면 즉 최초 방문 이라면
                graph[nx][ny] = graph[x][y] + 1 # 직전 노드에 1씩 더해준값을 넣어 준후 최신화
                queue.append((nx,ny))
    return graph[x - 1][y - 1] # 가장 오른쪽 아래 까지의 최단 거리 반환

print(bfs_maze(0, 0))