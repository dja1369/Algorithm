result = []
while True:
    word = input()
    if word == '.':
        break
    stack = []
    for s in word:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] == '[':
                result.append("no")
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] == '(':
                result.append("no")
                break
            stack.pop()
    else:
        if stack:
            result.append("no")
        else:
            result.append("yes")
for i in result:
    print(i)

