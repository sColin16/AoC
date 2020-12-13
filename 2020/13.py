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

    with open('13-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('13-test.txt', 'r').read().strip()

else:
    raw = open('13-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

test = int(lines[0])
nums = [int(line) for line in lines[1].split(',') if line != 'x']

min_wait = 10000000
min_num = 0
for num in nums:
    new = num - (test % num)

    if new < min_wait:
        min_wait = new
        min_num = num

ans = min_wait * min_num

print('Part 1:', ans)

###########################

# Part 2

'''
My solution to this part is based on the "Search by sieving method" described in this article:
https://en.wikipedia.org/wiki/Chinese_remainder_theorem
'''

ans = 0

# Extract the bus numbers and their target departure offset
nums = [int(num) for num in lines[1].split(',') if num != 'x']
target_indices = [i for i, num in enumerate(lines[1].split(',')) if num != 'x']

zipped = list(zip(nums, target_indices))

# Calculate the target modulus value to get the target departure offset
mods = [elem[0] - elem[1] for elem in zipped]

# Adjust some of the target mods
# The first bus should have a modulus of 0
# There should be no negative target modulus values
for i, num in enumerate(nums):
    if mods[i] == num:
        mods[i] = 0

    while mods[i] < 0:
        mods[i] += nums[i]

# Start testing at the lowest value that makes the first bus id work
test = mods[0]

# Increment by the first bus id so that its modulus is unchanged
inc = nums[0]

# Incrementally solve each bus id after
for i in range(1, len(nums)):
    # Keep incrementing to find the lowest number that works for bus i
    while test % nums[i] != mods[i]:
        test += inc

    # Once we solve this bus, multiple increment by the number, so future searches
    # do not change the modulus of this bus
    inc *= nums[i]

ans = test
        
print('Part 2:', ans)
