size = 80
# size = 5

f = open("in.txt")
# f = open("sampleIn.txt")
grid = []
for line in f:
    line = line.strip()
    grid.append([int(x) for x in line.split(",")])
#cannot go left
#so we go from left to right
for col in range(size-2,-1,-1):
    grid[size-1][col] += grid[size-1][col+1]

for row in range(size-2,-1,-1):
    grid[row][size-1] += grid[row+1][size-1]
    for col in range(size-2,-1,-1):
        grid[row][col] += min(grid[row+1][col], grid[row][col+1])



# for g in grid: print(g)
print(grid[0][0])