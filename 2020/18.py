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

    with open('18-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('18-test.txt', 'r').read().strip()

else:
    raw = open('18-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

def evaluate(line):
    if '(' in line:
        group_indices = []
        groups = []

        start = 0
        while '(' in line[start:]:
            first = line[start:].index('(') + start

            n = 1
            for i in range(first + 1, len(line)):
                if line[i] == ')':
                    n -= 1
                elif line[i] == '(':
                    n += 1

                if n == 0:
                    group_indices.append((first, i))
                    groups.append(line[first+1:i])
                    start = i + 1
                    break

        evaled = []
        for group in groups:
            evaled.append(evaluate(group))

        chars = list(line)
        removed = 0
        for i in range(len(group_indices)):
            chars[group_indices[i][0]-removed:group_indices[i][1]-removed+1] = str(evaled[i])
            removed += group_indices[i][1] - group_indices[i][0] + 1 - len(str(evaled[i]))

        line = ''.join(chars)

    elems = line.split(' ')
 
    a = int(elems[0])
    for i in range(int(len(elems)/2)):
        op = elems[2 * i + 1]
        num = int(elems[2 * i + 2])

        if op == '+':
            a += num
        elif op =='*':
            a *= num

    return a

for line in lines:
    ans += evaluate(line)

print('Part 1:', ans)

###########################

# Part 2
ans = 0

def evaluate(line):
    if '(' in line:
        group_indices = []
        groups = []

        start = 0
        while '(' in line[start:]:
            first = line[start:].index('(') + start

            n = 1
            for i in range(first + 1, len(line)):
                if line[i] == ')':
                    n -= 1
                elif line[i] == '(':
                    n += 1

                if n == 0:
                    group_indices.append((first, i))
                    groups.append(line[first+1:i])
                    start = i + 1
                    break

        evaled = []
        for group in groups:
            evaled.append(evaluate(group))

        chars = list(line)
        removed = 0
        for i in range(len(group_indices)):
            chars[group_indices[i][0]-removed:group_indices[i][1]-removed+1] = str(evaled[i])
            removed += group_indices[i][1] - group_indices[i][0] + 1 - len(str(evaled[i]))

        line = ''.join(chars)

    elems = line.split(' ')
 
    while '+' in elems:
        idx = elems.index('+')
        result = int(elems[idx - 1]) + int(elems[idx + 1])

        elems[idx - 1: idx + 2] = [str(result)]

    a = int(elems[0])
    for i in range(int(len(elems)/2)):
        num = int(elems[2 * i + 2])

        a *= num

    return a

for line in lines:
    ans += evaluate(line)

print('Part 2:', ans)
