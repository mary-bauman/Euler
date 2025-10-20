size = 80
size = 5
file = "in.txt"
file = "sampleIn.txt"

# Read the grid
with open(file, "r") as f:
    grid = [list(map(int, line.strip().split(','))) for line in f]

size = len(grid)
dp = [row[0] for row in grid]  # minimal cost to reach each row by the first column

for col in range(1, size): #left to right

    dp = [dp[row] + grid[row][col] for row in range(size)] #move right

    for row in range(1, size): #move down
        dp[row] = min(dp[row], dp[row - 1] + grid[row][col])

    for row in range(size - 2, -1, -1): #move up
        dp[row] = min(dp[row], dp[row + 1] + grid[row][col])

print(min(dp))


