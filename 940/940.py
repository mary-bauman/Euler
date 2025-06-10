i = 5
arr = [[0 for _ in range(i)] for _ in range(i)]
arr[0][0] = 0
arr[0][1] = 1
arr[1][1] = 2
arr[1][1] = 2
arr[1][2] = 5
arr[2][1] = 7
arr[2][2] = 16
#new m, n=1
arr[3][1] = 23
arr[3][2] = 53

# arr[4][1] = arr[3][1] + arr[3][0] = 23 + 0

# arr[1][1] = 2 = 2*arr[1][0] + arr[0][0]
# arr[1][2] = 5 = 2*arr[1][1] + arr[0][1] = 4+1
# arr[2][1] = 7 = 2*arr[2][0] + arr[1][0]
# arr[2][2] = 16 = 2*arr[2][1] + arr[1][1] = 14+2
# #new m, n=1
# arr[3][1] = arr[2][2] + arr[2][1] = 16 + 7 = 23
# arr[3][2] = 2 * arr[3][1] + arr[2][1] = 2 * 23 + 7 = 46 + 7 = 53

for n in range(2,i):
    arr[1][n] = 2 * arr[1][n - 1] + arr[0][n - 1]

for m in range(1,i):

for m in range(1,i):
    # arr[m][1] = arr[m-1][1]
    for n in range(2,i):
        arr[m][n] = 2 * arr[m][n - 1] + arr[m - 1][n - 1]
        # for a in arr: print(a)
        # print(f"({m},{n})")

for a in arr: print(a)
total = 0
for m in range(1,i):
    for n in range(1,i):
        print(f"m = {m}, n = {n}, arr[m][n] = {arr[m][n]}")
        total += arr[m][n]

print(f"Total: {total}")
