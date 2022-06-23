def solution(notes):
    answer = 0
    notes.sort()
    length = len(notes)
    for i in range(length):
        if notes[i] >= length-i:
            return length-i
    return 0

'''
문제 정의 
과학자의 파워를 구함 
n편중 h번이상 인용된논문이 h편 이상 나머지논문이 h번 이하라면 
h의 최댓값이 파워 이다 
'''