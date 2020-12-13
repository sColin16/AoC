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

start = int(lines[0])
nums = [int(line) for line in lines[1].split(',') if line != 'x']

min_wait = 10000000
min_num = 0
for num in nums:
    new = num - (start % num)

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

My original idea used a similar thought process, but began testing multiples of x2, instead of
multiples of the previously solved factors

I think sorting the factors by size wasn't necessary, because my code freezing had to do with
negative target modulo values, but I think it still speeds it up
'''

ans = 0

nums = [int(num) for num in lines[1].split(',') if num != 'x']
target_indices = [i for i, num in enumerate(lines[1].split(',')) if num != 'x']

zipped = zip(nums, target_indices)
zipped = list(zipped)
zipped.sort()
zipped = list(reversed(zipped))

nums = [elem[0] for elem in zipped]
mods = [elem[0] - elem[1] for elem in zipped]

for i, num in enumerate(nums):
    if mods[i] == num:
        mods[i] = 0

    while mods[i] < 0:
        mods[i] += nums[i]

test = mods[0]
inc = nums[0]

for i in range(2, len(nums) + 1):
    while True:
        valid = True

        for j, num in enumerate(nums[:i]):
            if test % num != mods[j]:
                valid = False
                break

        if valid:
            break

        test += inc

    inc *= nums[i-1]
    print('Solved i =', i)
    print(test, inc)

ans = test
        
print('Part 2:', ans)
