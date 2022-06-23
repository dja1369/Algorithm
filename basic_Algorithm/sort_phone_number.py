def solution(phone_book):
    answer = True
    # 2중 반복문을 이용 및 startswith함수를 이용하여 접두어 인지 비교
    # for num in range(len(phone_book)):
    #     for nextnum in range(num+1,len(phone_book)):
    #         if phone_book[num].startswith(phone_book[nextnum]):
    #             return False
    #         if phone_book[nextnum].startswith(phone_book[num]):
    #             return False
    phone_book.sort()
    for s, e in zip(phone_book, phone_book[1:]):
        if e.startswith(s):
            return False
    return answer

'''
문제 정의 
어느 한 숫자가 다른 숫자의 접두사 인가
하나라도 이어진다면 False반환 

'''