import re
import sys
import argparse
import itertools
import math
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-r", "--repeat_test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

    with open('19-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('19-test.txt', 'r').read().strip()

else:
    raw = open('19-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

rules, messages = raw.split('\n\n')
rules = rules.split('\n')
messages = messages.split('\n')

r_dict = {}

for rule in rules:
    col_idx = rule.index(':')

    num = int(rule[:col_idx])
    parts = rule[col_idx+2:]

    if '"' in parts:
        p = parts[1]

    else:
        options = parts.split(' | ')
        p = []
        for option in options:
            p.append([int(num) for num in option.split(' ')])

    r_dict[num] = p

def possible(rule):
    if type(r_dict[rule]) == str and r_dict[rule] in 'ab':
        return [r_dict[rule]]

    p = []
    for option in r_dict[rule]:
        a = []
        for num in option:
            a.append(possible(num))

        a = list(itertools.product(*a))
        a = [''.join(t) for t in a]

        p.extend(a)

    return p

valid = set(possible(0))

for m in messages:
    if m in valid:
        ans += 1

print('Part 1:', ans)

###########################

# Part 2
ans = 0

rules, messages = raw.split('\n\n')
rules = rules.split('\n')
messages = messages.split('\n')

r_dict = {}

for rule in rules:
    col_idx = rule.index(':')

    num = int(rule[:col_idx])
    parts = rule[col_idx+2:]

    if '"' in parts:
        p = parts[1]

    else:
        options = parts.split(' | ')
        p = []
        for option in options:
            p.append([int(num) for num in option.split(' ')])

    r_dict[num] = p

#r_dict[8] = [[42], [42, 8]]
#r_dict[11] = [[42, 31], [42, 11, 31]]

memo = {}

def possible(rule):
    if rule in memo:
        return memo[rule]

    if type(r_dict[rule]) == str and r_dict[rule] in 'ab':
        memo[rule] = [r_dict[rule]]

        return [r_dict[rule]]

    p = []
    for option in r_dict[rule]:
        a = []
        for num in option:
            a.append(possible(num))

        a = list(itertools.product(*a))
        a = [''.join(t) for t in a]

        p.extend(a)

    memo[rule] = p
    return p

valid = set(possible(0))

memo[8] = list(set(memo[8]))
memo[11] = list(set(memo[11]))

eight = memo[8]
eleven = memo[11]
four2 = memo[42]
three1 = memo[31]

del memo

final = set()

size = len(four2[0])

for msg in messages:
    for i in range(int((len(msg) - 2 * size) / size)):
        if msg[i * size: (i + 1) * size] in four2:
            half = msg[(i + 1) * size:]

            augment = (len(half) / size / 2)
            
            if abs(int(augment) - augment) > 0.0001:
                continue

            augment = int(augment)

            valid = True
            for i in range(augment):
                if half[i * size:(i + 1) * size] not in four2:
                    valid = False
                    break

            if valid:
                for i in range(augment):
                    if half[(augment + i) * size: (augment + i + 1) * size] not in three1:
                        valid = False
                        break

            if valid:
                final.add(msg)
                break

        else:
            break

ans = len(final)

print('Part 2:', ans)
