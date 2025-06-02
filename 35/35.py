import math
import time
t = time.time()

top = 1000000
ans = 0

#Sieve of Eratosthenes to generate all primes up to top
def sieve(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    # print(sieve)
    return {i for i, is_p in enumerate(sieve) if is_p}

primes = sieve(top)

def good(i):
    if i not in primes: return False
    #check rotations
    s = str(i)
    for j in range(len(s)-1):
        s = (s[1:] + s[0])
        if int(s) not in primes: return False
    return True


for i in range(2,top): ans += int(good(i))
        
print(ans)
print("time =", round((time.time()-t),4), "s")