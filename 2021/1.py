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

    with open('1-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('1-test.txt', 'r').read().strip()

else:
    raw = open('1-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

prev = nums[0]

for num in nums[1:]:
    if num > prev:
        ans += 1

    prev = num

print('Part 1:', ans)

###########################

# Part 2
ans = 0

prev = nums[0] + nums[1] + nums[2]

for i in range(1, len(nums) - 2):
    if nums[i] + nums[i + 1] + nums[i + 2] > prev:
        ans += 1

    prev = nums[i] + nums[i + 1] + nums[i + 2]

print('Part 2:', ans)
