total = 0
prev, cur = 1, 2
while cur<4000000:
    if cur%2==0: total+=cur
    prev, cur = cur, cur+prev



print(total)