s = []
s.append(123) # 데이터 삽입
s.append(456) # 데이터 삽입
s.append(789) # 데이터 삽입

print("size : ", len(s)) # 데이터의 길이 출력
while len(s) > 0: # s의 길이가 0보다 클때 동안
    print(s[-1]) # s에서 제일 상단값 출력
    s.pop(-1) # s에서 데이터 한개 제거 