'''
소수 판별 알고리즘
소수는 1과 자기 자신으로만 나누어지는 수를 의미한다.
'''


def is_Prime(x):  # 기본적인 소수 알고리즘 O(N)
    for i in range(2, x + 1):
        if x % i == 0:
            return False
    return True

import math
def is_Prime_sqrt(x):
    for i in range(2, int(math.sqrt(x)) + 1 ): # 2부터 x의 제곱근 까지의 모든 수를 확인
        if x % i == 0:
            return False
    return True

'''
하나의 수가 아닌 범위에 한애 소수를 판별할때 
에라토스테네스의 체 O(nloglogn)
2부터 N까지의 모든 자연수를 나열한다 
남은 수 중에서 아직 처리되지 않은 가장 작은수 i를 찾는다
남은 수 중에서 i의 배수를 모두 제거한다
위 과정을 반복한다 
'''
# n = 1000 # 2부터 1000 까지 모든수 검사
# array = [True for i in range(n+1)] # 초기값으로 모두 소수로 설정
# for i in range(2, math.sqrt(n) + 1): # 2부터 n까지의 제곱근을 모두 확인하며
#     if array[i] == True: # i가 소수인 경우
#         j = 2
#         while i * j <= n: # i * j를 하여 i의 모든 배수 제거
#             array[i*j] = False
#             j += 1
# # 이후 True인 소수값 들만 출력
# for i in range(2, n+1):
#     if array[i]:
#         print(i)

'''
투포인터 알고리즘 
리스트에 순차적으로 접근해야 할 때 두 개의 점 위치를 기록하면서 처리하는 알고리즘 
시작점과 끝점 두개의 점으로 접근할 데이터의 범위를 표현 할수 있음.
'''
array = [1,2,3,2,5]
# def two_pointer(array,target):
#     count = 0
#     for i in range(len(array)-1):
#         j= i+1
#         if array[i] == target or array[j] == target:
#             count += 1
#         if array[i]+array[j] == target:
#             count += 1
#         else:
#             pass
#     return count
#
# print(two_pointer(array, 5))

def two_pointer(array,target):
    count = 0
    total = 0
    end = 0
    for i in range(len(array)):
        while total < target and end < len(array):
            total += array[end]
            end += 1
        if total == target:
            count += 1
        total -= array[i]
    return count



