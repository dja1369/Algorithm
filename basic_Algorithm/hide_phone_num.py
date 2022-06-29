'''
문제정의 문자열로 번호가 주어질때 전화번호의 뒷4자리를 제외한 나머지 숫자를 *로 가리는 함수 정의
'''

def solution(phone_number):
    answer = ''
    number_len = len(phone_number)
    answer += '*' * (number_len-4)
    answer += phone_number[-4:]
    return answer

phone_number = "01033334444"
solution(phone_number)