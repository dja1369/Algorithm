

def hanoi(n, start, mid, end):
    if n == 1: # 1개만 존재한다면 바로 도착지로 이동
        print(f'disk {n} from {start} to {mid}')
        return
    else:
        hanoi(n-1, start, end, mid) # 재귀 2가 들어옴
        print(f'disk {n} move {start} > {mid}') # 재귀된 2가 여기서 출력됨
        hanoi(n-1, end, mid, start) # 다시 재귀 하여 끝에있는 값을 중간으로 이동

hanoi(3, 1, 2, 3)






'''
문제 정의 
하노이의 탑 
규칙 : 원반을 모두 옮기는데 작은 원반 위에 큰원반이 올라가면 안됨 
재귀적으로 반복하여서 N개를 줄여 작은것 부터 이동하도록 로직 고안
'''