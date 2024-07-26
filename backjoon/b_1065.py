"""
- 주어진 수의 등차수열 개수 구하기 이때 그 수의 각 자리가 앞 뒤로 일정한 차이가 난다면 그것은 한수 라고 함
- 주어진 수 까지 순환하여 한수의 개수 출력
- 이때 100 미만은 비교 대상이 없기에 모두 한수 이다.
- 100 이상 부터는 각 자리 수를 비교하여 일정한 차이가 난다면 한수로 취급한다
"""

limit = int(input())

count = 0

for i in range(1, limit+1):
    if i < 100:
        count += 1
    else:
        target = list(map(int, str(i)))
        if target[0] - target[1] == target[1] - target[2]:
            count += 1

print(count)