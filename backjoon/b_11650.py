N = int(input())
arr = []
for _ in range(N):
    temp_arr = list(map(int, input().split()))
    arr.append(temp_arr)

arr.sort()


for i in range(N):
    print(f"{arr[i][0]} {arr[i][1]}")