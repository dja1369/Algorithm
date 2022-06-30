'''사분면 표현 하기'''
# x = int(input())
# y = int(input())
#
#
# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y > 0:
#     print(2)
# else:
#     print(3)

# '''1부터 n까지 합 출력'''
# x = int(input())
# print(sum(range(1,x+1)))
#
# '''첫째 줄 부터 N번째 줄 까지 차례대로 출력'''
# x = int(input())
# for i in range(x,0,-1):
#     print(i)

# '''첫째 줄 부터 n번째 줄까지 차례대로 별 출력'''
# x = int(input())
# for i in range(1,x+1):
#     print('*'*i)

# '''첫째 줄 부터 n번째 줄까지 별 출력 대신 오른쪽으로 붙여서'''
# x = int(input())
# for i in range(1,x+1):
#     print(' ' * (x - i) + '*' * i)

# '''EOF문제'''
# while True:
#     try:
#         x, y = map(int, input().split())
#         print(x + y)
#     except:
#         break

# '''1110 숫자의 각 자리를 더해 새로운 숫자를 만들고 10 이하라면 앞 수의 오른쪽 수를 가져와 새로운 수를 만든다'''
# x = input()
# num = x
# cut = 0
# while True:
#     if len(x) == 1:
#         num = '0' + num
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     cut += 1
#     if num == x:
#         print(cut)
#         break

''' 1110 시간 초과 해결 방안
N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)
'''

'''10818 최소, 최대'''
# x = int(input())
# y = list(map(int,input().split()))
#
# print(min(y), max(y))


'''2562 최댓값 출력 + 인덱스도!'''
# num_list = []
# for i in range(9):
#     num_list.append(int(input()))
#
# print(max(num_list))
# print(num_list.index(max(num_list)) + 1)

'''2577 숫자의 갯수 a * b * c 의 수를 만드는데 0이 몇번 쓰였는지 출력'''
# from collections import Counter
# a = int(input())
# b = int(input())
# c = int(input())
# num_list = list(str(a * b * c))
#
# cnt = Counter(num_list)
# for i in range(10):
#     if str(i) in cnt.keys():
#         print(cnt[str(i)])
#     else:
#         print(0)

'''1546 평균 점수중에 최대값을 골라 이를 M이라고 정의후 모든 점수를 점수/M*100'''
# n = int(input())
# y = list(map(int, input().split()))
# maxi = max(y)
# avg = 0
# for i in y:
#     avg += i/maxi*100
# print(float(avg/n))

'''8958 OX퀴즈 첫째줄에 테스트개수, 두번째부턴 정답지 이때 점수는 연속된 O의 갯수'''

# n = int(input())
#
# for i in range(n):
#     quiz_list = list(input())
#     count = 0
#     add_count = 0
#     for j in quiz_list:
#         if j == 'O':
#             count += 1
#             add_count += count
#         else:
#             count = 0
#     print(add_count)

'''4344 평균점수 알려주기 첫째줄에는 케이스 갯수 C주어짐 
    둘째줄 부터 각 학생의 수 N명이 주어지고 이어서 N명의 점수가 주어짐
'''
# n = int(input())
# for _ in range(n):
#     student_avg = list(map(int, input().split()))
#     avg = sum(student_avg[1:])/student_avg[0]
#     result = 0
#     for i in student_avg[1:]:
#         if i > avg:
#             result +=1
#     rate = (result/student_avg[0]) * 100
#     print(f'{rate :.3f}%')

'''15596 정수 N개의 합을 구하는 함수 정의'''
# def solve(a: list) -> int:
#     sum = 0
#     for i in a:
#         sum += i
#     return sum

'''
아스키코드 변환 
ord 문자 > 아스키 
chr 아스키 > 문자
'''

'''11720 문자의 합'''
# n = int(input())
# s = str(input())
# answer = 0
# for i in s:
#     answer += int(i)
# print(answer)

# '''10809 알파벳 찾기'''
# a = list(range(97,123))
# s = input()
# for i in a:
#     print(s.find(chr(i)))

'''2675 문자열 반복'''
# t = int(input())
#
# for _ in range(t):
#     num, s = list(input().split())
#     word = ''
#     for i in s:
#         word += i*int(num)
#     print(word)

'''1157 단어공부'''
# s = input().upper()
# s_set = list(set(s))
# count_list = [s.count(i) for i in s_set]
#
# if count_list.count(max(count_list)) > 1:
#     print('?')
# else:
#     print(s_set[count_list.index(max(count_list))])

'''1712 손익분기점 
a 고정 b 인건비(가변) c 판매가격 
최초로 생산비 보다 총 판매가격이 역전하는 순간을 손익분기점 이라 한다 
'''
# a, b, c = map(int, input().split())
# if b >= c:
#     print(-1)
# else:
#     print(int(a/(c-b)+1))

'''2292 벌집 벌집은 6의 배수로 늘어남'''
# n = int(input())
# size = 1 # 벌집 크기
# cnt = 1
# while n > size:
#     size += 6 * cnt
#     cnt += 1
# print(cnt)

'''2839 설탕배달 그리디'''
n = int(input()) # 설탕을 입력받음
bag = 0 # 가방수 초기화
while n >= 0: # 설탕이 0이거나 클때 까지
    if n % 5 == 0: # 설탕이 5의 배수라면
        bag += (n // 5) # 설탕에 나누기 5를 한값을 출력후 종료
        print(bag)
        break
    n -= 3 # 설탕이 5의 배수가 아니라면 -3을 하고 가방수 +1
    bag += 1
else: # 어느조건식에도 성립이 안된다면 -1 출력
     print(-1)


