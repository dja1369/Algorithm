def solution(brown, yellow):
    answer = []
    total_carpet = brown + yellow
    for i in range(2, total_carpet + 1):
        if (total_carpet % i) == 0:
            col = total_carpet // i
            if col >= i:
                if ((col + i) * 2 - 4) == brown:
                    answer = [col, i]
    return answer
