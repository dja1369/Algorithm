

d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] =1

best = max(d.values())
candi = []
for k, v in d.items():
    if v ==best:
        candi.append(k)

candi.sort()
print(candi[0])
# d.keys() #키만 출력
# d.values() #값만 출력
# d.items() # 키 값 둘다 출력
