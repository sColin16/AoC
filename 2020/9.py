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
    raw = open('9-input.txt', 'r').read().strip()

lines = raw.split('\n')

# Part 1
ans = 0
NUMS =25

numbers = [int(num) for num in lines]
prev = numbers[:NUMS]

for i in range(NUMS, len(numbers)):
    valid = False
    for number in prev:
        if numbers[i] - number in prev and numbers[i] - number != number:
            valid = True
            break

    if not valid:
        ans = numbers[i]
        break

    prev.pop(0)
    prev.append(numbers[i])

print('Part 1:', ans)

###########################

target = ans

# Part 2
ans = 0

numbers = [int(num) for num in lines]

for i in range(2, len(lines)):
    for j in range(0, len(lines) - i + 1):
        s = sum(numbers[j:j+i])
        if s == target:
            large = max(numbers[j:j+i])
            small = min(numbers[j:j+i])
            ans = large + small
            break

print('Part 2:', ans)
