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

    with open('25-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('25-test.txt', 'r').read().strip()

else:
    raw = open('25-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

card_key = int(lines[0])
door_key = int(lines[1])

d = 1
d_loops = 0
while d != door_key:
    d = (d * 7) % 20201227
    d_loops += 1

ans = 1
for i in range(d_loops):
    ans = (ans * card_key) % 20201227

print('Part 1:', ans)

###########################

# Part 2
ans = 0



print('Part 2:', ans)
