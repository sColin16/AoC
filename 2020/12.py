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

    with open('12-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('12-test.txt', 'r').read().strip()

else:
    raw = open('12-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

direction = [1, 0]

pos = [0, 0]

def rotate(degrees):
    for i in range(degrees // 90):
        temp = direction[0]
        direction[0] = -direction[1]
        direction[1] = temp

for line in lines:
    char = line[0]
    num = int(line[1:])

    if char == 'N':
        pos[1]+= num

    elif char == 'E':
        pos[0]+=num
    elif char == 'S':
        pos[1] -= num

    elif char == 'W':
        pos[0] -= num

    elif char == 'F':
        pos[0] += num * direction[0]
        pos[1] += num * direction[1]

    elif char == 'R':
        rotate(360 - num)

    elif char == 'L':
        rotate(num)

ans = abs(pos[0]) + abs(pos[1])

print('Part 1:', ans)

###########################

# Part 2
ans = 0

pos = [0, 0]
waypoint = [10, 1]

def rotate(degrees):
    for i in range(degrees // 90):
        temp = waypoint[0]
        waypoint[0] = -waypoint[1]
        waypoint[1] = temp

for line in lines:
    char = line[0]
    num = int(line[1:])

    if char == 'N':
        waypoint[1] += num

    elif char == 'E':
        waypoint[0] += num

    elif char == 'S':
        waypoint[1] -= num

    elif char == 'W':
        waypoint[0] -= num

    elif char == 'F':
        pos[0] += num * waypoint[0]
        pos[1] += num * waypoint[1]

    elif char == 'R':
        rotate(360 - num)

    elif char == 'L':
        rotate(num)

ans = abs(pos[0]) + abs(pos[1])
print('Part 2:', ans)
