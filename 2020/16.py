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

    with open('16-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('16-test.txt', 'r').read().strip()

else:
    raw = open('16-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

sections = raw.split('\n\n')

fields = sections[0].split('\n')

valid = {}

for field in fields:
    col_idx = field.index(":")
    name = field[:col_idx]
    ranges = field[col_idx + 2:].split(' or ')

    valid[name] = []

    for r in ranges:
        n1, n2 = r.split('-')
        valid[name].append([int(n1), int(n2)])

nearby = sections[2].split('\n')[1:]

for line in nearby:
    for num in line.split(','):
        is_valid = False
        num = int(num)

        for key, value in valid.items():
            for v in value:
                if v[0] <= num <= v[1]:
                    is_valid = True
                    break

        if not is_valid:
            ans += num
    
print('Part 1:', ans)

###########################

# Part 2
ans = 0

sections = raw.split('\n\n')

fields = sections[0].split('\n')

valid = {}

for field in fields:
    col_idx = field.index(":")
    name = field[:col_idx]
    ranges = field[col_idx + 2:].split(' or ')

    valid[name] = []

    for r in ranges:
        n1, n2 = r.split('-')
        valid[name].append([int(n1), int(n2)])

nearby = sections[2].split('\n')[1:]

use = []

def line_valid(line):
    global valid

    for num in line:
        num = int(num)
        num_valid = False
        for key, value in valid.items():
            for v in value:
                if v[0] <= num <= v[1]:
                    num_valid = True
                    break

        if not num_valid:
            return False

    return True

for i, line in enumerate(nearby):
    line = line.split(',')
    if line_valid(line):
        use.append([int(num) for num in line])

num_fields = len(use[0])

names = [name for name in valid]
possible = []
for i in range(len(use[0])):
    possible.append(names[:])

for i, line in enumerate(use):
    for j, num in enumerate(line):
        for key, value in valid.items():
            if not (value[0][0] <= num <= value[0][1]) and not (value[1][0] <= num <= value[1][1]):
                if key in possible[j]:
                    possible[j].remove(key)

i = 0
while i < len(possible):
    if len(possible[i]) == 1:
        for l in possible:
            if l != possible[i] and possible[i][0] in l:
                l.remove(possible[i][0])
                i = 0
                continue

    i += 1

idxs = []
for i, name in enumerate(possible):
    if 'departure' in name[0]:
        idxs.append(i)

ans = 1
ticket = sections[1].split('\n')[1].split(',')

for i in idxs:
    ans *= int(ticket[i])

print('Part 2:', ans)
