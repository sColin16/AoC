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

    with open('14-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('14-test.txt', 'r').read().strip()

else:
    raw = open('14-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

mem = {}

for line in lines:
    if line[:4] == 'mask':
        mask = line[7:]

    else:
        equal_index = line.index('=')
        left_index = line.index('[')
        right_index = line.index(']')
        addr = line[4:right_index]
        value = int(line[equal_index+2:])

        bin_string = '{0:036b}'.format(value)

        new_string = ""
        for i, char in enumerate(bin_string):
            if mask[i] == "1":
                new_string += "1"
            elif mask[i] == "0":
                new_string += "0"
            else:
                new_string += char

        mask_value = int(new_string, 2)

        mem[addr] = mask_value

for key,value in mem.items():
    ans += value

print('Part 1:', ans)

###########################

# Part 2
ans = 0

mem = {}

def get_addrs(string):
    possible = []

    for i, char in enumerate(string):
        if char == 'X':
            copy = list(string[:])
            copy[i] = '0'
            copy = ''.join(copy)
            possible.extend(get_addrs(copy))

            copy = list(string[:])
            copy[i] = '1'
            copy = ''.join(copy)
            possible.extend(get_addrs(copy))

            break

    if possible == []:
        return [string]

    return possible

for line in lines:
    if line[:4] == 'mask':
        mask = line[7:]

    else:
        equal_index = line.index('=')
        left_index = line.index('[')
        right_index = line.index(']')
        addr = int(line[4:right_index])
        value = int(line[equal_index+2:])

        bin_string = '{0:036b}'.format(addr)

        new_string = ""
        for i, char in enumerate(bin_string):
            if mask[i] == "1":
                new_string += "1"
            elif mask[i] == "0":
                new_string += char
            else:
                new_string += 'X'

        addrs = get_addrs(new_string)

        for a in addrs:
            b = int(a, 2)
            mem[b] = value

for key,value in mem.items():
    ans += value

print('Part 2:', ans)
