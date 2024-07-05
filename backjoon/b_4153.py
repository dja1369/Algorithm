while 1:
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    if (arr[0]*arr[0] + arr[1]*arr[1]) == arr[2]*arr[2]:
        print("right")
    else:
        print("wrong")