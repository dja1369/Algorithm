from os import remove


s = set()
s.add(142)
s.add(30)
s.add(505)
s.add(2020)

print('Size : ', len(s))

for i in s:
    print(i)
    
    
s.remove(30)
print(s)