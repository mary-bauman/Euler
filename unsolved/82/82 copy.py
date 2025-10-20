size = 80
size = 5

f = open("in.txt")
f = open("sampleIn.txt")
grid = []
for line in f:
    line = line.strip()
    grid.append([int(x) for x in line.split(",")])
#cannot go left
#so we go from left to right

for col in range(1,size):
    for row in range(1,size):



for g in grid: print(g)