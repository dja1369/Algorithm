"""
- 단어가 이어지면서 한번만 나오는지 검증
- 단어가 끊겨서 나올경우 패스
"""
n = int(input())

count = 0

for _ in range(n):
    word = input()
    check_arr = []
    for i in range(len(word)):
        prev = None
        if i == 0:
            check_arr.append(word[i])
        else:
            if word[i-1] == word[i]:
                check_arr.append(word[i])
            else:
                if word[i] in check_arr:
                    break
                check_arr.append(word[i])
        if word == "".join(check_arr):
            count += 1
print(count)
