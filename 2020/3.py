
arena = []
width = 0
height = 0

with open('3-input.txt', 'r') as f:
    for line in f:
        arena.append(line.strip())
        width = len(line.strip())
        height += 1

row = 0
col = 0

trees = 0

ri = 2
ci = 1
while row < height:
    if arena[row][col] == '#':
        trees += 1

    row += ri
    col = (col + ci) % width

print(trees)
