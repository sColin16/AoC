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

    with open('3-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('3-test.txt', 'r').read().strip()

else:
    raw = open('3-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

gamma = 0
epsilon = 0

for i in range(len(lines[0])):
    ones = 0

    for line in lines:
        if line[-i - 1] == '1':
            ones += 1

    if ones > len(lines) / 2:
        gamma += 2 ** i

    else:
        epsilon += 2 ** i

ans = gamma * epsilon

print('Part 1:', ans)

###########################

# Part 2
ans = 0

new = lines

for i in range(len(lines[0])):
    if len(new) == 1:
        break

    ones = 0

    for line in new:
        if line[i] == '1':
            ones += 1

    if ones >= len(new) / 2:
        updated = []

        for value in new:
            if value[i] == '1':
                updated.append(value)

        new = updated

    else:
        updated = []

        for value in new:
            if value[i] == '0':
                updated.append(value)

        new = updated

first = int(new[0], 2)

new = lines
for i in range(len(lines[0])):
    if len(new) == 1:
        break

    ones = 0

    for line in new:
        if line[i] == '1':
            ones += 1

    if ones >= len(new) / 2:
        updated = []

        for value in new:
            if value[i] == '0':
                updated.append(value)

        new = updated

    else:
        updated = []

        for value in new:
            if value[i] == '1':
                updated.append(value)

        new = updated

second = int(new[0], 2)

ans = first * second

print('Part 2:', ans)
