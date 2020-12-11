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

    with open('11-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('11-test.txt', 'r').read().strip()

else:
    raw = open('11-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

prev = lines[:]

new_lines = []

while True:
    new_lines = []
    for i, line in enumerate(prev):
        new_line = ""
        for j, char in enumerate(line):
            adj = 0
            if char == '.':
                new_line += '.'
                continue
            if i + 1 < len(prev) and prev[i+1][j] == '#':
                adj += 1
            if i + 1 < len(prev) and j + 1 < len(line) and prev[i+1][j+1] == '#':
                adj += 1 
            if i + 1 < len(prev) and j - 1 >= 0 and prev[i + 1][j - 1] == '#':
                adj += 1
            if i - 1 >= 0 and prev[i - 1][j] == '#':
                adj += 1
            if i - 1 >=0 and j + 1 < len(line) and prev[i-1][j+1] == '#':
                adj += 1
            if i - 1 >= 0 and j - 1 >= 0 and prev[i - 1][j-1] == '#':
                adj += 1
            if j + 1 < len(line) and prev[i][j + 1] == '#':
                adj += 1
            if j - 1 >= 0 and prev[i][j - 1] == '#':
                adj += 1

            if char == 'L' and adj == 0:
                new_line += '#'
            elif char == '#' and adj >= 4:
                new_line += 'L'
            else:
                new_line += char

        new_lines.append(new_line)

    if new_lines == prev:
        break

    prev = new_lines

for line in new_lines:
    ans += line.count('#')

print('Part 1:', ans)

###########################

# Part 2
ans = 0

def visible_adj(lines, si, sj, i_dir, j_dir):
    si += i_dir
    sj += j_dir
    while si >= 0 and si < len(lines) and sj >= 0 and sj < len(lines[0]):
        if lines[si][sj] == '#':
            return 1
        elif lines[si][sj] == 'L':
            return 0

        si += i_dir
        sj += j_dir

    return 0

prev = lines[:]

new_lines = []

while True:
    new_lines = []
    for i, line in enumerate(prev):
        new_line = ""
        for j, char in enumerate(line):
            adj = 0

            if char == '.':
                new_line += '.'
                continue
            adj += visible_adj(prev, i, j, 1, 1)
            adj += visible_adj(prev, i, j, 0, 1)
            adj += visible_adj(prev, i, j, 1, 0)
            adj += visible_adj(prev, i, j, -1, 0)
            adj += visible_adj(prev, i, j, -1, -1)
            adj += visible_adj(prev, i, j, 0, -1)
            adj += visible_adj(prev, i, j, 1, -1)
            adj += visible_adj(prev, i, j, -1, 1)

            if char == 'L' and adj == 0:
                new_line += '#'
            elif char == '#' and adj >= 5:
                new_line += 'L'
            else:
                new_line += char

        new_lines.append(new_line)

    if new_lines == prev:
        break

    prev = new_lines

for line in new_lines:
    ans += line.count('#')

print('Part 2:', ans)
