from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        now = k
        count = 0
        for dungeon in p:
            if now >= dungeon[0]:
                now -= dungeon[1]
                count += 1
        answer = max(answer, count)
    return answer