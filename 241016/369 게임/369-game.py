n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end=" ")
        continue
    for j in str(i):
        if j in [3,6,9]:
            print(0, end=" ")
            break
    else:
        print(i, end=" ")
        continue