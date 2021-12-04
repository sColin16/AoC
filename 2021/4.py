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

    with open('4-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('4-test.txt', 'r').read().strip()

else:
    raw = open('4-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

nstr = sections[0][0]

boards = sections[1:]

nums = [int(n) for n in nstr.split(',')]

b = []

for board in boards:
    nb = []
    for line in board:
        nl = [int(i) for i in line.split()]
        nb.append(nl)

    b.append(nb)

winner = -1
for q, num in enumerate(nums):
    for i, board in enumerate(b):
        for j, line in enumerate(board):
            for k, element in enumerate(line):
                if element == num:
                    b[i][j][k] = -1

    winner = -1

    for i, board in enumerate(b):
        for line in board:
            if sum(line) == -5:
                winner = i

                break

        # For each column
        for k in range(5):
            col = []
            for l in range(5):
                col.append(board[l][k])

            if sum(col) == -5:
                winner = i

                break


        if winner > 0:
            break

    if winner > 0:
        break

for line in b[winner]:
    for n in line:
        if n > 0:
            ans += n

ans = ans * nums[q]

print('Part 1:', ans)

###########################

# Part 2
ans = 0

nstr = sections[0][0]

boards = sections[1:]

nums = [int(n) for n in nstr.split(',')]

b = []

for board in boards:
    nb = []
    for line in board:
        nl = [int(i) for i in line.split()]
        nb.append(nl)

    b.append(nb)

wait = [True] * len(b)
last = -1
for q, num in enumerate(nums):
    for i, board in enumerate(b):
        if not wait[i]:
            continue

        for j, line in enumerate(board):
            for k, element in enumerate(line):
                if element == num:
                    b[i][j][k] = -1

    for i, board in enumerate(b):
        if not wait[i]:
            continue

        for line in board:
            if sum(line) == -5:
                wait[i] = False
                last = i

        # For each column
        for k in range(5):
            col = []
            for l in range(5):
                col.append(board[l][k])

            if sum(col) == -5:
                wait[i] = False
                last = i

    if sum(wait) == 0:
        break

for line in b[last]:
    for n in line:
        if n > 0:
            ans += n

ans = ans * nums[q]

print('Part 2:', ans)
