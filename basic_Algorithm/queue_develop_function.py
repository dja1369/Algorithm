import math


def solution(progresses, speeds):
    n = len(progresses)
    date_left = []
    answer = []

    for i in range(n):
        '''
        100 - 현재 작업
        종료일 = 남은 작업 / 속도 = 결과값(올림)
        남은 일수.append(종료일)
        '''
        work_left = 100 - progresses[i]
        end = math.ceil(work_left / speeds[i])
        date_left.append(end)
    # [7, 3, 9]
    while date_left:
        date = date_left.pop(0)
        result = 1
        while len(date_left) != 0 and date >= date_left[0]:
            result += 1
            date_left.pop(0)
        answer.append(result)
    return answer