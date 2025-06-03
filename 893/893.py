
from math import ceil, inf

top = 1000000
top = 100
dp = [6,2,5,5,4,5,6,3,7,6] #0-9
dp += [inf] * (top-10+1)
for i in range(10,top+1):
    og = sum(dp[int(c)] for c in str(i))
    # print(best)
    #check addition
    for j in range(1,ceil(i/2)):
        best = min(best, dp[j] + dp[i-j] + 2)

    #check multiplication
    for j in range(2,i):
        if i%j==0: best = min(best, dp[j] + dp[i//j] + 2)
               
    dp[i] = best
    

ans = sum(dp)
print(ans)
# a = 0
# for d in dp: a+=d
# print(a)
print(dp)