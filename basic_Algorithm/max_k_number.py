def solution(array, commands):
    answer = []
    for i in commands:
        ary = array[i[0] - 1: i[1]]
        ary.sort()
        answer.append(ary[i[2] - 1])

    return answer


'''
문제 정의 
array는 잘려질 배열 이다 
commands는 [시작, 끝, 추출] 순이다 
commands안의 배열은 한개가 아니다.(여러개)
'''