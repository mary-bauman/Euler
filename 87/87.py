limit = 7080

#Sieve of Eratosthenes to generate all primes up to top
sieve = [True] * limit
sieve[0:2] = [False, False]
for i in range(2, int(limit**0.5) + 1):
    if sieve[i]:
        sieve[i*i:limit:i] = [False] * len(sieve[i*i:limit:i])
primes =  [i for i, is_p in enumerate(sieve) if is_p]
nums = set()
for c in primes:
    if c**4 > 50000000: break
    for b in primes:
        if b**3 + c**4 > 50000000: break
        for a in primes:
            tripleSum = a**2 + b**3 + c**4
            if tripleSum >= 50000000: break
            nums.add(tripleSum)
print(len(nums))
