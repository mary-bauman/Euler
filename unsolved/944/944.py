total = 0
top = 10
prev = 0
for i in range(1, top + 1):
#each next one should be prev
# + sum of all the divisors of num
    for j in range(1,i):
        if i%j==0: prev += j
    total += prev
    print(f"i: {i}, prev: {prev}, total: {total}")


print(total%1234567891)