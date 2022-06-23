def solution(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(num)))


'''
문제 정의
주어진 정수를 재배치해 가장 큰수 추출 
'''