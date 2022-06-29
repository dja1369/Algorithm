'''
문제 정의 
2개의 행렬을 입력받아 행렬의 덧셈 결과를 반환하는 함수 정의
'''

def solution(arr1, arr2):
    for i in range(len(arr1)): # 배열의 크기는 같기에 arr1의 길이만큼 반복
        for j in range(len(arr2)): # 중첩된 반복문으로 arr1의 0번 인덱스만큼 반복 
            arr1[i][j] += arr2[i][j] # arr1에 arr2를 더함
    print(arr1)
    return arr1

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
solution(arr1, arr2)
# print(len(arr1[0]))