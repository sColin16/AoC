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

    with open('17-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('17-test.txt', 'r').read().strip()

else:
    raw = open('17-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

active = set()

x_range = [0, 0]
y_range = [0, 0]
z_range = [0, 0]
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            active.add((j, i, 0))

        if j > x_range[1]:
            x_range[1] = j
        elif j < x_range[0]:
            x_range[0] = j

        if i > y_range[1]:
            y_range[1] = i
        elif i < y_range[0]:
            y_range[0] = i

dirs = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 1, -1],
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, -1],
    [1, -1, 1],
    [1, -1, 0],
    [1, -1, -1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 1, 1],
    [0, 1, 0],
    [0, 1, -1],
    [0, -1, 1],
    [0, -1, 0],
    [0, -1, -1],
    [-1, 1, 1],
    [-1, 1, 0],
    [-1, 1, -1],
    [-1, 0, 1],
    [-1, 0, 0],
    [-1, 0, -1],
    [-1, -1, 1],
    [-1, -1, 0],
    [-1, -1, -1]
]


nx_range = x_range[:]
ny_range = y_range[:]
nz_range = z_range[:]

nactive = set(list(active)[:])

for i in range(6):
    for x in range(x_range[0] - 1, x_range[1] + 2):
        for y in range(y_range[0] - 1 , y_range[1] + 2):
            for z in range(z_range[0] - 1, z_range[1] + 2):
                a = 0
                for d in dirs:
                    if (x + d[0], y + d[1], z + d[2]) in active:
                        a += 1

                if (x, y, z) in active and not (a == 2 or a == 3):
                    nactive.remove((x, y, z))

                elif (x, y, z) not in active and a == 3:
                    nactive.add((x, y, z))

                    if x > x_range[1]:
                        nx_range[1] = x
                    elif x < x_range[0]:
                        nx_range[0] = x

                    if y > y_range[1]:
                        ny_range[1] = y
                    elif y < y_range[0]:
                        ny_range[0] = y

                    if z > z_range[1]:
                        nz_range[1] = z
                    elif z < z_range[0]:
                        nz_range[0] = z

    x_range = nx_range[:]
    y_range = ny_range[:]
    z_range = nz_range[:]

    active = set(list(nactive)[:])

ans = len(list(active))

print('Part 1:', ans)

###########################

# Part 2
ans = 0

active = set()

x_range = [0, 0]
y_range = [0, 0]
z_range = [0, 0]
w_range = [0, 0]
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            active.add((j, i, 0, 0))

        if j > x_range[1]:
            x_range[1] = j
        elif j < x_range[0]:
            x_range[0] = j

        if i > y_range[1]:
            y_range[1] = i
        elif i < y_range[0]:
            y_range[0] = i

dirs = [
    [0, 0, 0, 1],
    [0, 0, 0, -1],
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, -1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 0, -1, 0],
    [1, -1, 1, 0],
    [1, -1, 0, 0],
    [1, -1, -1, 0],
    [0, 0, 1, 0],
    [0, 0, -1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, -1, 0],
    [0, -1, 1, 0],
    [0, -1, 0, 0],
    [0, -1, -1, 0],
    [-1, 1, 1, 0],
    [-1, 1, 0, 0],
    [-1, 1, -1, 0],
    [-1, 0, 1, 0],
    [-1, 0, 0, 0],
    [-1, 0, -1, 0],
    [-1, -1, 1, 0],
    [-1, -1, 0, 0],
    [-1, -1, -1, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, -1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 0, -1, 1],
    [1, -1, 1, 1],
    [1, -1, 0, 1],
    [1, -1, -1, 1],
    [0, 0, 1, 1],
    [0, 0, -1, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, -1, 1],
    [0, -1, 1, 1],
    [0, -1, 0, 1],
    [0, -1, -1, 1],
    [-1, 1, 1, 1],
    [-1, 1, 0, 1],
    [-1, 1, -1, 1],
    [-1, 0, 1, 1],
    [-1, 0, 0, 1],
    [-1, 0, -1, 1],
    [-1, -1, 1, 1],
    [-1, -1, 0, 1],
    [-1, -1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 0, -1],
    [1, 1, -1, -1],
    [1, 0, 1, -1],
    [1, 0, 0, -1],
    [1, 0, -1, -1],
    [1, -1, 1, -1],
    [1, -1, 0, -1],
    [1, -1, -1, -1],
    [0, 0, 1, -1],
    [0, 0, -1, -1],
    [0, 1, 1, -1],
    [0, 1, 0, -1],
    [0, 1, -1, -1],
    [0, -1, 1, -1],
    [0, -1, 0, -1],
    [0, -1, -1, -1],
    [-1, 1, 1, -1],
    [-1, 1, 0, -1],
    [-1, 1, -1, -1],
    [-1, 0, 1, -1],
    [-1, 0, 0, -1],
    [-1, 0, -1, -1],
    [-1, -1, 1, -1],
    [-1, -1, 0, -1],
    [-1, -1, -1, -1],
]

nx_range = x_range[:]
ny_range = y_range[:]
nz_range = z_range[:]
nw_range = w_range[:]

nactive = set(list(active)[:])

for i in range(6):
    for x in range(x_range[0] - 1, x_range[1] + 2):
        for y in range(y_range[0] - 1 , y_range[1] + 2):
            for z in range(z_range[0] - 1, z_range[1] + 2):
                for w in range(w_range[0] - 1, w_range[1] + 2):
                    a = 0
                    for d in dirs:
                        if (x + d[0], y + d[1], z + d[2], w + d[3]) in active:
                            a += 1

                    if (x, y, z, w) in active and not (a == 2 or a == 3):
                        nactive.remove((x, y, z, w))

                    elif (x, y, z, w) not in active and a == 3:
                        nactive.add((x, y, z, w))

                        if x > x_range[1]:
                            nx_range[1] = x
                        elif x < x_range[0]:
                            nx_range[0] = x

                        if y > y_range[1]:
                            ny_range[1] = y
                        elif y < y_range[0]:
                            ny_range[0] = y

                        if z > z_range[1]:
                            nz_range[1] = z
                        elif z < z_range[0]:
                            nz_range[0] = z

                        if w > w_range[1]:
                            nw_range[1] = w
                        elif w < w_range[0]:
                            nw_range[0] = w

    x_range = nx_range[:]
    y_range = ny_range[:]
    z_range = nz_range[:]
    w_range = nw_range[:]

    active = set(list(nactive)[:])

ans = len(list(active))

print('Part 2:', ans)
