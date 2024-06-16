while True:
    n = int(input())
    if n == -1:
        break
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
    if sum(result) == n:
        print(f"{n} = {' + '.join(map(str, result))}")
    else:
        print(f"{n} is NOT perfect.")
