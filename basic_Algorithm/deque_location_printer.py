from collections import deque


def solution(priorities, location):
    answer = 0
    index_list = deque([i for i in range(len(priorities))])
    # 대기목록과 같은 인덱스 리스트 생성
    maxi = max(priorities)
    # 대기목록중 최고 우선순위 값 추출
    while True:
        index = index_list.popleft()
        # 인덱스 리스트 에서 왼쪽 pop
        if priorities[index] < maxi:
            # 만약 대기 목록의 인덱스가 최대값 보다 작다면
            index_list.append(index)
            # 이미 인덱스 리스트에서 pop이 되었으므로 제일 뒤에 append
        else:
            # 대기 목록의 인덱스가 최대값 보다 크거나 같다면
            answer += 1
            priorities[index] = 0
            # 대기 목록의 인덱스 값을 0으로 변경하고 순서에 1추가
            maxi = max(priorities)
            # 최대값 업데이트
            if index == location:
                break

    return answer


'''
문제 정의 
인쇄 대기 목록이 부여됨 
중요도에 따라 인쇄 순서가 바뀜 
나의 요청이 몇번째 인지 알고싶음. 
'''