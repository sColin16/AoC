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
    raw = open('8-input.txt', 'r').read().strip()

lines = raw.split('\n')

# Part 1
ans = 0

acc = 0
i = 0

run = set()

while True:
    if i in run:
        ans = acc
        break

    run.add(i)
    command, num = lines[i].split()
    num = int(num)

    if command == 'nop':
        i += 1

    elif command == 'acc':
        acc += num
        i += 1

    elif command == 'jmp':
        i += num

print('Part 1:', ans)

###########################

# Part 2
ans = 0


for j, line in enumerate(lines):
    copy = lines[:]
    command, num = lines[j].split()

    if command == 'nop':
        copy[j] = f'jmp {num}'

    elif command == 'jmp':
        copy[j] = f'nop {num}'

    acc = 0
    i = 0

    run = set()

    while True:
        if i >= len(copy):
            ans = acc
            break

        if i in run:
            break

        run.add(i)
        command, num = copy[i].split()
        num = int(num)

        if command == 'nop':
            i += 1

        elif command == 'acc':
            acc += num
            i += 1

        elif command == 'jmp':
            i += num

print('Part 2:', ans)
