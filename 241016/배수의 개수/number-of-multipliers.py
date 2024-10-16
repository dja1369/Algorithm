sam_cnt, o_cnt = 0, 0 
for _ in range(10):
    num = int(input())
    if num % 3 == 0:
        sam_cnt +=1 
    if num % 5 == 0:
        o_cnt += 1
print(f"{sam_cnt} {o_cnt}")