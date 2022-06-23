from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    # 트럭 무게 deque(stack)생성
    bridge = deque([0 for _ in range(bridge_length)])
    # 다리 길이 생성
    time = 0
    bridge_weight = 0

    while len(bridge) != 0:
        # 다리의 길이가 0이 아닐 동안 반복
        out = bridge.popleft()
        # 큐 에서 왼쪽 pop
        bridge_weight -= out
        # 다리 무게에서 out 제거
        time += 1
        # 시간 1 증가
        if truck_weights:
            # 만약 트럭의 무게가 존재한다면
            if bridge_weight + truck_weights[0] <= weight:
                # 만약 다리 무게 + 1번째 트럭 이 다리의 부하 보다 작거나 같다면
                left = truck_weights.popleft()
                # 트럭 무게 및 순서 왼쪽 pop
                bridge_weight += left
                # 다리의 부하 에 트럭 무게 추가
                bridge.append(left)
                # 브릿지에 트럭 진입
            else:
                bridge.append(0)
                # 부하가 견디지 못할경우 0 추가하며 대기
    return time


'''
문제 정의 
트럭 여러대 다리 건너야함 
모든 트럭 건너는데 최소 몇초 인지 파악 
최대 무게 존재 
브릿지렝스 최대 트럭 숫자
견디는 무게 웨이트 
트럭별 무게 트럭 웨이트 
'''