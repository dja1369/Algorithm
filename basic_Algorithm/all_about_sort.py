
array = [9,8,3,4,5,6,1,2,7]
n = len(array)

def bubble_sort():
    '''인접한 두 수를 비교하며 정렬함 O(N^2)'''
    for i in range(n): # 리스트 전체 순회
        for j in range(n - 1): # 리스트 최대 길이 -1 만큼 순회 > 리스트 길이 초과 방지
            if array[j] > array[i]: # 만약 j가 i보다 크다면
                array[i], array[j] = array[j], array[i] # i,j의 위치 변경

        print(array[:i+1])

def selection_sort():
    '''한바퀴 를 돌때 가장 작은 값을 찾아 맨 앞과 교환 O(N^2)'''
    for i in range(n):
        min_idx = array[i] # 첫번째 값 저장
        for j in range(array[i]+1 ,n): # 첫번째인덱스 +1, arr의 길이보다 적은수로 반복
            if array[min_idx] > array[j]:
                array[min_idx] = array[j]
        array[i], array[min_idx-1] = array[min_idx-1], array[i] # 인덱스는 0부터 시작하기에 -1 하여 인덱스값 맞춤

        print(array[:i+1])

def insertion_sort():
    '''타겟인 데이터의 앞순번을 따져 본인보다 큰 데이터는 앞 본인보다 작은 데이터는 뒤에 삽입하는 방식 (일반적으로 선택 정렬보다 더 빠르게 동작)'''
    for i in range(n):
        for j in range(n-1,0,-1):
            if array[j-1] > array[j]:
                array[j-1] , array[j] = array[j], array[j-1]
        print(array[:i+1])

def advanced_insertion_sort():
    '''정렬이 되어있다는 조건하에 작동함'''
    array.sort()
    for i in range(n): # array의 길이만큼 반복
        j = i # j = i 첫번째 값 을 저장
        while j > 0 and array[j-1] > array[j]: # j 가 0보다 크고 j-1번 인덱스가 j보다 클때 작동 즉 이전의 수보다 타겟이 작아질때 까지 루프
            array[j-1] , array[j] = array[j], array[j-1] # 스왑
        print(array[:i+1])

# array = [9,8,3,4,5,6,7,2,1]
def merge_sort(array):
    '''분할 정복과 재귀를 이용한 알고리즘 O(n log n)'''
    if len(array) < 2: # n이 1이면 종료 # 무한 재귀 방지
        return array
    mid = len(array) // 2 # 분할정복을 위해 분할
    lx = merge_sort(array[:mid]) # 모든 0~mid 까지 재귀.1 > 9,8,3,4 > 9,8 > 9 재귀 종료 lx[0] rx[1]
    print("lx :",lx)
    rx = merge_sort(array[mid:]) # mid~end 까지 재귀.1 > 3,4 > lx = 3,rx = 4 처음부터 코드가 다시 수행된다는것을 명심.
    print("rx :",rx)
    merge_arr = [] # 반복하며 merge_arr에 값 추가함

    l , r = 0, 0
    while l < len(lx) and r < len(rx): # 값 비교하여 낮은수 부터 삽입
        if lx[l] < rx[r]:
            merge_arr.append(lx[l])
            l += 1
        else:
            merge_arr.append(rx[r])
            r += 1
    merge_arr += lx[l:]
    merge_arr += rx[r:]
    print(f'merge_arr : {merge_arr}') # 함수가 끝나면 이때까지 재귀하던 값들이 하나로 합쳐짐 e.g. 1번재귀 8,9 > 3,4 > 3,4,8,9 > 5,6 > 1,2 > 1,2,7 > 1,2,5,6,7 > 합체
    return merge_arr

# array = [9,8,3,4,5,6,7,2,1]
def quick_sort(array):
    '''퀵정렬은 피봇을 기준으로 이원화를 하고 재귀하여 최종적으로 최소한 1개의 원소는 위치가 정해진다
       이를 반복하여 리스트의 크기가 1이나 0이 될때까지 반복해 최종적으론 분할된 리스트 들을 합친다.
       평균적으로 nLogn 이나 최악의 경우 n^2 시간복잡도를 가진다
    '''
    if len(array) <= 1:
        return array
    pivot = len(array) // 2 # 중간값 생성
    front, mid, end = [], [], []
    for i in array: # 배열을 순회하며 이원화 하여 각 값들을 넣어준다 >> 피봇을 기준으로!
        if i < array[pivot]:
            front.append(i)
        elif i > array[pivot]:
            end.append(i)
        else:
            mid.append(i)

    print(f'front : {front}')
    print(f'mid : {mid}')
    print(f'end : {end}')

    return quick_sort(front) + quick_sort(mid) + quick_sort(end) # 입력된 값을 재귀로 다시 호출하여 반복
    # return quick_sort(end) + quick_sort(mid) + quick_sort(front) # 입력된 값을 재귀로 다시 호출하여 반복

# array = quick_sort(array)
# print(f'array : {array}')



'''두 배열의 원소 교체 a,b 배열이 주어질때 k번 교체를 진행했을때 가장 큰 조합 찾기'''
# a = [1,2,5,4,3]
# b = [5,5,6,6,5]
#
# for _ in range(3):
#     min_a = min(a)
#     max_b = max(b)
#     a.append(max_b)
#     a.remove(min_a)
#     b.append(min_a)
#     b.remove(max_b)
# print(sum(a))

