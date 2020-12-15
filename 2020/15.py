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

    with open('15-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('15-test.txt', 'r').read().strip()

else:
    raw = open('15-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

turns = {}
repeat = set()

i = 1
for num in lines[0].split(','):
    if int(num) not in turns:
        turns[int(num)] = [i]
    else:
        turns[int(num)].append(i)

    if len(turns[int(num)]) == 3:
        turns[int(curr)].pop(0)

    i += 1

    last = int(num)

while i <= 2020:
    if len(turns[int(last)]) == 1:
        curr = 0
    else:
        curr = turns[int(last)][1] - turns[int(last)][0]

    if int(curr) not in turns:
        turns[int(curr)] = [i]
    else:
        turns[int(curr)].append(i)

    if len(turns[int(curr)]) == 3:
        turns[int(curr)].pop(0)

    i += 1

    last = int(curr)

ans = last

print('Part 1:', ans)

###########################

# Takes like a minute to run...

# Part 2
ans = 0

turns = {}
repeat = set()

i = 1
for num in lines[0].split(','):
    if int(num) not in turns:
        turns[int(num)] = [i]
    else:
        turns[int(num)].append(i)

    if len(turns[int(num)]) == 3:
        turns[int(curr)].pop(0)

    i += 1

    last = int(num)

while i <= 30000000:
    if len(turns[int(last)]) == 1:
        curr = 0
    else:
        curr = turns[int(last)][1] - turns[int(last)][0]

    if int(curr) not in turns:
        turns[int(curr)] = [i]
    elif len(turns[int(curr)]) == 1:
        turns[int(curr)] = [turns[int(curr)][0], i]
    else:
        turns[int(curr)] = [turns[int(curr)][1], i]

    i += 1

    last = int(curr)

ans = last

print('Part 2:', ans)
