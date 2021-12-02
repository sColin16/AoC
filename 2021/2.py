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

    with open('2-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('2-test.txt', 'r').read().strip()

else:
    raw = open('2-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

h = 0
d = 0

for line in lines:
    direc, n = line.split()

    n = int(n)

    if direc == 'forward':
        h += n

    elif direc == 'up':
        d -= n

    elif direc == 'down':
        d += n

ans = h * d

print('Part 1:', ans)

###########################

# Part 2
ans = 0

h = 0
d = 0
a = 0

for line in lines:
    direc, n = line.split()

    n = int(n)

    if direc == 'forward':
        h += n
        d += a * n

    elif direc == 'down':
        a += n

    elif direc == 'up':
        a -= n

ans = h * d

print('Part 2:', ans)
