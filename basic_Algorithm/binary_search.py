import bisect

print('Hello Binary Search!!!')
'''
순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나식 확인하는 방법
이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법 시간복잡도 O(log N)
        이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함.
'''
# array = [1,4,5,6,8,9,10,13,18]
def binary_search(array,target, start, end): # 이진 탐색
    mid = (start + end) // 2 # 중간점 설정
    if start > end: # 출발점이 끝점 보다 커지면 종료 즉 타겟이 없음
        return None
    if array[mid] == target: # 타겟이 발견되면 반환
        return mid
    elif array[mid] > target: # 중간값이 타겟보다 크다면
        return binary_search(array, target, start, mid-1) # 재귀하며 왼쪽 값 확인
    else:
        return binary_search(array, target, mid+1, end) # 중간값이 타겟 보다 크다면 재귀 하며 오른쪽 값 확인
        # 재귀적으로 반복하며 값 출력.
# result = binary_search(array, 8, 0, (len(array)-1))
#
# if result == None:
#     print('목표 값이 없습니다')
# else:
#     print(f'목표값의 인덱스는 {result+1}')

'''
파이썬의 이진 탐색 라이브러리 
from bisect import bisect_left, bisect_right
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환 
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽일할 가장 오른쪽 인덱스 반환
'''
from bisect import bisect_left, bisect_right
# 데이터의 갯수를 구하는 코드
def bisect_range_count(a, left_value, right_value):
    right_idx = bisect_right(a, right_value) # 가장 오른쪽에 있는 인덱스 번호
    left_idx = bisect_left(a, left_value) # 가장 왼쪽에 있는 인덱스 번호
    return right_idx - left_idx # 큰 인덱스 에서 작은 인덱스를 빼주어 갯수 출력
# a = [1,3,3,3,4,5,6]
# print(bisect_range_count(a,3,3))


'''파라메트릭 서치 
최적화 문제를 결정 문제("예" or "아니요")로 바꾸어 해결하는 기법
e.g. 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제 
'''
'''떡볶이 떡 만들기 문제 즉 조건에 맞는 최댓값 구하기'''

# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# start = 0
# end = max(array) # 시작점 과 끝점 구하기
# result = 0 # 결과값 저장
# while(start <= end): # 시작점이 끝점보다 작거나 같을때 까지 반복
#     total = 0
#     mid = (start + end) // 2 # 중간점 계산
#     for i in array: # 배열에서 하나씩 추출 하면서
#         if i > mid: # 자른뒤 떡의 길이 추출
#             total += i - mid # 총합에 떡 - 절단점 값 추가
#     if total < m: # 떡의 총합이 손님이 원하는 길이보다 작다면
#         end = mid - 1 # 절단점을 늘려나감으로써 자를 떡 길이 증가 하기
#     else: # 떡의 길이 총합이 손님이 원하는 값 보다 크거나 같다면
#         result = mid # 결과 값에 절단점을 저장하고
#         start = mid + 1 # 출발점은 절단점 +1 을 하여 다시 계산
#     # 위 과정이 끝나면 result엔 최적의 절단값이 남게된다
# print(result)


'''정렬된 배열에서 특정 수의 개수 구하기 즉 범위 구하기'''
n = [1,1,2,2,2,2,3]
from bisect import bisect_left, bisect_right
def array_value_range(n,left_value, right_value):
    left_idx = bisect_left(n, left_value)
    right_idx = bisect_right(n, right_value)
    if not left_idx:
        return -1
    return right_idx - left_idx

print(array_value_range(n,2,2))