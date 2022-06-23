def solution(participant, completion):
    # 배열을 이용한 문제 해결
    # participant.remove(competion)
    # for runner in completion: participant.remove(runner)
    # answer = participant[0]
    # 정렬을 이용한 문제 해결
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

# 문제 정의
# 선수 이름 배열 participant
# 완주 이름 배열 completion
# 완주 못한 사람 ret