upper = 10**4
base = 9
num = 81
ans = 0
while num <= upper:
    s = str(num)
    print(s)
    options = [[int(s[0])]]
    for c in s[1:]:
        newO = []
        for o in options:
            newO.append(o+[int(c)])
    o = newO.copy()
    print(o)
    base+=1
    num=base*base
print(ans)