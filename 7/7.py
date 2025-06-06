limit  = 1000000
sieve = [True] * limit
sieve[0:2] = [False, False]
for i in range(2, int(limit**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, limit, i):
            sieve[j] = False


i = -1
count = 0
while count < 10001:
    i += 1
    if i >= len(sieve):
        print("Limit exceeded")
        break
    count += sieve[i]
print(i)
    
