container = []
for i in range(5):
    word = input()
    container.append(word)

for i in range(15):
    for j in range(5):
        if i < len(container[j]):
            print(container[j][i], end='')
