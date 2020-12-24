import re
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-r", "--repeat_test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

    with open('24-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('24-test.txt', 'r').read().strip()

else:
    raw = open('24-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

dirs = []
for line in lines:
    line_dirs = []
    i = 0

    while i < len(line):
        if line[i] in 'ew':
            line_dirs.append(line[i])

        else:
            line_dirs.append(line[i:i+2])
            i += 1

        i += 1

    dirs.append(line_dirs)

tiles = set()

x_r = [0, 0]
y_r = [0, 0]
for d in dirs:
    location = [0, 0]

    for l in d:
        if l == 'e':
            location[0] += 1

        elif l == 'w':
            location[0] -= 1

        elif l == 'se':
            location[1] += 1

        elif l == 'nw':
            location[1] -= 1

        elif l == 'ne':
            location[0] += 1
            location[1] -= 1

        elif l == 'sw':
            location[0] -= 1
            location[1] += 1

    if location[0] < x_r[0]:
        x_r[0] = location[0]
    elif location[0] > x_r[1]:
        x_r[1] = location[0]

    if location[1] < y_r[0]:
        y_r[0] = location[1]
    elif location[1] > y_r[1]:
        y_r[1] = location[1]

    if str(location) in tiles:
        tiles.remove(str(location))

    else:
        tiles.add(str(location))

ans = len(tiles)

print('Part 1:', ans)

###########################

# Part 2
ans = 0

def count_adj(tile):
    adj = 0

    x, y = tile

    if str([x + 1, y]) in tiles:
        adj += 1

    if str([x-1, y]) in tiles:
        adj += 1

    if str([x, y-1]) in tiles:
        adj += 1

    if str([x, y+1]) in tiles:
        adj += 1

    if str([x+1, y-1]) in tiles:
        adj += 1

    if str([x-1, y+1]) in tiles:
        adj += 1

    return adj

for n in range(100):
    n_tiles = set(list(tiles))
    n_xr = x_r[:]
    n_yr = y_r[:]

    for i in range(x_r[0] - 1, x_r[1] + 2):
        for j in range(y_r[0] - 1, y_r[1] + 2):
            adj = count_adj([i, j])

            if str([i, j]) in tiles and (adj == 0 or adj > 2):
                n_tiles.remove(str([i, j]))

            elif str([i, j]) not in tiles and adj == 2:
                n_tiles.add(str([i, j]))

                if i < x_r[0]:
                    n_xr[0] = i
                elif i > x_r[1]:
                    n_xr[1] = i

                if j < y_r[0]:
                    n_yr[0] = j
                elif j > y_r[1]:
                    n_yr[1] = j

    tiles = n_tiles
    x_r = n_xr[:]
    y_r = n_yr[:]

ans = len(tiles)
print('Part 2:', ans)
