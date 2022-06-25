test = [1, 3, 10, 9, 2, 12]
k = 7

def module(test, k):
    heapq.heapify(test) # 힙Q로 변환
    add = 0 # 최소 스코빌값을 계산해줄 변수
    ret = 0 # 섞은 횟수
    while len(test) >= 2: # 인덱스 에러 방지용 
        _min1 = heapq.heappop(test) # 첫번째 최소값 추출 
        if _min1 >= k: #heapq의 최소값이 K보다 크다면 종료
            return ret
        else: 
            _min2 = heapq.heappop(test) # 아니라면 두번째 최소값을 추출한후 섞은횟수 +1, 계산식을 이용하여 더해준후 기존 리스트에 추가.
            ret += 1
            add = _min1 + (_min2 * 2)
            test.append(add)
    
    if test[0] > k: #리스트의 가장 낮은값이 원하는 스코빌 지수 보다 높다면 종료 
        return ret
    else: # 그럴수 없는 상황이라면 즉 모든값을 더해도 원하는 지수 보다 낮은 상황이 만들어 진다면. -1 반환
        ret = -1
        return ret
           
        

module(test, k)
