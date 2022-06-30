'''
피보나치 수열
n(0) = 0
n(1) = 1
n(i+2) = (i+1)+ (i)
'''

cache = [-1] * 91 #DP를 위한 DP 테이블 정의
cache[0] = 0
cache[1] = 1
count = 0
def f(n): # Top-Down
    global count
    count += 1
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]

print(f(int(input())))
print('count',count)

# N = int(input()) # bottom - Up
# cache = [-1] * 91 #DP를 위한 DP 테이블 정의
# cache[0] = 0
# cache[1] = 1
#
# for i in range(2, N+1):
#     cache[i] = cache[i-1] + cache[i-2]
#
# print(cache[N])



