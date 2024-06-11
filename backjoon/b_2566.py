max_value = 0
col, row = 0, 0
temp = 0
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if max_value < arr[j]:
            max_value = arr[j]
            col = j
            row = i

print(max_value)
print(row+1, col+1)

