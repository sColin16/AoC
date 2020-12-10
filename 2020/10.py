import re
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

else:
    raw = open('10-input.txt', 'r').read().strip()

lines = raw.split('\n')

# Part 1
ans = 0

jolts = [int(line) for line in lines]
jolts.append(0)
jolts.sort()

diffs = []

for i in range(len(jolts) - 1):
    diffs.append(jolts[i + 1] - jolts[i])

threes = diffs.count(3) + 1
ones = diffs.count(1)

ans = threes * ones

print('Part 1:', ans)

###########################

# Part 2
ans = 0

jolts = [int(line) for line in lines]
jolts.append(max(jolts) + 3)
jolts.sort()

counts = {}

def count_combos(start, jolts):
    total = 0

    if str(jolts) in counts:
        return counts[str(jolts)]

    if len(jolts) == 0:
        return 1

    for i in range(min(3, len(jolts))):
        if jolts[i] - start <= 3:
            copy = jolts[i+1:]
            total += count_combos(jolts[i], copy)

    counts[str(jolts)] = total

    return total

ans = count_combos(0, jolts)

print('Part 2:', ans)
